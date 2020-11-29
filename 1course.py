# print(6.996+(45*((13/2)**2))+2*(18**(1/2)))
# print((1267-20*(((5**3)/2)**2))/(8**5*(36**(1/2))))
# print((8**5)*(36**(1/2)))
# print(-2639.25/196608)
# print(((((9**(1/2))**3)**2)**2)/(-2**-3))

# name = input('Скажи как тебя зовут?\n')
# print('Сегодня Вас зовут ' + name)

# word = 'Очаровательно'
# # print(len(word))
# a = 117
# b = 23
#
# # print(a%b)
# a = 12
# b = 17
# c = 25
# print ((a*b*c)**(1/3))

# x = 100500
# print(6.996+45*(x/2)**2+x*2)

# weight = 80
# height = 1.8
# print(weight/(height**2))
#
# a = 270
# b = 12.8
# print(((a+b)/2)**(1/3))

# a = 23
# print('Вы ввели число, которое при умножении на 3 даёт ' + str(a*3))

# string_1 = 'Hello, world!'
# string_2 = 'Python <3'
# string_3 = 'qwerty'
#
# print((len(string_1)*len(string_2)*len(string_3))**(1/3))

# string = 'Привет!'
# power = 5
# print(string, len(string), len(string)**power)

# word = 'ОченьДлинноеСлово'
# if 'ф' in word:
#     print('Ого! Вы ввели редкое слово!')
# else:
#     print('Эх, это не очень редкое слово..')
# print(123%4)
# number = 169
# result = number**0.5
# print(result)
# if result%1 == 0:
#     print(int(result))
# else:
#     print('Квадратный корень из ' + str(number) + ' - не целое число')
# number = 6
# if number == 1:
#     print('понедельник')
# elif number == 2:
#     print('вторник')
# elif number == 3:
#     print('среда')
# elif number == 4:
#     print('четверг')
# elif number == 5:
#     print('пятница')
# elif number == 6:
#     print('суббота')
# elif number == 7:
#     print('воскресенье')


# weight = 120
# height = 1.8
# imt = weight/(height**2)
# if imt <= 18.5:
#     print('Недостаточная масса тела')
# elif imt >= 24.99:
#     print('Избыточная масса тела')
# else:
#     print('Норма')

# mark = 7
# if mark < 4:
#     print('неудовлетворительно')
# elif mark == 4 or mark == 5:
#     print('удовлетворительно')
# elif mark == 6 or mark == 7:
#     print('хорошо')
# elif mark >= 8:
#     print('отлично')


# balance = 1000
# if balance >= 5000:
#     print('Сегодня твой выбор - ресторан!')
# elif balance >= 2500 and balance < 5000:
#     print('Эх, только фастфуд.')
# elif balance < 2500:
#     print('Придётся потерпеть!')

# number = 455
# print(number%1)
# if ((number/2)%1) == 0:
#     print((number/2)%1)
#     print('Число делится на 2 без остатка')
# elif ((number/3)%1) == 0:
#     print((number/3) % 1)
#     print('Число делится на 3 без остатка')
# elif ((number/5)%1) == 0:
#     print((number/5)%1)
#     print('Число делится на 5 без остатка')

# flower = 'роза'
# color = 'фиолетовый'
#
# if color == 'синий' or color == 'белый':
#     print('Ане понравятся эти цветы')
# else:
#     print('Аня не любит такие цветы')

# height = 180
# weight = 92
# color = 'синий'
# if height > 170 and weight < 80 and color == 'красный':
#     print('Ваша половинка нашлась!')
# else:
#     print('Попробуем поискать ещё...')


# number = 346
# if ((number/2)%1) == 0 or ((number/5)%1) == 0 or ((number/173)%1) == 0 or ((number/821)%1) == 0:
#     print('Вова, это нужное число')
# else:
#     print('Вова, в этот раз ты не попал')

# fav_word = 'Аппликация'
# if  fav_word == 'рептилия' or fav_word == 'питон' or fav_word == 'змея':
#     print('Python')
# elif fav_word == 'плюс' or fav_word == 'плюсы':
#     print('C++')
# elif fav_word == 'рубин' or fav_word == 'кристалл':
#     print('Ruby')
# else:
#     print('Python')

# #hour = 18
# minute = 47
# if (hour==10 and minute>30 or hour<12) or (hour==13 and minute>40 or hour<15) or (hour==18 or hour==19 and minute<30):
#     print('Преподаватель занят.')
# else:
#     print('Преподаватель свободен.')

# word = 'подшипник'
# for i, letter in enumerate(word):
#     if i%2 == 0:
#         print(letter)

# year_1 = 2013
# year_2 = 2020
# for i in range(year_1, year_2 + 1):
#     if i % 4 == 0:
#         print('%d год високосный' %i)
#     else:
#         print('%d год невисокосный' %i)

# word = 'Зимушка-зима'
# result = ['а', 'у', 'о', 'ы', 'и', 'э', 'я',  'ю', 'ё', 'е']
# for i in word:
#     if i in result:
#         print(i)

# name = 'Сергей'
# for i, letter in enumerate(name):
#     print('Буква %d в этом имени - %s ' % (i + 1, letter))

# name = 'Сергей'
# for i, letter in enumerate(name):
#     print('Буква ' + str(i + 1) + ' в этом имени - ' + str(letter))

# num_1 = 25
# num_2 = 45
# if num_1 > num_2 or num_1 < 0:
#     print('Введён неверный диапазон чисел')
# else:
#     for i in range(num_1, num_2 + 1):
#         if i % 2 == 1 and (i % 3 == 0 or i % 5 == 0):
#             print(i)

# while True:
#     print('Я работаю!')

# for i in range(1, 11):
#     print(i, i**2, i**3)

# number = 84
# for i in range(1, number + 1):
#     if number%i == 0:
#         print(i)

# num_1 = 12
# num_2 = 38
# for i in range(2, num_2 + 1):
#     if num_1 % i ==0 and num_2 % i == 0:
#         print(i)

# n = 10
# fib1 = 1
# fib2 = 1
# print(fib1, end=' ')
# print(fib2, end=' ')
# for i in range(2, n):
#     tmp = fib1 + fib2
#     print(tmp, end=' ')
#     fib1 = fib2
#     fib2 = tmp

# n=10
# f_0=1
# f_n=1
# print('№ элемента в последовательности Фиббоначи n=',1,'  f_0=',f_0,'  f_n=',f_n)
# for i in range (2, n+1):
#     print('№ элемента в последовательности Фиббоначи n=',i,'  f_0=',f_0,'  f_n=',f_n)
#     f = f_n
#     f_n = f_0 + f_n
#     f_0 = f
# print(f)

# number = 15
# for i in range(1, 11):
#     print(str(number) + ' X ' + str(i) + ' = ' + str(number*i))

# num_1 = 1812
# num_2 = 2500
# for i in range(min(abs(num_1), abs(num_2)), 1, -1):
#     if num_2%i == 0 and num_1%i == 0:
#         print(str(i))
#         break
# else:
#     print('Общих делителей не найдено')

# string = 'абстракция'
# exept = ['а', 'б', 'в']
# for i in string:
#     if i in exept:
#         continue
#     else:
#         print(i, end='')
#         continue

# string = 'Нет'
# j = 0
# while j < 6:
#     j +=1
#     if j == 6:
#         print('Это безнадёжно!')
#     elif string in ['Нет', 'нет']:
#         print('Увы, это неправильный ответ')
#         continue
#     elif string in ['Да', 'да']:
#         print('Это отлично!')
#         break

# number = 173
# k = 0
# for i in range(2, number // 2+1):
#     if (number % i == 0):
#         k += 1
# if (k <=0):
#     print('Простое')
# else:
#     print('Не является простым')

# string = 'поАа'
# result = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е',
#           'А', 'У', 'О', 'Ы', 'И', 'Э', 'Я', 'Ю', 'Ё', 'Е']
# for i, letter in enumerate(string):
#     if letter not in result and i % 2 == 0:
#         print('Какая хорошая строка!')
#         break
#     elif i % 2 == 0 and letter in result:
#         print('Строка мне не нравится!')
#         break


# string = 'прелестная строка'
# #string='пока!'\n",
# count=len(string)
# for i, letter in enumerate(string):
#     if i%2==0:
#         if letter in 'аоиеёэыуюя':
#             print('Строка мне не нравится!')
#             break
#         else:
#             print('Какая хорошая строка!')


# Y = 170000
# Z = 1000000
# i = 0
# procent = 10
# while Y < Z:
#     Y = Y*1.1
#     i = i + 1
# print(i)


# weight = 77
# total = weight
# lift = 400
# res = 0
# final = 0
# while total < lift:
#     total += weight
#     final = total - lift
#
# print('Перевес ' + str(final) + ' кг')

#
# attack = 80
# health = 500
# current_health = health
# i = 0
# while current_health >= 0:
#     current_health -= attack
#     i += 1
#     continue
# print(i)

# spent = 2800
# balance = 10000
# while balance > 0:
#     print(balance)
#     balance -= spent
#     continue
# print('Слишком большие расходы')

# result = 0
# list = []
# for i in range(1, 50):
#     if i%3==0:
#         list.append(i)
#         result = sum(list)
# print(result)

# raw_list = ['переменные', 'циклы', 'условия', 'списки', 'словари', 'файлы', 'функции']
# result = 0
# my_list = []
# max_list = 0
# min_list = 0
# for i in raw_list:
#     my_list.append(len(i))
#     my_list.sort()
#     max_list = max(my_list)
#     min_list = min(my_list)
# print(max_list + min_list)

# raw_list = [2, 8, 10, 23, 64, 49, 11, 52, 71, 14]
# result = []
# my_list = []
# x_min = min(raw_list)
# x_max = max(raw_list)
# print(x_max, x_min)
# for i in raw_list:
#     if i % 2 == 0:
#         my_list.append(i*x_min)
#     else:
#         my_list.append(i*x_max)
# result = max(my_list)
# print(result)

# my_list = [x**0.5 for x in range(1,50) if x%7 == 0]
# print(my_list)
#
# my_list1 = []
# for x in range(1, 50):
#     if x%7 == 0:
#         my_list1.append(x**0.5)
# print(my_list1)

# my_list1 = []
# for x in range(90, 100):
#     first_digit = x//10
#     last_digit = x%10
#     my_list1.append(first_digit + last_digit)
# print(my_list1)
# my_list = [x//10 + x%10 for x in range(90, 100)]
# print(my_list)
#
# employee_base = {'Мария Никитина': '+79033923029',
#                                    'Егор Савичев': '+78125849204',
#                                    'Александр Пахомов': '+79053049385',
#                                    'Алина Егорова': '+79265748370',
#                                    'Руслан Башаров': '+79030598495'
#                                    }
# print(employee_base['Алина Егорова'])
# draw_dict = {
# 'Россия': 'A',
# 'Португалия': 'B',
# 'Франция': 'C',
# 'Дания': 'C',
# 'Египет': 'A'
# }
# country = 'Россия'
# group = draw_dict.get(country, 'unknown')
# print(group)

# draw_dict = {
# 	'Россия': 'A',
# 	'Португалия': 'B',
# 	'Франция': 'C',
# 	'Дания': 'C',
# 	'Египет': 'A'
# }
# group = draw_dict.setdefault('Италия', 'unknown')
# print(group)
#

# draw_dict = {
# 	'Россия': 'A',
# 	'Португалия': 'B',
# 	'Франция': 'C',
# 	'Дания': 'C',
# 	'Египет': 'A'
# }
# draw_new = {}
# for draw in draw_dict:
#     if draw_dict[draw] == 'A':
#         draw_new[draw] = 'A'
#         print(draw_new)

# draw_dict = {
# 	'Россия': 'A',
# 	'Португалия': 'B',
# 	'Франция': 'C',
# 	'Дания': 'C',
# 	'Египет': 'A'
# }
# draw_new = {}
# for i, position in draw_dict.items():
#     if position == 'A':
#         draw_new[i] = 'A'
#         print(draw_new)

# phones = {
# 	'Гордиенко Виктория': 5140,
# 	'Анисимов Кирилл': 5145,
# 	'Кузнецова Дарья': 5142
# }
#
# for record in phones:
# 	if record == 'Кузнецова Дарья' and phones[record] == 5142:
# 		print('Номер верен')

# csv_file = [
#     ['100412', 'Ботинки для горных лыж ATOMIC Hawx Prime 100', 9],
#     ['100728', 'Скейтборд Jdbug RT03', 32],
#     ['100732', 'Роллерсерф Razor RipStik Bright', 11],
#     ['100803', 'Ботинки для сноуборда DC Tucknee', 20],
#     ['100898', 'Шагомер Omron HJA-306', 2],
#     ['100934', 'Пульсометр Beurer PM62', 17],
# ]
#
# pulsometer_id = []
#
# pulsometer_id = csv_file[5][0]
# print(pulsometer_id)

# csv_file = [
#     ['100412', 'Ботинки для горных лыж ATOMIC Hawx Prime 100', 9],
#     ['100728', 'Скейтборд Jdbug RT03', 32],
#     ['100732', 'Роллерсерф Razor RipStik Bright', 11],
#     ['100803', 'Ботинки для сноуборда DC Tucknee', 20],
#     ['100898', 'Шагомер Omron HJA-306', 2],
#     ['100934', 'Пульсометр Beurer PM62', 17],
# ]
# csv_file_filtered = []
#
# for i in csv_file:
#     if i[2] > 10:
#         csv_file_filtered.append(i)
#         print(csv_file_filtered)

# csv_dict = [
#     {'id': '100412', 'position': 'Ботинки для горных лыж ATOMIC Hawx Prime 100', 'count': 9},
#     {'id': '100728', 'position': 'Скейтборд Jdbug RT03', 'count': 32},
#     {'id': '100732', 'position': 'Роллерсерф Razor RipStik Bright', 'count': 11},
#     {'id': '100803', 'position': 'Ботинки для сноуборда DC Tucknee', 'count': 20},
#     {'id': '100898', 'position': 'Шагомер Omron HJA-306', 'count': 2},
#     {'id': '100934', 'position': 'Пульсометр Beurer PM62', 'count': 17},
# ]
#
# csv_dict_boots = []
#
# for i in csv_dict:
#     if 'Ботинки' in i['position']:
#         csv_dict_boots.append(i)
#         print(csv_dict_boots)

# results = [
#  	{'cost': 98, 'source': 'vk'},
#  	{'cost': 153, 'source': 'yandex'},
#  	{'cost': 110, 'source': 'facebook'},
# ]
#
# mi=1000
# for stat in results:
#     if stat['cost']<mi:
#         mi=stat['cost']
# print(mi)
# print(results[0])

# defect_stats = [
# 	{'step number': 1, 'damage': 0.98},
# 	{'step number': 2, 'damage': 0.99},
# 	{'step number': 3, 'damage': 0.99},
# 	{'step number': 4, 'damage': 0.96},
# 	{'step number': 5, 'damage': 0.97},
# 	{'step number': 6, 'damage': 0.97},
# ]
# detail = 1
# for i in defect_stats:
#     if detail > 0.9:
#         detail *= i['damage']
#         result = i['step number']
#         print(result)

# currency = {
#     'AMD': {
#         'Name': 'Армянских драмов',
#         'Nominal': 100,
#         'Value': 13.121
#     },
#
# 	'AUD': {
# 		'Name': 'Австралийский доллар',
# 		'Nominal': 1,
# 		'Value': 45.5309
# 	},
#
# 	'INR': {
# 		'Name': 'Индийских рупий',
# 		'Nominal': 1000,
# 		'Value': 92.9658
# 	},
#
# 	'MDL': {
# 		'Name': 'Молдавских леев',
# 		'Nominal': 10,
# 		'Value': 36.9305
# 	},
# }
# data = 1000000
# lider = 0
# for i, num in currency.items():
#     if num['Value']/num['Nominal'] < data:
#         data = num['Value']/num['Nominal']
#         lider = i
#         print(lider)


# bodycount = {
# 	'Проклятие Черной жемчужины': {
# 		'человек': 17
# 	},
#
# 	'Сундук мертвеца': {
# 		'человек': 56,
# 		'раков-отшельников': 1
# 	},
#
# 	'На краю света': {
# 		'человек': 88
# 	},
#
# 	'На странных берегах': {
# 		'человек': 56,
# 		'русалок': 2,
# 		'ядовитых жаб': 3,
# 		'пиратов зомби': 2
# 	}
# }
#
# res = 0
# for i in bodycount.values():
#     for x in i.values():
#         res +=x
#         print(res)

# arrivals = {
# 	'Париж': {'время': '15:25', 'статус': 'ожидается', 'рейс': ['Аэрофлот']},
# 	'Пекин': {'время': '15:35', 'статус': 'опаздывает', 'рейс': ['China Southern Airlines', 'Россия']},
# 	'Лиссабон': {'время': '15:40', 'статус': 'ожидается', 'рейс': ['Nordwind', 'Аэрофлот']},
# }
#
# print(arrivals['Пекин']['рейс'][0] + arrivals['Пекин']['рейс'][1])
import json, collections

with open('../../data.json', 'rb') as infile:
    data = json.load(infile)
c = collections.Counter()

# categories = []
# data_list = data['events_data']
# # for item in data_list:
# #     category = item['client_id']
# #     categories.append(category)
# #
# # for category in categories:
# #     c[category]+= 1
# tables_clients = []
# for item in data_list:
#     client_id = item['client_id']
#     category = item['category']
#     if category == 'report':
#         tables_clients.append(client_id)
#         print(tables_clients)
#  #       print(tables_clients)
#     for table in tables_clients:
#         c[table] += 1
#       print(c)
# for table_client in tables_clients:
#      c[table_client] += 1
# print(c)
# j = 0
# for i in data_list:
#     if i['client_id'] == 62602 and i['category'] == 'page':
#         j += 1
# #         print(j)
# rainbow_list = 'каждый охотник желает знать где сидит фазан'.split()
# for word in rainbow_list:
# #     print(word)
# rainbow_dict = {'каждый': 'красный',
#                 'охотник': 'оранжевый',
#                 'желает': 'жёлтый',
#                 'знать': 'зелёный',
#                 'где': 'голубой',
#                 'сидит': 'синий',
#                 'фазан': 'фиолетовый'}
#
# # Перебираем ключи
# for word in rainbow_dict.keys():
#     print(word)
# # Перебираем значения
# for color in rainbow_dict.values():
#     print(color)
# for word, color in rainbow_dict.items():
#     print(word, color)

# string = 'Вы - самый крутой студент в SkillFactory'
# for letter in string:
#     print(letter, end = '')
# proverb = 'Программисты - это устройства, преобразующие кофеин в код.'
# result = proverb[19:29].split()+'о'
# print(result)

# proverb = 'Программисты - это устройства, преобразующие кофеин в код.'
# new_proverb = ''
# for i in range(0, len(proverb)+1):
#     if i%2!=0:
#         new_proverb = new_proverb+proverb[i]+proverb[i-1]
# print(new_proverb)

# proverb = 'Программисты - это устройства, преобразующие кофеин в код.'
# new_proverb=''
# for i in range(0, len(proverb)+1):
#     if i%2!=0: new_proverb=new_proverb+proverb[i]+proverb[i-1]
# print(new_proverb)


# basic_word = 'программирование'
# inverted_word = basic_word[::-1]
# #print(inverted_word)
# if basic_word == inverted_word:
#     print('Слово "%s" является палиндромом' %basic_word)
# else:
#     print('Слово "%s" - это не палиндром' %basic_word)

# city_list = ['Москва', 'Санкт-Петербург', 'Новосибирск',
#              'Екатеринбург', 'Нижний Новгород', 'Казань',
#              'Челябинск', 'Омск', 'Самара', 'Ростов-на-Дону']
# counter = 0
# for city in city_list:
#     if ' ' in city or '-' in city:
#         counter += 1
# print('Число городов со сложными названиями - {}'.format(counter))
# email = 'VeryBigBoss@skillfactory.ru'
# pos = email.find('@')
# domain = email[pos+1:]
# print(domain)

# tongue_twister = 'Ехал Грека через реку, видит Грека - в реке рак. Сунул Грека руку в реку, рак за руку Греку - цап!'
# counter = tongue_twister.count('Грек')
# print(counter)


# proverbs = ['Без труда не вытянешь и рыбку из пруда',
#             'Терпение и труд всё перетрут',
#             'Работа не волк - в лес не убежит',
#             'Чем труднее дело, тем выше честь',
#             'Учиться, учиться и учиться!']
#
# counter = 0
# for proverb in proverbs:
#     if 'труд' in proverb:
#         counter += 1
# print(counter)

# proverb = 'Хорошо написанная программа - это программа, написанная 2 раза'
#
# while True:
#     index = proverb.find('программа')
#     if index == -1:
#         break
#     secret = proverb[:index].split()[-1]
#     proverb = proverb[index+9:]
#     print(secret)

# email = 'VeryBigBoss@skillfactory.ru'
# print(email[email.find('@')+1:])
# number = 56.257
# x = str(number)
# new_num = list(x[x.find('.')+1:])
# new_num2 = []
# for i in new_num:
#     new_num2.append(int(i))
# sum = 0
# for i in new_num2:
#     sum += i
# print(sum)

# emails_list = ['vasya@mail.ru',
#           'akakiy@yandex.ru',
#           'spyderman@yandex.ru',
#           'XFiles@gmail.com',
#           'hello@mail.ru',
#           'noname@gmail.com',
#           'DonaldTrump@mail.ru',
#           'a768#af@yandex.ru',
#           'Ivan_Ivanovich@yandex.ru',
#           'thebestmail@yandex.ru']


# string = 'Интернет-открытки - это лучшее средство для мужчины сказать женщине о своих чувствах прямо в глаза.'
# secret = string[24:30]
# new_string = string.replace(secret.lower(), secret.upper())
# print(secret)
# string = 'Тяжёлая интернет-зависимость - это когда ты выходишь из интернета, а он из тебя нет.'
# #string = 'Привет, Андрей!'
# x=['.',',',':','-','!','?']
# for i in string:
#     if i in x:
#         string = string.replace(i, ':)')
# print(string)
# string = string.replace('.', ':)').replace(',', ':)').replace(':', ':)').replace('-', ':)').replace('!', ':)').replace('?', ':)')
# print(string)


# string = 'Тяжёлая интернет-зависимость - это когда ты выходишь из интернета, а он из тебя нет.'
# signs=['.',',','-','!','?']
# for sign in string:
#     if sign in signs:
#         string= string.replace(sign, ':)')
#         print(string)


# name = 'Севастиан'
# glas = ['а', 'и', 'е', 'ё', 'о', 'у', 'ы', 'э', 'ю', 'я',
#         'А', 'И', 'Е', 'Ё', 'О', 'У', 'Ы', 'Э', 'Ю', 'Я']
#
# sogl = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м',
#         'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш',
#         'щ', 'Б', 'В', 'Г', 'Д', 'Ж', 'З', 'Й', 'К', 'Л',
#         'М', 'Н', 'П', 'Р', 'С', 'Т', 'Ф', 'Х', 'Ц', 'Ч',
#         'Ш', 'Щ']
#
# new_name = ''
#
# for i in name:
#     if i in glas:
#         print('%s - гласная буква' % i)
#     else:
#         print('%s - согласная буква' % i)


# import re
# pattern = re.compile('[оиаыюяэёуе]\s[бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФЧХЦЧШЩ]')
#
# text = 'Разработка языка Python была начата в конце 1980-х годов' \
#        ' сотрудником голландского института CWI Гвидо ван Россумом.' \
#        ' Для распределённой ОС Amoeba требовался расширяемый скриптовый язык,' \
#        ' и Гвидо начал писать Python на досуге, позаимствовав некоторые наработки' \
#        ' для языка ABC (Гвидо участвовал в разработке этого языка, ориентированного ' \
#        'на обучение программированию). В феврале 1991 года Гвидо опубликовал исходный ' \
#        'текст в группе новостей alt.sources. Название языка произошло вовсе не от вида ' \
#        'пресмыкающихся. Автор назвал язык в честь популярного британского комедийного телешоу ' \
#        '1970-х "Летающий цирк Монти Пайтона".'
# #print(pattern.match(text))
# #print(pattern.search(text))
# print(pattern.findall(text))
# print(len(pattern.findall(text)))

f = open('../../StudentsPerformance.csv')

# males = 0
# females = 0
# for line in f:
#        info = line.split(',')
#        gender = info[0]
#        print(gender)
#        if gender == 'female':
#               females += 1
#        elif gender == 'male':
#               males += 1
# print('Мальчиков: {}, девочек: {}'.format(males, females))
#
# f = open('StudentsPerformance.csv')
#
# parent = 0
# for line in f:
#        info = line.split(',')
#        level = info[2]
#        # print(level)
#        if level == 'bachelor\'s degree':
#               parent += 1
# print(parent)


# f = open('StudentsPerformance.csv')
#
# level_education_all = []
# level_education = []
# unique = []
# for line in f:
#        info = line.split(',')
#        edu = info[2]
#        level_education_all.append(edu)
#        # print(level_education_all)
#        level_education = level_education_all[1:-1]
#        # print(level_education)
#
#        unique = list(set(level_education))
#        print(len(unique))


# f = open('StudentsPerformance.csv')
#
# how_much = []
# current = 0
#
# for line in f:
#        info = line.split(',')
#        lunch = info[3]
#        how_much.append(lunch)
#        all = len(how_much[1:-1])
#        if lunch == 'standard':
#
#               current +=1
#               print(current)
# print((current / all)*100)

# f = open('StudentsPerformance.csv')
# count_race = 0
# for line in f:
#        info = line.split(',')
#        race = info[1]
#        print(race)
#        if race == 'group C':
#               count_race +=1
# print(count_race)
# race/ethnicity

# f = open('StudentsPerformance.csv')
# count_race = 0
# all = []
# unique = []
# for line in f:
#        info = line.split(',')
#        race = info[1]
#        all.append(race)
#        print(all[1:-1])
#        for i in all[1:-1]:
#               if i not in unique:
#
#                      count_race +=1
#                      unique.append(i)
# print(len(unique))

# math = []
#
# f = open('StudentsPerformance.csv')
#
# for line in f:
#
#        info = line.split(',')
#        if info[0] == '"gender"':
#
#               continue
#        else:
#               mark = int(info[5])
#               math.append(mark)


# f = open('StudentsPerformance.csv')
# i = 0
# j = 0
# x = 0
# avg_read = 0
# write_read = 0
# for line in f:
#     info = line.split(',')
#     write = info[3:7:3]
#     if info[0] == '"gender"':
#            continue
#     else:
#            all = write[1].replace('\n','').replace("\"",'')
#
#            if int(all) > 90 and write[0] == '"standard"':
#                   write_read += int(all)
#                   i += 1
#                   print((i/1000)*100)
#                   # avg_read = write_read / i
#                   # print(avg_read)
#
#
# students = {}

# f = open('StudentsPerformance.csv')
# i = 0
# for line in f:
#     info = line.split(',')
#     if info[0] == '"gender"':
#         continue
#     else:
#         ethnicity = info[1]
#         if ethnicity in students:
#             students[ethnicity] += 1
#         else:
#             students[ethnicity] = 1
# print()
#
# students = {}
#
# f = open('StudentsPerformance.csv')
#
# for line in f:
#     info = line.split(',')
#     if info[0] == '"gender"':
#         continue
#     else:
#         ethnicity = info[1][1:-1]
#         parents = info[2][1:-1]
# print(ethnicity, parents)


# a = 0
# f = open('StudentsPerformance.csv')
# j = 0
# x = []
# for c in f:
#     d = c.split(',')
#     if d[0] == '"gender"' """ or d[0] == '"female"' """:
#         continue
#     else:
#         int(d[5].replace('"','') == 100
#         :
#             j = sum(int(d[5].replace('"','')))
#             i +=1
#             print(j, i)
#         # if int(d[6].replace('"','')) > 90:
#         #     a += 1
# print(a)

#
# word = 'qwerty'
# print(word[::-1])
# X = 3.14
# X = int(X.replace(',', '.'))
# print(X)

# students = {}
# f = open('StudentsPerformance.csv')
# score = 0
# for line in f:
#     info = line.split(',')
#     if info[0] == '"gender"':
#         continue
#     else:
#         gender = info[0][1:-1]
#         reading = int(info[6][1:-1])
#         if gender == 'male':
#             if gender in students:
#                 students[gender] += 1
#                 score += reading
#             else:
#                 students[gender] = {}
#                 students[gender] = 1
#                 score += reading
# print(round(score / students['male'],3))


# f = open('StudentsPerformance.csv')
# a=[]
# for line in f:
#     info = line.split(',')
#     if info[0] == '"gender"':
#         continue
#     else:
#         r = int(info[-2][1:-1])
#         m = int(info[-3][1:-1])
#         if m == 100:
#             a.append(r)
# print(sum(a)/len(a))

# writing=[]
# count=0
# read_avg = 0
# f = open('StudentsPerformance.csv')
# for line in f:
#     info = line.split(',')
#     if info[0] == '"gender,':
#         continue
#     else:
#         if info[3][1:-1] == '"free/reduced"':
#             count+=1
#             mark = int(info[7][2:-4])
#             reading.append(mark)
#             read_avg=sum(reading)/len(reading)
#     print(read_avg)

#
# def square(x):
#     return x**2
#
# square_result = square(5)
# print(square(20))


# def count_cost(product):
#     if product =='apple':
#         cost = 30
#     else:
#         cost = 60
#         return cost
#
# orange_cost = count_cost("orange")


# Дополните аргументы и код функции
# def sum_2(x, y):
#     result = x + y
#     return result
#
# # Передайте аргументы 42 и 73 в функцию
# print(sum_2(42, 73))

#
# def power(x,y):
#     result = x**y
#     return result
# print(power(2,3))
#
# get_median([])
# for i in get_median:
#     print(i)
#     return i
# #
# user_db = [{'orders': 12}, {'orders': 30}, {'orders': 45}]
#
# # перепишите эту часть
# order_sum = sum([user['orders'] for user in user_db])
# orders_per_user = order_sum/len(user_db)
# print(orders_per_user)
#
# user_db = [{'orders': 12}, {'orders': 30}, {'orders': 45}]
# def avg_orders(user_db):
#     order_sum = sum([user['orders'] for user in user_db])
#     return order_sum / len(user_db)
# print(avg_orders(user_db))


# # добавьте функцию get_euro_rate
# import random
# print(random.randint(65,85))
#
# # используйте get_euro_rate в следующей функции
# # def to_euro(price):
# #     exchange_rate = get_euro_rate
# #     rounded = round(price/exchange_rate, 2)
# #     return '€' + str(rounded)
#
# all_the = sum
# magic = range
# print(all_the(magic(5)))
#
# print(list(map(abs, [10,  -1, 42, -73]))[3])

# word_sizes = list(map(len, ["all", "you", "need", "is", "map"]))
# print(word_sizes)
# values = [1, 2, 3]
# values2 = [4, 5, 6]
# vectors = [(10, 3), (4, 5), (6, 7)]
# vectors2 = [(5, 6), (9, 11), (14, 13)]
# print(list(map(lambda vec: (vec[0]**2 + vec[1]**2)**0.5, vectors)))
# print(list(map(lambda x, y: x + y, vectors, vectors2)))
# values = [4, 8, 15, 16, 23, 42]
# mean = 18
#
# result =(list(filter(lambda value: (value > mean), values)))
# print(result)


# std = 42
#
#
# def normalize(value):
#     result = value / std
#     return result
#
#
# print(normalize(21))
#
# std = 42
#
#
# def normalize(value, std):
#     result = value / std
#     return result
#
#
# print(normalize(21, 7))
#
# values = [-7, -7, 7, 7]
# std = 42
#
# def count_std():
#     mean = sum(values)/len(values)
#     std = (sum([(value-mean)**2 for value in values])/len(values))**0.5
#     return std
#
# def normalize(value):
#     result = value/std
#     return result
#
# print(normalize(21))

# def normalize(numbers,std=1,mean=0):
#     return [(i-mean)/std for i in numbers]
#
# print(normalize(10,20))
#
# def sum_args(*args):
#     res = 0
#     for i in args:
#         res += i
#     return res
#
# print(sum_args(10, 15, -4))

# def show_keys(**kwargs):
#     print(' '.join(kwargs.keys()))
#
# show_keys(verbose=True, mode='constant')

# def count_letters(letters, average=False):
#     word_list=list(letters.split())
#     word_sizes=list(map(len,word_list))
#     if average == False:
#         answer = sum(word_sizes)
#     else:
#         answer = sum(word_sizes)/len((word_sizes))
#     return answer

# words = ["sofa", "suitcase", "valise", "picture", "basket", "carton", "doggie"]
# print(list(map(lambda w: sorted(w)[0], words))[5])
import numpy as np

# for count in range(1,101):         # более компактный вариант счетчика
#     if number == count: break    # выход из цикла, если угадали

def game_core_v2(number):
    count = 0
    predict = np.random.randint(1, 101)
    while number != predict:
        count += 1
        if number > predict:
            predict += (100 - predict) // 2
            print(predict)
        elif number < predict:
            predict -= (100 - predict) // 2
            print(predict)
    return(count)

number = np.random.randint(1, 101)  # загадали число
print("Загадано число от 1 до 100")
print(f"Вы угадали число {number} за {count} попыток.")