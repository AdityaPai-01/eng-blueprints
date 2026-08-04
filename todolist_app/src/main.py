from model.task import Task
from managers.task_manager import Task_Manager
from managers.datamanager import Data_Manager, Path

import os, time

file_path = Path(f"{Path.cwd()}/data/taskdata.json")
todolist = Task_Manager()
dm = Data_Manager(file_path)

def initialize():
    todolist.to_list(dm.load_data())

def clear():
    time.sleep(2)
    os.system('cls' if os.name=='nt' else 'clear')

def main():
    while True:
        command = input("enter your command >>>: ")
        match command:
            case 'at':
                title = input('enter task title: ')
                print(todolist.add_task(title=title))
            case 'st':
                for obj in todolist.show_tasks():
                    print(obj)
                input("enter anything to exit: ")
            case 'q':
                print("exiting program.")
                break
            case 'dt':
                print(todolist.delete_task(input("enter task's title to delete: ")))
            case 'md':
                print(todolist.mark_done(input('enter taskname to mark as complete: '))) 
            case 'ut':
                print(todolist.update_taskname(input("enter old taskname: "), input('enter new taskname: ')))
            case _:
                print('invalid command.')
        dm.save_data(todolist.to_dict())
        clear()
    clear()

if __name__ == '__main__':
    initialize()
    main()