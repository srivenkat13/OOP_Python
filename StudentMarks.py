#  create a student class with the below attributes


class Student:
    def __init__(self, name, sub1, sub2, sub3):
        self.studentName = name
        self.subOne = sub1
        self.subTwo = sub2
        self.subThree = sub3

    def calculateResult(self):
        minScore = 40
        if (
            self.subOne >= minScore
            and self.subTwo >= minScore
            and self.subThree >= minScore
        ):
            return sum(self.subOne, self.subTwo, self.subThree) / 3
        else:
            return 0

#  create another class School with the below attributes

class School:
    def __init__(self,sname,sdict):
        self.schoolName = sname
        self.studentDict = sdict
    
    def getStudentResult(self):
        for i in self.studentDict.keys():
            average = i .calculateResult()
            if average > 60:
                self.studentDict[i]= "pass"

        return self.studentDict


    def findStudentWithHighestMarks(self,sdict):
        if len(sdict)==0:
            return None
        
        else:
            highAv = {}
            avg = 0
            for i in self.studentDict.keys():
                avg= i. calculateResult()
                highAv[i]=avg