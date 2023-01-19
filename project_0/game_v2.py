"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def game_core_v3(number: int = 1) -> int:
    """
    Берем за основу список с промежуточными цифрами с шагом 10, и циклом проверяем, 
    больше или меньше загаданное число каждого из них.
    Затем, в подходящем промежутке, перебираем цифры, прибавляя по единице.
    Функция принимает загаданное число и возвращает число попыток
    
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    predict = 0    
    check_nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
   
    for num in check_nums:
        count += 1
        if number > num:
            predict = num
    
    while predict != number:
        count += 1
        predict += 1  
            
    return count


def score_game(game_core_v3) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
       game_core_v3 ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(game_core_v3(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


print('Run benchmarking for game_core_v3: ', end='')
score_game(game_core_v3)

