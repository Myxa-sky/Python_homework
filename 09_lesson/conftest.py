import pytest
from StudentTable import StudentTable

@pytest.fixture
def student_table():
    """Создаем экземпляр StudentTable для SQLite in-memory"""
    table = StudentTable('sqlite:///:memory:')
    yield table
    # Очищаем после каждого теста
    table.cleanup()

@pytest.fixture
def test_student_data():
    return {
        "name": "Иван Иванов",
        "email": "ivan@example.com"
    }
