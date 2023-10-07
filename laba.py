def is_same_color_square(k, l, m, n):
    return (k + l) % 2 == (m + n) % 2

def is_threatened(figure, k, l, m, n):
    if figure == 'ферзь':
        return k == m or l == n or abs(k - m) == abs(l - n)
    elif figure == 'ладья':
        return k == m or l == n
    elif figure == 'слон':
        return abs(k - m) == abs(l - n)
    elif figure == 'конь':
        return (abs(k - m) == 1 and abs(l - n) == 2) or (abs(k - m) == 2 and abs(l - n) == 1)
    else:
        return False

def can_reach_in_one_move(figure, k, l, m, n):
    if figure == 'ферзь':
        return k == m or l == n or abs(k - m) == abs(l - n)
    elif figure == 'ладья':
        return k == m or l == n
    elif figure == 'слон':
        return abs(k - m) == abs(l - n)
    else:
        return False

def two_moves_path(figure, k, l, m, n):
    if figure == 'ферзь':
        return [(k, n), (m, n)]
    elif figure == 'ладья':
        return [(k, n), (m, n)]
    elif figure == 'слон':
        return [(k, l), (k, m), (m, n)]
    else:
        return []

def display_chessboard(k, l, m, n):
    for i in range(8, 0, -1):
        for j in range(1, 9):
            if (i + j) % 2 == 0:
                print('□', end=' ')
            else:
                print('■', end=' ')
        print()

    print(f"\nВыбранные поля: ({k}, {l}) и ({m}, {n})")

k = int(input("Введите вертикальную координату для поля k (буква a-h): ")).lower
l = int(input("Введите горизонтальную координату для поля l(цифра 1-8): "))
m = int(input("Введите вертикальную координату для поля m(буква a-h): ")).lower
n = int(input("Введите горизонтальную координату для поля n(цифра 1-8): "))
figure = input("Введите фигуру (ферзь, ладья, слон или конь): ")

result_a = "Поля разного цвета"
if is_same_color_square(k, l, m, n):
    result_a = "Поля одного цвета"

result_b = "Не угрожает"
if is_threatened(figure, k, l, m, n):
    result_b = "Угрожает"

result_c_one_move = "Нельзя добраться за один ход"
if can_reach_in_one_move(figure, k, l, m, n):
    result_c_one_move = "Можно добраться за один ход"

result_c_two_moves = two_moves_path(figure, k, l, m, n)

# Вывод результатов
print(f"а) {result_a}")
print(f"б) {result_b}")
print(f"в) {result_c_one_move}")
if result_c_one_move == "Нельзя добраться за один ход":
    print(f"   Маршрут за два хода: {result_c_two_moves}")

display_chessboard(k, l, m, n)