#Abstraction
class ineuron:

    __student = 'data science'

    def students(self):
        print('print the class of students',ineuron.__student)

i = ineuron()
i.students()
print(i._ineuron__student)