from abc import ABCMeta, abstractmethod
from Personality import *
import json
class Individual(object):
    __metaclass__ = ABCMeta

    def __init__(self, IndividualBase):
        self.GeneralData = json.load(open(IndividualBase))
        self.setPersonality()
    
    @abstractmethod
    def printName(self):
        for attribute, value in self.GeneralData.iteritems():
            print attribute, value

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

    @abstractmethod
    def setPersonality(self):
        self.setPersonality = Personality( self.GeneralData["fear"],self.GeneralData["humor"],
                                self.GeneralData["love"], self.GeneralData["confidence"],
                                self.GeneralData["esteem"], self.GeneralData["cockiness"], 
                                self.GeneralData["sexiness"])
    @abstractmethod
    def getPersonality(self):
        return self.GeneralData