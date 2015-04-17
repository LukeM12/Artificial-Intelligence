
from PersonBase import *
class CollegeStudent(Individual):

    def printName(self):
        super(CollegeStudent, self).printName()
        return True
    def printName(self):
        super(CollegeStudent, self).printName()
    
    def getHeight(self):
        return super(CollegeStudent, self).getHeight()

    def getWeight(self):
        return super(CollegeStudent, self).getWeight()

    def getAnxietyLevel(self):
        return super(CollegeStudent, self).getAnxietyLevel()
    
    def getLanguages(self):
        return super(CollegeStudent, self).getLanguages()

class Mode:
    #instantiate the node with a memory
    def __init__(event):
        self.event = event

