import numpy as np

class StudentRecord :
    def __init__(self, line ) :
        self.firstname_ = ''
        self.lastname_ = ''
        self.score_ = None
        self.scores_ = None
        self.inputline(line)        
        
    def __str__(self):
        return self.lastname_ + ', ' + self.firstname_ + ' : ' + ' '.join([str(x) for x in self.scores_])

    def firstname(self):
        return self.firstname_

    def lastname(self):
        return self.lastname_

    def score(self):
        return self.score_

    def inputline(self,data):        
        self.lastname_ = data[0]
        self.firstname_ = data[1]
        self.scores_ = np.array([ float(x) for x in data[2:] ])

    def calcscore(self):
        ### your code goes here

class StudentRecordPhysics(StudentRecord):
    def __init__(self, line):
        ### your code goes here

class StudentRecordLiterature(StudentRecord):
    def __init__(self, line):
        ### your code goes here

class StudentRecordHistory(StudentRecord):
    def __init__(self, line):
        ### your code goes here

