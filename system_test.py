import pytest
import System
import json
import Professor
import TA
import Student
import Staff
import User


username = 'akend3'
password = '123454321'

#Tests if the program can handle a wrong username
def test_login(grading_system):
    grading_system.login(username,password)
    grading_system.reload_data()
    assert grading_system.users[grading_system.usr.name]['courses']['comp_sci']['assignment2']['grade'] == 66

def test_check_password(grading_system):
    grading_system.login(username,password)
    grading_system.reload_data()
    assert grading_system.users[grading_system.usr.name]['password'] == password


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem



