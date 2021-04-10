class IsNumber(Exception):
    def __init__(self, text):
        self.txt = text


list_of_numbers = ''
while True:
    try:
        num = input('Введите число: ')
        if num == 'stop': break
        if not num.isdigit():
            raise IsNumber('Это не число!')
    except IsNumber as m:
        print(m)
        while not num.isdigit():
            num = input('Введите число, а не текст: ')
            if not num.isdigit(): print(m)
        list_of_numbers += num
    else:
        list_of_numbers += num

    print(list_of_numbers)
