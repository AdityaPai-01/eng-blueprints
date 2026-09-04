from pathlib import Path

class Manager:
    def __init__(self):
        self.working_directory = []

    def create_file(self, file_name):
        pass

    def create_dictionary(self):
        pass

    def rename(self):
        pass

    def copy(self):
        pass

    def move(self):
        pass

    def delete(self):
        pass

    def search(self):
        pass

    def cwd(self):
        path = ""
        for path_obj in self.working_directory:
            path.join(str(path_obj))
        return path

    def cd(self, path_object):
        self.working_directory.append(path_object)

    def cd_previous(self):
        self.working_directory.pop()
        return self.working_directory[-1]
    
    def show_items(self, path):
        path = Path(path)
        all_items = []
        for item in path.iterdir():
            all_items.append(item)
        return all_items        

    def show_drives(self):
        drives = []
        for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            drive = Path(f"{letter}:\\")
            if drive.exists():
                drives.append(drive)
        return drives