'''
user_name = input('Введите ФИО: ')
user_age = input('Введите возраст: ')
user_gender = input('Введите пол: ')
user_place_work = input('Введите место работы: ')
user_place_study = input('Введите место учебы: ')
user_course = input('Введите место работы: ')

print(user_name, user_age, user_gender, user_place_work, user_place_study, user_course, sep='\n')
'''
aaaffaaaaadd
"""
country = input('Text your country: ')
prise = input('Text how many money do you want: ')
count_work_day = input('How many day do you want to work in week: ')
company = input('What kind of company do you want to work: ')
print(f'''
Я хочу работать в {country}, и должен получать в месяц +{prise}
Хочу работать {count_work_day} дня в неделю, остальное время путешествовать
Хочу работать в {company} компании и отдыхать когда захочу!
''')
"""

"""
name = 'Acer'
model = 'pro 15'
diagonal = '15.6'
ram = 16
hard = 500
cpu = 'Intel Core I3-7th Gen'
gpu = 'GeForce 750MX'
vram = 2
weight = 2.02
print(f'''
name = {name}
model = {model}
diagonal = {diagonal}
ram = {ram}
hard = {hard}
cpu = {cpu}
gpu = {gpu}
vram = {vram}
weight = {weight}
''')
"""

"""
k = int(input('Введите сумму кредита: '))
m = int(input('Количество месяцев: '))

if m > 6:
    p = 15
else:
    p = 10
a = k*0.01*p*(1+0.01*p)**m/((1+0.01*p)**m-1)
print(a)
"""

"""
k = float(input("Охват по бюсту: "))
m = float(input("Охват по бедрам: "))
n = float(input("Охват по талии: "))
t = float(input("Рост: "))
p = float(input("Вес: "))
l = (k * m * t) / ((n ** 2) * p)
print(round(l, 1))
"""

"""
u = int(input('напряжение: '))
i = int(input('сила тока: '))
p = u * i
print(f'Ваш электрический прибор потребляет {p} Вт мощности')
"""

"""
PI = 3.1415
height = int(input("Text silindr's height: "))
radius = int(input("Text silindr's radius: "))
v = PI * radius ** 2 * height
print(f"Цилиндр с высотой {height} и радиусом {radius} имеет объем: {v}")
"""

"""
for i in range(1,16):
    print('*' * i)
"""

"""
for i in range(1, 16):
    print('*' * i)
for j in range(14, 1, -1):
    print('*' * j)
"""

"""
n = int(input('Number: ')) + 1
for i in range(1, n):
    print(' ' * (n - i) + '*' * i, end='')
    print('*' * i)
for i in range(1, n):
    print(' ' * i + '*' * (n - i), end='')
    print('*' * (n - i))
"""

"""
orm = int(input('Выберите количество оперативной памяти 4 или 8: '))
ssd = int(input('Выберите 1 если SSD, выберите 0 если HDD: '))
hard = int(input('Выберите объем: 256, 512, 1024 Gb: '))
condition = int(input('Выберите состояние ноутбука 1 если новый, выберите 0 если б/у: '))
price = int(input('Введите цену: '))

hp = 'Hp 550x 1000$ 8Gb 256SSD новый'
samsung = 'Samsung 150 Turbo 900$ 8Gb 256SSD б/у'
acer = 'Acer Predator 600$ 4Gb 1024HDD новый'
asus = 'Asus 550x 300$ 4Gb 1024HDD б/у'

'orm ssd hard condition price'
if orm == 8 and hard >= 256 and ssd == True and price > 300 and condition == True:
    print(hp)
if orm == 8 and hard > 256 and ssd == True and price > 300 and condition == False:
    print(samsung)
if orm == 4 and hard > 256 and ssd == False and price > 300 and condition == True:
    print(acer)
if orm == 4 and hard > 256 and ssd == False and price > 300 and condition == False:
    print(asus)

"""

"""
u_orm = input('Выберите количество оперативной памяти 4 или 8: ')
u_ssd = input('Выберите 1 если SSD, выберите 0 если HDD: ')
u_hard = input('Выберите объем: 256, 512, 1024 Gb: ')
u_condition = input('Выберите состояние ноутбука 1 если новый, выберите 0 если б/у: ')
u_price = input('Введите цену: ')

hp = {'brend': 'hp',
      'orm': '8',
      'ssd': '1',
      'hard': '256',
      'condition': '1',
      'prise': '1000',
      }

samsung = {'brend': 'samsung',
           'orm': '8',
           'ssd': '1',
           'hard': '256',
           'condition': '0',
           'prise': '900',
           }

acer = {'brend': 'acer',
        'orm': '4',
        'ssd': '0',
        'hard': '1024',
        'condition': '1',
        'prise': '600',
        }

asus = {'brend': 'asus',
        'orm': '4',
        'ssd': '0',
        'hard': '1024',
        'condition': '0',
        'prise': '300',
        }

asus2 = {'brend': 'asus2',
        'orm': '4',
        'ssd': '0',
        'hard': '1024',
        'condition': '0',
        'prise': '300',
        }


computers = [hp, samsung, acer, asus, asus2]
count_com = 1
for computer in computers:
    if (computer.get('orm') == u_orm or u_orm == '') and \
            (computer.get('ssd') == u_ssd or u_ssd == '') and \
            (computer.get('hard') == u_hard or u_hard == '') and \
            (computer.get('condition') == u_condition or u_condition == '') and \
            (int(computer.get('prise')) <= int(u_price) or u_price == ''):
        print(f'''
Компьютер №{count_com}
Brend: {computer.get('brend')}
orm: {computer.get('orm')}
ssd: {computer.get('ssd')}
hard: {computer.get('hard')}
condition: {computer.get('condition')}
prise: {computer.get('prise')}
''')
        count_com += 1
"""

# main
"""
u_orm = input('Выберите количество оперативной памяти 4 или 8: ')
u_ssd = input('Выберите 1 если SSD, выберите 0 если HDD: ')
u_hard = input('Выберите объем: 256, 512, 1024 Gb: ')
u_condition = input('Выберите состояние ноутбука 1 если новый, выберите 0 если б/у: ')
u_price = input('Введите цену: ')

hp = {'brend': 'hp',
      'orm': '8',
      'ssd': '1',
      'hard': '256',
      'condition': '1',
      'prise': '1000',
      }

samsung = {'brend': 'samsung',
           'orm': '8',
           'ssd': '1',
           'hard': '256',
           'condition': '0',
           'prise': '900',
           }

acer = {'brend': 'acer',
        'orm': '4',
        'ssd': '0',
        'hard': '1024',
        'condition': '1',
        'prise': '600',
        }

asus = {'brend': 'asus',
        'orm': '4',
        'ssd': '0',
        'hard': '1024',
        'condition': '0',
        'prise': '300',
        }

asus2 = {'brend': 'asus2',
        'orm': '4',
        'ssd': '0',
        'hard': '1024',
        'condition': '0',
        'prise': '300',
        }


computers = [hp, samsung, acer, asus, asus2]
count_com = 1
for computer in computers:
    if (computer.get('orm') == u_orm or u_orm == '') and \
            (computer.get('ssd') == u_ssd or u_ssd == '') and \
            (computer.get('hard') == u_hard or u_hard == '') and \
            (computer.get('condition') == u_condition or u_condition == ''):
        try:
            if int(computer.get('prise')) <= int(u_price):
                print(f'''
Компьютер №{count_com}
Brend: {computer.get('brend')}
orm: {computer.get('orm')}
ssd: {computer.get('ssd')}
hard: {computer.get('hard')}
condition: {computer.get('condition')}
prise: {computer.get('prise')}
            ''')

        except ValueError:
            print(f'''
Компьютер №{count_com}
Brend: {computer.get('brend')}
orm: {computer.get('orm')}
ssd: {computer.get('ssd')}
hard: {computer.get('hard')}
condition: {computer.get('condition')}
prise: {computer.get('prise')}
''')
        count_com += 1
"""

"""
house = input('House: ')
made = int(input('break = 1 or pes = 0: '))
land = int(input('land: '))
price = int(input('Price: '))

print(house)
if made == 1 and land <= 4 and price <= 50000:
    print('first house')
elif made == 0 and land <= 5 and price <= 45000:
    print('second house')
else:
    print('Nothing!!!')
"""

"""
num = int(input('Text number: ')) + 1

l1 = [i for i in range(1, num)]
"""

n = int(input('Number: ')) + 1
if (n-1) % 2 == 1:
    d1 = int(n / 2)
    for i in range(1, n, 2):
        d1 -= 1
        print('0' * d1 + i * '*')

    d2 = 1
    for i in range(n-3, 0, -2): # 3 1
        print('0' * d2 + i * '*')
        d2 += 1
else:
    n -= 1
    d1 = int(n / 2)
    for i in range(1, n, 2):
        d1 -= 1
        print(' ' * d1 + i * '*')

    d2 = 1
    for i in range(n - 3, 0, -2):  # 3 1
        print(' ' * d2 + i * '*')
        d2 += 1

