
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

def View_Courses_by_Student(User_id):
    pass
    
    
def View_Courses_by_Lecturer(User_id):
    pass