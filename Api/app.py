from flask import Flask, request, make_response
import extra.py as ex
import mysql.connector
import json

with open('Configs\db_config.json', 'r') as f:
    db_config = json.load(f)


app = Flask(__name__)

    
@app.route('/', methods=['GET'])
def hello_world():
    return "hello world"

"""
Rule for Users:
1. Student Id start with 62
2. Student Id is 9 digits
3. Lecturer Id starts with 100
4. Lecturer Id is 6 digits long
5. Lecturer Id starts with 999
6. Lecturer Id is 8 digits long

"""

"""The body for the request is 
{
    "User_Name"  : "######",
    "User_id": "6201234567",
    password = "########"
}
"""
#This function creates a User and sets its type based on the format of the id number.
@app.route('/register_user', methods=['Post'])
def register_user():

    content = request.json
    User_id = content['User_ID']
    print(content['Password'])

    if ex.Stud_id_check(User_id):
        return ("Student")
    
    elif ex.Lec_id_check(User_id):
        return ("Lecturer")
    
    elif ex.Admin_id_check(User_id):
        return ("Admin")
    
    else:
        return "Invalid User ID"

"""The body for the request is 
{
    "User_id": "621234567",
    password = "########"
}
"""
#This function allows a user to login into one of three login pages based on the user id type.
@app.route('/User_login', methods=['Get'])
def User_login():

    content = request.json
    User_id = content['User_ID']
    print(User_id,content['Password'])

    if ex.Stud_id_check(User_id):
        return ("Student")
    
    elif ex.Lec_id_check(User_id):
        return ("Lecturer")
    
    elif ex.Admin_id_check(User_id):
        return ("Admin")
    
    else:
        return "Invalid User ID"

"""The body for the request is 
{
    "User_id": "620123456",
    "Course_Name" : "#####",
}
"""
#This function allows a user to login into one of three login pages based on the user id type.

@app.route('/Create_Course', methods=['Post'])
def Create_Course():

    content = request.json
    User_id = content['User_ID']
    print(User_id,content['Password'])
    
    
    if ex.Admin_id_check(User_id):
        return ("Admin")
    
    else:
        return "Invalid User type"

@app.route('/View_Courses', methods=['Get'])
def View_Courses():

    pass

@app.route('/View_Courses/<User_id>', methods=['Get'])
def View_Courses(User_id):

    content = request.json
    
    if ex.Stud_id_check(User_id):
        return ex.View_Courses_by_Student(User_id)
    
    elif ex.Lec_id_check(User_id):
        return  ex.View_Courses_by_Lecturer(User_id)




if __name__ == '__main__':
    app.run(port=10000)
