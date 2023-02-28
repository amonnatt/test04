import json

class CoursesDB:
    def __init__(self):
        self.data = None

    def connect(self, data_files):
        with open(data_files) as json_files:
            self.data = json.load(json_files)

    def get_data(self, name):
        for courses in self.data["courses"]:
            if courses["name"] == name:
                return courses

    def close(self):
        pass