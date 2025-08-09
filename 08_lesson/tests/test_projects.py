import pytest
from requests.exceptions import HTTPError

# Позитивные тесты
def test_create_project_success(api_client):
    """Успешное создание проекта"""
    project = api_client.create_project("Тестовый проект")
    assert "id" in project
    assert isinstance(project["id"], str)

def test_get_project_success(api_client, created_project):
    """Успешное получение проекта"""
    project = api_client.get_project(created_project["id"])
    assert project["id"] == created_project["id"]
    # Дополнительные проверки на основе реального ответа API

def test_update_project_success(api_client, created_project):
    """Успешное обновление проекта"""
    updated = api_client.update_project(
        created_project["id"],
        "Обновленное название"
    )
    assert updated["id"] == created_project["id"]

# Негативные тесты
def test_create_project_empty_title(api_client):
    """Попытка создания без названия (400)"""
    with pytest.raises(HTTPError) as exc:
        api_client.create_project("")
    assert exc.value.response.status_code == 400

def test_get_nonexistent_project(api_client):
    """Попытка получить несуществующий проект (404)"""
    with pytest.raises(HTTPError) as exc:
        api_client.get_project("несуществующий-id")
    assert exc.value.response.status_code == 404

def test_update_nonexistent_project(api_client):
    """Попытка обновить несуществующий проект (404)"""
    with pytest.raises(HTTPError) as exc:
        api_client.update_project("несуществующий-id", "Новое название")
    assert exc.value.response.status_code == 404
