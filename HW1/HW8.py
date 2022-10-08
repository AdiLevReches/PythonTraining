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
        self.order_list = []

    def get_balance(self):
        return self.balance

    def add_money(self,amount):
        self.balance = self.balance + amount

    def maximize(self, order, d=0):
        price_list = []

        for phone in order.phones:
            price_list.append(phone.discount(d))
        price_list.sort()

        sum_so_far = 0
        n = 0
        for j in price_list:
            if sum_so_far+j < self.balance:
                sum_so_far += j
                n += 1
            else:
                break
        return n

    def buy(self, order, d=0):
        price_list = []
        num_products = len(order.phones)

        for i in range(0,num_products):
            price_list.append((order.phones[i].discount(d)))

        if sum(price_list) < self.get_balance():
            for i in range(0,num_products):
                order.phones[i].change_price(price_list[i])
            self.add_money(-1*sum(price_list))
            self.order_list.append(order)

        return self.balance

    def buy2(self, order, d=0):
        if len(order.phones)==self.maximize(order,d):
            for phone in order.phones:
                phone.change_price(phone.discount(d))
                self.add_money(-1*phone.price)
            self.order_list.append(order)

        return self.balance



    def find_order(self,ord_num):
        order_found = False
        name_phones = []
        for order in self.order_list:
            if order.get_id()==ord_num:
                order_found = True
                for phone in order.phones:
                    name_phones.append(phone.model)
        if order_found:
            return name_phones
        return None


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

print(adi_phone)
print(yuval_phone)

print(adi.maximize(Order([adi_phone,yuval_phone])))

adi = Client("adi","308014174")
adi.add_money(200)
print(adi.get_balance())
order = Order([adi_phone,yuval_phone])
print(adi.buy(order, 30))
print(adi.find_order(order.order_id))
print(adi.find_order(order.order_id+1))