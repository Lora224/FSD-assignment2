#Student Class goes here
#attributes: ID, email, password?, subjects
#methods: 
import sys
import random as rd
import re
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model.database import Database
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
        self.subjects = ""
        self.db = Database()
        self.path = 'student.csv'
        
        
    def login(self,email,password):
        if Validator.match(email,password):
            #find corresponding student in student.csv
           if not Validator.valid_email(email) or not Validator.valid_password(password): #invalid email or password
               return False 
           df=pd.read_csv(self.path)
           pwd = df.loc[df['email'] == email,'password'].values[0]
           if pwd == password:
               return df.loc[df['email'] == email]           #return student data dataframe
           else:
               return False
    def register(self,email,password):
        if self.db.get_student_by_email(email).empty == False:
            print('Student already exists')
            return False                     # student already exists
        if Validator.valid_email(email) and Validator.valid_password(password):
            self.email = email
            self.password = password
            data = f'{self.ID},{self.name},{self.email},{self.password},{self.subjects}\n'
            self.db.write(data)
            
            return True
        else:
            print('Invalid Email or Password')
            return False #invalid email or password
    
    def input_name(self):
        self.name = input("Name: ")
        
        
# if __name__ == "__main__":
#     s = Student()
#     email =input("Enter email: ")
#     password = input("Enter password: ")
#     if s.register(email,password):
#         print("Register successful")
#         name = input("Enter name: ")
#         data = f'{s.ID},{s.name},{s.email},{s.password},{s.subjects}\n'
#         s.db.write(data)
#     else:
#         print("Register failed")
#     if input("Login? y/n") == "y":
#         email =input("Enter email: ")
#         password = input("Enter password: ")
#         if s.login(email,password):
#             print("Login successful")
#         else:
#             print("Login failed")