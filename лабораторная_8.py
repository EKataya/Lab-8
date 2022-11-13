import random
import logging

# Работаем с логированием
logger = logging.getLogger("Logger")
logger.setLevel(logging.INFO)

# Создаем файл для логирования
file_handler = logging.FileHandler("log.log")
# Создаем форматер, отображающий дату, время, имя логгера, уровень и сообщение
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Диалог с пользователем
print('''Здравствуйте, это программа жеребьевки.
Для того чтобы провести жеребьевку, необходимо ввести количество(положительное натуральное число) пользователей
для жеребьевки.
Далее последствием нажатия клавиши ENTER вам будут выводится соответствующие числа для жеребьевки
''')

while True:
    logger.info('Program started')
# Вводим данные и проверяем на ввод
    try:
        n = int(input('Введите количество пользователей для жеребьевки: '))
    except ValueError:
        print('Данные введены неверно. Попробуйте снова.')
        logger.error('Incorrect value.')
        continue
    if n <= 0:
        print('Введены неверные данные. Попробуйте снова.')
        logger.error('Incorrect value.')
        continue
    logger.info(f'User entered value {n}')

# Создаем и заполненяем список чисел от 1 до n
    a = list()
    for i in range(n):
        a.append(i+1)

# Выводим случайные числа при помощи удаления уже выпавших
    for i in range(n):
        rand = random.randint(0, len(a) - 1)
        print(a[rand])
        logger.info(f'Displayed number: {a[rand]}')
        a.pop(rand)
        input('Нажмите ENTER для того чтобы вытащить следующее число')

# Выход из цикла
    break
logger.info('Programm done')

