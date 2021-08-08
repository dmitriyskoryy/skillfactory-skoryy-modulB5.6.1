field = []
def build_clean_field():
    # двумерный список в качестве игрового поля
    global field
    field = [
        ['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-']
    ]

# функция для отрисовки поля во время игры
def display_field():
    print('  1  2  3')
    num_row = 0
    global field
    for i in field:
        num_row += 1
        print(f"{num_row} {i[0]}  {i[1]}  {i[2]}")


# проверяем на выигрыш
def check_win(ch):
    # проверяем на выигрыш по строкам
    global field
    for i in field:
        if i[0] == ch and i[1] == ch and i[2] == ch:
            # отобразить поле
            display_field()
            print(f"Поздравим игрока - '{ch}', он выиграл!")
            return 1
    # проверяем на выигрыш по столбцам
    count = 0
    for i in field:
        if i[0] == ch:
            count += 1
    if count == 3:
        # отобразить поле
        display_field()
        print(f"Поздравим игрока - '{ch}', он выиграл!")
        return 1

    # проверяем на выигрыш по диагонали
    if field[0][0] == ch and field[1][1] == ch and field[2][2] == ch or \
            field[0][2] == ch and field[1][1] == ch and field[2][0] == ch:
        # отобразить поле
        display_field()
        print(f"Поздравим игрока - '{ch}', он выиграл!")
        return 1



# игрок компьютер
def player_AI():
    def fun_AI(ch_1, ch_2):
        count = -1
        # проверяем по строкам
        for i in field:
            count += 1
            if i[0] == ch_1 and i[1] == ch_1:
                if field[count][2] == '-':
                    field[count][2] = ch_2
                    #проверяем на выигрыш
                    if check_win('o') == 1:
                        build_clean_field()
                        return 1
                    return 2

            elif i[0] == ch_1 and i[2] == ch_1:
                if field[count][1] == '-':
                    field[count][1] = ch_2
                    # проверяем на выигрыш
                    if check_win('o') == 1:
                        build_clean_field()
                        return 1
                    return 2

            elif i[1] == ch_1 and i[2] == ch_1:
                if field[count][0] == '-':
                    field[count][0] = ch_2
                    # проверяем на выигрыш
                    if check_win('o') == 1:
                        build_clean_field()
                        return 1
                    return 2



        # проверяем по столбцам
        for j in range(0, 3):
            if field[0][j] == ch_1 and field[1][j] == ch_1:
                if field[2][j] == '-':
                    field[2][j] = ch_2
                    # проверяем на выигрыш
                    if check_win('o') == 1:
                        build_clean_field()
                        return 1
                    return 2

            if field[0][j] == ch_1 and field[2][j] == ch_1:
                if field[1][j] == '-':
                    field[1][j] = ch_2
                    # проверяем на выигрыш
                    if check_win('o') == 1:
                        build_clean_field()
                        return 1
                    return 2

            if field[1][j] == ch_1 and field[2][j] == ch_1:
                if field[0][j] == '-':
                    field[0][j] = ch_2
                    # проверяем на выигрыш
                    if check_win('o') == 1:
                        build_clean_field()
                        return 1
                    return 2


        # проверяем по диагонали
        if field[0][0] == ch_1 and field[1][1] == ch_1:
            if field[2][2] == '-':
                field[2][2] = ch_2
                # проверяем на выигрыш
                if check_win('o') == 1:
                    build_clean_field()
                    return 1
                return 2

        if field[0][0] == ch_1 and field[2][2] == ch_1:
            if field[1][1] == '-':
                field[1][1] = ch_2
                # проверяем на выигрыш
                if check_win('o') == 1:
                    build_clean_field()
                    return 1
                return 2

        if field[1][1] == ch_1 and field[2][2] == ch_1:
            if field[0][0] == '-':
                field[0][0] = ch_2
                # проверяем на выигрыш
                if check_win('o') == 1:
                    build_clean_field()
                    return 1
                return 2


        if field[0][2] == ch_1 and field[1][1] == ch_1:
            if field[2][0] == '-':
                field[2][0] = ch_2
                # проверяем на выигрыш
                if check_win('o') == 1:
                    build_clean_field()
                    return 1
                return 2

        if field[0][2] == ch_1 and field[2][0] == ch_1:
            if field[1][1] == '-':
                field[1][1] = ch_2
                # проверяем на выигрыш
                if check_win('o') == 1:
                    build_clean_field()
                    return 1
                return 2

        if field[1][1] == ch_1 and field[2][0] == ch_1:
            if field[0][2] == '-':
                field[0][2] = ch_2
                # проверяем на выигрыш
                if check_win('o') == 1:
                    build_clean_field()
                    return 1
                return 2


    # если в строке, столбце или по диагонали более одного х, или более одного О, то проставляем О
    if fun_AI('o', 'o') != 2 and \
        fun_AI('x', 'o') != 2:
            for i in range(0, 3):
                for j in range(0, 3):
                    if field[i][j] == '-':
                        field[i][j] = 'o'
                        if check_win('o') == 1:
                            build_clean_field()
                            return
                        return





build_clean_field()
print("Игра крестики-нолики")
print("Вы играете за 'Х', вводите № строки и № столбца. Для выхода из игры введите q.")


# игра с компьютером
game = True
while game:
    row = 0
    col = 0

    # отобразить поле
    display_field()

    f = False
    for i in range(0, 3):
        for j in range(0, 3):
            if field[i][j] == '-':
                f = True
    if not f:
        print("Ничья!")
        build_clean_field()
        continue

    input_Player_one = True
    while input_Player_one:
        player_one = input("Ваш ход, введите № строки и № столбца: ")
        player_one = player_one.replace(" ", "")

        if not player_one.isdigit():
            print("Необходимо указать строку и столбец, например ввести: 23")
            continue

        if player_one == 'q':
            break

        if int(player_one) // 10 < 1 or int(player_one) // 10 > 3 and  \
                int(player_one) % 10 < 1 or int(player_one) % 10 > 3 or \
                len(player_one) != 2:
            print("Необходимо указать строку и столбец в диапазонах от 1 до 3, например ввести: 23")
            continue
        else:
            row = int(player_one) // 10 - 1
            col = int(player_one) % 10 - 1

        if field[row][col] == '-':
            break
        else:
            print(f"Ячейка {row+1}-{col+1} уже занята, выберите другую!")
            continue

    if player_one == 'q':
        print("Игра окончена!")
        break

    # заносим на поле ячейку выбранную игроком
    field[row][col] = 'x'

    # проверяем на выигрыш
    if check_win('x') == 1:
        build_clean_field()
        continue

    # ход player AI
    player_AI()




