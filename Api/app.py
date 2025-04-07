from flask import Flask, request, make_response
import mysql.connector
import json

with open('Configs\db_config.json', 'r') as f:
    db_config = json.load(f)


app = Flask(__name__)

#Check to see if valid student Id and returns boolean
def Stud_id_check(Stud_id):
    if Stud_id[0:3] == "62" and len(Stud_id) == 9:
        return True
    else:
        return False

#Check to see if valid Lecturer Id and returns boolean
def Lec_id_check(Lec_id):
    if Lec_id[0:3] == "100" and len(Lec_id) == 7:
        return True
    else:
        return False

#Check to see if valid Admin Id and returns boolean
def Admin_id_check(Admin_id):
    if Admin_id[0:3] == "999" and len(Admin_id) == 8:
        return True
    else:
        return False
    
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
    "User_id": "620123456",
    password = "########"
}
"""
#This function creates a User and sets its type based on the format of the id number.
@app.route('/register_user', methods=['Post'])
def register_user():

    content = request.json
    User_id = content['User_ID']
    print(content['Password'])

    if Stud_id_check(User_id):
        return ("Student")
    
    elif Lec_id_check(User_id):
        return ("Lecturer")
    
    elif Admin_id_check(User_id):
        return ("Admin")
    
    else:
        return "Invalid User ID"

"""The body for the request is 
{
    "User_id": "620123456",
    password = "########"
}
"""
#This function allows a user to login into one of three login pages based on the user id type.
@app.route('/User_login', methods=['Get'])
def User_login():

    content = request.json
    User_id = content['User_ID']
    print(User_id,content['Password'])

    if Stud_id_check(User_id):
        return ("Student")
    
    elif Lec_id_check(User_id):
        return ("Lecturer")
    
    elif Admin_id_check(User_id):
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
    
    
    if Admin_id_check(User_id):
        return ("Admin")
    
    else:
        return "Invalid User type"

@app.route('/View_Courses', methods=['Get'])
def View_Courses():

    pass

@app.route('/View_Courses/<User_id>', methods=['Get'])
def View_Courses(User_id):

    content = request.json
    
    if Stud_id_check(User_id):
        return View_Courses_by_Student(User_id)
    
    elif Lec_id_check(User_id):
        return  View_Courses_by_Lecturer(User_id)
    

    def View_Courses_by_Student(User_id):
        pass
    
    
    def View_Courses_by_Lecturer(User_id):
        pass

if __name__ == '__main__':
    app.run(port=10000)

