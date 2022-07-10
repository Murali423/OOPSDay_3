#Encapsulatiom
class ineuron:
    def __init__(self):
        self.student0 = 'data science'

    def students(self):
        print(self.student0)

i = ineuron()
i.students()
i.student0 = 'Python progranm'
i.students()


class ineuron1:
    def __init__(self):
        self.__student1 = 'data science'

    def students(self):
        print(self.__student1)
    def student_change(self,newvalue):  # only class methods can only change private value
        self.__student1 = newvalue

i1 = ineuron1()
i1.students()
i1.__student1 = 'big data from out'
i1.students()
i1.student_change('murali')
i1.students()