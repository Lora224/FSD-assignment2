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
    def get_grade(self):
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
        
    def get_subjectID(self):
        randnum = str(rd.randint(1,999))
        self.subject_ID = randnum.zfill(3)
        #print("subject.py Subject ID: ",randnum.zfill(3))
        return self.subject_ID



#s = Subject()
#print(s)
#write to database tested and working
#db= Database()
#Database.write(db,s.subject_id + " " + str(s.mark) + " " + s.grade + "\n")