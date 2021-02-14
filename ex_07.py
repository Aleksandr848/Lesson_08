class ComplexNumber:
    def __init__(self, a, bi):
        self.a = a
        self.bi = bi

    def __add__(self, other):
        if (self.a * other.bi + self.bi * other.a) >= 0:
            i = 1
            sign = '+'
        else:
            i = -1
            sign = '-'
        return f'{self.a + other.a} {sign} {i * (self.bi + other.bi)}i'

    def __mul__(self, other):
        if (self.a * other.bi + self.bi * other.a) >= 0:
            i = 1
            sign = '+'
        else:
            i = -1
            sign = '-'
        return f'{self.a * other.a - (self.bi * other.bi)} {sign} {i * (self.a * other.bi + self.bi * other.a)}i'


v = ComplexNumber(2, -6)  # 2 - 6i
b = ComplexNumber(4, 5)  # 4 + 5i

print(v + b)
print(v * b)
