import pytest
from api.yougile_client import YougileClient

@pytest.fixture(scope="session")
def api_client():
    """Фикстура с тестовым клиентом API"""
    TEST_TOKEN = ""
    return YougileClient(TEST_TOKEN)

@pytest.fixture
def created_project(api_client):
    """Фикстура создает тестовый проект и возвращает его данные"""
    project = api_client.create_project("Проект для тестов")
    yield project
    # Здесь можно добавить удаление проекта через API, если доступно
