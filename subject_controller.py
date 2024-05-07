#Subject operations controller
#Enrolling, removal, save to student.data etc
#attributes:
#methods:

from subject import Subject
from database import Database
#from student import Student

class SubjectController:
    def __init__(self):
        
        self.db = Database()
        self.studentId = 123456 #exampe student ID
       
        #print("Subject ID: ",self.subject.subject_id)
    def enrollSubject(self,subjectId,subject=Subject()):
        self.subject_id = subjectId
        self.mark = subject.getmark()
        self.grade = subject.getGrade()
        self.writeSubject()
        self.printSubjectData()
    
    def writeSubject(self):
        data = f'{self.studentId},{self.subject_id},{self.mark},{self.grade}\n'
        self.db.write(data) #write student ID, subject ID, mark and grade to student.data

    def getSubjectData(self):
        return self.db.read(self.db)
    
    def printSubjectData(self):
        print(f'Subject ID:: {self.subject_id} -- Mark = : {self.mark} -- Grade =  {self.grade}')
        
    def removeSubject(self,subjectId):
        self.db.remove(self.db,subjectId)
        print("Subject removed")
        
#test
sc = SubjectController()
s = Subject()
s.subject_id = 100
sc.enrollSubject(s.subject_id)
#if input("Remove database? y/n") == "y":
#    sc.db.clear()

