"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    left_edge = 1
    right_edge = 101
    number = np.random.randint (left_edge,right_edge)  # компьютер загадывает число  
    while True:
        count += 1
        predict_number = np.random.randint(left_edge,right_edge) # предполагаемое число
        if number == predict_number:
            break # угадали
        else:
            while number != predict_number:
               if number > predict_number:
                   left_edge = predict_number # левая граница заменяется на предполагаемое число
                   predict_number = np.random.randint(left_edge,right_edge) #предполагается число в диапазоне с измененной левой границей
               elif number < predict_number:
                   right_edge = predict_number #правая граница заменяется на предполагаемое число
                   predict_number = np.random.randint(left_edge,right_edge) #предполагается число в диапазоне с измененной правой границей
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)