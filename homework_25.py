'''Модуль 10. Объектно-ориентированное программирование
Тема: Перегрузка операторов. Часть 5'''


'''Задание 1
Создайте класс Circle (окружность). Для данного
класса реализуйте ряд перегруженных операторов:
■ Проверка на равенство радиусов двух окружностей (операция = =);
■ Сравнения длин двух окружностей (операции >, <, <=,>=);
■ Пропорциональное изменение размеров окружности,
путем изменения ее радиуса (операции + - += -=).'''

radius = 10
class Circle:
    def __init__(self, radius: int):
        self.radius = radius

    def circ_len(self):  # довжина кола
        return self.radius * 3.14 * 2

    def __eq__(self, other):  # ==
        return self.radius == other.radius

    def __lt__(self, other):  # <
        return self.circ_len() < other.circ_len()

    def __le__(self, other):  # <=
        return self.circ_len() <= other.circ_len

    def __gt__(self, other):  # >
        return self.circ_len() > other.circ_len

    def __ge__(self, other):  # >=
        return self.circ_len() >= other.circ_len

    def __add__(self, num: int):  # +
        return Circle(self.radius + num)

    def __iadd__(self, num: int):  # +=
        self.radius += num

    def __sub__(self, num: int):  # -
        return Circle(self.radius - num)

    def __isub__(self, num: int):  # -=
        self.radius -= num

new_radius1 = Circle(12)
new_radius2 = Circle(12)

print('Check ==')
is_eq = (new_radius1.radius == new_radius2.radius)
print(f'Radius1({new_radius1.radius}) == Radius2({new_radius2.radius}) is {is_eq}')

print('Check <')
is_eq = (new_radius1.radius < new_radius2.radius)
print(f'Radius1({new_radius1.radius}) < Radius2({new_radius2.radius}) is {is_eq}')

print('Check >')
is_eq = (new_radius1.radius > new_radius2.radius)
print(f'Radius1({new_radius1.radius}) > Radius2({new_radius2.radius}) is {is_eq}')

print('Check <=')
is_eq = (new_radius1.radius <= new_radius2.radius)
print(f'Radius1({new_radius1.radius}) <= Radius2({new_radius2.radius}) is {is_eq}')

print('Check >=')
is_eq = (new_radius1.radius >= new_radius2.radius)
print(f'Radius1({new_radius1.radius}) >= Radius2({new_radius2.radius}) is {is_eq}')

print('Check +')
is_eq = (new_radius1.radius + 1)
print(f'Radius1({new_radius1.radius}) + 1 is {is_eq}')

print('Check -')
is_eq = (new_radius1.radius - 1)
print(f'Radius1({new_radius1.radius}) - 1 is {is_eq}')

print('Check +=')
print(f'Radius1({new_radius1.radius}) += 1 = ')
new_radius1.radius += 1
print(f'Radius1({new_radius1.radius}) ')

print('Check -=')
print(f'Radius1({new_radius1.radius}) -= 1 = ')
new_radius1.radius -= 1
print(f'Radius1({new_radius1.radius}) ')



#new_radius1.radius = 5
#new_radius2.radius = 8

#is_eq = (new_radius1.radius == new_radius2.radius)
#print(f'Radius1({new_radius1.radius}) == Radius2({new_radius2.radius}) is {is_eq}')



'''Задание 2
Создайте класс Complex (комплексное число). Более
подробно ознакомиться с комплексными числами можно
по ссылке.
Создайте перегруженные операторы для реализации
арифметических операций для по работе с комплексными
числами (операции +, -, *, /).'''

class Complex:
    def __init__(self, a, b):
        self.a = a  # дійсна частина
        self.b = b  # уявна частина

    def __repr__(self):
        if (self.b == 0):
            return f'({self.a})'
        return f'({self.a}{"-" if self.b < 0 else "+"}{abs(self.b)}i)'

    def __add__(self, other):
        if type(other) == Complex:
            return Complex(self.a + other.a, self.b + other.b)
        elif type(other) == int or type(other) == float:
            return Complex(self.a + other, self.b)

    def __sub__(self, other):
        if type(other) == Complex:
            return Complex(self.a - other.a, self.b - other.b)
        elif type(other) == int or type(other) == float:
            return Complex(self.a - other, self.b)

    def __mul__(self, other):
        if type(other) == Complex:
            first = (self.a * other.a) - (self.b * other.b)
            second = self.a * other.b + self.b * other.a
            return Complex(first, second)
        elif type(other) == int or type(other) == float:
            return Complex(self.a * other, self.b * other)

    def __truediv__(self, other):
        if type(other) == Complex:
            first = (self.a * other.a + self.b * other.b) / (other.a ** 2 + other.b ** 2)
            second = (self.b * other.a - self.a * other.b) / (other.a ** 2 + other.b ** 2)
            return Complex(first, second)
        elif type(other) == int or type(other) == float:
            return Complex(self.a / other, self.b / other)

    def __eq__(self, other):
        if self.a == other.a and self.b == other.b:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.a != other.a and self.b != other.b:
            return True
        else:
            return False


new_complex1 = Complex(2, 3)
new_complex2 = Complex(4, 6)

print('Check for output of entered data:')
check = new_complex1, new_complex2
print(f'Complex1({new_complex1.a, new_complex1.b}),{new_complex2.a, new_complex2.b} is {check}')

print('Check /:')
check = new_complex1 / new_complex2
print(f'Complex1({new_complex1.a, new_complex1.b}) / {new_complex2.a, new_complex2.b} is {check}')

print('Check +:')
check = new_complex1 + new_complex2
print(f'Complex1({new_complex1.a, new_complex1.b}) + {new_complex2.a, new_complex2.b} is {check}')

print('Check -:')
check = new_complex1 - new_complex2
print(f'Complex1({new_complex1.a, new_complex1.b}) - {new_complex2.a, new_complex2.b} is {check}')

print('Check *:')
check = new_complex1 * new_complex2
print(f'Complex1({new_complex1.a, new_complex1.b}) * {new_complex2.a, new_complex2.b} is {check}')

print('Check Complex/2:')
check = new_complex1 / 2
print(f'Complex1({new_complex1.a, new_complex1.b}) / 2 is {check}')

print('Check ==:')
check = new_complex1 == new_complex2
print(f'Complex1({new_complex1.a, new_complex1.b}) == {new_complex2.a, new_complex2.b} is {check}')

print('Check !=:')
check = new_complex1 != new_complex2
print(f'Complex1({new_complex1.a, new_complex1.b}) != {new_complex2.a, new_complex2.b} is {check}')

'''Задание 3
Вам необходимо создать класс Airplane (самолет).
С помощью перегрузки операторов реализовать:
■ Проверка на равенство типов самолетов (операция = =);
■ Увеличение и уменьшение пассажиров в салоне самолета (операции + - += -=);
■ Сравнение двух самолетов по максимально возможному количеству пассажиров на борту (операции >
< <= >=).'''
class Airplane:
    def __init__(self, capacity: int):
        self.capacity = capacity

    def __eq__(self, other):  # ==
        return self.capacity == other.capacity

    def __lt__(self, other):  # <
        return self.capacity < other.capacity

    def __le__(self, other):  # <=
        return self.capacity <= other.capacity

    def __gt__(self, other):  # >
        return self.capacity > other.capacity

    def __ge__(self, other):  # >=
        return self.capacity >= other.capacity

    def __add__(self, num: int):  # +
        return Airplane(self.capacity + num)

    def __iadd__(self, num: int):  # +=
        self.capacity += num

    def __sub__(self, num: int):  # -
        return Airplane(self.capacity - num)

    def __isub__(self, num: int):  # -=
        self.capacity -= num

new_capacity1 = Airplane(120)
new_capacity2 = Airplane(150)

print('Check ==')
check = (new_capacity1.capacity == new_capacity2.capacity)
print(f'Capacity1({new_capacity1.capacity}) == Capacity2({new_capacity2.capacity}) is {check}')

print('Check <')
check = (new_capacity1.capacity < new_capacity2.capacity)
print(f'Capacity1({new_capacity1.capacity}) < Capacity2({new_capacity2.capacity}) is {check}')

print('Check >')
check = (new_capacity1.capacity > new_capacity2.capacity)
print(f'Capacity1({new_capacity1.capacity}) > Capacity2({new_capacity2.capacity}) is {check}')

print('Check <=')
check = (new_capacity1.capacity <= new_capacity2.capacity)
print(f'Capacity1({new_capacity1.capacity}) <= Capacity2({new_capacity2.capacity}) is {check}')

print('Check >=')
check = (new_capacity1.capacity >= new_capacity2.capacity)
print(f'Capacity1({new_capacity1.capacity}) >= Capacity2({new_capacity2.capacity}) is {check}')

print('Check +')
check = (new_capacity1.capacity + 100)
print(f'Capacity1({new_capacity1.capacity}) + 100 is {check}')

print('Check -')
check = (new_capacity1.capacity - 50)
print(f'Capacity1({new_capacity1.capacity}) - 50 is {check}')

print('Check +=')
print(f'Capacity1({new_capacity1.capacity}) += 100 = ')
new_capacity1.capacity += 100
print(f'Capacity1({new_capacity1.capacity}) ')

print('Check -=')
print(f'Capacity1({new_capacity1.capacity}) -= 50 = ')
new_capacity1.capacity -= 50
print(f'Capacity1({new_capacity1.capacity}) ')


'''Задание 4
Создать класс Flat (квартира). Реализовать перегруженные операторы:
■ Проверка на равенство площадей квартир (операция ==);
■ Проверка на неравенство площадей квартир (операция !=);
■ Сравнение двух квартир по цене (операции > < <= >=).'''

class Flat:
    def __init__(self, square: int, price: int):
        self.square = square
        self.price = price


    def __eq__(self, other):  # ==
        return self.square == other.square

    def __ne__(self, other):  # !=
        return self.square != other.square

    def __lt__(self, other):  # <
        return self.price < other.price

    def __le__(self, other):  # <=
        return self.price <= other.price

    def __gt__(self, other):  # >
        return self.price > other.price

    def __ge__(self, other):  # >=
        return self.price >= other.price

new_flat1 = Flat(25,15000)
new_flat2 = Flat(50,30000)

print('Check ==')
check = (new_flat1.square == new_flat2.square)
print(f'Square1({new_flat1.square}) == Square2({new_flat2.square}) is {check}')

print('Check !=')
check = (new_flat1.square != new_flat2.square)
print(f'Square1({new_flat1.square}) != Square2({new_flat2.square}) is {check}')


print('Check <')
check = (new_flat1.price < new_flat2.price)
print(f'Price1({new_flat1.price}) < Price2({new_flat2.price}) is {check}')

print('Check >')
check = (new_flat1.price > new_flat2.price)
print(f'Price1({new_flat1.price}) > Price2({new_flat2.price}) is {check}')

print('Check <=')
check = (new_flat1.price <= new_flat2.price)
print(f'Price1({new_flat1.price}) <= Price2({new_flat2.price}) is {check}')

print('Check >=')
check = (new_flat1.price >= new_flat2.price)
print(f'Price1({new_flat1.price}) >= Price2({new_flat2.price}) is {check}')
