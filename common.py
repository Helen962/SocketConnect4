## Mengchen Xu 61281584 and Zhuoyue Lian 33822074
##
## common.py
## ICS 32 lab 7
## This module provides a set of functions that are shared in other modules

import connectfour
def print_board(state:'game_board')->None:
    '''print the board of the game state'''
    point = ""
    for num in range(1,connectfour.BOARD_COLUMNS+1):
        print(str(num), end = " ")
    print()
    for i in range(connectfour.BOARD_ROWS):
        for j in range(connectfour.BOARD_COLUMNS):
            if state.board[j][i] == 1:
                point = "R"
            elif state.board[j][i] == 2:
                point = "Y"
            else:
                point = "."
            print(point,end = " ")
        print()

def determine_new_game(game_board:"game_board")->bool:
    '''determine whether it is a new game'''
    result = ""
    number1 = 0
    number2 = 0
    for raw in range(len(game_board.board)):
        for column in range(len(game_board.board[raw])):
            result = result + str(game_board.board[raw][column])
            number1 = result.count("1")
            number2 = result.count("2")
    if number1 >= 1 and number2 >= 1 :
        return False
    else:
        return True

def handle_input_action(game_state:"GameState")->str:
    '''return the action of the player'''
    done = False
    while not done:
        action =  valid_drop_pop()
        if determine_new_game(game_state):
            try:
                if action == "drop":
                    return action
                    done = True
                elif action == "pop":
                    print("You are playing a new game, the first step should be drop, please try agin.")
                    done = False
                else:
                    print("It is an invalid move, please try again")
                    done = False
            except connectfour.InvalidMoveError:
                print("It is an invalid move, please try again")
                done = False
        elif determine_new_game(game_state) == False:
            return action
            done = Trueb
        else:
            print("The statement is invalid, please try again.")
            done = False


def valid_column()->int:
    '''return the valid column'''
    while True:
        column = input("What column do you want to choose? (Between 1 and 7)\n")
        try:
            if 1 <= int(column) <= 7:
                return int(column)-1
                break
            else:
                print("Please enter a valid number between 1 and 7")
        except ValueError:
            print("Please enter a valid number between 1 and 7")


def valid_drop_pop()->str:
    '''return the valid action'''
    result = ""
    while True:
        move = input("What is the next step? Drop/Pop"+ "\n")
        move = move.strip()
        try:
            if move.lower() == "drop":
                result = "drop"
                return result
            elif move.lower() == "pop":
                result = "pop"
                return result
            else:
                print("Please enter a valid commend. (Drop / Pop)")
        except ValueError:
            print("Please enter a valid commend. (Drop / Pop)")
        except AttributeError:
            print("Please enter a valid commend. (Drop / Pop)")
        except TypeError:
            print("Please enter a valid commend. (Drop / Pop)")

def each_drop(game_board:'GameState')->['GameState','column']:
    '''return a list of game state and column number after each drop'''
    result_list = []
    column = valid_column()
    game_board = connectfour.drop(game_board,column)
    result_list.append(game_board)
    result_list.append(column)
    return result_list

def each_pop(game_board:'GameState')->['GameState','column']:
    '''return a list of game state and column number after each pop'''
    result_list = []
    column = valid_column()
    game_board = connectfour.pop(game_board,column)
    result_list.append(game_board)
    result_list.append(column)
    return result_list


def output_of_winner(state:connectfour.GameState)->bool:
    '''check the winner'''
    while True:
        if connectfour.winner(state) == 1:
            print("The winner is RED.")
            return True
        elif connectfour.winner(state) == 2:
            print("The winner is YELLOW.")
            return True
        else:
            return False

