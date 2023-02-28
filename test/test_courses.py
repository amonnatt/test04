import sys
sys.path.insert(0, './function')
from courses_db import CoursesDB
db = None
def setup_module(module):
    print("-----------Connected----------")
    global db
    db = CoursesDB()
    db.connect("data/data_file.json")

def teardown_module (module):
    print("------------close-----------")
    db.close()


def test_Test_driven_Software_Development_data():
    data = db.get_data("Test-driven Software Development")
    assert data["name"] == "Test-driven Software Development"
    assert data["id"] == 1

def test_Digital_Content_Storage_Retrieval_data():
    data = db.get_data("Digital Content Storage and Retrieval")
    assert data["name"] == "Digital Content Storage and Retrieval"
    assert data["id"] == 2


# fixture
# def test_scott_data(db):
#     data = db.get_data("Scott")
#     assert data["name"] == "Scott"
#     assert data["id"] == 1
#     assert data["result"] == "pass"