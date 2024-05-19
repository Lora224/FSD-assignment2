#CLI main file for CLIUNIApp
# university 
# student_system
# student_course
# admin system
import sys
import os
import re

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model.subject import Subject
from model.database import Database
from model.student import Student
from controller.student_controller import StudentController as SC
from controller.admin_controller import AdminController as AC
from termcolor import colored


EMAIL_PATTERN= r'\b[A-Za-z]+@university\.com\b'
PASSWORD_PATTERN = r'\b[A-Z][A-Za-z]{5,}[0-9]{3,}\b'


class Validator:
    @staticmethod
    def match(email,password):
        return email== email and password == password
    
    @staticmethod
    def valid_email(email):
        return re.search(EMAIL_PATTERN,email)
    
    @staticmethod
    def valid_password(password):
        return re.fullmatch(PASSWORD_PATTERN,password)

def student_system():
    while True:
          db=Database()
          student = Student()
          sc = SC()
          student_choice = input(colored("Student System(l/r/x) : ","light_cyan")).upper()
          if student_choice == 'L':
              print(colored("Student Sign In","green"))
              email = input("Enter email: ")
              password = input("Enter password: ")
              if student.login(email,password):
                subjects =[]
                s = db.get_student_by_email(email)
                student.email = s['email'].values[0]
                student.password = s['password'].values[0]
                student.name = s['name'].values[0]
                if s['subjects'].values[0] != ' ':
                   s['parsed_subjects'] = s['subjects'].apply(db.parse_subjects)
                   subjects = sc.get_subject(s['parsed_subjects'].values[0])
                   student.subjects = s['subjects'].values[0]
                student_course_system(student,subjects)
          elif student_choice == 'R':
              print(colored("Student Sign Up","green"))
              email = input("Enter email: ")
              password = input("Enter password: ")
              if student.register(email,password):
                s = db.get_student_by_email(email)  
                student.email = email
                student.password = password
                student.id = s['studentID'].values[0]
                student.name = s['name'].values[0]
                subjects = []
                student_course_system(student,subjects)
          elif student_choice == 'X':
              break




        
def student_course_system(student,subjects):
    while True:
      sc = SC()
      db = Database()
      #print(f'[Student: {student.name},Subjects: {student.subjects},Password: {student.password}')
      student_choice=input(colored("Student Course System(c/e/r/s/x): ","light_cyan")).upper()
      if student_choice == 'S':
            sc.show_subject_data(subjects)
      if student_choice == 'E':
            if sc.subject_count(subjects)<4:
                subjects  = sc.enroll_subject(subjects)  
                print(colored(f'You are now enrolled in {sc.subject_count(subjects)} out of 4 subjects' ))
            else:
                print(colored("Students are allowed to enrol in 4 subjects only","red"))
      if student_choice == 'R':
            subjectID = input("Remove Subject by ID: ")
            sc.remove_subject(subjectID,subjects)
            print(colored(f'You are now enrolled in {sc.subject_count(subjects)} out of 4 subjects' ))
      if student_choice == 'C':
            print(colored("Updating Password","yellow"))
            new_password = input("New password: ")
            confirm_password = input("Confirm Password: ")
            sc.update_password(student.email,new_password,confirm_password)
      elif student_choice == 'X':
            if(sc.subject_count(subjects)):
               db.update_student_subjects(student.email,subjects)
            break
       
def admin_system():
    while True:
        db=Database()    
        ac = AC()
        admin_choice = input(colored("Admin System(c/g/p/r/s/x) : ","light_cyan")).upper()
        if admin_choice == 'C':
            # print(colored('Clearing students database', 'yellow'))
            ac.clear_database(print(colored('Clearing students database', 'yellow')))   
        elif admin_choice == 'G':
            ac.group_student()              
        elif admin_choice == 'P':
            ac.partition()
        elif admin_choice == 'R':
            ac.remove_student(int(input('Remove by ID: ')))
        elif admin_choice == 'S':
            ac.show_student()                      
        elif admin_choice == 'X':
              break
def main():
    while True:
        #display_university_menu()
        university_choice = input(colored("University System: (A)Admin, (S)tudent, or X : ","light_cyan")).upper()
        
        if university_choice == 'A':
            admin_system()
        elif university_choice == 'S':
            #student = Student()
            student_system()
            
        elif university_choice == 'X':
            print("Thank You")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
   main()
