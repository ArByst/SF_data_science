'''Игра Угадай число'''

import numpy as np

# Компьютер загадывает число
number = np.random.randint(1, 101) 

# Количество попыток
count = 0

while True:
    count += 1
    predict_number = int(input('Угадайте число: '))
    
    if predict_number > number:
        print('Загаданное число меньше')
    
    elif predict_number < number:
        print('Загаданное число больше')
        
    else:
        print(f'Поздравляю!!! Вы угадали с {count} попытки. Это число {number}!')    
        break    