from sqlalchemy import create_engine, text

class StudentTable:
    __scripts = {
        "create_table": text("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            )
        """),
        "select_all": text("SELECT * FROM students"),
        "select_by_id": text("SELECT * FROM students WHERE id = :student_id"),
        "insert_new": text("INSERT INTO students (name, email) VALUES (:name, :email)"),
        "update_by_id": text("UPDATE students SET name = :name, email = :email WHERE id = :student_id"),
        "delete_by_id": text("DELETE FROM students WHERE id = :student_id"),
        "get_max_id": text("SELECT MAX(id) FROM students"),
        "drop_table": text("DROP TABLE IF EXISTS students")
    }

    def __init__(self, connection_string):
        self.db = create_engine(connection_string)
        self._create_table()

    def _create_table(self):
        """Создаем таблицу студентов"""
        # Для SQLite autocommit работает автоматически в большинстве случаев
        with self.db.connect() as conn:
            conn.execute(self.__scripts["create_table"])
            # Для SQLite commit не нужен для DDL операций

    def get_all_students(self):
        """Получить всех студентов"""
        with self.db.connect() as conn:
            result = conn.execute(self.__scripts["select_all"])
            return result.fetchall()

    def get_student_by_id(self, student_id):
        """Получить студента по ID"""
        with self.db.connect() as conn:
            result = conn.execute(self.__scripts["select_by_id"], {"student_id": student_id})
            return result.fetchone()

    def create_student(self, name, email):
        """Создать нового студента"""
        with self.db.connect() as conn:
            # Для SQLite используем begin() для транзакций
            with conn.begin():
                conn.execute(self.__scripts["insert_new"], {"name": name, "email": email})

    def update_student(self, student_id, name, email):
        """Обновить данные студента"""
        with self.db.connect() as conn:
            with conn.begin():
                conn.execute(self.__scripts["update_by_id"],
                           {"student_id": student_id, "name": name, "email": email})

    def delete_student(self, student_id):
        """Удалить студента"""
        with self.db.connect() as conn:
            with conn.begin():
                conn.execute(self.__scripts["delete_by_id"], {"student_id": student_id})

    def get_max_id(self):
        """Получить максимальный ID"""
        with self.db.connect() as conn:
            result = conn.execute(self.__scripts["get_max_id"])
            return result.scalar() or 0

    def cleanup(self):
        """Очистить таблицу (для тестов)"""
        with self.db.connect() as conn:
            # Для DDL операций commit не нужен в SQLite
            conn.execute(self.__scripts["drop_table"])
            conn.execute(self.__scripts["create_table"])
