import json
from pathlib import Path

class Data_Manager:
    def __init__(self, filepath):
        self.filepath = filepath

        # Creating file at specified storage if it doesn't exists already
        if not self.filepath.exists():
            self.filepath.touch()
            with open(self.filepath, 'w') as file:
                json.dump({}, file)

    # Saves the taskdata obtained to the local storage   
    def save_data(self, data):
        try:
            with open(file=self.filepath, mode='w') as datafile:
                json.dump(data, datafile, indent=4)
        except Exception as e:
            print(f"ERROR: {e}")

    # Extracts the taskdata from local storage, returns a dictionary
    def load_data(self):
        try:
            with open(file=self.filepath, mode='r') as readfile:
                data = json.load(readfile)
            return data
        except Exception as e:
            print(f"ERROR: {e}")