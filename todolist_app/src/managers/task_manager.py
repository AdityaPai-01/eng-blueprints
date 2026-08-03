import uuid
from model.task import Task

class Task_Manager:
    def __init__(self):
        self.tasklist = []
        self._assigned_id = uuid.uuid4()
        
    def add_task(self, title):
        task = Task(taskname=title, task_id=self._assigned_id)
        self.tasklist.append(task)
        return 'Task added to your todolist!'

    def delete_task(self, title):
        if title in self.tasklist:
            self.tasklist.pop(title)
            return 'Task removed from your todolist!'
        return 'Task not found in your todolist!'

    def update_taskname(self):
        pass

    def show_tasks(self):
        return [str(t) for t in self.tasklist]