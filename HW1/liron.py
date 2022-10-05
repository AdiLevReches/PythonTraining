import math


class Rational:
    def __init__(self, n, d=1):
        if d == 0:
            raise ZeroDivisionError("cant be zero!")

        # gcd = math.gcd(n,d)
        gcd = self.find_gcd(n, d)
        self.n = int(n / gcd)
        self.d = int(d / gcd)

    def find_gcd(self, n, d):
        gcd = 1
        for i in range(2, int(min(n,d))+1):
            if n % i == 0 and d % i==0:
                gcd = i
        return gcd

    def __repr__(self):
        return str(self.n) + "/" + str(self.d)

    def __add__(self, other):
        if isinstance(other, int):
            other = Rational(other)
        return Rational(self.n*other.d + self.d*other.n, self.d*other.d)

    def __radd__(self, other):
        return self + other

    def __eq__(self, other):
        return self.n == other.n and self.d == other.d

    def __lt__(self, other):
        return self.n*other.d < self.d*other.n

    def __le__(self, other):
        return self.n * other.d <= self.d * other.n

    def __gt__(self, other): # self > other
        return other < self

    def __ge__(self, other): # self >= other
        return other <= self


r1 = Rational(1, 2)
r2 = Rational(2, 4)
r3 = Rational(3,7)
r4 = Rational(5,6)
print(r1==r2)
print(r1 + r2)
print(r1 + 2 + 5) # r1.__add__(2)
print(r1 + Rational(2))

print(2 + r1) # r1.__radd__(2)

print("--------")
all_r = [r1, r2, r3, r4]
all_r.sort()
print(all_r)

print(5/3)
print(5//3)