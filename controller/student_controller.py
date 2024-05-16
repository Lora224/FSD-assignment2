#Student operation controller (combine with subject controller)
import re
import sys
import os
#import csv
import pandas as pd
import random as ran
from termcolor import colored #https://pypi.org/project/termcolor/ requried to install
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model.subject import Subject
from model.database import Database
#from subject_controller import SubjectController
#from student import Student


EMAIL_PATTERN= r'\b[A-Za-z]+@university\.com\b'
PASSWORD_PATTERN = r'\b[A-Z][A-Za-z]{5,}[0-9]{3,}\b'


class Validator:
    @staticmethod
    def match(email,password):
        return email==email and password == password
    
    @staticmethod
    def valid_email(email):
        return re.search(EMAIL_PATTERN,email)
    
    @staticmethod
    def valid_password(password):
        return re.fullmatch(PASSWORD_PATTERN,password)

class StudentController:
    def __init__(self):
        
        self.db = Database()
        #self.studentId = 123456 #example student ID
       
        #print("Subject ID: ",self.subject.subject_id)
    def enroll_subject(self,subjects):    #enroll subject
        s = Subject(111,0,'')             #create a new subject object
        s.get_subjectID()
        s.get_mark()
        s.grade = s.get_grade()
        data = [s.subject_ID,s.mark,s.grade] #parsed or not?
        subjects.append(data)
        #self.write_subject(data)
        self.print_subject(s) 
    
    def get_subject(self,student):              #turn subject into a list of objects
        s = []
        for subject in student['parsed_subjects']:
           s.append(Subject(subject[0],subject[1],subject[2]))
        return s
    
    def subject_count(self,subjects):           #count number of subjects enrolled
        return len(subjects)  
      
    def print_subject(self,subject):               #print newly enrolled subject data
        print(f'Subject ID:: {subject.subject_ID} -- Mark = : {subject.mark} -- Grade =  {subject.grade}')
    
    def show_subject_data(self,subjects):           #show all subjects enrolled by student 
        print(colored(f'Showing {len(subjects)} subjects\n','yellow'))
        for subject in subjects:                    #subject is an object of Subject
            print(f'Subject ID:: {subject[0]} -- Mark = : {subject[1]} -- Grade =  {subject[2]}')
           
    def remove_subject(self,subjectId,subjects):     #remove subject from subjects list
        for subject in subjects:
            print(subject[0])
            if str(subject[0]) == str(subjectId):
                subjects.remove(subject)
                print("Subject removed")
                return

        print('cannot find subject')
    
    def update_password (self, email, newPassword,confirmPassword):
        print(colored('Updating password','yellow'))
        if newPassword != confirmPassword:
            print(colored('Password does not match - try again','red'))
            self.update_password(email,newPassword,input('Confirm password: '))
        student = self.db.get_student_by_email(email)
        if student.empty is True:
            print(colored('Student not found','red')) 
        else:
            if Validator.valid_password(newPassword): #print success message
               #update db with new password
               self.db.update_student_password(email,newPassword)
               #print(colored('Your password is updated','green'))
            else:
                print(colored('Invalid new password','red'))
               
    def calculate_average_mark(self,subjects):
        total_mark = 0
        for s in subjects:
            total_mark += s[1]
        return total_mark/len(subjects)       
#test
# if __name__ == "__main__":
#   sc = StudentController()
#   subjects =[(321,100,'HD'),(322,75,'D'),(323,65,'C')]
  
# #   while input("Enroll subject? y/n") == "y":
# #       if len(subjects) < 4:
# #           sc.enroll_subject(subjects)
# #           sc.show_subject_data(subjects)
# #       else:
# #           print("Maximum number of subjects reached")
# #           break
# #   sc.remove_subject(input("Enter subject ID to remove: "),subjects)
# #   sc.show_subject_data(subjects)
# #   print(f'Average mark: {sc.calculate_average_mark(subjects)}')
  
# #   if input("Remove database? y/n") == "y":
# #      sc.db.clear()
#   db= Database()
#   student = db.get_student_by_email(input("Enter email: "))
#   newpwd = input("Enter new password: ")
#   #print(student)
#   #print(student['name'].values[0])
#   sc.update_password(student['email'].values[0],newpwd,newpwd)
  
  
  
  

  #Registering, login, choose subject, etc
