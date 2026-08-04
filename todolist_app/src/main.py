from model.task import Task
from managers.task_manager import Task_Manager
from managers.datamanager import Data_Manager, Path

import os, sys, time

# WRITTEN BY AI: relevance of filepath with respect to the executable
def get_data_filepath(filename="taskdata.json"):
    # If running as a PyInstaller bundle
    if getattr(sys, 'frozen', False):
        # Place data folder next to the .exe file
        base_dir = os.path.dirname(sys.executable)
    else:
        # Standard Python execution (src/../ -> root)
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(base_dir, "data")
    os.makedirs(data_dir, exist_ok=True)  # Ensure data directory exists
    return os.path.join(data_dir, filename)

todolist = Task_Manager()
dm = Data_Manager(Path(get_data_filepath()))

def initialize():
    todolist.to_list(dm.load_data())

def clear():
    time.sleep(3)
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