class Data:
    def __init__(self, date):
        self.date = date

    @classmethod
    def format_date(cls, date):
        date_list = []
        for el in date.split('-'):
            date_list.append(el)
        return f'{int(date_list[0]):0{2}}.{int(date_list[1]):0{2}}.{int(date_list[2]):0{4}}'

    @staticmethod
    def is_valid_date(date):
        print(date)
        date_list = []
        for el in date.split('-'):
            date_list.append(el)
        day = int(date_list[0])
        month = int(date_list[1])
        year = int(date_list[2])

        if day < 1 or day > 31:
            print(f'"{day}" - это неправильное число')
        if month < 1 or month > 12:
            print(f'"{month}" - нет такого месяца')
        if year < 0 or year > 9999:
            print(f'{year}???? Да ты издеваешься!!!')
        if month in [4, 6, 9, 11] and day == 31:
            print("В этом месяце 30 дней!")
        if year % 4 == 0 and month == 2 and day in [30, 31]:
            print("В этом году в феврале 29 дней!")
        if year % 4 != 0 and month == 2 and day in [29, 30, 31]:
            print("В феврале 28 дней, едрён-батон!")


m = Data.format_date('1-11-2020')
Data.is_valid_date('31-02-7801')

print(Data.format_date('1-2-2020'))
