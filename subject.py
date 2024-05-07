#Subject class
#attributes: SubjectID, Mark, Grade
#methods:getGrade, getSubjectID

#from database import Database
import random as rd
class Subject:
    def __init__(self):
       # self.subject_id = self.getSubjectID()
       self.subject_id= 000
       self.mark = 0
       self.grade = 0
        
    #return subject id and mark
    def __str__(self):
        return f'Subject ID:: {self.subject_id} -- Mark = : {self.mark} -- Grade =  {self.grade}'
    def getmark(self):        
        self.mark = rd.randint(25,100)
        return self.mark
    def getGrade(self):
        if self.mark >= 85:
            return "HD"
        elif self.mark >= 75 & self.mark < 85:
            return "D"
        elif self.mark >= 65 & self.mark < 75:
            return "C"
        elif self.mark >= 50 & self.mark < 65:
            return "P"
        else:
            return "F"
    def getSubjectID(self):
        randnum = str(rd.randint(1,999))
        print("subject.py Subject ID: ",randnum.zfill(3))
        return randnum.zfill(3)


#s = Subject()
#print(s)
#write to database tested and working
#db= Database()
#Database.write(db,s.subject_id + " " + str(s.mark) + " " + s.grade + "\n")