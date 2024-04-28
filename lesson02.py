# -------------Наборы (коллекциями)------------------ #
# () tuple кортеж
# [] list список
# {} set множества
# {} dict словарь (ассоциативный массив)
# range() - диапазон


# --------------- list - список ---------------------#
# [] - набор значений любого типа данных
# [1, 5.6, 'Hello', [1, 2, 0], {}, (),  None, True, range(1,3)]
# список == массив (допустимо)


# Зачем?
# -> хранит сразу много значений
# -> можно изменить содержимое
# ->

# list_ = []
# list_num = [5, 10, 213, 89]
# list_str_num = list(('1', '2', '3', '4', '5'))
#
# # Edit - редактирование элементов
# print(list_num)
# print('list_num[1] =', list_num[1]) # 10
# print('list_num[2] =', list_num[2]) # 213
# list_num[1] = 77
# print('list_num[1] =', list_num[1]) # 77
# print(list_num)
#
# # Add  добавление элементов в список
# print(list_) # []
# # print(list_[0]) # error IndexError: list index out of range
# list_.append(8) # вставка в конец
# print(list_)
# print(list_[0])
# #-----вставка на определенную позицию----
# print('------------')
# print(list_num)
# list_num.insert(1, 88)# вставка на определенную позицию
# print(list_num)
#


#------------- Задача ------------------#
'''
Создайте список из случайных чисел размером 10.  Числа от 0 до 100.
'''
# import random
# numbers = []
#
# for i in range(10):
#     num = random.randint(0,100)
#     numbers.append(num)
#     print(numbers)
#
# print(numbers)



'''
Посчитать кол-во положительных чисел в списке чисел. 
Список чисел сформировать от -100 до 100 любого размера
'''
# import random
# numbers = []
# count = 0
# n = int(input('len: '))
# for i in range(n):
#     num = random.randint(-100,100)
#     if num > 0:
#         count += 1
#     numbers.append(num)
# print(numbers, count)



'''
Дан список целых чисел. 
Найти процент отрицательных чисел от общего кол-во чисел.
найти сумму первого и последнего элемента списка
'''
# nums = [78, -10, -8, -1, -3, 56] # может быть любого размера
# count_negative = 0
# for num in nums:
#     if num < 0:
#         count_negative += 1
#
# length = len(nums) # кол-во всех элементов в списке
# print(length)
# print('% :', count_negative / length * 100)





'''
Дан список 0 случайного размера(минимум 1). 
0 - место не занято
1 - место занято.
Необходимо посадить гостей через одного, только справа от первого гостя.
Первый гость выбирает желаемый номер места
'''
#
# seats = [0, 0, 0, 0, 0]
# for i in range(0, len(seats)):
#     print('index:', i, 'element: ', seats[i])
#
#
# num_seat = int(input('Введите номер места: ')) # стоит добавить проверку
#
# # seats.insert(num_seat, 1) # !!!
# # print(seats)
# for i in range(num_seat, len(seats), 2):
#     seats[i] = 1
# print(seats)



'''
Дан список 1 случайного размера(минимум 1). 
Пасхальный кролик должен на каждую 1 принести пасхальное яичко, 
которое заменит 1 на 0.

пример
вход: [1,1,1] 
выход: [0,0,0]

вход: [1] 
выход: [0]
'''
#
# l = [1, 1, 1]
# for i in range(len(l)): # Что перебираем? индексы
#     print(f'index: {i} -> element l[{i}] = {l[i]}')
#
# for element in l:# Что перебираем? элементы списка
#     print('element: ', element)
#     element = 0 # !!! Не заменит содержимое списка
# print(l)
#
# for index, element in enumerate(l):# Что перебираем? индексы, элементы
#     print(f'index: {index} -> element: {element}',
#           f'\nl[{index}] = {l[index]}')
#     l[index] = 0
# print(l)

'''
Дан список целых чисел случайного размера.
Если среди чисел спрятался пасхальный кролик, то заменить его на пасхальное яичко.
Пасхальный кролик -  2
Пасхальное яичко - 0

пример
вход: [1,2,1] 
выход: [1,0,1]


пример
вход: [] 
выход: []

пример
вход: [2, 3, 0, 2] 
выход: [0, 3, 0, 0]
'''
# l = []
# for i in range(len(l)):
#     if l[i] == 2:
#         l[i] = 0
#
# print(l)

# --------2 способ-------- #
# l = [1,2,1, 2]
# while 2 in l:# l.count(2) != 0: # пока есть кролики
#     i = l.index(2) # находим точное расположение
#     l[i] = 0
# print(l)
#

'''
Если есть 'солнышко' в списке в произвольном списке 
напечатать 'вот и лучик',
иначе 'где солнышко?'
'''
l = ['муравей', 'солнышко','облачко','кот','дерево']

if 'солнышко' in l:
    print('вот и лучик')
else:
    print('где солнышко?')

if l.count('солнышко') >= 1 :
    print('вот и лучик')
else:
    print('где солнышко?')



'''
Задача 3: Поиск уникального яйца
Описание:
Все яйца в корзине, кроме одного, встречаются дважды. Найдите яйцо, которое встречается один раз.

Пример входных данных:


яйца = [5, 7, 5, 6, 7]

Пример выходных данных:
6
'''



'''
Дети играют в игру на Пасху, где каждый ребенок получает карточку с номером,
 и все вместе они становятся в ряд. Вам дан список, содержащий номера карточек в том порядке, в котором дети стоят. Ваша задача — написать функцию, которая находит индекс ребенка с определенным номером карточки. Если такой карточки нет, функция должна возвращать -1.

Пример входных данных:
карточки = [10, 20, 30, 40, 50]
номер_искомой_карточки = 30


Пример выходных данных:
2
'''
