#include <stdio.h>
#include <ctype.h>

int countOccurrences(char array[], char target) {
    int count = 0;
    for (int i = 0; array[i] != '\0'; i++) {
        if (array[i] == target) {
            count++;
        }
    }
    return count;
}

int checkWin(char grid[], char player) {
    return (grid[0] == player && grid[1] == player && grid[2] == player) ||
           (grid[3] == player && grid[4] == player && grid[5] == player) ||
           (grid[6] == player && grid[7] == player && grid[8] == player) ||
           (grid[0] == player && grid[3] == player && grid[6] == player) ||
           (grid[1] == player && grid[4] == player && grid[7] == player) ||
           (grid[2] == player && grid[5] == player && grid[8] == player) ||
           (grid[0] == player && grid[4] == player && grid[8] == player) ||
           (grid[2] == player && grid[4] == player && grid[6] == player);
}

void printGrid(char grid[]) {
    printf("---------\n");
    printf("| %c %c %c |\n", grid[0], grid[1], grid[2]);
    printf("| %c %c %c |\n", grid[3], grid[4], grid[5]);
    printf("| %c %c %c |\n", grid[6], grid[7], grid[8]);
    printf("---------\n");
    printf("# 1 2 3\n");
    printf("# 4 5 6\n");
    printf("# 7 8 9\n");
}

int main() {
    char grid[9] = {' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '};
    int errors = 0;

    printf("\nWelcome to Tic-Tac-Toe! Grid coordinates are on the right from the grid.\n");
    printf("Write '5' if you want to place X in the center.\n");

    while (1) {
        if (errors == 0) {
            printGrid(grid);
        }
        errors = 0;

        int x_num = countOccurrences(grid, 'X');
        int o_num = countOccurrences(grid, 'O');
        int xo_sum = x_num + o_num;

        if (checkWin(grid, 'X')) {
            printf("X wins\n");
            break;
        } else if (checkWin(grid, 'O')) {
            printf("O wins\n");
            break;
        } else if (xo_sum == 9) {
            printf("Draw\n");
            break;
        }

        int cors = 0;
        printf("Enter cell: ");
        if (scanf("%d", &cors) != 1) {
            errors = 1;
            printf("Please, enter numbers\n");
            while (getchar() != '\n');
            continue;
        }

        if (1 <= cors && cors <= 9) {
            int index = cors - 1;
            if (grid[index] == ' ') {
                grid[index] = (xo_sum % 2 == 0) ? 'X' : 'O';
            } else {
                printf("This cell is occupied! Choose another one!\n");
                errors = 1;
            }
        } else {
            printf("Coordinates should be from 1 to 9!\n");
            errors = 1;
        }
        while (getchar() != '\n');
    }

    return 0;
}
