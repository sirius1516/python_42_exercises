"""
Write a getChessSquareColor() function that has parameters column and row. The
function either returns 'black' or 'white' depending on the color at the specified column and
row. Chess boards are 8 x 8 spaces in size, and the columns and rows in this program begin at 0 and
end at 7 like in Figure 9-1. If the arguments for column or row are outside the 0 to 7 range, the
function returns a blank string.
"""

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
