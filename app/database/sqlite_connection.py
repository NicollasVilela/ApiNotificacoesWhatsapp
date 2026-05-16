import os
import sqlite3
from contextlib import contextmanager

from dotenv import load_dotenv

load_dotenv()

DATABASE_NAME = os.getenv("DATABASE_NAME", "notifications.db")


@contextmanager
def get_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row

    try:
        yield conn
        conn.commit()
    finally:
        conn.close()


def criar_tabelas():
    with get_connection() as conn:
        conn.execute(
            '''
            CREATE TABLE IF NOT EXISTS eventos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                telefone TEXT NOT NULL,
                mensagem TEXT NOT NULL,
                processado INTEGER DEFAULT 0,
                criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            '''
        )
