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
import student as Student
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
        
    #def remove_student(self,studentID):
    #    df = pd.read_csv(self.path)
    #    df = df.drop(df[(df['studentID']==studentID)].index)
    #    df.to_csv(self.path, index=False)
        

    def get_student(self):
        df = pd.read_csv(self.file_path)
        students = []
        for index, row in df.iterrows():
            student = Student (row['studentID'],row['name'], row['email'], row['password'], row['subjects'].split(';'))
            students.append(student)
        return students   
    def get_student(self,email):
        df = pd.read_csv(self.path)
        return df.loc[df['email'] == email]
    def update_student(self,email,newPassword):
        df = pd.read_csv(self.path)
        df.loc[df['email'] == email, 'password'] = newPassword
        df.to_csv(self.path, index=False)


db=Database()
df = pd.read_csv(db.path)        #has problem reading the new file
print (df.columns)
def parse_subjects(subject_str):
    subjects = subject_str.split(';')
    return [subject.split(':') for subject in subjects]
df['parsed_subjects'] = df['subjects'].apply(parse_subjects)
print(df[['studentID', 'name', 'email', 'parsed_subjects']])
print (df.columns)
#print(db.get_student('johnsmiths@university.com'))
#print (db.get_student())