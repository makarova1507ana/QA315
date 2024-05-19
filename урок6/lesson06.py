# # ----------------------ДЗ------------------------------- #
# # Редактирование: Найти самую низкую оценку и показать студента(ов),
# # а также самую высокую  и показать студента(ов) .
# students = {'Alice': 85, 'Bob': 92, 'Charlie': 78}
# max_ball = 0
# name = ""
# min_ball = 100**100
# for key in students:
#     if max_ball < students[key]:
#         max_ball = students[key]
#         name = key
#     if min_ball > students[key]:
#         min_ball = students[key]
#         name = key
#
# print(f"студент: {name}  оценка: {max_ball}")
#
# print(f"студент: {name}  оценка: {min_ball}")









# ---------------------- Файлы ------------------------------- #
# файлы:
# текстовые файлы (.txt, .doc, .xlsx, .csv, .pdf, .html, .xml, .json и т.д.)
# бинарные (.png, .mp3, .mp4 и т.д.)

# открытие
# чтение файла
# запись файлы
# закрытие

# 1 способ
# file = open('mark_of_students.txt', 'r') # r - read, w - write
# #print(file)
# text = file.read()# содержимое файла
# print(text)
# file.close()


# #  2 способ (Лучший!!)
# # C:\Users\Anastasia\Desktop\Groups\QA315\result.txt - прямой путь
# # ..\result.txt - относительный путь (относительтено папки с исполняемым файлом  'папка1\file.txt')
# # ..\ - выход текущий папки
# with open(r'..\result.txt', 'r', encoding='utf-8') as file: # with ... сам открывает и сам закрывает
#     text = file.read() # получаем сплошной текст
#
# print(text)

# получение полного пути файла
# import os
# current_directory = os.path.dirname(__file__) # узнаем путь текущего модуля (где находиться исполняемый файл)
# file_path = os.path.join(current_directory, 'mark_of_students.txt') # склеиваем путь + название файла
# print(file_path)
#

# #—------------------------------- Задача —--------------------------------#
# # дан файл, в каждой строке которого содержится стоимость товара.
# # Найти самый дорогой товар, самый дешевый товар и общую сумму покупки.
#
# # открыть файл,
# # получить значения из файла
# # проанализировать эти значения (найти самый дорогой товар, самый дешевый товар и общую сумму покупки.)
# # закрытие
#
# #--------получение данных из файла--------#
# with open('prices.txt', 'r') as f:
#     prices = f.readlines() # ['line1', 'line2', ...]
# #print(prices, type(prices)) # ['100\n', '700\n', '500\n', '300']
#
# #--------преобразование полученных данных --------#
# prices_integer = []
# for price in prices:
#     #print(price, type(price)) # price -> '100\n' и т.д.
#     prices_integer.append(int(price))
#
# #--------решение поставленной задачи--------#
# print(prices_integer, type(prices_integer)) # [100, 700, 500, 300]
# print(f'max: {max(prices_integer)} | min: {min(prices_integer)} | sum: {sum(prices_integer)}')
#
#



# #—------------------------------- Задача —--------------------------------#
# # Дан файл, в каждой строке которого содержится фамилия человека.
# # Найти всех людей фамилия, которых начинается на К(кириллица)
#
# with open('names.txt', 'r', encoding='utf-8') as file:
#     names = file.readlines()
# print(names)
# otvet = []
# for i, name in enumerate(names):
#     if name[0] == 'К' or name[0] == 'к':
#         if i == len(names) - 1:
#             print(name)
#         else:
#             print(name[:-1])



# #—------------------------------- Задача —--------------------------------#
'''
дан JSON файл. Напиши CLI (command lines interfaces) для получение информации о товаре.
ПРИМЕР файла
    {
      "название": "Смартфон",
      "цена": 500,
      "категория": "Электроника"
    }

'''
import json
with open('product.json', 'r', encoding='utf-8') as f:
    product = json.load(f) # json.load(f)  -> {'название': 'Смартфон', 'цена': 500, 'категория': 'Электроника'}
print(product, type(product))

while True:
    command = input('''
1. узнать имя товара
2. узнать цену
3. узнать  категорию
4. выйти из программы
''')
    match command:
        case '1': ## if command == '1
            print(product['название'])
        case '2': #  elif command == '2'
            print(product['цена'])
        case '3': # elif command == '3'
            print(product['категория'])
        case '4':
            break
