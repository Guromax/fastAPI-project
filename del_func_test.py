from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_delete_task():
    # Создаем задачу для теста
    response = client.post("/tasks", json={"name": "Test Task", "description": "Test Description"})
    task_id = response.json()["task"]["id"]

    # Удаляем задачу
    delete_response = client.delete(f"/tasks/{task_id}")
    assert delete_response.status_code == 200
    assert delete_response.json() == {"ok": True, "message": "Task deleted"}

    # Проверяем, что задача действительно удалена
    get_response = client.get(f"/tasks/{task_id}")
    assert get_response.status_code == 404
