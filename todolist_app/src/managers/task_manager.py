import uuid
from model.task import Task

class Task_Manager:
    def __init__(self):
        self.tasklist = []

    # Adds a task to the todolist  
    def add_task(self, title: str):
        task = Task(taskname=title, task_id=uuid.uuid4())
        self.tasklist.append(task)
        return 'Task added to your todolist!'

    # Deletes the task from the todolist
    def delete_task(self, title: str):
        for task in self.tasklist:
            if title == task.to_dict()['taskname']:
                self.tasklist.remove(task)
                return 'Task removed from your todolist!'
        return 'Task not found in your todolist!'

    # Updates the task's title
    def update_taskname(self, oldtitle: str, newtitle: str):
        for task in self.tasklist:
            if task.taskname == oldtitle:
                task.taskname = newtitle  # Directly updates the object's attribute
                return f'Task name changed from <{oldtitle}> to <{newtitle}>!'    
        return f'Task <{oldtitle}> not found in your todolist!'
    
    def show_tasks(self):
        return [str(t) for t in self.tasklist] if self.tasklist else ['Your task list is empty!']

    # Returns relevant data about the task objects to be stored in local storage
    def to_dict(self):
        task_data = {}
        if self.tasklist:
            for task in self.tasklist:
                task_dict = task.to_dict()
                task_data[str(task_dict['taskid'])] = [task_dict['taskname'], task_dict['taskstatus']]
            return task_data
        return task_data

    # Creates task objects from the extracted data from local storage, adds it to the list
    def to_list(self, data_dir: dict):
        if data_dir:
            for t_id, task_details in data_dir.items():
                status = False if task_details[1] == '⭕' else True
                task_obj = Task(task_id=t_id, taskname=task_details[0], is_completed=status)
                self.tasklist.append(task_obj)
        else:
            pass

    # Marks the given task as complete, identified using its title
    def mark_done(self, title: str):
        for task in self.tasklist:
            if task.taskname == title:
                task.mark_complete()
                return f"Task <{title}> marked as completed!"
        return f"Task <{title}> not found in your todolist!"