import time


def show_board():
    print(f"{board[1]} | {board[2]} | {board[3]}")
    print("--------- ")
    print(f"{board[4]} | {board[5]} | {board[6]}")
    print("---------")
    print(f"{board[7]} | {board[8]} | {board[9]}\n")


def is_win(symbol):
    if ((board[1] == symbol and board[2] == symbol and board[3] == symbol) or
            (board[4] == symbol and board[5] == symbol and board[6] == symbol) or
            (board[7] == symbol and board[8] == symbol and board[9] == symbol) or
            (board[1] == symbol and board[4] == symbol and board[7] == symbol) or
            (board[2] == symbol and board[5] == symbol and board[8] == symbol) or
            (board[3] == symbol and board[6] == symbol and board[9] == symbol) or
            (board[1] == symbol and board[5] == symbol and board[9] == symbol) or
            (board[3] == symbol and board[5] == symbol and board[7] == symbol)):
        return True
    else:
        return False


def is_draw(symbol):
    if " " not in board.values() and not is_win(symbol):
        return True
    else:
        return False


def is_space_free(position):
    if board[position] == " ":
        return True


def place_symbol(position, symbol):
    if is_space_free(position):
        board[position] = symbol
        show_board()

        if is_draw(symbol):
            print("It's a draw")
            exit()

        elif is_win(symbol):
            if symbol == "O":
                print("Bad luck. You lose.")
                exit()
            else:
                print("Congrats, you win!")
                exit()
        return

    else:
        position = input(f"That place is not empty.\nWhere do you want to place the {symbol} (1 to 9)?: ")
        place_symbol(int(position), symbol)
        return


def player_place_x():
    x_input = input("Where do you want to place the X (1 to 9)?: ")
    place_symbol(int(x_input), "X")


def bot_place_o():
    # Bot is trying to MAX the score
    best_score = - float('inf')
    best_move = None
    for key in board:
        if board[key] == " ":
            board[key] = "O"
            score = minimax(board, 0, False)
            board[key] = " "
            if score > best_score:
                best_score = score
                best_move = key
    place_symbol(best_move, "O")
    return


def minimax(board, depth, is_maximizing):
    # Check if bot wins
    if is_win("O"):
        return 1
    # Check if bot loses
    elif is_win("X"):
        return -1
    # Check if it is a draw
    elif is_draw("O"):
        return 0

    if is_maximizing:
        best_score = - float('inf')
        for key in board:
            if board[key] == " ":
                board[key] = "O"
                score = minimax(board, 0, False)
                board[key] = " "
                if score > best_score:
                    best_score = score
        return best_score

    else:
        best_score = float('inf')
        for key in board:
            if board[key] == " ":
                board[key] = "X"
                score = minimax(board, 0, True)
                board[key] = " "
                if score < best_score:
                    best_score = score
        return best_score


board = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "}

show_board()

GAME_ON = True

while GAME_ON:
    player_place_x()
    time.sleep(1)
    bot_place_o()
