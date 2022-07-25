game_board = [[" "," "," "],[" "," "," "],[" "," "," "]]

line = "-" * 9


def print_board():
    for row in game_board:
        for i in range(0, 3):
            if i == 0:
                print(f"{row[i]} |", end="")
            elif i == 1:
                print(f" {row[i]} |", end="")
            elif i == 2:
                print(f" {row[i]}")
        print(line)



play_again = "Y"
loop = False

while play_again.upper() == "Y":
    game_board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    print_board()

    open_spots = 9
    game_over = None

    while open_spots > 0:

        if game_over:
            if (open_spots + 1) % 2 == 0:
                print("O's Win!")
                break
            elif (open_spots + 1) % 2 != 0:
                print("X's Win!")
                break


        if open_spots % 2 != 0:

            placement_col = None
            placement_row = None
            options = [0, 1, 2]
            while placement_row not in options:
                try:
                    placement_row = int(input("Choose a ROW to place an 'X' (1, 2, or 3): ")) - 1
                except ValueError:
                    placement_row = -1

            while placement_col not in options:
                try:
                    placement_col = int(input("Choose a COLUMN to place an 'X' (1, 2, or 3): ")) - 1
                except ValueError:
                    placement_col = -1

            if game_board[placement_row][placement_col] == " ":
                game_board[placement_row][placement_col] = "X"
                open_spots -= 1

            else:
                print("That spot is taken.")



        elif open_spots % 2 == 0:

            placement_col = None
            placement_row = None
            options = [0, 1, 2]
            while placement_row not in options:
                try:
                    placement_row = int(input("Choose a ROW to place an 'X' (1, 2, or 3): ")) - 1
                except ValueError:
                    placement_row = -1

            while placement_col not in options:
                try:
                    placement_col = int(input("Choose a COLUMN to place an 'X' (1, 2, or 3): ")) - 1
                except ValueError:
                    placement_col = -1

            if game_board[placement_row][placement_col] == " ":
                game_board[placement_row][placement_col] = "O"
                open_spots -= 1

            else:
                print("That spot is taken.")

        print_board()

        # v  Checks for horizontal win  v #
        for row in game_board:
            if row[0] == row[1] == row[2] and " " not in row:
                game_over = True

        # v  Checks for vertical win  v #
        for index in range(0, 3):
            col_i = 0
            row_i = 0

            row_1 = game_board[row_i][col_i]
            row_i += 1
            row_2 = game_board[row_i][col_i]
            row_i += 1
            row_3 = game_board[row_i][col_i]
            col_i += 1

            col_list = [row_1, row_2, row_3]

            if row_1 == row_2 == row_3 and " " not in col_list:
                game_over = True
                break

        # v  Checks for left to right diagonal win  v #
            if not game_over:
                col_i = 0
                row_i = 0

                row_1 = game_board[row_i][col_i]
                row_i += 1
                col_i += 1
                row_2 = game_board[row_i][col_i]
                row_i += 1
                col_i += 1
                row_3 = game_board[row_i][col_i]

                col_list = [row_1, row_2, row_3]

                if row_1 == row_2 == row_3 and " " not in col_list:
                    game_over = True

            # v  Checks for right to left diagonal win  v #
            if not game_over:
                col_i = 2
                row_i = 0

                row_1 = game_board[row_i][col_i]
                row_i += 1
                col_i -= 1
                row_2 = game_board[row_i][col_i]
                row_i += 1
                col_i -= 1
                row_3 = game_board[row_i][col_i]

                col_list = [row_1, row_2, row_3]

                if row_1 == row_2 == row_3 and " " not in col_list:
                    game_over = True

    play_again = input("Enter 'Y' to play again or any other key to quit: ")