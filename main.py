import functions

pick_nick = True
revenge = True
gameplay = True

while pick_nick:
    functions.clear()
    print(functions.logo)
    p1_nick = input("Player 1 nickname: ")
    p1_symbol = input(f"{p1_nick} symbol: ")
    p2_nick = input("Player 2 nickname: ")
    p2_symbol = input(f"{p2_nick} symbol: ")
    functions.clear()
    print(f"{p1_nick} - {p1_symbol}")
    print(f"{p2_nick} - {p2_symbol}\n\n")
    input("Press any key . . .")
    revenge = True
    gameplay = True
    while revenge:
        board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        functions.clear()
        while gameplay:
            functions.clear()
            functions.draw_board(board)
            if functions.board_count(board,
                                     p1_symbol) == functions.board_count(
                                         board, p2_symbol):
                #player 1 turn
                print(f"{p1_nick} turn.")
                coord = input("Type Coordinates where you want to pick: ")
                board[int(coord[0]) - 1][int(coord[1]) - 1] = p1_symbol
                functions.clear()
                functions.draw_board(board)
            if functions.check_win(board):
                print(f"{p1_nick} win!")
                break
            if functions.board_count(board, p1_symbol) > functions.board_count(
                    board, p2_symbol):
                print(f"{p2_nick} turn.")
                coord = input("Type Coordinates where you want to pick: ")
                board[int(coord[0]) - 1][int(coord[1]) - 1] = p2_symbol
                functions.clear()
                functions.draw_board(board)
            if functions.check_win(board):
                print(f"{p2_nick} win!")
                break
        input("Press any key . . .")
        functions.clear()
        revenge = int(
            input("Type '1' if you want a revenge (if not type '0')"))
    pick_nick = int(
        input("Type '1' if you want to check nickname (to exit type '0')"))
