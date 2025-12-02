import psycopg
import os
from passlib.hash import bcrypt

DATABASE_URL = os.getenv("DATABASE_URL")


def get_conn():
    return psycopg.connect(DATABASE_URL, autocommit=True)


def init_db():
    with get_conn() as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        );
        """)

        conn.execute("""
        CREATE TABLE IF NOT EXISTS submissions (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users(id),
            task_id INTEGER NOT NULL,
            is_correct BOOLEAN NOT NULL,
            answer TEXT,
            created_at TIMESTAMPTZ DEFAULT NOW()
        );
        """)


def create_user(username: str, password: str):
    password_hash = bcrypt.hash(password)

    try:
        with get_conn() as conn:
            conn.execute(
                "INSERT INTO users (username, password) VALUES (%s, %s)",
                (username, password_hash)
            )
        return True
    except psycopg.errors.UniqueViolation:
        return False


def verify_user(username: str, password: str):
    with get_conn() as conn:
        row = conn.execute(
            "SELECT id, username, password FROM users WHERE username = %s",
            (username,)
        ).fetchone()

    if not row:
        return None

    user_id, username, password_hash = row
    if bcrypt.verify(password, password_hash):
        return {"id": user_id, "username": username}
    return None


def add_submission(user_id: int, task_id: int, is_correct: bool, answer: str):
    with get_conn() as conn:
        conn.execute(
            "INSERT INTO submissions (user_id, task_id, is_correct, answer) VALUES (%s, %s, %s, %s)",
            (user_id, task_id, is_correct, answer)
        )


def get_rating():
    with get_conn() as conn:
        rows = conn.execute("""
        SELECT 
            u.username,
            COUNT(s.*) FILTER (WHERE s.is_correct = true) AS solved
        FROM users u
        LEFT JOIN submissions s ON u.id = s.user_id
        GROUP BY u.id
        ORDER BY solved DESC, username ASC;
        """).fetchall()

    return [{"username": r[0], "solved": r[1]} for r in rows]
