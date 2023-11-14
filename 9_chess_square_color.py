def get_chess_square_color(column, row):
    if column >= 8 or row >= 8:
        return ' '
    elif column % 2 == row % 2:
        return 'White'
    else:
        return 'Black'


print(get_chess_square_color(1, 2))

assert get_chess_square_color(1, 1) == 'White'
assert get_chess_square_color(2, 1) == 'Black'
assert get_chess_square_color(1, 2) == 'Black'
assert get_chess_square_color(8, 8) == ' '
assert get_chess_square_color(0, 8) == ' '
assert get_chess_square_color(2, 9) == ' '
