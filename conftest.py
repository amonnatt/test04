import sys
sys.path.insert(0, './function')
from student_db import StudentDB
from pytest import fixture

@fixture(scope="module")
def db():
    print("-----------Connected----------")
    db = StudentDB()
    db.connect("data/data_file.json")
    yield db
    print("------------close-----------")
    db.close()
