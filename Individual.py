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


