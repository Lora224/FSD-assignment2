import tkinter as tk
import sys
import os
import re
import random as rd
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tkinter import messagebox
from enrollment_view import EnrollmentView
from exception_view import ExceptionView
from subject_view import SubjectView
from model.database import Database
from model.student import Student
from controller.student_controller import StudentController as SC

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

class MainView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("GUIUniApp - University System")
        self.geometry("600x300")

        self.db = Database()

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Email:").pack(pady=5)
        self.email_entry = tk.Entry(self)
        self.email_entry.pack(pady=5)

        tk.Label(self, text="Password:").pack(pady=5)
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack(pady=5)
        
        tk.Label(self, text="Name: ").pack(pady=5)
        self.name_entry = tk.Entry(self)
        self.name_entry.pack(pady=5)
        tk.Button(self, text="Login", command=self.login).pack(pady=5)
        tk.Button(self, text="Register", command=self.register).pack(pady=5)

    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        if not Validator.valid_email(email) or not Validator.valid_password(password):
            ExceptionView(self, "Invalid email or password format.").show()
            return 
        student = self.db.get_student_by_email(email)
        if not student.empty and student['password'].values[0] == password:
            messagebox.showinfo("Login", "Login successful!")
            self.open_student_view(email)
        if student.empty:
             ExceptionView(self, "Student does not exist").show()
        else:
             ExceptionView(self, "Invalid credentials. Please try again.").show()

    def register(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        if not Validator.valid_email(email) or not Validator.valid_password(password):
            ExceptionView(self, "Invalid email or password format.").show()
            return
        if self.db.get_student_by_email(email).empty:
            messagebox.showinfo("Input Name", "Please input your name.")
            with open(self.db.path, "a") as file:
                id = rd.randint(100000, 999999) 
                name = self.name_entry.get()
                file.write(f"{id},{name},{email},{password},\n")
            messagebox.showinfo("Register", "Registration successful!")
            self.open_student_view(email)
        else:
            ExceptionView(self, "Student already existed.").show()

    def open_student_view(self, email):
        self.withdraw()
        SubjectView(self, email).mainloop()

if __name__ == "__main__":
    app = MainView()
    app.mainloop()
