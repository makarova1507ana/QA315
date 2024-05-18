# l = [4, 6, 9, 1, 3]
# # 1 способ
# l.index(9)
# # 2 способ
# for i, el in enumerate(l):
#     if el == 9:
#         print(i)

#
# d = {'Артем': 'Щит', 'Ваня': 'Меч', 'Алена': 'Броня'}
# for key in d:
#     if d[key] == 'Меч':
#         print(key)



# ---------------------- Строки ---------------------------- #
'''
строки - это набор символов заключенные в кавычки (" ' \''' """)

'''
# s = "это строка с 2-ными \" "
# s1 = 'это тоже строка с 1-ными " '
# s3 = """ это тоже
# строка с 3-ными \" """
# print(s)

'''
1. чтение
2. редактирование (изменение или добавление)
3. удаление
'''
# s = 'Это кот2' # ['Э', 'т', 'о', ..., '2']
# # примеры чтения данных из строки
# print(s, type(s))
# print(s[0], s[-1])
# print(s[4:])

# редактирование
# s1 = 'Это'
# s2 = 'кот2'
# s = s1 + ' ' + s2 # склеивание строк  == конкатенация
# s1_duble = s1 * 3 # дублирование строк
# print(s)
# print(s1_duble)


#
# s = 'Это кот'
# s[3] = '*' # TypeError: 'str' object does not support item assignment
# # 1
# s = s.replace(' ','*')
# # 2
# s = s[:3] + '*' + s[4:]
# # 3
# s = f'{s[:3]}*{s[4:]}' # f'' - f флаг (type)

# print(s)


#
#s = 'Это кот, скажи "Привет!"'
# s = s.replace(' ', '*')
# print(s)
# s = s.replace(' ', '*', 1)
# print(s)

# s = s.split(' ') # разделить
# print(s) # это список строк
# s1 = s[0] + ' ' + s[1]
# s2 = s[2] + ' ' + s[3]
# s = s1 + '*' + s2
# print(s)

# s = s.split(', ')
# print(s)
# s = s[0] + ',*' + s[1]
# print(s)

#
# s = '134'
# s = s[::-1]
# print(s)



# #
# '''
# Дана строка формата 0100010110
# небходимо поменять местами 0 и 1
# '''
# s = '0100010110'
# print(s)
# s = s.replace('0', '*')
# s = s.replace('1', '0')
# s = s.replace('*', '1')
#
# print(s)


# #
# '''
# Дано число
# узнать сколько цифр в числе
# '''
# n = 456
# s = str(n)
# print(len(s))



# #—------------------------------- Задача —--------------------------------#
# # # дано 4-х значное число, необходимо написать сколько единиц в числе
# # # сколько сотен и сколько тысяч и десятков
# # 2345
# n = 2345
# s = str(n)
# print(f'Тысячи - {s[0]}, Сотни - {s[1]}, Десятки - {s[2]}, Единицы - {s[3]}')


#
# #—------------------------------- Задача —--------------------------------#
# # 1. посчитать кол-во "0" в строке, а также заменить первый "0" и последний "0"  в строке на '*'
# #
# # ввод: 10234067
# # выход: 1*234*67
# #
# # ввод: 1023406708
# # выход: 1*234067*8
# #
# # ввод: 1023467
# # выход: 1*23467
# #
# # ввод: 123467
# # выход: 123467
# # s = '123467'
# # print(s.count('0'))
#
# d = '123467'##input("Введите: ")
# if d.count('0') != 0:
#     d = d.replace('0', "*", 1)
#     d = d[::-1]
#     d = d.replace('0', "*", 1)
#     d = d[::-1]
#     print(d)
# else:
#     print('В числе нет нолей', d)


# #—------------------------------- Задача —--------------------------------#
# # Дана строка, состоящая из слов, разделенных пробелами.
# # Определите, сколько в ней слов.
# s = 'кот  1231 -  , :   лук ток '
# #print(s.count(' ')+1)
# s = s.split(' ')
# print(s)
# print(f'Всего: {len(s)}',f'пустые: {s.count("")}', f'кол-во слов: {len(s)-s.count("")}')



#------------ Анализ ------------#
# категории символов
# буквы s.isalpha()
# цифры s.isdigit()
# пустоты spaces (пробелы, перенос строк(\n), таблуция(\t) и т.д.) s.isspace()
# спец. символы (все остальное)
# s = 'кот\n'
# print(len(s))

# s = '123fsa  , 4567'
# #print(s.isdigit())
# for el in s:
#     print(el, el.isdigit())


# # ACII   и кодировки
# s = '1234</,.abcdef абвгд'
# for el in s:
#     print(el, el.isascii())

# #—------------------------------- Задача —--------------------------------#
# # Дано строковое представление времени таймера '03:25:57'.
# # Выведите на экран количество секунд,
# # оставшихся до момента срабатывания таймера.
# # Используйте формат сообщения «До срабатывания таймера осталось {total_seconds} сек.».
# s = '03:25:57'
# h = s[:2]
# total_seconds = 0 # всего секунд
# m = s[3:5]
# s = s[6:] # s - секунды
#
# if h.isdigit() and m.isdigit() and s.isdigit():
#     h = int(h)
#     m = int(m)
#     s = int(s)
#     total_seconds = h*60*60 + m*60 + s
#
#
# print(f'До срабатывания таймера осталось {total_seconds} сек.')

# #—------------------------------- Задача —--------------------------------#
#Дана произвольная строка .
# Подсчитайте в ней количество буквенных символов в любом регистре и
# выведите результат на экран.

s = 'Кот 234.'
count_total = 0 #буквенных символов в любом регистре
count_upper = 0
count_lower = 0
for el in s:
    if el.isalpha():
        count_total += 1
    if el.isupper():
        count_upper += 1
    elif el.islower():
        count_lower += 1


print(f'count_total: { count_total} | count_upper: {count_upper} | count_lower: {count_lower} ')