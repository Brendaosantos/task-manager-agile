from src.app import create_task

def test_create_task():
    task = create_task("Teste")
    assert task.title == "Teste"

def test_default_status():
    task = create_task("Nova tarefa")
    assert task.status == "To Do"
