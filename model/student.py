#Student Class goes here
#attributes: ID, email, password?, subjects
#methods: 
import sys
import random as rd
import re
sys.path.insert(0, './model')
import subject as Subject
import database as Database
import pandas as pd
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
class Student:
    def __init__ (self): 
        self.ID = rd.randint(100000,999999)         #random 6 digit student ID
        self.name = 'John Smith'
        self.email = 'johnsmith@univerisity.com' #default email
        self.password = 'Abcdef123'              #default password
        self.subjects = []
        self.db = Database()
        self.path = 'student.csv'
        
    def __init__ (self, studentID, name, email, password,subjects):
        self.ID = studentID
        self.name = name
        self.email = email
        self.password = password
        self.subjects = subjects
        
    def login(self):
        if Validator.match(email,password):
            #find corresponding student in student.csv
           df=pd.read_csv(self.path)
           pwd = df.loc[df['email'] == email,'password']
           if pwd == password:
               return True
           else:
               return False
    def input_name(self):
        self.name = input("Name: ")