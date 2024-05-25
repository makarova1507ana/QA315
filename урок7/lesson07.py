#---------------------Файлы---------------------------#
# Запись данных в  файл
# !!! Старые данные будут перезаписаны !!!
# with open('data.txt', 'w', encoding='UTF-8') as f:
#     # s = 'это строка'
#     prices = ['1000', '2000', '340']
#     s = '\n'.join(prices) #  prices[0] + '\n' +....
#     f.write(s) #  write() argument must be str

# # Дозапись данных
# with open('data.txt', 'a', encoding='UTF-8') as f: # a - add
#     s = '\nэто строка'
#     f.write(s)

# import json
# # # запись данных в json
# # with open('data.json', 'a', encoding='UTF-8') as file:
# #     d = {'product1': 1000,
# #          'product2': 2300}
# #     json.dump(d, file)






# ------------------- функции -------------------------- #
# функция - это сохраненный алгоритм(кусок кода, который решает поставленную задачу)

# from turtle import*
# from time import sleep
#
# left(45)
#
# # нарисовать квадрат
# for side in range(4):
#     forward(100)
#     left(90)
#
# right(180)
#
# # нарисовать квадрат
# for side in range(4):
#     forward(100)
#     left(90)
#
# right(180)
# forward(100)
# right(90)
#
# # нарисовать квадрат
# for side in range(4):
#     forward(100)
#     left(90)
#
#
# sleep(5)




# #--------------------------#
# from turtle import*
# from time import sleep
#
# # def name_function(arguments):
# #     actions
#
# def draw_square(): #Определяем функцию
#     for side in range(4):
#         forward(100)
#         left(90)
#
# left(45)
#
# # нарисовать квадрат
# draw_square() # вызов функции
#
# right(180)
#
# # нарисовать квадрат
# draw_square()
#
# right(180)
# forward(100)
# right(90)
#
# # нарисовать квадрат
# draw_square()
#
#
# sleep(5)



#
# # #-------------корабль рисуем-------------#
#
# from turtle import *
# from time import sleep
# def draw_triangle():
#     for side in range(3):
#         forward(100)
#         right(120)
# left(90)
# draw_triangle()
# right(90)
# draw_triangle()
# right(60)
# draw_triangle()
# right(60)
# draw_triangle()
# sleep(5)

#
#
# # #------------Аргументы функции--------------#
# from turtle import*
# from time import sleep
# # Аргументы, параметры
# # :int - подсказка / аннотация !!! НИКАК не влияет на проверку типа данных
# def draw_square(a:int, col='black'): # a -обязательный параметр , col - необязательный параметр
#     color(col)
#     for side in range(4):
#         forward(a)
#         left(90)
# # draw_square() # TypeError: draw_square() missing 1 required positional argument: 'a'
# draw_square(100)
# draw_square(150, 'red')
# draw_square(200)
# draw_square()
# #draw_square(300, 'green', 130) #TypeError: draw_square() takes from 1 to 2 positional arguments but 3 were given
# sleep(5)
#
#


from turtle import*
from time import sleep
# def draw_octagon():
#     for side in range(8):
#         forward(50)
#         left(45)
#
#
# for n in range(8):
#     draw_octagon()
#     left(45)
#
# sleep(10)
#
# from turtle import *
# from time import sleep
# def draw_octagon(a, col = 'blue'):
#     col = 'blue' if col == None else col
#     color(col)
#     for side in range(8):
#         forward(a)
#         left(45)
#
# cols = ['red', 'green', 'black', 'yellow', 'orange', None, None, None]
# for col in cols:
#     draw_octagon(50, col)
#     left(45)
# sleep(5)


# ------------Возвращаемое значение функции--------------#
#
# # даны три стороны треугольника -> вычислить его площадь
# # определить функцию периметра треугольника
#
# def triangle_P(a: float, b: float, c: float):
#     return a + b + c
# def triangle_S(p: float, a: float, b: float, c:float):
#     return (p*(p-a)*(p-b)*(p-c))**0.5
#
# a = 3
# b = 3
# c = 3
# p = triangle_P(a,b,c)/2 # полупериметр
#
# print(triangle_S(p,a,b,c))



#
#
# #—------------------------------- Задача —--------------------------------#
# # Создайте функцию для расчета общей стоимости товаров с учетом скидки.
# # Функция должна принимать на вход список цен и процент скидки,
# # а затем возвращать общую стоимость.
#
# def total_cost_discount_products(list_of_cost: list, discount: float):
#     total_cost = sum(list_of_cost) # найти общую сумму
#     total_cost = total_cost * (1 - discount/100)# вычислить сумму с учетом скидки
#     return total_cost# вернуть результат
# print(f'общая стоимость с учетом скидки: {total_cost_discount_products([100, 100, 200, 600], 40)}')


#—------------------------------- Задача —--------------------------------#
# Создайте функции для ввода оценок студентов,
# расчета средней оценки по предмету и выдачи рекомендации (например, "хорошо", "удовлетворительно").
# Функция расчета средней оценки может использовать результаты функции ввода оценок.
def input_grades():
    grades = []
    while True:
        grade = input('Введите оценку: ')
        if grade == 'q':
            break
        grades.append(int(grade))
    return grades

def avarage_grades(grades: list):
    return sum(grades) / len(grades)

grades = input_grades()
print(avarage_grades(grades))
