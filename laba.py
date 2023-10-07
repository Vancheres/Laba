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