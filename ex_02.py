class DivByZero(Exception):
    def __init__(self, text):
        self.txt = text


try:
    a = int(input('Введите делимое: '))
    b = int(input('Введите делитель: '))
    if b == 0:
        raise DivByZero('На ноль делить нельзя! Введите другое число!')
    else:
        print(a / b)
except DivByZero as m:
    print(m)
    b = 0
    while b == 0:
        b = int(input('Введите делитель отличный от нуля: '))
        if b == 0:
            print(m)
        else:
            print(a / b)
