# -- coding: utf-8 --


class IsNumber(Exception):
    def __init__(self, text):
        self.txt = text


class Warehouse:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
        self.warehouse_dict = {'Наименование товара': self.product,
                               'Количество': self.quantity}

    def save_to_file(self):
        with open("wh_data.txt", "w+") as file:
            file.writelines(self.warehouse_dict)


class OfficeEquipment(Warehouse):
    def __init__(self, product, brand, quantity):
        super().__init__(product, quantity)
        self.brand = brand


class Printer(OfficeEquipment):
    def __init__(self, product, brand, quantity, printer_type):
        super().__init__(product, brand, quantity)
        self.printer_type = printer_type
        self.printer_dict = {'Принтер': self.product,
                             'Производитель': self.brand,
                             'Кол-во на складе': self.quantity,
                             'Тип принтера': self.printer_type}

    def __str__(self):
        try:
            if not str(self.quantity).isdigit():
                raise IsNumber('В поле "количество" надо вводить число!')
        except IsNumber as pr:
            print(pr)
        finally:
            return str(self.printer_dict)

    def save_to_file(self):
        with open("printer_data.txt", "a+", encoding='UTF8') as file:
            try:
                if not str(self.quantity).isdigit():
                    raise IsNumber(
                        f'Данные для {self.product} {self.brand} не сохранятся, '
                        f'так как поле "количество" указано неверно!')
                else:
                    file.writelines(f"{str(self.printer_dict)}\n")
            except IsNumber as m:
                print(m)


class Scanner(OfficeEquipment):
    def __init__(self, product, brand, quantity, scanner_type):
        super().__init__(product, brand, quantity)
        self.scanner_type = scanner_type
        self.scanner_dict = {'Сканер': self.product,
                             'Производитель': self.brand,
                             'Кол-во на складе': self.quantity,
                             'Тип сканера': self.scanner_type}

    def __str__(self):
        try:
            if not str(self.quantity).isdigit():
                raise IsNumber('В поле "количество" надо вводить число!')
        except IsNumber as pr:
            print(pr)
        finally:
            return str(self.scanner_dict)

    def save_to_file(self):
        with open("scanner_data.txt", "a+", encoding='UTF8') as file:
            try:
                if not str(self.quantity).isdigit():
                    raise IsNumber(
                        f'Данные для {self.product} {self.brand} не сохранятся, '
                        f'так как поле "количество" указано неверно!')
                else:
                    file.writelines(f"{str(self.scanner_dict)}\n")
            except IsNumber as m:
                print(m)


class Xerox(OfficeEquipment):
    def __init__(self, product, brand, quantity, xerox_type):
        super().__init__(product, brand, quantity)
        self.xerox_type = xerox_type
        self.xerox_dict = {'Ксерокс': self.product,
                           'Производитель': self.brand,
                           'Кол-во на складе': self.quantity,
                           'Тип ксерокса': self.xerox_type}

    def __str__(self):
        return str(self.xerox_dict)

    def save_to_file(self):
        with open("xerox_data.txt", "a+", encoding='UTF8') as file:
            try:
                if not str(self.quantity).isdigit():
                    raise IsNumber(
                        f'Данные для {self.product} {self.brand} не сохранятся, '
                        f'так как поле "количество" указано неверно!')
                else:
                    file.writelines(f"{str(self.xerox_dict)}\n")
            except IsNumber as m:
                print(m)


d = Printer('KN-34', 'Samsung', 22, 'Струйный')
c = Printer('KN-35', 'Samsung', 'dfg', 'Лазерный')
m = Scanner('LLU', 'HP', 12, 'А3')
k = Xerox('H-456', 'Brother', 16, 'Цветной')
print(d)
print(c)
print(m)
print(k)
d.save_to_file()
c.save_to_file()
m.save_to_file()
k.save_to_file()
