#See subject list for enrolling
import tkinter as tk
from tkinter import messagebox
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from enrollment_view import EnrollmentView
from model.database import Database

class SubjectView(tk.Toplevel):
    def __init__(self, parent, email):
        super().__init__(parent)
        self.title("Student View")
        self.geometry("300x200")

        self.db = Database()
        self.email = email

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Enrolled Subjects").pack(pady=5)
        subjects = self.db.get_student_by_email(self.email)['parsed_subjects'].values[0]
        for subject in subjects:
            tk.Label(self, text=f"Subject ID: {subject[0]}, Mark: {subject[1]}, Grade: {subject[2]}").pack()
         
        tk.Button(self, text="Enroll in Subject", command=self.open_enrollment_view).pack(pady=5)
        tk.Button(self, text="Logout", command=self.logout).pack(pady=5)

    def open_enrollment_view(self):
        subjects = self.db.get_student_by_email(self.email)['parsed_subjects'].values[0] 
        self.withdraw()
        if len(subjects) == 4:
            messagebox.showerror("Enrollment Error", "Student can't enroll in more than 4 subjects.")
            SubjectView(self, self.email).mainloop()
            return
        
        EnrollmentView(self, self.email).mainloop()

    def logout(self):
        self.destroy()
        self.master.deiconify()

if __name__ == "__main__":
    app = tk.Tk()
    app.withdraw()
    SubjectView(app, "muzelyu@university.com").mainloop()
