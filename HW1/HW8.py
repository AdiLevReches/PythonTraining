import random


class CellPhone:
    def __init__(self, model,price,year):
        self.model = model
        self.price = price
        self.year = year

    def get_price(self):
        return self.price

    def change_price(self,price):
        if price <= 0 :
            raise ValueError("should be a positive number")
        else:
            self.price = price

    def __repr__(self):
        return "<" + str(self.model) + "><" + str(self.price) + ">"

    def discount(self,rate):
        return self.price * (100-rate) / 100

    def __eq__(self,other):
        return self.price == other.price

    def __gt__(self,other):
        return self.price > other.price

    def __lt__(self, other):
        return other > self

print("another class")

class Order:

    def __init__(self, phones):
        self.phones = phones
        self.order_id = random.randint(1,10000)

    def get_id(self):
        return self.order_id

print("another class")

class Client:

    def __init__(self, name, id_num):
        self.name = name
        self.id_num = id_num
        self.balance = 0

    def get_balance(self):
        return self.balance

    def add_money(self,amount):
        self.balance = self.balance + amount

adi_phone = CellPhone('Nokia',200,2010)
yuval_phone = CellPhone('Nokia',20,2010)
print(adi_phone.get_price())
adi_phone.change_price(130)
print(adi_phone.get_price())
print(adi_phone)
print(adi_phone.discount(30))

print(adi_phone.__eq__(yuval_phone))
print(adi_phone == yuval_phone)

print(adi_phone.__gt__(yuval_phone))
print(adi_phone > yuval_phone)

print(adi_phone.__lt__(yuval_phone))
print(adi_phone < yuval_phone)

order = Order([adi_phone,yuval_phone])
print(order.get_id())

adi = Client("adi","308014174")
print(adi.get_balance())
adi.add_money(95)
print(adi.get_balance())