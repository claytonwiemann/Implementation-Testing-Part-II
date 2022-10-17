from pickle import FALSE
import pytest
import System



username = 'calyam'
password = '#yeet'

def test_add_student(grading_system):
    grading_system.login(username,password)
    grading_system.usr.add_student('hdjsr7','databases')
    grading_system.reload_data()

    student = grading_system.users['hdjsr7']['courses']
    for key in student:
        if student == 'databases':
            assert True
    assert False


def test_drop_student(grading_system):
    grading_system.login(username,password)
    grading_system.usr.drop_student('hdjsr7','databases')
    grading_system.reload_data()

    student = grading_system.users['hdjsr7']['courses']
    for item in student:
        if student == 'databases':
            assert False
    assert True



@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem



"""

'calyam': {
        'courses': [
            'cloud_computing',
        ],
        'password': '#yeet',
        'role': 'professor'
    },


 'akend3': {
        'courses': {
            'comp_sci': {
                'assignment1': {
                    'grade': 99,
                    'submission_date': '2/1/20',
                    'submission': 'Blah Blah Blah',
                    'ontime': True
                },
                'assignment2': {
                    'grade': 66,
                    'submission_date': '2/8/20',
                    'submission': 'Blah2 Blah2 Blah2',
                    'ontime': True
                }
            },
            'databases': {
                'assignment1': {
                    'grade': 23,
                    'submission_date': '1/5/20',
                    'submission': 'Blah Blah Blah',
                    'ontime': True
                },
                'assignment2': {
                    'grade': 46,
                    'submission_date': '2/5/20',
                    'submission': 'Blah2 Blah2 Blah2',
                    'ontime': True
                }
            }
        },
        'password': '123454321',
        'role': 'student'


"""