# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код:

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
MAXIMUM_ATTEMPTS = 10
count = 0

print('Вашему вниманию предлагается числовая угадайка! Загаданное число от 0 до 1000')
print('У Вас есть 10 попыток на её решение')
print('Удачи!')

num = randint(LOWER_LIMIT, UPPER_LIMIT)

for attempt in range(MAXIMUM_ATTEMPTS):
    count += 1
    user_numb = int(input(f'Попытка № {count}: '))
    if user_numb > num:
        print('Загаданное число меньше введенного Вами! Попробуйте ещё раз!')
        print(f'Осталось попыток {MAXIMUM_ATTEMPTS - count} !')
    elif user_numb < num:
        print(f'Загаданное число больше введенного Вами! Попробуйте ещё раз!')
        print(f'Осталось попыток{MAXIMUM_ATTEMPTS - count} !')
    else:
        print(f'Поздравляю вас! Вы справились с заданием за попыток {count} !')
        break
else:
    print('К сожалению вы исчерпали все попытки!')
    print('Удачи в следующий раз!')