def sudoku():
    sudoku = [  [5, 0, 0, 0, 4, 0, 0, 0, 9],
                [0, 2, 0, 0, 1, 0, 6, 8, 0],
                [0, 0, 9, 8, 7, 0, 1, 0, 0],
                [0, 0, 6, 7, 0, 0, 2, 0, 0],
                [0, 9, 0, 3, 5, 4, 0, 6, 0],
                [3, 0, 0, 0, 0, 0, 0, 0, 1],
                [9, 0, 0, 0, 6, 0, 0, 0, 2],
                [0, 1, 4, 0, 3, 0, 0, 5, 7],
                [0, 0, 5, 0, 8, 7, 0, 0, 0]]

    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                print(" ", end=" ")
            else:
                print(sudoku[i][j], end=" ")
        print()

