class Task:
    def __init__(self, title, priority="Média"):
        self.title = title
        self.priority = priority
        self.status = "To Do"

tasks = []

def create_task(title, priority="Média"):
    task = Task(title, priority)
    tasks.append(task)
    return task

def list_tasks():
    return tasks


if __name__ == "__main__":
    create_task("Primeira tarefa")
    print("Sistema funcionando!")
