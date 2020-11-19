import random

def display(board):
    print(board[0]+"    |  "+board[1]+"  |    "+board[2])
    print("------------------")
    print(board[3]+"    |  "+board[4]+"  |    "+board[5])
    print("------------------")
    print(board[6]+"    |  "+board[7]+"  |    "+board[8])

def winner(board):
    # across top
    if board[0] == board[1] == board[2] != '':
        return True
    # across middle
    elif board[3] == board[4] == board[5] != '':
        return True
    # across bottom
    elif board[6] == board[7] == board[8] != '':
        return True
    # vertical left
    elif board[0] == board[3] == board[6] != '':
        return True
    # vertical middle
    elif board[1] == board[4] == board[7] != '':
        return True
    # vertical right
    elif board[2] == board[5] == board[8] != '':
        return True
    # diagonal
    elif board[0] == board[4] == board[8] != '':
        return True
    # diagonal
    elif board[2] == board[4] == board[6] != '':
        return True
    else:
        return False

def ai_move(turn,possible_moves,board):
    # turn 1
    if turn == 1:
        if board[4] == '':
            return 5
        else:
            return 1
    else:
        # check the board state for 2 in a row pieces.
        # across top
        if board[0] == board[1] != '' or board[0] == board[2] != '' or board[1] == board[2] != '':
            moves = str([1,2,3])
            for move in moves:
                if move in possible_moves:
                    return move
        # across middle
        if board[3] == board[4] != '' or board[3] == board[5] != '' or board[4] == board[5] != '':
            moves = str([4,5,6])
            for move in moves:
                if move in possible_moves:
                    return move
        # across bottom
        if board[6] == board[7] != '' or board[6] == board[8] != '' or board[7] == board[8] != '':
            moves = str([7,8,9])
            for move in moves:
                if move in possible_moves:
                    return move
        # vertical left
        if board[0] == board[3] != '' or board[0] == board[6] != '' or board[3] == board[6] != '':
            moves = str([1,4,7])
            for move in moves:
                if move in possible_moves:
                    return move
        # vertical middle
        if board[1] == board[4] != '' or board[1] == board[7] != '' or board[4] == board[7] != '':
            moves = str([2,5,8])
            for move in moves:
                if move in possible_moves:
                    return move
        # vertical right
        if board[2] == board[5] != '' or board[2] == board[8] != '' or board[5] == board[8] != '':
            moves = str([3,6,9])
            for move in moves:
                if move in possible_moves:
                    return move
        # diagonal
        if board[0] == board[4] != '' or board[0] == board[8] != '' or board[4] == board[8] != '':
            moves = str([1,5,9])
            for move in moves:
                if move in possible_moves:
                    return move
        # diagonal
        if board[2] == board[4] != '' or board[2] == board[6] != '' or board[4] == board[6] != '':
            moves = str([3,5,7])
            for move in moves:
                if move in possible_moves:
                    return move

def rand_move(possible_moves):
    max_int = len(possible_moves)-1
    rand = random.randint(0,max_int)
    return possible_moves[rand]

def engine():
    print("Squares are labelled as such: \n")
    possible_moves = [str(i+1) for i in range(9)]
    print(display(possible_moves))
    turn = 0
    max_turns = 9
    while turn < max_turns:
        print("\nIt is %s turn. Which square would you like to place your %s:" %(p_turn,piece))
        print(possible_moves)
        if p_turn != 'Computer':
            move = input()
            if move in possible_moves:
                possible_moves.remove(move)
                board[int(move)-1] = piece
                turn += 1
            else:
                print("That move is not valid.")
                continue
        else:
            move = ai_move(turn,possible_moves,board)
            if move == None:
                move = rand_move(possible_moves)
            print("Computer selects square %s." % (move))
            possible_moves.remove(str(move))
            board[int(move)-1] = piece
            turn += 1
        # winner check
        if turn >= 5:
            if winner(board) == True:
                print(display(board))
                return print("Congratulations %s, you are the Winner!" %(p_turn))         
        # change turn and piece
        if piece == "X":
            p_turn = p2
            piece = "O"
        else:
            p_turn = p1
            piece = "X"
        # display board for new turn
        display(board)
    return print("The game is a draw.")

if __name__ == "__main__":
    play = 'y'
    while play == 'y':
        board = ['' for i in range(9)]
        ai = ''
        while ai != 'n' or 'y':
            ai = input("Would you like to play against the computer?(y/n) ")
            if ai == 'n':
                p1 = input("Player 1: ")
                p2 = input("Player 2: ")
                break
            elif ai == 'y':
                p1 = input("Player 1: ")
                p2 = "Computer"
                break
            else:
                print('Invalid Input \n')

        print(p1 + " is X")
        print(p2 + " is O")
        engine()
        play = input("Would you like to play again?(y/n) ")
