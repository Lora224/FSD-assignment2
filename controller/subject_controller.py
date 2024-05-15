#Subject operations controller
#Enrolling, removal, save to student.data etc
#attributes:
#methods:

from subject import Subject
from database import Database
from termcolor import colored
#from student import Student

class SubjectController:
    def __init__(self):
        
        self.db = Database()
        self.path = 'student.csv'
       
        #print("Subject ID: ",self.subject.subject_id)
    def enrollSubject(self,subjectId,subject=Subject()):
        self.subject_id = subjectId
        self.mark = subject.getmark()
        self.grade = subject.getGrade()
        self.writeSubject()
        print(f'Subject ID:: {self.subject_id} -- Mark = : {self.mark} -- Grade =  {self.grade}')
        #self.printSubjectData()
    
    def writeSubject(self):
        data = f'{self.studentId},{self.subject_id},{self.mark},{self.grade}\n'
        self.db.write(data) #write student ID, subject ID, mark and grade to student.data

    def get_subject(self,studentID):       #TBD
        return self.db.read(self.db)
    
    def showSubjectData(self):
        print(colored(f'Showing {self.subject_count()} subjects\n','yellow'))
        subjects = self.get_subject(self.studentId)
        for subject in subjects:
           print(f'Subject ID:: {subject.subject_id} -- Mark = : {subject.mark} -- Grade =  {subject.grade}')
        
    def removeSubject(self,subjectId):
        self.db.remove(self.db,subjectId)
        print("Subject removed")
        
    def subject_count(self):
        return len(self.get_subject(studentId))    
#test
sc = SubjectController()
s = Subject()
s.subject_id = 100
sc.enrollSubject(s.subject_id)
#if input("Remove database? y/n") == "y":
#    sc.db.clear()

