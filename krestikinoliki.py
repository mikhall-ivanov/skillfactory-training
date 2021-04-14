## крестики - нолики
import numpy as np

board = np.full([3, 3], '-')


def readme():
    print('Игроки по очереди ставят на свободные клетки поля 3х3 знаки (один всегда крестики, другой всегда нолики.')
    print('Первый, выстроивший в ряд 3 своих фигуры по вертикали, горизонтали или диагонали, выигрывает.')
    print('Первый ход делает игрок, ставящий крестики.')


def draw_board_np(board):
    # отрисовка игрового поля
    print ("    0   1   2")
    for i in range(3):
        print(f"{i}   {board[i, 0]}   {board[i, 1]}   {board[i, 2]}")


def list_correct(mas_answer):
    # проверяет, находятся обе координаты массива в легальном диапазоне от 0 до 2
    # возвращает True, если находятся, False - в противном случае
    if (0 <= mas_answer[0] <= 2) and (0 <= mas_answer[1] <= 2):
        return True
    else:
        return False


def take_input_np(player_hod):
    # принимает ход в параметрах [координата х, координата y] и проверяет его на легальность
    # ничего не возвращает, но меняет список board, занося в него сделанный ход

    val = False
    while not val:
        str_answer = input(
            f"Куда поставим {player_hod}?  Ввведите координаты строки (от 0 до 2) и, через пробел, столбца (от 0 до 2)").split()
        if len(str_answer) == 2:
            try:
                mas_answer = list(map(int, str_answer))
            except:
                print("Некорректный ввод. Вы ввели не число, а что-то другое")
                continue
            if list_correct(mas_answer):
                if board[mas_answer[0], mas_answer[1]] not in 'xo':
                    board[mas_answer[0], mas_answer[1]] = player_hod
                    val = True
                else:
                    print("Это поле уже заполнено, выберите другое")
            else:
                print("Недопустимая комбинация. Повторите ввод как указано ниже")
        else:
            print(
                "Вы не ввели обе координаты, не разделили их пробелом, либо указали слишком много координат через пробел. Повторите ввод")


def check_winner(board):
    # переводим двумерный список в одномерный и сравниваем его с условиями выигрыша
    # возвращает: крестик или нолик победителя или False, если выигрышная комбинация не достигнута
    res = board.flatten()

    win_combination = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for i in win_combination:
        if (res[i[0]] == res[i[1]] == res[i[2]]) and (res[i[0]] != '-'):
            return res[i[0]]
    return False


def krestikinoliki(board):
    readme()
    counter = 0  # счетчик количества ходов
    win = False
    while not win:
        draw_board_np(board)
        if counter % 2 == 0:
            take_input_np("x")
        else:
            take_input_np("o")
        counter += 1
        if counter > 4:  # до 5-го хода, учитывая очередность ходов, ни один из игроков не может выиграть
            tmp = check_winner(board)
            if tmp:
                print(f'Игрок, ставящий {tmp}, выиграл! Смотрите')
                win = True
                break
        if counter == 9:  # все поле заполнено
            print('Получилась ничья! Убедитесь сами:')
            break
    draw_board_np(board)


krestikinoliki(board)
