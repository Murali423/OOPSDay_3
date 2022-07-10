class Car:

    def __init__(self, body, engine, type):
        self.body = body
        self.engine = engine
        self.type = type

    def milage(self):
        print('milage of this car')

c = Car('solid','v6','good')
print(c)


class tata(Car):
    pass

t = tata('solid','v8','radial')
print(t)
print(t.milage())