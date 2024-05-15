#Student operation controller (combine with subject controller)
import re
import sys
#import csv
import pandas as pd
import random as ran
from termcolor import colored #https://pypi.org/project/termcolor/ requried to install

sys.path.insert(0, './model')
from subject import Subject
from database import Database
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
    def enroll_subject(self,s=Subject()):    #enroll subject
        self.subject_id = s.subject_ID
        self.mark = s.mark
        self.grade = s.grade
        self.writeSubject()
        self.printSubjectData() 
    
    def write_subject(self,data):          #write stuent ID, subject ID, mark and grade to student.data
  
        self.db.write(data) 

    def get_subject(self):                 #read subject data from student.data
        return self.db.read(self.db)
    
    def print_subject(self):               #print newly enrolled subject data
        print(f'Subject ID:: {self.subject_id} -- Mark = : {self.mark} -- Grade =  {self.grade}')
        
    def remove_subject(self,subjectId):
        self.db.remove_subject(subjectId)      #remove subject from student.data
        print("Subject removed")
    

    def update_password (self, email, newPassword,confirmPassword):
        if newPassword != confirmPassword:
            print(colored('Passwords do not match - try again','red'))
            self.update_password(email,newPassword,input('Confirm password: '))
        student = self.db.get_student(email)
        if student is None:
            print(colored('Student not found','red')) 
        else:
            if Validator.valid_password(newPassword): #print success message
               #update db with new password
               self.db.update_student(email,newPassword)
               #print(colored('Your password is updated','green'))
               
    def calculate_average_mark(self):
        student = self.db.get_student()          #get marks from the subjectlist
        total_mark = 0
        for student in student:
            total_mark += student.mark
        return total_mark/len(student)       
#test
sc = StudentController()
s = Subject()
sc.enroll_subject(s.subject_id)
#if input("Remove database? y/n") == "y":
#    sc.db.clear()
print(colored('Print test','green')) #test printing color

#Registering, login, choose subject, etc
