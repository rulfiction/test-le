# auth.py
import sqlite3
from datetime import datetime
from passlib.hash import bcrypt

DB_PATH = "db.sqlite3"


def get_conn():
    return sqlite3.connect(DB_PATH)


def init_db():
    conn = get_conn()
    cur = conn.cursor()

    # Таблица пользователей
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            role TEXT NOT NULL DEFAULT 'student'
        )
    """)

    # Таблица отправок решений
    cur.execute("""
        CREATE TABLE IF NOT EXISTS submissions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            task_id INTEGER NOT NULL,
            is_correct INTEGER NOT NULL,
            answer TEXT NOT NULL,
            created_at TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    conn.commit()
    conn.close()


# --- Пользователи ---


def create_user(username: str, password: str, role: str = "student") -> bool:
    """Создаёт пользователя, возвращает True/False (успех/уже занят)."""
    conn = get_conn()
    cur = conn.cursor()
    password_hash = bcrypt.hash(password)
    try:
        cur.execute(
            "INSERT INTO users (username, password_hash, role) VALUES (?, ?, ?)",
            (username, password_hash, role),
        )
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        # username уже занят
        return False
    finally:
        conn.close()


def verify_user(username: str, password: str):
    """Возвращает dict с данными пользователя или None."""
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "SELECT id, password_hash, role FROM users WHERE username = ?",
        (username,),
    )
    row = cur.fetchone()
    conn.close()

    if not row:
        return None

    user_id, password_hash, role = row
    if bcrypt.verify(password, password_hash):
        return {"id": user_id, "username": username, "role": role}
    return None


# --- Отправки и рейтинг ---


def add_submission(user_id: int, task_id: int, is_correct: bool, answer: str):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO submissions (user_id, task_id, is_correct, answer, created_at)
        VALUES (?, ?, ?, ?, ?)
        """,
        (user_id, task_id, 1 if is_correct else 0, answer, datetime.utcnow().isoformat()),
    )
    conn.commit()
    conn.close()


def get_rating():
    """
    Возвращает список:
    [
      {"username": "Иван", "solved": 3},
      ...
    ]
    Считаем количество уникальных задач, решённых правильно.
    """
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        """
        SELECT u.username,
               COUNT(DISTINCT s.task_id) AS solved
        FROM users u
        LEFT JOIN submissions s
          ON u.id = s.user_id AND s.is_correct = 1
        GROUP BY u.id
        ORDER BY solved DESC, u.username ASC
        """
    )
    rows = cur.fetchall()
    conn.close()

    return [
        {"username": r[0], "solved": r[1]}
        for r in rows
    ]
