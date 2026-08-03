class Task:
    def __init__(self, taskname):
        self.taskname: str = taskname
        self.is_completed: bool = False

    def __str__(self):
        if self.is_completed:
            return f'✅: {self.taskname}'
        return f'⭕: {self.taskname}'

    def mark_complete(self):
        self.is_completed = True