#Subject class
#attributes: SubjectID, Mark, Grade
#methods:getGrade, get_subjectID

#from database import Database
import random as rd
class Subject:
        
    def __init__(self,subjectID,mark,grade):
       # self.subject_id = self.get_subjectID()
       self.subject_ID = subjectID
       self.mark = int(mark)
       self.grade = grade
        
    #return subject id and mark
    def __str__(self):
        return f'Subject ID:: {self.subject_ID} -- Mark = : {self.mark} -- Grade =  {self.grade}'
    def get_mark(self):        
        self.mark = rd.randint(25,100)
        return self.mark
    def get_grade(self,mark):
        if mark >= 85:
            return "HD"
        elif mark >= 75 and mark < 85:
            return "D"
        elif mark >= 65 and mark < 75:
            return "C"
        elif mark >= 50 and mark < 65:
            return "P"
        else:
            return "F"
        
    def get_subjectID(self):
        randnum = str(rd.randint(1,999))
        self.subject_ID = randnum.zfill(3)
        #print("subject.py Subject ID: ",randnum.zfill(3))
        return self.subject_ID

# if __name__ == "__main__":
#     s = Subject("1",90,"HD")
#     x= int(input("Enter mark: "))
#     print(s.get_grade(x))

#s = Subject()
#print(s)
#write to database tested and working
#db= Database()
#Database.write(db,s.subject_id + " " + str(s.mark) + " " + s.grade + "\n")