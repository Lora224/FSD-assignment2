#Admin tasks handling controller
#viewing, grouping, partitioning students, clearing database, remove student
import re
import os
from termcolor import colored 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model.student import Student
from model.database import Database
from model.subject import Subject
from student_controller import StudentController as SC

# EMAIL_PATTERN = r'\b[A-Za-z]+@university\.com\b'
# PASSWORD_PATTERN = r'\b[A-Z][A-Za-z]{5,}[0-9]{3,}\b'

# class Validator:
#     @staticmethod
#     def valid_email(email):
#         return re.search(EMAIL_PATTERN, email)
    
#     @staticmethod
#     def valid_password(password):
#         return re.fullmatch(PASSWORD_PATTERN, password)
class AdminController:
    def __init__(self):        
        self.db = Database()

    def show_student(self,students):
        #Op1: create function show in student module: student.show()
        # def show(self):
        #for student in self.student:
        #   print(f"Student ID: {self.studentID()}, Name: {self.studentName()}.")
        #op2: 
        students = self.db.get_student()
        studentID = self.db.get_student_by_id    
        studentName = self.db.get_student_by_name     
        print(colored("Showing all students:", "yellow"))
        for student in students:
            print(colored(f"Student ID: {studentID()}, Name: {studentName()}.", 'yellow'))

    def remove_student(self,student_id):
        if self.db.remove_student(student_id):
            print(colored(f"Removed student with ID {student_id} from the database.", "yellow"))
        else:
            print(colored(f"Student with ID {student_id} does not exist in the database.", "red"))

        #Op2: 
        # studentID = self.db.get_studentID()
        # for studentID in self.studentID:
        #     if studentID.get_studentID() == studentID:
        #         studentID.remove(studentID)
        #         self.db.write_data(studentID)
        #         print(f'Student with student ID {studentID} has been removed.')
        #         return
        # print(f'Student with student ID {studentID} not found.')
    
    def partition(self,student):
        student = self.db.get_student()
        pass_student = []
        fail_student = []
        for student in student:
            if SC.calculate_average_mark() >= 50:
                pass_student.append(student)
            else:
                fail_student.append(student)
        print(colored(f"Pass students: {pass_student}",'yellow'))
        print(colored(f"Fail students: {fail_student}",'yellow'))
    
    def group_student(self,student):
        student = self.db.get_student()
        HD_grade = []
        D_grade = []
        C_grade = []
        P_grade = []
        F_grade = [] 
        for student in student:
            if SC.calculate_average_mark() >= 85:
                HD_grade.append(student)
            elif SC.calculate_average_mark() >= 75 & SC.calculate_average_mark() < 85 :
                D_grade.append(student)
            elif SC.calculate_average_mark() >= 65 & SC.calculate_average_mark() < 75 :
                C_grade.append(student)
            elif SC.calculate_average_mark() >= 50 & SC.calculate_average_mark() < 65 :
                P_grade.append(student) 
            else:
                F_grade.append(student)
        # for student in student:
        #     if Subject.get_grade() == 'HD':
        #         HD_grade.append(student)
        #     elif Subject.get_grade() == 'D':
        #         D_grade.append(student)
        #     elif Subject.get_grade() == 'C':
        #         C_grade.append(student)
        #     elif Subject.get_grade() == 'P':
        #         P_grade.append(student) 
        #     else:
        #         F_grade.append(student)
        print(colored(f"HD students: {len(HD_grade)}",'yellow'))
        print(colored(f"D students: {len(D_grade)}",'yellow'))
        print(colored(f"C students: {len(C_grade)}",'yellow'))
        print(colored(f"P students: {len(P_grade)}",'yellow'))
        print(colored(f"F students: {len(F_grade)}",'yellow')) 
  

    def clear_database(self):
        self.db.clear()
        print(colored("Cleared all student data.", "yellow"))
   
    

# Running the main function
#student = Student()
#student.main()

