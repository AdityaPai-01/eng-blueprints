from model.task import Task
from managers.task_manager import Task_Manager

todolist = Task_Manager()

while True:
    command = input("enter your command >>>: ")
    if command == 'at':
        title = input('enter task title: ')
        print(todolist.add_task(title=title))
    elif command == 'st':
        for obj in todolist.show_tasks():
            print(obj)
    elif command == 'q':
        break
    else:
        print("invalid command.")
