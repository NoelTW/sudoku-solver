board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7],
]


def solve(bo):
    """
    solve sudoku
    this function recursively solve each element in the board (row,col)
    if find function return False means there is no longer and element is 0
    """
    print_board(bo)
    print('===================================')
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def valid(bo, num, pos):
    # check row
    for element in range(len(bo[0])):
        if bo[pos[0]][element] == num and pos[1] != element:
            return False

    # check column
    for element in range(len(bo)):
        if bo[element][pos[1]] == num and pos[0] != element:
            return False

    # check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for y in range(box_y * 3, box_y * 3 + 3):
        for x in range(box_x * 3, box_x * 3 + 3):
            if bo[y][x] == num and (y, x) != pos:
                return False
    return True


def print_board(bo):
    for row in range(len(bo)):
        if row % 3 == 0 and row != 0:
            print('--------------------------')
        for col in range(len(bo[0])):
            if col % 3 == 0 and col != 0:
                print(' | ', end='')
            if col == 8:
                print(str(bo[row][col]))
            else:
                print(str(bo[row][col]) + ' ', end='')


def find_empty(bo):
    for row in range(len(bo)):
        for col in range(len(bo[0])):
            if bo[row][col] == 0:
                return (row, col)  # give the empty y x
    return None


print_board(board)
print('===================================')
solve(board)
