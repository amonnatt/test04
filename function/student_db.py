import json

class StudentDB:
    def __init__(self):
        self.data = None

    def connect(self, data_files):
        with open(data_files) as json_files:
            self.data = json.load(json_files)

    def get_data(self, name):
        for student in self.data["students"]:
            if student["name"] == name:
                return student

    def close(self):
        pass