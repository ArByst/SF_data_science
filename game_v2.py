'''Игра Угадай игру'''

import numpy as np


def random_predict(number: int = 1) -> int:
    """Угадываем случайное число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток.
    """
    
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(1, 101)
        if predict_number == number:
            break
    return count


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем программа угадает загаданное число

    Args:
        random_predict (_type_): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1) # Фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # Загадали список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
    
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает загаданное число в среднем за {score} попыток.")
    return score


if __name__ == '__main__':
    score_game(random_predict)