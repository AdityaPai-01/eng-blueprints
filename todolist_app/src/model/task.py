class Task:
    def __init__(self, taskname, task_id, is_completed=False):
        self.taskname: str = taskname
        self.task_id: str = task_id
        self.is_completed: bool = is_completed

    # Used to display only the necessary information about the task
    def __str__(self):
        if self.is_completed:
            return f'✅: {self.taskname}'
        return f'⭕: {self.taskname}'

    # Useful to return data in the form of dictionary, to be stored in JSON format
    def to_dict(self):
        return {"taskid": self.task_id, 
                "taskname":self.taskname, 
                "taskstatus":'✅' if self.is_completed else '⭕'}

    # Marks the task as complete
    def mark_complete(self):
        self.is_completed = True