from abc import ABCMeta, abstractmethod
import json
class Individual(object):
    __metaclass__ = ABCMeta

    def __init__(self, IndividualBase):
        self.GeneralData = json.load(open(IndividualBase))
        self.height = self.GeneralData["height"]
    
    @abstractmethod
    def printName(self):
        print ''#self.GeneralData

    @abstractmethod
    def getHeight(self):
        return self.GeneralData["height"]

    @abstractmethod
    def getWeight(self):
        return self.GeneralData["weight"]

    @abstractmethod
    def getAnxietyLevel(self):
        return self.GeneralData["anxiety"]


    @abstractmethod
    def getLanguages(self):
        return self.GeneralData["languages"]




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
#class Graph:
#   def __init__():
#       self.ref = 
