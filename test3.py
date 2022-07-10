class ineuron:
    def student(self):
        print('print details of all the students')

    def achivers(self):
        print('print all the achievers')

    def hall_of_fame(self):
        print('print everyone from hall of fame')

class ineuron_vision(ineuron):

    def student(self): # method override in python inheritance
        print('these are filter students list')

iv = ineuron_vision()
iv.student()