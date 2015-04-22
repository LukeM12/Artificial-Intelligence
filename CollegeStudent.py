
from Individual import *
from Personality import *

class CollegeStudent(Individual):

    def printName(self):
        super(CollegeStudent, self).printName()
        return True

    def getHeight(self):
        return super(CollegeStudent, self).getHeight()

    def getWeight(self):
        return super(CollegeStudent, self).getWeight()

    def getAnxietyLevel(self):
        return super(CollegeStudent, self).getAnxietyLevel()
    
    def getLanguages(self):
        return super(CollegeStudent, self).getLanguages()
    
    def setPersonality(self):
        return super(CollegeStudent, self).setPersonality()
    
    def getPersonality(self):
        return super(CollegeStudent, self).getPersonality()
        

