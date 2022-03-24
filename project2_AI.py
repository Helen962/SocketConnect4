## Mengchen Xu 61281584 and Zhuoyue Lian 33822074
##
## project2_AI.py
## ICS 32 lab 7
## This module allows player to play a game of Connect Four via a network
## by connecting to a server

import project2_socket 
import project2_console
import connectfour
import common

HOST = 'woodhouse.ics.uci.edu'
PORT = 4444

def _get_user()->str:
    '''get the user'''
    user = input("What is your name?\n")
    return user

def _AI_Move(connection,game_state,user)->'game_state':
    '''return the game state after AI moved'''
    answer = project2_socket.game_drop(connection,user[1])
    game_state = user[0]
    print("AI's Move: " + answer)
    if answer.split()[0]=='DROP':
        game_state = connectfour.drop(game_state,int(answer.split()[-1])-1)
        common.print_board(game_state)
        return game_state
    elif answer.split()[0]=='POP':
        game_state = connectfour.pop(game_state,int(answer.split()[-1])-1)
        common.print_board(game_state)
        return game_state
    else:
        project2_socket.close(connection)

def _handle():
    '''play the game via a net work by connecting to a server'''
    connection = project2_socket.game_connect(HOST,PORT)
    out = project2_socket.game_hello(connection,_get_user())
    if project2_socket.game_play(connection):
        game_state = connectfour.new_game()
        while True:
            action = common.handle_input_action(game_state)
            try:
                if action.lower() == 'drop':
                    user = common.each_drop(game_state)
                    game_state = _AI_Move(connection,game_state,user)
                    if common.output_of_winner(game_state):
                        break
                else:
                    user = common.each_pop(game_state)
                    game_state = _AI_Move(connection,game_state,user)
                    if common.output_of_winner(game_state):
                        break

            except connectfour.InvalidMoveError:
                print("You cannot pop this point.\n" + "It is an invalid move\n" + "Please try again")
                pass
            except connectfour.GameOverError:
                pass
          
if __name__=='__main__':
    _handle()
