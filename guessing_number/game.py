import numpy as np


def predict_number(number: int = 1) -> int:
    """Загадываем случайное число и угадываем его.

    Args:
        number (int, optional): _Загаданное число_. Defaults to 1.

    Returns:
        int: _Количество попыток_
    """
        
    count = 0 
    min_number = 1
    max_number = 100
    predict = np.random.randint(1, 101)
    
    while True:
        count += 1
        if predict < number:
            min_number = predict
            predict = max_number - (max_number-min_number)//2
        elif predict > number:
            max_number = predict
            predict = min_number + (max_number-min_number)//2
        else:
            break    

    return count


def score_game(predict_number) -> int:
    """Вычисляем за сколько попыток в среднем
    наш алгоритм отгадает загаданное число

    Args:
        predict_number (_type_): _функция угадывания_

    Returns:
        int: _среднеее количество попыток_
    """
    count_ls = []
    np.random.seed(1)
    number_array = np.random.randint(1, 101, size = 1000)
    
    for number in number_array:
        count_ls.append(predict_number(number))
        
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    
    return score


if __name__ == "__main__":
    score_game(predict_number)
