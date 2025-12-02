import os
import hashlib

import psycopg
from passlib.hash import bcrypt

# Берём строку подключения из переменной окружения
DATABASE_URL = os.getenv("DATABASE_URL")


def get_conn():
    """
    Создаёт новое подключение к базе данных.
    Важно: autocommit=True, чтобы не возиться с явным conn.commit().
    """
    return psycopg.connect(DATABASE_URL, autocommit=True)


def init_db():
    """
    Инициализация схемы БД: таблицы users и submissions.
    Вызывается один раз при старте приложения.
    """
    with get_conn() as conn:
        # Таблица пользователей
        conn.execute(
            """
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        );
        """
        )

        # Таблица решений задач
        conn.execute(
            """
        CREATE TABLE IF NOT EXISTS submissions (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users(id),
            task_id INTEGER NOT NULL,
            is_correct BOOLEAN NOT NULL,
            answer TEXT,
            created_at TIMESTAMPTZ DEFAULT NOW()
        );
        """
        )


# ====== Работа с паролями ======
# bcrypt по стандарту поддерживает только первые 72 байта входного пароля.
# Чтобы не ловить ValueError и при этом разрешать длинные пароли,
# сначала прогоняем пароль через SHA-256, а уже результат хэшируем bcrypt'ом.


def _password_digest(password: str) -> str:
    """
    Превращает произвольной длины пароль в строку фиксированной длины
    (hex-digest SHA-256), пригодную для bcrypt.
    """
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def create_user(username: str, password: str) -> bool:
    """
    Создаёт пользователя.
    Возвращает:
        True  – если пользователь успешно создан
        False – если username уже существует
    """
    password_hash = bcrypt.hash(_password_digest(password))

    try:
        with get_conn() as conn:
            conn.execute(
                "INSERT INTO users (username, password) VALUES (%s, %s)",
                (username, password_hash),
            )
        return True
    except psycopg.errors.UniqueViolation:
        # username уже занят
        return False


def verify_user(username: str, password: str):
    """
    Проверяет логин/пароль.
    Возвращает:
        dict {"id": ..., "username": ...} – если пароль верный
        None                             – если пользователь не найден
                                           или пароль неверен
    """
    with get_conn() as conn:
        row = conn.execute(
            "SELECT id, username, password FROM users WHERE username = %s",
            (username,),
        ).fetchone()

    if not row:
        return None

    user_id, db_username, password_hash = row

    # ВАЖНО: используем тот же digest, что и при создании
    if bcrypt.verify(_password_digest(password), password_hash):
        return {"id": user_id, "username": db_username}

    return None


def add_submission(user_id: int, task_id: int, is_correct: bool, answer: str):
    """
    Добавляет отправку решения задачи конкретным пользователем.
    """
    with get_conn() as conn:
        conn.execute(
            """
            INSERT INTO submissions (user_id, task_id, is_correct, answer)
            VALUES (%s, %s, %s, %s)
            """,
            (user_id, task_id, is_correct, answer),
        )


def get_rating():
    """
    Возвращает рейтинг пользователей:
    список словарей {"username": ..., "solved": ...},
    где solved – количество верно решённых задач.
    """
    with get_conn() as conn:
        rows = conn.execute(
            """
        SELECT 
            u.username,
            COUNT(s.*) FILTER (WHERE s.is_correct = true) AS solved
        FROM users u
        LEFT JOIN submissions s ON u.id = s.user_id
        GROUP BY u.id
        ORDER BY solved DESC, username ASC;
        """
        ).fetchall()

    return [{"username": r[0], "solved": r[1]} for r in rows]
