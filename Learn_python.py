'''Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если слово длинное, выводить только первые 10 букв в слове. '''
line = input()
words = line.split()
for i, word in enumerate(words, start=1):
    print(i, word[:10])

'''Программа принимает действительное положительное число x и целое отрицательное число y.
 Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
 При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.'''
#with**
def my_func(x = int(input("Введите целое положительное число: ")), y = int(input("Введите целое отрицательное число: "))):
    z = x**y
    return z
print(my_func())

#loop
def my_func(x = int(input("Введите целое положительное число: ")), y = int(input("Введите целое отрицательное число: "))):
    for i in (1, abs(y)):
        x = x*x
        z= 1/ x
        return z
print(my_func())

'''Программа запрашивает у пользователя строку чисел, 
разделенных пробелом. При нажатии Enter должна выводиться 
сумма чисел. Пользователь может продолжить ввод чисел, 
разделенных пробелом и снова нажать Enter. Сумма вновь 
введенных чисел будет добавляться к уже подсчитанной сумме. 
Но если вместо числа вводится специальный символ, выполнение 
программы завершается. Если специальный символ введен после 
нескольких чисел, то вначале нужно добавить сумму этих чисел 
к полученной ранее сумме и после этого завершить программу.'''


def my_sum ():
    common_sum = 0
    exit = False
    while exit == False:
        number = input('Input numbers or Q for quit - ').split()
        current_sum = 0
        for el in number:
            if el == 'q' or el == 'Q':
                number.remove(el)
                exit = True
                break
            else:
                try:
                    current_sum += int(el)
                except ValueError:
                    number.remove(el)
                    continue
            common_sum += current_sum
        print(f'Общая сумма чисел = {common_sum}')
my_sum()

'''Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
 но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов,
разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
 Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
 Необходимо использовать написанную ранее функцию int_func().'''
def int_func (*args):
    words = input("Введите слова: ")
    print(words.title())
    return
int_func()

'''Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. 
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия. 
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.'''
from sys import argv
salary_calc, hours, rate, bonus = argv
salary = (float(hours) * float(rate)) + float(bonus)
print(int(salary))

'''Представлен список чисел. Необходимо вывести элементы исходного списка, 
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. 
Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].'''
source_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [source_list[el] for el in range(1, len(source_list)) if source_list[el] > source_list[el-1]]
print(source_list)
print(new_list)

'''Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. 
Необходимо решить задание в одну строку.
Подсказка: использовать функцию range() и генератор.'''
print([el for el in range(20, 241) if el % 20 == 0])

'''Реализовать формирование списка, используя функцию range() и возможности генератора. 
В список должны войти четные числа от 100 до 1000 (включая границы). 
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().'''
from functools import reduce
def my_func(prev_el, el):
	return prev_el * el
print(reduce(my_func, [el for el in range(100, 1001) if el % 2 == 0]))

'''Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, 
что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл. 
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.'''

# a)
from itertools import count
start_num = int(input("Введите первое число цикла: "))
end_num = int(input("Введите последнее число цикла: "))
for el in count(start_num):
    if el > end_num:
        break
    else:
        print(el)

# б)
from itertools import cycle

cycl = 0
end_cyc = int(input("Введите количество повторов цикла: "))
for el in cycle([1, "w", 125, True]):
    if cycl > end_cyc:
        break
    print(el)
    cycl += 1


"""Создать программно файл в текстовом формате, 
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка."""
with open("out_file.txt", "w") as out_f:
	line = input('Введите текст ')
	while line:
		out_f.write(line+'\n')
		line = input('Введите текст ')
		if not line:
			break

"""Создать текстовый файл (не программно), 
построчно записать фамилии сотрудников и величину их окладов. 
Определить, кто из сотрудников имеет оклад менее 20 тыс., 
вывести фамилии этих сотрудников. 
Выполнить подсчет средней величины дохода сотрудников."""
with open("salary.txt") as my_file:

	salary_sum = 0
	salary_num = 0

	for line in my_file:
		name, salary = line.split()
		salary = int(salary)
		salary_sum += salary
		salary_num += 1
		if salary < 20000:
			print(name)

print("Средняя зарплата = ", salary_sum / salary_num)

"""Создать (программно) текстовый файл,
 записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму 
 чисел в файле и выводить ее на экран."""

def summa():
    try:
        with open("numbers.txt", "w+") as numbers:
            line = input('Введите целые числа через пробел \n')
            numbers.writelines(line)
            my_num = line.split()

            print(sum(map(int, my_num)))
    except IOError:
        print("Ошибка в файле")
    except ValueError:
        print("Проверьте правильность ввода")
summa()

"""Создать многопользовательскую игру 'Угадай число'
Компьютур загадывает число от 1 до 100. Игроки вводят свои имена. 
Каждый игрок отгадывает число по очереди. При вводе неверного числа программа сообщает
игроку что введенное число больше либо меньше загаданного.
Предусмотреть разные уровени сложности игры в виде ограничения максимального числа попыток.
Указать имя победившего игрока."""
import random
number = random.randint(1, 100)

user_number = None
count = 0
levels = {1 : 10, 2 : 5, 3 : 3}

level = int(input("Выберите уровень сложности \n (1, 2 или 3): "))
max_count = levels[level]
print(f"У каждого игрока есть {levels.get(level)} попыток")

user_count = int(input("Введите количетво пользователей: "))
users = []
for i in range(user_count):
	user_name = input(f"Введите имя пользователя {i+1}: ")
	users.append(user_name)

is_winner = False
winner_name = None

while not is_winner:
	count += 1
	if count > max_count:
		print("Все пользователи проиграли")
		break
	print(f"Попытка № {count}")
	for user in users:
		print(f"Ход пользователя {user}")
		user_number = int(input("Введите целое число от 1 до 100: "))
		if user_number == number:
			is_winner = True
			winner_name = user
			break

		elif number < user_number:
			print("Ваше число больше загаданного")
		elif number > user_number:
			print("Ваше число меньше загаданного")
else:
	print(f" Победитель - {winner_name}. Поздравляем!")

'''Реализовать класс Road (дорога), в котором определить атрибуты:
length (длина), width (ширина). Значения данных атрибутов должны передаваться
при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра
дороги асфальтом, толщиной в 1 см * число см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т'''


class Road:
    def __init__(self, _length, _width, thickness, mass):
        self._lnth = _length
        self._wdth = _width
        self.thick = thickness
        self.mas = mass

    def pavement(self, _length, _width, thickness, mass):
        print(f"Масса дорожного полотна равна {int(self._lnth * self._wdth * self.thick * self.mas / 1000)} тонн")


road = Road(20, 5000, 25, 5)
road.pavement(20, 5000, 25, 5)

'''Реализовать базовый класс Worker (работник),
в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь,
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов,
вызвать методы экземпляров).'''




class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')
worker = Position("Вася", "Пупкин", "учитель", 5000, 250)
print(worker.get_full_name())
print(worker.position)
print(worker.get_total_income())

'''Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
остановилась, повернула (куда). Опишите несколько дочерних классов:
TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.'''


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


    def go(self):
        return f"{self.color} {self.name} поехал"

    def stop(self):
        return f"{self.name} остановился"

    def turn_left(self):
        return f"{self.name} повернул направо"

    def turn_rigt(self):
        return f"{self.name} повернул налево"

    def show_speed(self):
        return f"{self.name} едет со скростью {self.speed}"

    def police(self):
        if self.is_police == True:
            return f"Автомобиль {self.name} - служебная машина полиции. Разбегаемся!!!"
        else:
            return f"Все тихо, похоже {self.name} - не полицейский автомобиль. Можно поднажать)"

class WorkCar(Car):

    def show_speed(self):
        print(f"{self.name} едет со скростью {self.speed}")
        if self.speed > 40:
            return f"Автомобиль {self.name} превысил скорость. Полиция уже в пути!"
        else:
            return "Это нормальная скорость для грузового автомобиля"



work = WorkCar(40, "gray", "Kamaz", False)
print(work.go())
print(work.police())
print(work.turn_left())
print(work.turn_rigt())
print(work.turn_rigt())
print(work.turn_left())
print(work.show_speed())
print(work.stop())


class TownCar(Car):

    def show_speed(self):
        print(f"{self.name} едет со скростью {self.speed}")
        if self.speed > 60:
            return f"Автомобиль {self.name} превысил скорость. Полиция уже в пути!"
        else:
            return "Это нормальная скорость для городского автомобиля"



town = TownCar(70, "green", "Жигуль", False)
print(town.go())
print(town.police())
print(town.turn_left())
print(town.turn_rigt())
print(town.show_speed())
print(town.stop())

class SportCar(Car):
    pass

sport = SportCar(200, "red", "Lamborgini", False)
print(sport.go())
print(sport.police())
print(sport.turn_left())
print(sport.turn_rigt())
print(sport.stop())

class PoliceCar(Car):
    pass

police = PoliceCar(200, "черный", "Уазик", True)
print(police.go())
print(police.police())
print(police.turn_left())
print(police.turn_rigt())
print(police.stop())
