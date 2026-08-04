import uuid
from model.task import Task

class Task_Manager:
    def __init__(self):
        self.tasklist = []
        self._assigned_id = uuid.uuid4()
        
    def add_task(self, title: str):
        task = Task(taskname=title, task_id=self._assigned_id)
        self.tasklist.append(task)
        return 'Task added to your todolist!'

    def delete_task(self, title: str):
        if title in self.tasklist:
            self.tasklist.pop(title)
            return 'Task removed from your todolist!'
        return 'Task not found in your todolist!'

    def update_taskname(self):
        pass

    def show_tasks(self):
        return [str(t) for t in self.tasklist] if self.tasklist else ['Your task list is empty!']

    def to_dict(self):
        task_data = {}
        if self.tasklist:
            for task in self.tasklist:
                task_data[str(task.to_dict()['taskid'])] = task
            return task_data
        return task_data

    def to_list(self, data_dir: dict):
        if data_dir:
            for t_id, task_obj in data_dir.items():
                self.tasklist.append(task_obj)
        else:
            pass