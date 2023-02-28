import sys
sys.path.insert(0, './function')
from student_db import StudentDB
db = None
def setup_module(module):
    print("-----------Connected----------")
    global db
    db = StudentDB()
    db.connect("data/data_file.json")

def teardown_module (module):
    print("------------close-----------")
    db.close()


def test_scott_data():
    data = db.get_data("Scott")
    assert data["name"] == "Scott"
    assert data["id"] == 1
    assert data["result"] == "pass"


def test_Mark_data():
    data = db.get_data("Mark")
    assert data["name"] == "Mark"
    assert data["id"] == 2
    assert data["result"] == "fail"

# fixture
# def test_scott_data(db):
#     data = db.get_data("Scott")
#     assert data["name"] == "Scott"
#     assert data["id"] == 1
#     assert data["result"] == "pass"