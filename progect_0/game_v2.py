"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

from tracemalloc import start
import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    start = 1
    end = 101
    
    while True:
        count += 1
        predict_number = np.random.randint(start, end)  # предполагаемое число
                     
        if predict_number == number:
            break  # выход из цикла если угадали
               
        elif predict_number > number:
            end = predict_number    
                  
        elif predict_number < number:
            start = predict_number     
               
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
