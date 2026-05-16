import sqlite3
import threading
from contextlib import contextmanager

class DatabaseManager:
    def __init__(self, db_path="data.db"):
        self.db_path = db_path
        self._lock = threading.Lock()

    @contextmanager
    def get_cursor(self):
        """
        Context manager to make sure thread-safe & auto-close connection.
        """
        self._lock.acquire()
        conn = sqlite3.connect(self.db_path, check_same_thread=False)
        try:
            yield conn.cursor()
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            conn.close()
            self._lock.release()

    def execute_query(self, query, params=()):
        """Execute a single query (Select, Update, Insert)"""
        with self.get_cursor() as cursor:
            cursor.execute(query, params)
            return cursor.fetchall()

db = DatabaseManager()