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
        print(colored("Student List", "yellow"))  
        students = self.db.get_student() 
        if not students:
            print("<Nothing to display>")
            return            
        for student in students:
            print(f"{student[1]} :: {student[0]} --> Email: {student[2]}")
    

    def remove_student(self,student_id):         
        if self.db.remove_student(student_id):
            print(colored(f"Removed Student {student_id} Account", "yellow"))
        else:
            print(colored(f"Student {student_id} does not exist", "red"))

        
    
    def partition(self):
        students = self.db.get_student()
        pass_student = []
        fail_student = []
        for student in students:
            if SC.calculate_average_mark(student[-1]) >= 50:
                pass_student.append(f'{student[1]} :: {student[0]} --> MARK:{SC.calculate_average_mark(student[-1])}')
            else:
                fail_student.append(f'{student[1]} :: {student[0]} --> MARK:{SC.calculate_average_mark(student[-1])}')
        print(colored('PASS/FAIL Partition', 'yellow'))
        print(f"FAIL --> [{'\n'.join(fail_student)}]")
        print(f"PASS --> [{'\n'.join(pass_student)}]")
        
    
    # # OP1
    # def group_student(self):
    #     students = self.db.get_student()
    #     students.sort(key=lambda student: SC.calculate_average_mark(student[-1]), reverse=True)
       
    #     print(colored("Grouping students by grade:", "yellow"))
    #     for student in students:
    #         print(colored(f"Student ID: {student[0]}, Name: {student[1]}, Grade: {SC.calculate_average_mark(student[-1])}.", 'yellow'))

    # OP2

    def group_student(self):
        students = self.db.get_student()

        HD_grade = []
        D_grade = []
        C_grade = []
        P_grade = []
        F_grade = [] 
        for student in students:  
            if SC.calculate_average_mark(student[-1]) >= 85:
                HD_grade.append(f'{student[1]} :: {student[0]} --> GRADE: HD - Mark: {SC.calculate_average_mark(student[-1])}')
            elif SC.calculate_average_mark(student[-1]) < 85 and SC.calculate_average_mark(student[-1]) >= 75:
                D_grade.append(f'{student[1]} :: {student[0]} --> GRADE: D - Mark: {SC.calculate_average_mark(student[-1])}')
            elif SC.calculate_average_mark(student[-1]) < 75 and SC.calculate_average_mark(student[-1]) >= 65:
                C_grade.append(f'{student[1]} :: {student[0]} --> GRADE: C - Mark: {SC.calculate_average_mark(student[-1])}')
            elif SC.calculate_average_mark(student[-1]) < 65 and SC.calculate_average_mark(student[-1]) >= 50:
                P_grade.append(f'{student[1]} :: {student[0]} --> GRADE: P - Mark: {SC.calculate_average_mark(student[-1])}')
            else:
                F_grade.append(f'{student[1]} :: {student[0]} --> GRADE: F - Mark: {SC.calculate_average_mark(student[-1])}')
       
        print(colored("Grade Grouping", "yellow"))
        if not students:
            print("<Nothing to display>")
            return
        print(f'HD --> {'\n'.join(HD_grade)}')
        print(f"D --> {'\n'.join(D_grade)}")
        print(f"C --> {'\n'.join(C_grade)}")
        print(f"P --> {'\n'.join(P_grade)}")
        print(f"F --> {'\n'.join(F_grade)}") 
  

    def clear_database(self,choice):        
        while True:
            choice = str(input(colored('Are you sure you want to clear the database (Y)ES/ (N)O: ', 'red')).upper())
            if choice == 'N':
                break                  
            elif choice == 'Y':
                self.db.clear()
                print(colored("Student data cleared", "yellow"))
                break
            else:
                print("Invalid choice. Please try again.")
            
            
   
    

# Running the main function
#student = Student()
#student.main()










