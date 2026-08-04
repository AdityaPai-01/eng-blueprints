import json
from pathlib import Path

class Data_Manager:
    def __init__(self, filepath):
        self.filepath = filepath
        if not self.filepath.exists():
            self.filepath.touch()
            with open(self.filepath, 'w') as file:
                json.dump({}, file)
        

    def save_data(self, data):
        try:
            with open(file=self.filepath, mode='w') as datafile:
                json.dump(data, datafile, indent=4)
        except Exception as e:
            print(f"ERROR: {e}")

    def load_data(self):
        pass