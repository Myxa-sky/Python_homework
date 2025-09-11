import requests
from typing import Dict, Any


class YougileClient:
    def __init__(self, token: str):
        self.base_url = "https://ru.yougile.com/api-v2"
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

    def create_project(self, title: str) -> Dict[str, Any]:
        """[POST] Создание проекта"""
        data = {"title": title}
        response = requests.post(
            f"{self.base_url}/projects",
            json=data,
            headers=self.headers
        )
        response.raise_for_status()
        return {"id": response.json()["id"]}  # Возвращаем только ID

    def get_project(self, project_id: str) -> Dict[str, Any]:
        """[GET] Получение проекта"""
        response = requests.get(
            f"{self.base_url}/projects/{project_id}",
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()  # Возвращаем полный ответ API

    def update_project(self, project_id: str, new_title: str) -> Dict[str, Any]:
        """[PUT] Обновление проекта"""
        data = {"title": new_title}
        response = requests.put(
            f"{self.base_url}/projects/{project_id}",
            json=data,
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()
