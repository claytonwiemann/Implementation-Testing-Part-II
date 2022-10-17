import pytest
import System



username = 'cmhbf5'
password = 'bestTA'

def test_change_grade(grading_system):
    grading_system.login('cmhbf5','bestTA')
    grading_system.usr.change_grade('hdjsr7','software_engineering','assignment1',90)
    grading_system.reload_data()
    grading_system.login('hdjsr7','pass1234')
    assert grading_system.users[grading_system.usr.name]['courses']['software_engineering']['assignment1']['grade'] == 90
    

def test_create_assignment(grading_system):
    grading_system.login('cmhbf5','bestTA')
    grading_system.usr.create_assignment('new_assignment','02/02/2002','cloud_computing')
    grading_system.reload_data()
    assert grading_system.courses['cloud_computing']['assignments']['new_assignment']['due_date'] == '02/02/2002'




@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem



"""

 'cmhbf5': {
        'courses': [
            'cloud_computing',
            'software_engineering'
        ],
        'password': 'bestTA',
        'role': 'ta'
    }

"""