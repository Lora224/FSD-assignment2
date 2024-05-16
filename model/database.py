#database class goes here

#checks if student.data exists √
#creates student.data if it does not exist √
#write object to student.data √
#read object from student.data √
#clear student.data √

#verify student credentials?
#update password?

#subject, student controllers etc intereact with student.data
import pandas as pd
import os

class Database:
    def __init__(self):
        self.path = 'student.csv'
        if not os.path.isfile(self.path):
            with open(self.path, "x") as file:
                pass

    def write(self, data):
        with open(self.path, "a") as file:
            file.write(data)
            
    def read(self):
        with open(self.path, "r") as file:
            return file.readlines()
        
    def clear(self):
        open(self.path, "w")
        
    def remove_student(self,studentID):
        df = pd.read_csv(self.path)
        tmp = df.loc[df['studentID'] == studentID]
        if tmp.empty:
            return False
        df = df.drop(df[(df['studentID']==studentID)].index)
        df.to_csv(self.path, index=False)
        return True
        
    def parse_subjects(self,subject_str):
        subjects = subject_str.split(';')
        return [subject.split(':') for subject in subjects]

    def get_student(self):
        df = pd.read_csv(self.path)
        students = []
        for index, row in df.iterrows():
            student = [row['studentID'],row['name'], row['email'], row['password'],row['subjects'].split(';')]
            students.append(student)
        #students.append
       # students['parsed_subjects'] = students['subjects'].apply(self.parse_subjects)
        return students   
    
    def get_student_by_email(self,email):
        df = pd.read_csv(self.path)
        student = df.loc[df['email'] == email].copy()
        student['parsed_subjects'] = student['subjects'].apply(self.parse_subjects)
        return student
    def get_student_by_id(self,studentID):
        df = pd.read_csv(self.path)
        student = df.loc[df['studentID'] == studentID].copy()
        student['parsed_subjects'] = student['subjects'].apply(self.parse_subjects)
        return student
    def update_student_password(self,email,newPassword):
        df = pd.read_csv(self.path)
        df.loc[df['email'] == email, 'password'] = newPassword
        df.to_csv(self.path, index=False)     
    def update_student_subjects(self,email,subjects):
        df = pd.read_csv(self.path)
        s =''
        for subject in subjects:
            subject_str = f'{subject[0]}:{subject[1]}:{subject[2]}'
            s = s + subject_str + ';'
        df.loc[df['email'] == email, 'subjects'] = s
        df.to_csv(self.path, index=False)

if __name__ == "__main__":
  db=Database()

  #print (df.columns)          #giving double output?
#   print('get student by email') #working
#   student = db.get_student_by_email('janedoe@university.com')
#   print(f'Student ID :: {student['studentID'].values[0]} -- Name: {student['name'].values[0]} ')
#   for subject in student['parsed_subjects'].values[0]:
#      print(f'Subject ID: {subject[0]} -- Mark: {subject[1]} -- Grade: {subject[2]}')

  subjects = [['111', 85, 'HD'], ['222', 75, 'D'], ['333', 0, 'F']]
  db.update_student_subjects('janedoe@university.com',subjects)
  
#   print('get student')
#   print (db.get_student()) #working
#   id = input('Remove student by ID:') #working
#   db.remove_student(id)