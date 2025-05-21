from models import Task

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.counter = 1

    def add_task(self, title, due):
        task = Task(self.counter, title, due)
        self.tasks.append(task)
        self.counter += 1
        print("Task added successfully.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        for task in self.tasks:
            print(task)

    def edit_task(self, task_id, title, due):
        for task in self.tasks:
            if task.id == task_id:
                task.title = title
                task.due_date = due
                print("Task updated.")
                return
        print("Task not found.")

    def delete_task(self, task_id):
        self.tasks = [t for t in self.tasks if t.id != task_id]
        print("Task deleted.")

    def toggle_complete(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.complete = not task.complete
                print("Task status toggled.")
                return
        print("Task not found.")
