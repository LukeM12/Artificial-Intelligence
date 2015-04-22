
from CollegeStudent import *
from Conversation import *
person_A = CollegeStudent('carl.json')
#now lets make another person
person_B = CollegeStudent('janet.json')
print person_A.getPersonality()
conv = Conversation(person_A, person_B)

