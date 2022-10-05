class Person:
    def __init__(self, age, high):
        self.age = age
        self.high = high
        self.iq = 0


def print_person(person):
    print("Age: " + str(person.age) + ". High: " + str(person.high) + ". IQ: " + str(person.iq))


adi = Person(29, 1.69)
print_person(adi)

liron = Person(24.5, 1.70)
liron.iq = 200
print_person(liron)
