import pytest
import System



username = 'akend3'
password = '123454321'

def test_assign_same_assignment(grading_system): #might want to make an assignment with the same name, for repeative purposes
    grading_system.login('cmhbf5','bestTA')
    grading_system.usr.create_assignment('new_assignment1','02/02/2002','cloud_computing')
    grading_system.usr.create_assignment('new_assignment1','02/02/2003','cloud_computing')
    grading_system.reload_data()
    
    counter = 0
    assignements = grading_system.courses['cloud_computing']['assignments']
    for item in assignements:
        if assignements == 'new_assignment1':
            counter+=1
    if(counter>1):
        assert True
    else:
        assert False#seeing if you can add an assignment with the same name

def test_assign_same_name(grading_system): #should be able to add student with same name, it would be rare but could happen
    grading_system.login('calyam','#yeet')
    grading_system.usr.add_student('hdjsr7','databases')
    grading_system.usr.add_student('hdjsr7','databases')#add student with the same name
    grading_system.reload_data()

    counter = 0
    student = grading_system.users['hdjsr7']['courses']
    for key in student:
        if student == 'databases':
            counter += 1
    if(counter > 1):
        assert True
    else: 
        assert False

def test_submit_assignment_multiple_times(grading_system):
    grading_system.login(username,password)
    grading_system.usr.submit_assignment('comp_sci','assignment1','TES1','02/02/2002')
    grading_system.usr.submit_assignment('comp_sci','assignment1','TEST2','02/03/2002')
    grading_system.reload_data()
    assert grading_system.users[grading_system.usr.name]['courses']['comp_sci']['assignment1']['submission_date'] == '02/02/2002' ##if submission date is changed that means a student can submit as many times as they want. This can be bad for some cases

def test_drop_non_existint_student(grading_system):
    grading_system.login(username,password)
    grading_system.usr.drop_student('DOES NOT EXIST','databases')
    grading_system.reload_data()

    student = grading_system.users['hdjsr7']['courses'] #if no student is found with that name it should not return the student list for the class
    if student == None: 
        return True
    else: 
        return False


def test_students_with_same_name(grading_system):
    grading_system.login(username,password)
    grading_system.usr.add_student('hdjsr7','databases')#same name
    grading_system.usr.add_student('hdjsr7','databases')#same name
    grading_system.reload_data()

    count = 0
    student = grading_system.users['hdjsr7']['courses']
    for item in student:
        if student == 'databases':
            count += 1
    if(count > 1):
        assert True # students may have the same name on rare ocassions. Needs to be tested to see if this is possible
    else:
        assert False

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