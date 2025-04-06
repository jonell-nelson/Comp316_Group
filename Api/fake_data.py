import pandas as pd
from faker import Faker
import random 

fake = Faker()  

course_names = {
        "COMP": ["Intro to Computing", "Data Structures", "Algorithms", "Operating Systems", "Software Engineering", "Database Systems", "Artificial Intelligence", "Computer Networks"],
        "PHYS": ["General Physics", "Mechanics", "Electromagnetism", "Thermodynamics", "Quantum Physics", "Optics", "Nuclear Physics"],
        "MATH": ["Calculus I", "Calculus II", "Linear Algebra", "Discrete Mathematics", "Probability Theory", "Abstract Algebra", "Differential Equations"],
        "CHEM": ["General Chemistry", "Organic Chemistry", "Inorganic Chemistry", "Physical Chemistry", "Analytical Chemistry", "Biochemistry"],
        "BIOL": ["Intro to Biology", "Genetics", "Microbiology", "Cell Biology", "Ecology", "Human Anatomy", "Evolution"],
        "ECON": ["Microeconomics", "Macroeconomics", "Econometrics", "Public Economics", "International Economics", "Game Theory"],
        "PSYC": ["Intro to Psychology", "Developmental Psychology", "Social Psychology", "Abnormal Psychology", "Cognitive Psychology"],
        "HIST": ["World History", "Ancient Civilizations", "Modern History", "American History", "European History"],
        "ENGL": ["English Composition", "Creative Writing", "Literary Analysis", "Shakespeare Studies", "Modern Literature"],
        "PHIL": ["Intro to Philosophy", "Ethics", "Logic", "Philosophy of Mind", "Political Philosophy"],
        "STAT": ["Intro to Statistics", "Probability and Statistics", "Regression Analysis", "Statistical Inference", "Time Series Analysis"],
        "SOCI": ["Intro to Sociology", "Social Theory", "Urban Sociology", "Sociology of Education", "Gender Studies"],
        "GEOG": ["Physical Geography", "Human Geography", "Cartography", "Geographical Information Systems", "Environmental Geography"],
        "ARTS": ["Art History", "Painting Techniques", "Sculpture Basics", "Modern Art", "Photography"],
        "MUSC": ["Music Theory", "History of Music", "Composition", "Instrumental Techniques", "Choral Studies"]
        }

subject_codes = [
"COMP",  # Computer Science
"PHYS",  # Physics
"MATH",  # Mathematics
"CHEM",  # Chemistry
"BIOL",  # Biology
"ECON",  # Economics
"PSYC",  # Psychology
"HIST",  # History
"ENGL",  # English
"PHIL",  # Philosophy
"STAT",  # Statistics
"SOCI",  # Sociology
"GEOG",  # Geography
"ARTS",  # Arts
"MUSC",  # Music
]

def insert_person(type,num):
    data = {}
    if type == "Student":
        ids = [fake.unique.random_int(min=62000000000, max=62099999999) for _ in range(num)]
       
        first = [fake.first_name() for x in range(0,num)]
        last = [fake.last_name() for x in range(0,num)]

        data["StudentID"] = ids
        data["First Name"] = first
        data["Last Name"] = last
                                
        return data
    
    elif type == "Lecturer":
        ids = [fake.unique.random_int(min=1000000, max=1009999) for _ in range(num)]
       
        name = [fake.name() for _ in range(0,num)]

        departs = [random.choice(subject_codes) for _ in range(0,num) ]
        data["LecturerID"] = ids
        data["Lecturer Name"] = name

        return data
    
    elif type == "Admin":
        ids = [fake.unique.random_int(min=99900000, max=99999999) for _ in range(num)]
       
        name = [fake.name() for _ in range(0,num)]

        departs = [random.choice(subject_codes) for _ in range(0,num) ]
        data["AdminID"] = ids
        data["Admin Name"] = name

        return data

def insert_course(num):
    data = {}
    def generate_course_data(num):
        
        course_name = []
        course_code = []

        def generate_course_number():
            first_digit = random.choice(['1', '2', '3'])
            remaining_digits = ''.join(random.choices('0123456789', k=3))
            return first_digit + remaining_digits


        courses = [f"{random.choice(subject_codes)} {generate_course_number()}" for _ in range(num)]
        
        for course in courses:
            subject_code = course.split()[0]
            course_title = random.choice(course_names.get(subject_code, ["Special Topics"]))
            course_code.append(course)
            course_name.append(course_title)

        return courses,course_name
    
    ids = [fake.unique.random_int(min=0, max=99999) for _ in range(num)]
    course,course_title  = generate_course_data(num)

    data["Course ID"] = ids
    data["Course Name"] = course_title
    data["Course Code"] = course

    return data

def teaches(lecturers,courses):
    lec_data,course_data = [],[]

    if not(len(lecturers) < len(courses)):
        print("Number of courses must exceed number of lecturers")
        exit(0)
    if not((5 * len(lecturers)) >= len(courses)):
        print("Number of courses must be less or equal to that 5 times number of lecturers")
        exit(0)
    random.shuffle(courses)

    for i, lecturer in enumerate(lecturers):
        lec_data.append(lecturer)
        course_data.append(courses[i]) 

    for course in courses[len(lecturers):]:
        lec_data.append(random.choice(lecturers))
        course_data.append(course) 
    
    data = pd.DataFrame({
        "Course ID": course_data,
        "Lecturer ID": lec_data
        })

    return data

def enroll(students,courses):
    stu_data,course_data,grade = [],[],[]
    
    for course in courses:

        student = (random.choice(students))
        num_course = random.randint(3,3)
    
        for _ in range(num_course):
            stu_data.append(student)
            course_data.append(random.choice(courses)) 
    
    data = pd.DataFrame({
        "CourseID": course_data,
        "StudentID": stu_data,
        })
    
    return data


def inserts(students,lecturers,courses,teach,enroll):       
    with open('Api/Sql_inserts.sql',"w") as sql:

        print("-- Inserting into Student Table --")

        for i in range(len(students["StudentID"])):
            sql.write(f"INSERT INTO Student (StudentID, FirstName, LastName) VALUES ('{students['StudentID'][i]}', '{students['First Name'][i]}', '{students['Last Name'][i]}');\n")
        
        sql.write("\n-- Inserting into Lecturer Table\n")

        for i in range(len(lecturers["LecturerID"])):
            sql.write(f"INSERT INTO Lecturer (LecID, LecName, Department) VALUES ('{lecturers['LecturerID'][i]}', '{lecturers['Lecturer Name'][i]}', '{lecturers['Department'][i]}');\n")
        
        sql.write("\n-- Inserting into Course Table\n")

        for i in range(len(courses["Course ID"])):
            sql.write(f"INSERT INTO Course (CourseID, CourseName, CourseCode) VALUES ('{courses['Course ID'][i]}', '{courses['Course Name'][i]}', '{courses['Course Code'][i]}');\n")
        
        sql.write("\n-- Inserting into Teaches Table\n")

        for i in range(len(teach["Course ID"])):
            sql.write(f"INSERT INTO Teaches (CourseID, LecID) VALUES ('{teach['Course ID'][i]}', '{teach['Lecturer ID'][i]}');\n")
        
        sql.write("\n-- Inserting into Enroll Table --\n")
        for i in range(len(enroll["StudentID"])):
            sql.write(f"INSERT INTO Enroll (StudentID, CourseID, Grade) VALUES ('{enroll['StudentID'][i]}', '{enroll['CourseID'][i]}', '{enroll['Grade'][i]}');\n")


    print("-- SQL insert statements successfully written --")


if __name__ == '__main__':

    students = pd.DataFrame(insert_person("Student",100000))
    Lecturers = pd.DataFrame(insert_person("Lecturer",2))
    admin = pd.DataFrame(insert_person("Admin",1))
    courses = pd.DataFrame(insert_course(8))
    #teach = teaches(Lecturers.loc[:,("LecturerID")],courses.loc[:,"Course ID"])
    #grade = enroll(students["StudentID"],courses["Course ID"])



    #inserts(students,Lecturers,courses,teach,grade)

    print(students)
    print("\n")
    print(Lecturers)
    print("\n")
    print(admin)
    print("\n")
    print(courses)