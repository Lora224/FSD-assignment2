#Admin tasks handling controller
#viewing, grouping, partitioning students, clearing database, remove student

from student import Student
from database import Database
from subject import Subject
#from config import DTF,NOW

class AdminController:
    def __init__(self):
        self.name = "Admin"
        self.db = Database()

    def show_student(self,student):
        #student.show()
        student = self.db.get_student()
        #### get student =???
        for student in self.student:
            print(f"Student ID: {self.studentID()}, Name: {self.studentName()}.")

    def remove_student(self,studentID):
        #student.remove()
        studentID = self.db.get_studentID()
        for studentID in self.studentID:
            if studentID.get_studentID() == studentID:
                studentID.remove(studentID)
                self.db.write_data(studentID)
                print(f'Student with student ID {studentID} has been removed.')
                return
        print(f'Student with student ID {studentID} not found.')
    
    def partition(self,student):
        student = self.db.get_student()
        pass_student = []
        fail_student = []
        for student in student:
            if student.calculate_average_mark() >= 50:
                pass_student.append(student)
            else:
                fail_student.append(student)
        print(f"Pass students: {len(pass_student)}")
        print(f"Fail students: {len(fail_student)}")
    
    def group_student(self,student):
        student = self.db.get_student()
        HD_grade = []
        D_grade = []
        C_grade = []
        P_grade = []
        F_grade = [] 
        for student in student:
            if student.calculate_average_mark() >= 85:
                HD_grade.append(student)
            elif student.calculate_average_mark() >= 75 & student.calculate_average_mark() < 85 :
                D_grade.append(student)
            elif student.calculate_average_mark() >= 65 & student.calculate_average_mark() < 75 :
                C_grade.append(student)
            elif student.calculate_average_mark() >= 50 & student.calculate_average_mark() < 65 :
                P_grade.append(student) 
            else:
                F_grade.append(student)
        print(f"HD students: {len(HD_grade)}")
        print(f"D students: {len(D_grade)}")
        print(f"C students: {len(C_grade)}")
        print(f"P students: {len(P_grade)}")
        print(f"F students: {len(F_grade)}") 
  

    def clear_database(self):
        self.db.clear_data()
        print("Database has been cleared.")
   
    def read_choice(self):
        print("Admin System (c/g/p/r/s/x): ", end="")
        return input().strip().lower()
    
    def use(self,admin):
        print(f"{self.name} Admin system:")
        choice = ''

        while True:
            choice = self.read_choice()
            if choice == 'x':
                break
            elif choice == 's':
                self.show_student(student)
            elif choice == 'r':
                self.remove_student(student)
            elif choice == 'p':
                self.partition(student)
            elif choice == 'g':
                self.group_student(student)
            elif choice == 'c':
                self.clear_database(student)
            else:
                self.help()
        print("Back to University system")

    def help(self):
        print("Admin System")
        print("Please choose an option:")
        print("(c) Clear Database File")
        print("(g) Group Students")
        print("(p) Partition Students")
        print("(r) Remove Student")
        print("(s) Show Students")
        print("(x) Exit")

# Running the main function
#student = Student()
#student.main()
