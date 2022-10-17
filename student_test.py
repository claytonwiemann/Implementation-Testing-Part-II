import pytest
import System



username = 'akend3'
password = '123454321'

def test_submit_assignment(grading_system):
    grading_system.login(username,password)
    grading_system.usr.submit_assignment('comp_sci','assignment1','TEST','02/02/2002')
    grading_system.reload_data()
    assert grading_system.users[grading_system.usr.name]['courses']['comp_sci']['assignment1']['submission_date'] == '02/02/2002'


#check this
def test_check_ontime(grading_system):
    grading_system.login(username,password)
    if grading_system.usr.check_ontime('2/2/20','2/6/20') and grading_system.usr.check_ontime('2/10/20','2/6/20'):
        assert False
    else:
        if(grading_system.usr.check_ontime('2/2/20','2/6/20')):
            assert True

def test_check_grade(grading_system):
    grading_system.login(username,password)
    grades = grading_system.usr.check_grades('cloud_computing')
    if grades['assignment2']['grade'] == 3:
        assert True



def test_view_assignments(grading_system):
    grading_system.login(username,password)
    assignments = grading_system.usr.view_assignments('comp_sci')
    if(assignments['assignment1']['grade'] == 99):    
        assert True


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



 'hdjsr7': {
        'courses': {
            'cloud_computing': {
                'assignment1': {
                    'grade': 100,
                    'submission_date': '1/3/20',
                    'submission': 'Blah Blah Blah',
                    'ontime': True
                },
                'assignment2': {
                    'Grade': 100,
                    'Submission Data': '2/3/20',
                    'Submission': 'Blah2 Blah2 Blah2',
                    'ontime': True
                }
            },
            'databases': {
                'assignment1': {
                    'grade': 100,
                    'submission_date': '1/5/20',
                    'submission': 'Blah Blah Blah',
                    'ontime': True
                },
                'assignment2': {
                    'grade': 100,
                    'submission_date': '2/5/20',
                    'submission': 'Blah2 Blah2 Blah2',
                    'ontime': False
                }
            },
            'software_engineering': {
                'assignment1': {
                    'grade': 100,
                    'submission_date': '1/1/20',
                    'submission': 'Blah Blah Blah',
                    'ontime': True
                },
                'assignment2': {
                    'grade': 100,
                    'submission_date': '2/1/20',
                    'submission': 'Blah2 Blah2 Blah2',
                    'ontime': True
                }
            }
        },
        'password': 'pass1234',
        'role': 'student'
    },

"""