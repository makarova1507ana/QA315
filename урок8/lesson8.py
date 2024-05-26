# ---------Практика----------- #
# - Задача: написать функцию, которая будет вычислять периметр для правильных многоугольников
# def polygon_P(n: int, a: float):
#     if n >= 3 and a > 0:
#         return n * a # return - точка выхода из функции
#     return -1 # если не удовляет валидации
#
#
# P = polygon_P(3, 10)
# if P == -1:
#     print("Кол-во сторон должна быть больше или равна трем и сторона должна быть положительной")
# else:
#     print(f"P = {P}")


#
# # проверить является ли число положительным
# n = int(input("Введите число: "))
#
# if n >= 0 :
#     if n == 0:
#         print(f" {n} - не положительный и не отрицательный")
#     else:
#         print(f" {n} - положительный ")
# else:
#     print(f" {n} - отрицательный ")

# ------------------------ try except ------------------------------#
#
# l = [5] # оценки студентов
#
# s = sum(l)
# n = len(l)
# print("n: ", n)
# print("s: ", s)
# try: # делаем попытку деления
#     print(f"средний балл студента {s/n}")
# except ZeroDivisionError as err:
#     print(f'У стедента нет еще оценок', err)
# except Exception as err: # все исключения (Exception)
#     print("Какая-то ошибка!", err)
# finally:
#     print("завершение работы программы")



# - Задача: написать функцию, которая будет вычислять периметр для правильных многоугольников
# def polygon_P(n: int, a: float):
#     if n >= 3 and a > 0:
#         return n * a # return - точка выхода из функции
#     raise Exception("Кол-во сторон должна быть больше или равна трем и сторона должна быть положительной") # если не удовляет валидации
#
# try:
#     P = polygon_P(2, 10)
#     print(f"P = {P}")
# except Exception as err:
#     print(err)


# ---------------Пример с selenium------------------- #
# from selenium import webdriver
# from selenium.webdriver.common.by import By  # для поиска элементов DOMе
# from time import sleep
# driver = webdriver.Chrome()
# driver.get('http://shop.bugred.ru/shop/item/9')
# try:
#     count = driver.find_element(By.ID, 'exampleCount3')
#     count.send_keys(5)
# except Exception as err:
#     print(f"Error {err}")
# sleep(5)



# # - Задача: написать функцию, которая будет вычислять периметр для любого многоугольника
# def is_positive(sides: list): # is_positive - Положительны ли стороны?
#     for side in sides:
#         if side <= 0:
#             return False # Нет, не положительны, есть хотя бы одна отрицательная сторона
#     return True # Да, все стороны положительны
#
# def polygon_P(sides: list):
#     n = len(sides)
#     if is_positive(sides):
#         P = sum(sides)
#         if n >= 3:
#             return P # return - точка выхода из функции
#     raise Exception("Кол-во сторон должна быть больше или равна трем и сторона должна быть положительной") # если не удовляет валидации
#
# try:
#     P = polygon_P([2, 10, -3])
#     print(f"P = {P}")
# except Exception as err:
#     print(err)




# #—------------------------------- Задача —--------------------------------#
# # Сделайте функцию, которая будет возвращать сколько дней осталось до ближайшего 29 февраля.
#
# # Что надо знать?
# # какой день, месяц, год сейчас?
# # дату следующего 29 февраля
#
# def is_leap_year(year): # определяем высокосный ли год?
#     return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
#
# def days_in_year(year): # определяем сколько дней в году
#     return 366 if is_leap_year(year) else 365 # если высокосный, то возвращается 366, иначе 365
# def days_until_next_feb_29(current_day, current_month, current_year):
#     # Преобразуем текущую дату в количество дней с начала года
#     days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if is_leap_year(current_year):
#         days_in_months[1] = 29  # Февраль в високосном году
#
#     # Сколько дней с начала года?
#     current_day_of_year = sum(days_in_months[:current_month - 1]) + current_day
#
#     # Проверим, является ли текущий год високосным и уже ли прошло 29 февраля в этом году
#     if is_leap_year(current_year):
#         # Сколько дней прошло с начала года до 29 февраля
#         feb_29_this_year = sum(days_in_months[:1]) + 29
#         if current_day_of_year <= feb_29_this_year:
#             return feb_29_this_year - current_day_of_year
#
#     # Найдем следующий високосный год
#     next_leap_year = current_year + 1
#     while not is_leap_year(next_leap_year):
#         next_leap_year += 1
#
#
#
#     # Кол-во дконцаней до  года
#     days_until_end_of_current_year = days_in_year(current_year) - current_day_of_year
#
#     # Количество дней до 29 февраля в следующем високосном году
#     days_until_feb_29_next_leap_year = sum([31, 29])  # Дни в январе и феврале до 29 февраля
#     return (days_until_end_of_current_year
#             + days_until_feb_29_next_leap_year +
#             (next_leap_year - current_year - 1) * 365 )
#
#
# # Пример использования
# current_day = 60
# current_month = 2
# current_year = 2028
# print(days_until_next_feb_29(current_day, current_month, current_year))
#
# # сделать проверки на корректность даты

#
# # Неограниченное кол-во аргументов
#
# def f(*args):
#     return args
# print(f(5,6), type(f(5,6)))


# # Неограниченное кол-во именнованных аргументов
# def f(**kwargs): #kwargs - key word arguments
#     return kwargs
#
# print(f(name1=6, name2="hello"))



# # МОжно указывать любой порядок аргументов
# def f(year, month, day):
#     return (year, month, day)
#
# print(f(day=5, month=6, year=2024))


#
# # # ------------Функции высшего порядка и лямбда функции ------------- #
# #
# # l = [3, 4, 5, 6, 8, 3123, 78]
# # #отобрать только четные числа
# # l = list(filter(lambda el: el % 2 == 0, l))
# # print(l)
#
# d = {'Ivan': 5, 'Artem': 4, 'Vasya': 2}
# #показать всех, у кого рейтинг 4 и выше
# names = list(filter(lambda key: d[key] >= 4, d.keys()))
# marks = list(filter(lambda value: value >= 4, d.values()))
# print(names, marks)