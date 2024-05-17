import tkinter as tk
from tkinter import messagebox
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model.database import Database
from model.student import Student
from controller.student_controller import StudentController as SC
class EnrollmentView(tk.Toplevel):
    def __init__(self, parent, email):
        super().__init__(parent)
        self.title("Enrollment System")
        self.geometry("300x200")

        self.db = Database()
        self.email = email

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Enroll in Subject").pack(pady=5)

        tk.Button(self, text="Enroll", command=self.enroll_subject).pack(pady=5)
        tk.Button(self, text="Back to Student View", command=self.back_to_student_view).pack(pady=5)

    def enroll_subject(self):
        # Add code to enroll student in the subject
        db = Database()
        sc = SC()
        student = self.db.get_student_by_email(self.email)
        subjects = []
        if student['subjects'].values[0] != ' ':
                   student['parsed_subjects'] = student['subjects'].apply(db.parse_subjects)
                   subjects = sc.get_subject(student['parsed_subjects'].values[0])

        subject = sc.enroll_subject(subjects)
        if(sc.subject_count(subjects)):
               db.update_student_subjects(self.email,subjects)

        tk.Label(self, text=f"Subject ID: {subject[-1][0]}, Mark: {subject[-1][1]}, Grade: {subject[-1][2]}").pack()
    def back_to_student_view(self):
        from subject_view import SubjectView 
        SubjectView(self.master, self.email).mainloop()

if __name__ == "__main__":

    app = tk.Tk()
    app.withdraw()
    EnrollmentView(app, "muzelyu@university.com").mainloop()
