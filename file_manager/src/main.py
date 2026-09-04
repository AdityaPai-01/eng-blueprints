import os, time
from manager import Manager

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

manager = Manager()
drives = manager.show_drives()

print("WELCOME TO PYTHON FILE MANAGER")
print("You have following drives in your system: ")
for drive in drives:
    print(drive)

while True:
    function = input("enter your function >>>: ")
    function_contents = function.split(" >= ")
    match function_contents[0]:
        case "cd":
            manager.cd(function_contents[1])
            for item in manager.show_items(manager.cwd()):
                print(item)

    