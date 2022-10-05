class Person:
    def __init__(self, age, high):
        self.age = age
        self.high = high
        self.iq = 0

    def print_person(self):
        print("Age: " + str(self.age) + ". High: " + str(self.high) + ". IQ: " + str(self.iq))


adi = Person(29, 1.69)
liron = Person(24.5, 1.70)
liron.iq = 200

liron.print_person()
adi.print_person()
