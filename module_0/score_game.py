import numpy as np

def binary_hunting(number):
    '''Сначала устанавливаем любое random число, а потом реализуем алгоритм двоичного поиска.
       Функция принимает загаданное число и возвращает число попыток.'''
    count = 1
    low = 1  # нижняя граница последовательности чисел
    high = 100  # верхняя граница последовательности чисел
    predict = np.random.randint(1, 101)

    while number != predict:
        count += 1
        if number > predict:
            high = number - 1
        else:
            low = number + 1
        number = (low + high) // 2  # вычисляется средний элемент последовательности чисел, в которой ищем

    return (count)


def score_game(binary_hunting):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))

    for number in random_array:
        count_ls.append(binary_hunting(number))
    score = int(np.mean(count_ls))
    print(f"Этот алгоритм угадывает число в среднем за {score} попыток")

    return (score)


score_game(binary_hunting)