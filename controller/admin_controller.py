#Admin tasks handling controller
#viewing, grouping, partitioning students, clearing database, remove student
import re
import os
import sys
from termcolor import colored 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model.student import Student
from model.database import Database
from model.subject import Subject
from controller.student_controller import StudentController as SC

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

    def show_student(self):        
        print(colored("Showing all students:", "yellow"))               
        for student in self.db.get_student():
            print(colored(f"Student ID: {student[0]}, Name: {student[1]}, Mail: {student[2]}.", 'yellow'))
    

    def remove_student(self,student_id):         
        if self.db.remove_student(student_id):
            print(colored(f"Removed student with ID {student_id} from the database.", "yellow"))
        else:
            print(colored(f"Student with ID {student_id} does not exist in the database.", "red"))

        
    
    def partition(self):
        students = self.db.get_student()
        pass_student = []
        fail_student = []
        for student in students:
            if SC.calculate_average_mark(student[-1]) >= 50:
                pass_student.append(student)
            else:
                fail_student.append(student)
        print(colored(f"Pass students: {pass_student}",'yellow'))
        print(colored(f"Fail students: {fail_student}",'yellow'))
    
    
    def group_student(self):
        students = self.db.get_student()
        students.sort(key=lambda student: SC.calculate_average_mark(student[-1]), reverse=True)

        print(colored("Grouping students by grade:", "yellow"))
        for student in students:
            print(colored(f"Student ID: {student[0]}, Name: {student[1]}, Grade: {SC.calculate_average_mark(student[-1])}.", 'yellow'))

    # def group_student(self):
    #     student = self.db.get_student()
    #     HD_grade = []
    #     D_grade = []
    #     C_grade = []
    #     P_grade = []
    #     F_grade = [] 
    #     for student in student:
    #         if SC.calculate_average_mark(student[-1]) >= 85:
    #             HD_grade.append(student)
    #         elif SC.calculate_average_mark(student[-1]) >= 75 & SC.calculate_average_mark(student[-1]) < 85 :
    #             D_grade.append(student)
    #         elif SC.calculate_average_mark(student[-1]) >= 65 & SC.calculate_average_mark(student[-1]) < 75 :
    #             C_grade.append(student)
    #         elif SC.calculate_average_mark(student[-1]) >= 50 & SC.calculate_average_mark(student[-1]) < 65 :
    #             P_grade.append(student) 
    #         else:
    #             F_grade.append(student)
       
    #     print(colored(f"HD students: {len(HD_grade)}",'yellow'))
    #     print(colored(f"D students: {len(D_grade)}",'yellow'))
    #     print(colored(f"C students: {len(C_grade)}",'yellow'))
    #     print(colored(f"P students: {len(P_grade)}",'yellow'))
    #     print(colored(f"F students: {len(F_grade)}",'yellow')) 
  

    def clear_database(self):
        self.db.clear()
        print(colored("Cleared all student data.", "yellow"))
   
    

# Running the main function
#student = Student()
#student.main()










