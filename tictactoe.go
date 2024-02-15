package main

import (
	"fmt"
	"os"
	"os/exec"
)

func main() {
	grid := []rune{' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '}
	errors := 0

	clearScreen()
	fmt.Println()
	fmt.Println("Welcome to Tic-Tac-Toe! Grid coordinates are on the right from the grid.")
	fmt.Println("Write '5' if you want to place X in the center.")

	for {
		if errors == 0 {
			fmt.Println("---------")
			fmt.Printf("| %c %c %c | # 1 2 3\n", grid[0], grid[1], grid[2])
			fmt.Printf("| %c %c %c | # 4 5 6\n", grid[3], grid[4], grid[5])
			fmt.Printf("| %c %c %c | # 7 8 9\n", grid[6], grid[7], grid[8])
			fmt.Println("---------")
		}
		errors = 0
		x_num := countOccurrences(grid, 'X')
		o_num := countOccurrences(grid, 'O')
		xo_sum := x_num + o_num

		if checkWin(grid, 'X') {
			fmt.Println("X wins")
			break
		} else if checkWin(grid, 'O') {
			fmt.Println("O wins")
			break
		} else if xo_sum == 9 {
			fmt.Println("Draw")
			break
		}

		var cors int
		fmt.Print("Enter cell:")
		_, err := fmt.Scan(&cors)
		if err != nil {
			errors = 1
			fmt.Println("Please, enter numbers")
			continue
		}

		if 1 <= cors && cors <= 9 {
			index := cors - 1
			if grid[index] == ' ' || grid[index] == '_' {
				if xo_sum%2 == 0 {
					grid[index] = 'X'
				} else {
					grid[index] = 'O'
				}
			} else {
				fmt.Println("This cell is occupied! Choose another one!")
				errors = 1
			}
		} else {
			fmt.Println("Coordinates should be from 1 to 9!")
			errors = 1
		}
		clearScreen()
	}
}

func clearScreen() {
	cmd := exec.Command("clear") // Linux example, for Windows use "cls"
	cmd.Stdout = os.Stdout
	cmd.Run()
}

func countOccurrences(array []rune, target rune) int {
	count := 0
	for _, element := range array {
		if element == target {
			count++
		}
	}
	return count
}

func checkWin(grid []rune, player rune) bool {
	return (grid[0] == player && grid[1] == player && grid[2] == player) ||
		(grid[3] == player && grid[4] == player && grid[5] == player) ||
		(grid[6] == player && grid[7] == player && grid[8] == player) ||
		(grid[0] == player && grid[3] == player && grid[6] == player) ||
		(grid[1] == player && grid[4] == player && grid[7] == player) ||
		(grid[2] == player && grid[5] == player && grid[8] == player) ||
		(grid[0] == player && grid[4] == player && grid[8] == player) ||
		(grid[2] == player && grid[4] == player && grid[6] == player)
}
