# ------------лямбда функции ------------- #
# # lambda el: el % 2 == 0
# # 1. у таких нет имени (в питоне можно записать в переменную)
# # 2. состоят из одного действия
# # 3. используются в качестве аргумента в других функция

# num_odd = lambda el: el % 2 == 0
#
# l = [3, 4, 5, 6, 8, 3123, 78]
# #отобрать только четные числа
# l = list(filter(num_odd, l))
# print(l)

# ------------Функции высшего порядка------------- #
# map - нужен для модификации с коллекциями

# # Дан список чисел. увелечить все значения в списке в два раза
# l = [3, 4, 5, 6, 8, 3123, 78]
# l = list(map(lambda el: el*2, l))
# print(l)

# # Дан список чисел. сделать числа строкового формата
# l = [3, 4, 5, 6, 8, 3123, 78]
# l = list(map(lambda el: str(el), l))
# print(l)

#
# # Дан список строк. заменить первую букву на большую
# l = ['кот', 'пес', 'ель', "суп"]
# # l[0] = l[0].replace(l[0][0], l[0][0].upper(), 1) # преобразуем 0-ой элемент в строку с первой заглавной буквой
# l = list(map(lambda string: string.replace(string[0], string[0].upper(), 1), l))
# print(l)


# ---------- reduce -------------
# from functools import reduce
# # Поиск наименьшего  элемента
# l = [3, 4, 5, 6, 8, 3123, 78]
# l = reduce(lambda editable_el, next_el: editable_el if editable_el < next_el else next_el, l)
# print(l)



# from functools import reduce
#
# # посчитать произведение всех чисел в списке
# nums = [2, 1, 1, 1, 1, 1]
# multiply = reduce(lambda result, next_el: result * next_el, nums)
# print(multiply)




# from functools import reduce
#
# # посчитать произведение всех чисел в списке
# products = [
#     {'name': 'product1', 'price': 100},
#     {'name': 'product2', 'price': 200},
#     {'name': 'product3', 'price': 300}
# ]
# # reduce(
# # lambda результат, следующий элемента набора: результат + следующий элемента набора,
# # набор значений,
# # начальное значение для результата)
# total_summ = reduce(lambda summ, product_price: summ + product_price['price'], products, 0)
# print(total_summ)







# ---------------------класс---------------------- #
# класс - это шаблон, в котором описаны свойства и набор действий(методы)
#
# class Cat:
#     # self - ссылка на объект
#     def __init__(self, name, color, age): # специальный метод (инциализатор) - инициализицирует объект (записывает данные в объект)
#         self.name = name # self.name == поле класса == свойства == аргумент
#         self.color = color
#         self.age = age
#
#     def eat(self): # метод - то же, что и функция только описанная внутри класса
#         print(self.name + " ест")
#
# # объект (экземпляр класса) - это конкретный экземплярный класса
#
# cat_vasya = Cat('Vasya', 'black', 3) # cat_vasya
# print(cat_vasya, cat_vasya.name) # cat_vasya.name -> обращение к полю класса
# cat_vasya.eat() # cat_vasya.eat() - вызов метода



