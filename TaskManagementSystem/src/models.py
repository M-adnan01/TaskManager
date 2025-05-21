class Task:
    def __init__(self, id, title, due_date):
        self.id = id
        self.title = title
        self.due_date = due_date
        self.complete = False

    def __str__(self):
        status = "✓" if self.complete else "✗"
        return f"[{self.id}] {self.title} (Due: {self.due_date}) Status: {status}"
