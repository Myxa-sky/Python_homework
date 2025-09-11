import pytest
from sqlalchemy.exc import IntegrityError


class TestStudentCRUD:
    """Тесты для операций CRUD с сущностью Student используя прямой SQL"""

    def test_create_student(self, student_table, test_student_data):
        """Тест создания студента - INSERT"""
        # Act - создаем студента
        student_table.create_student(
            test_student_data["name"],
            test_student_data["email"]
        )

        # Assert - проверяем, что студент создан
        students = student_table.get_all_students()
        assert len(students) == 1
        print(f"✅ INSERT выполнен: создан студент {test_student_data['name']}")

    def test_read_student(self, student_table, test_student_data):
        """Тест чтения студента - SELECT"""
        # Arrange - создаем студента
        student_table.create_student(
            test_student_data["name"],
            test_student_data["email"]
        )
        max_id = student_table.get_max_id()

        # Act - читаем студента
        student = student_table.get_student_by_id(max_id)

        # Assert
        assert student is not None
        assert student[1] == test_student_data["name"]
        print(f"✅ SELECT выполнен: найден студент ID {max_id}")

    def test_update_student(self, student_table, test_student_data):
        """Тест обновления студента - UPDATE"""
        # Arrange - создаем студента
        student_table.create_student(
            test_student_data["name"],
            test_student_data["email"]
        )
        max_id = student_table.get_max_id()

        # Act - обновляем студента
        new_name = "Петр Петров"
        new_email = "petr@example.com"
        student_table.update_student(max_id, new_name, new_email)

        # Assert - проверяем обновление
        updated_student = student_table.get_student_by_id(max_id)
        assert updated_student[1] == new_name
        print(f"✅ UPDATE выполнен: студент обновлен на {new_name}")

    def test_delete_student(self, student_table, test_student_data):
        """Тест удаления студента - DELETE"""
        # Arrange - создаем студента
        student_table.create_student(
            test_student_data["name"],
            test_student_data["email"]
        )
        max_id = student_table.get_max_id()

        # Act - удаляем студента
        student_table.delete_student(max_id)

        # Assert - проверяем удаление
        student_after = student_table.get_student_by_id(max_id)
        assert student_after is None
        print(f"✅ DELETE выполнен: студент ID {max_id} удален")

    def test_get_all_students(self, student_table, test_student_data):
        """Тест получения всех студентов"""
        # Arrange - создаем нескольких студентов
        students_data = [
            {"name": "Иван Иванов", "email": "ivan@example.com"},
            {"name": "Петр Петров", "email": "petr@example.com"},
            {"name": "Мария Сидорова", "email": "maria@example.com"}
        ]

        for data in students_data:
            student_table.create_student(data["name"], data["email"])

        # Act - получаем всех студентов
        students = student_table.get_all_students()

        # Assert
        assert len(students) == 3
        print(f"✅ SELECT * выполнен: найдено {len(students)} студентов")

    def test_unique_email_constraint(self, student_table):
        """Тест ограничения уникальности email"""
        # Act - создаем первого студента
        student_table.create_student("Студент 1", "same@example.com")

        # Assert - пытаемся создать второго с тем же email, должна быть ошибка
        with pytest.raises(IntegrityError):
            student_table.create_student("Студент 2", "same@example.com")

        print("✅ UNIQUE constraint работает: нельзя создать студентов с одинаковым email")
