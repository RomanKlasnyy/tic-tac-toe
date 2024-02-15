import java.util.Scanner;

public class TicTacToe {
    public static void main(String[] args) {
        char[] grid = {' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '};
        int errors = 0;

        System.out.println();
        System.out.println("Welcome to Tic-Tac-Toe! Grid coordinates are on the right from the grid.");
        System.out.println("Write '5' if you want to place X in the center.");

        while (true) {
            if (errors == 0) {
                System.out.println("---------");
                System.out.println("| " + grid[0] + " " + grid[1] + " " + grid[2] + " |" + " # 1 2 3");
                System.out.println("| " + grid[3] + " " + grid[4] + " " + grid[5] + " |" + " # 4 5 6");
                System.out.println("| " + grid[6] + " " + grid[7] + " " + grid[8] + " |" + " # 7 8 9");
                System.out.println("---------");
            }
            errors = 0;
            int x_num = countOccurrences(grid, 'X');
            int o_num = countOccurrences(grid, 'O');
            int xo_sum = x_num + o_num;

            if (checkWin(grid, 'X')) {
                System.out.println("X wins");
                break;
            } else if (checkWin(grid, 'O')) {
                System.out.println("O wins");
                break;
            } else if (xo_sum == 9) {
                System.out.println("Draw");
                break;
            }

            int cors = 0;
            try {
                Scanner scanner = new Scanner(System.in);
                System.out.print("Enter cell:");
                cors = scanner.nextInt();
            } catch (Exception e) {
                errors = 1;
                System.out.println("Please, enter numbers");
                continue;
            }

            if (1 <= cors && cors <= 9) {
                int index = cors - 1;
                if (grid[index] == ' ' || grid[index] == '_') {
                    grid[index] = (xo_sum % 2 == 0) ? 'X' : 'O';
                } else {
                    System.out.println("This cell is occupied! Choose another one!");
                    errors = 1;
                }
            } else {
                System.out.println("Coordinates should be from 1 to 9!");
                errors = 1;
            }
        }
    }

    public static int countOccurrences(char[] array, char target) {
        int count = 0;
        for (char element : array) {
            if (element == target) {
                count++;
            }
        }
        return count;
    }

    public static boolean checkWin(char[] grid, char player) {
        return (grid[0] == player && grid[1] == player && grid[2] == player) ||
                (grid[3] == player && grid[4] == player && grid[5] == player) ||
                (grid[6] == player && grid[7] == player && grid[8] == player) ||
                (grid[0] == player && grid[3] == player && grid[6] == player) ||
                (grid[1] == player && grid[4] == player && grid[7] == player) ||
                (grid[2] == player && grid[5] == player && grid[8] == player) ||
                (grid[0] == player && grid[4] == player && grid[8] == player) ||
                (grid[2] == player && grid[4] == player && grid[6] == player);
    }
}
