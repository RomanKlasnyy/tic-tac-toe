grid = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
errors = 0

print()
print('Welcome to Tic-Tac-Toe! Grid coordinates are on the right from the grid.')
print('Write "2 2", if you want to place X in the center.')

while True:
    if errors == 0:
        print("---------")
        print("| " + grid[0] + " " + grid[1] + " " + grid[2] + " |" + " # (1, 3) (2, 3) (3, 3)")
        print("| " + grid[3] + " " + grid[4] + " " + grid[5] + " |" + " # (1, 2) (2, 2) (3, 2)")
        print("| " + grid[6] + " " + grid[7] + " " + grid[8] + " |" + " # (1, 1) (2, 1) (3, 1)")
        print("---------")
    errors = 0
    x_num = grid.count('X')
    o_num = grid.count('O')
    xo_sum = x_num + o_num

    # if X wins:
    if grid[0] == 'X' and grid[1] == 'X' and grid[2] == 'X':
        print('X wins')
        break
    elif grid[3] == 'X' and grid[4] == 'X' and grid[5] == 'X':
        print('X wins')
        break
    elif grid[6] == 'X' and grid[7] == 'X' and grid[8] == 'X':
        print('X wins')
        break
    elif grid[0] == 'X' and grid[3] == 'X' and grid[6] == 'X':
        print('X wins')
        break
    elif grid[1] == 'X' and grid[4] == 'X' and grid[7] == 'X':
        print('X wins')
        break
    elif grid[2] == 'X' and grid[5] == 'X' and grid[8] == 'X':
        print('X wins')
        break
    elif grid[0] == 'X' and grid[4] == 'X' and grid[8] == 'X':
        print('X wins')
        break
    elif grid[2] == 'X' and grid[4] == 'X' and grid[6] == 'X':
        print('X wins')
        break

    # if O wins:
    elif grid[0] == 'O' and grid[1] == 'O' and grid[2] == 'O':
        print('O wins')
        break
    elif grid[3] == 'O' and grid[4] == 'O' and grid[5] == 'O':
        print('O wins')
        break
    elif grid[6] == 'O' and grid[7] == 'O' and grid[8] == 'O':
        print('O wins')
        break
    elif grid[0] == 'O' and grid[3] == 'O' and grid[6] == 'O':
        print('O wins')
        break
    elif grid[1] == 'O' and grid[4] == 'O' and grid[7] == 'O':
        print('O wins')
        break
    elif grid[2] == 'O' and grid[5] == 'O' and grid[8] == 'O':
        print('O wins')
        break
    elif grid[0] == 'O' and grid[4] == 'O' and grid[8] == 'O':
        print('O wins')
        break
    elif grid[2] == 'O' and grid[4] == 'O' and grid[6] == 'O':
        print('O wins')
        break
    elif xo_sum == 9:
        print('Draw')
        break

    cors = input('Enter cells:').split()
    if cors[0].isdigit() and cors[1].isdigit():
        cors = [int(num) for num in cors]
        if 1 <= cors[0] <= 3 and 1 <= cors[1] <= 3:
            if cors[0] == 1 and cors[1] == 3:
                if grid[0] == ' ' or grid[0] == '_':
                    if xo_sum % 2 == 0:
                        grid[0] = 'X'
                    else:
                        grid[0] = 'O'
                else:
                    print('This cell is occupied! Choose another one!')
                    errors = 1

            elif cors[0] == 2 and cors[1] == 3:
                if grid[1] == ' ' or grid[1] == '_':
                    if xo_sum % 2 == 0:
                        grid[1] = 'X'
                    else:
                        grid[1] = 'O'
                else:
                    print('This cell is occupied! Choose another one!')
                    errors = 1

            elif cors[0] == 3 and cors[1] == 3:
                if grid[2] == ' ' or grid[2] == '_':
                    if xo_sum % 2 == 0:
                        grid[2] = 'X'
                    else:
                        grid[2] = 'O'
                else:
                    print('This cell is occupied! Choose another one!')
                    errors = 1

            elif cors[0] == 1 and cors[1] == 2:
                if grid[3] == ' ' or grid[3] == '_':
                    if xo_sum % 2 == 0:
                        grid[3] = 'X'
                    else:
                        grid[3] = 'O'
                else:
                    print('This cell is occupied! Choose another one!')
                    errors = 1

            elif cors[0] == 2 and cors[1] == 2:
                if grid[4] == ' ' or grid[4] == '_':
                    if xo_sum % 2 == 0:
                        grid[4] = 'X'
                    else:
                        grid[4] = 'O'
                else:
                    print('This cell is occupied! Choose another one!')
                    errors = 1

            if cors[0] == 3 and cors[1] == 2:
                if grid[5] == ' ' or grid[5] == '_':
                    if xo_sum % 2 == 0:
                        grid[5] = 'X'
                    else:
                        grid[5] = 'O'
                else:
                    print('This cell is occupied! Choose another one!')
                    errors = 1

            if cors[0] == 1 and cors[1] == 1:
                if grid[6] == ' ' or grid[6] == '_':
                    if xo_sum % 2 == 0:
                        grid[6] = 'X'
                    else:
                        grid[6] = 'O'
                else:
                    print('This cell is occupied! Choose another one!')
                    errors = 1

            if cors[0] == 2 and cors[1] == 1:
                if grid[7] == ' ' or grid[7] == '_':
                    if xo_sum % 2 == 0:
                        grid[7] = 'X'
                    else:
                        grid[7] = 'O'
                else:
                    print('This cell is occupied! Choose another one!')
                    errors = 1

            if cors[0] == 3 and cors[1] == 1:
                if grid[8] == ' ' or grid[8] == '_':
                    if xo_sum % 2 == 0:
                        grid[8] = 'X'
                    else:
                        grid[8] = 'O'
                else:
                    print('This cell is occupied! Choose another one!')
                    errors = 1

        else:
            print('Coordinates should be from 1 to 3!')
            errors = 1
    else:
        print('You should enter numbers!')
        errors = 1
