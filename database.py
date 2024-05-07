#database class goes here

#checks if student.data exists √
#creates student.data if it does not exist √
#write object to student.data √
#read object from student.data √
#clear student.data √

#verify student credentials?
#update password?

#subject, student controllers etc intereact with student.data

import os
class Database:
    def __init__(self):
        self.path = 'student.data'
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
           