from model.task import Task
from managers.task_manager import Task_Manager
from managers.datamanager import Data_Manager

import os, time
from pathlib import Path

file_path = Path(f"{Path.cwd()}/data/taskdata.json")
todolist = Task_Manager()
dm = Data_Manager(file_path)

def clear():
    time.sleep(5)
    os.system('cls' if os.name=='nt' else 'clear')

def main():
    while True:
        command = input("enter your command >>>: ")
        match command:
            case 'at':
                title = input('enter task title: ')
                print(todolist.add_task(title=title))
                dm.save_data(todolist.to_dict())
            case 'st':
                for obj in todolist.show_tasks():
                    print(obj)
                input("enter anything to exit: ")
            case 'q':
                print("exiting program.")
                break
            case _:
                print('invalid command.')
        clear()
    clear()

if __name__ == '__main__':
    main()