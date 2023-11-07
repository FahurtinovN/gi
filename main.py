# class DataBase:
#     __instance = None
#     def __new__(cls, *args, **kwargs):
#         if cls.__instance is None:
#             cls.__instance = super().__new__(cls)
#         return cls.__instance
#
#     def __init__(self, user, password, port):
#         self.user = user
#         self.password = password
#         self.port = port
#
#
#     def connect(self):
#         print(f'Соединение с БД: {self.user}, {self.password}, {self.port}')
#
#     def close(self):
#         print('соединение разорвано')
#
#     def read(self):
#         print(f'Чтение данных')
#
#     def write(self, data):
#         print(f'Запись в БД: {data}')
#
# db = DataBase('user1', 'psw1', '8000')
# db2 = DataBase('user1', 'psw1', '8000')
# print(db)
# print(db2)
# class Test:
#     pass
#
#     def __bool__(self):
#         return 2>6
#
#
# t = Test()
# if t:
#     print('hello gays')
#
#
# class Clock:
#     __DAY = 86400
#
#     def __init__(self, seconds : int):
#         if not isinstance(seconds, int):
#             raise TypeError(f'Нужно ввести целое число, придурок!')
#         self.seconds = seconds % self.__DAY
#
#     def get_time(self):
#         s = self.seconds % 60
#         m = self.seconds // 60 % 60
#         h = self.seconds // 3600 % 24
#         return f'{h} : {m} : {s}'
#
#     def __eq__(self, other):
#         if not isinstance(other, (int, Clock)):
#             raise TypeError('Нужно ввести целое число')
#
#         sc = other if isinstance(other, int) else other.seconds
#         return self.seconds == sc
#
#     def __lt__(self, other):
#         if not isinstance(other, (int, Clock)):
#             raise TypeError('Type Error')
#         sc = other if isinstance(other, int) else other.seconds
#         return self.seconds < sc
#
#
#
#     def __add__(self, other):
#         if not isinstance(other, (int, Clock)):
#             raise ArithmeticError(' Не можем сложить')
#
#         sc = other if isinstance(other, int) else other.seconds
#         return Clock(self.seconds + sc)
#
#     def __iadd__(self, other):
#         if not isinstance(other, (int, Clock)):
#             raise ArithmeticError(' Не можем сложить')
#
#         sc = other if isinstance(other, int) else other.seconds
#         return Clock(self.seconds + sc)
#
#     def __mul__(self, other):
#         if not isinstance(other, (int, Clock)):
#             raise ArithmeticError(' Не можем сложить')
#
#         sc = other if isinstance(other, int) else other.seconds
#         return Clock(self.seconds * sc)
#
# cl = Clock(86400)
# cl2 = Clock(54)
# cl3 = Clock(155)
# print(cl.get_time())
# cl = cl + cl2 + cl3
# print(cl.get_time())
#
# class Passport:
#     def __init__(self, first_name, last_name, country, date_of_birth, num_of_passport):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.country = country
#         self.date_of_birth = date_of_birth
#         self.num_of_passport = num_of_passport
#
#     def print_info(self):
#         print(f'''
# Full name: {self.first_name}, {self.last_name}
# Date of birth: {self.date_of_birth}
# Country: {self.country}
# Passport: {self.num_of_passport}''')
#
#     def __repr__(self):
#         return f'name {self.first_name} {self.last_name}, Passport {self.num_of_passport}'
#
#
# class ForeignPassport(Passport):
#
#     def __init__(self, first_name, last_name, country, date_of_birth, num_of_passport, visa):
#         super().__init__(first_name, last_name, country, date_of_birth, num_of_passport)
#         self.visa = visa
#
#     def print_info(self):
#         super().print_info()
#         print(f'Visa {self.visa}')
#
#
# MFC = []
# p = Passport('Ivan', 'Ivanov', 'Russia', '14.05.2005', '0719 539804')
# MFC.append(p)
# Fp = ForeignPassport('Petr', 'Petrov', 'Russia', '25.03.1999','4785 485647', 'China')
# MFC.append(Fp)
# print(MFC)
# for item in MFC:
#     item.print_info()
#
#
class Equipment:
    def __init__(self, name, make, year):
        self.name = name
        self.make = make
        self.year = year

    def action(self):
        return 'Не определено'

    def __str__(self):
        return f'{self.name}, {self.make}, {self.year}'

    def __le__(self, other):
        if not isinstance(other, Equipment):
            raise TypeError
        return self.year <= other.year


class Printer(Equipment):
    def __init__(self, series, name, make, year):
        super().__init__(name, make, year)
        self.series = series

    def action(self):
        return 'Печатает'

    def __str__(self):
        return f'{self.name}, {self.series}, {self.make}, {self.year}'


class Scaner(Equipment):
    def __init__(self, name, make, year):
        super().__init__(name, make, year)

    def action(self):
        return f'Сканирует'


class Xerox(Equipment):
    def __init__(self, name, make, year):
        super().__init__(name, make, year)

    def action(self):
        return f'Копирует и печатает'

storage = []
e = Equipment('Noname', 'X', 2001)
storage.append(e)
s = Printer('Azaza', 'Lalka', 'chicony',1337)
storage.append(s)
x = Xerox('Xexexerox', 'Yabujin', 228)
storage.append(x)
for item in storage:
    print(item)