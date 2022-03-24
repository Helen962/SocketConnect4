## Mengchen Xu 61281584 and Zhuoyue Lian 33822074
##
## project2_console.py
## ICS 32 lab 7
## This module is a console-only version of Connect Four

import connectfour
import common

def _handle_user_answer1()->bool:
    '''ask the user whether they wanna start a game'''
    done = False
    while not done:
        use_answer = input("Do you want to play the game? Y/N" + "\n")
        user_answer = use_answer.strip()
        if user_answer.lower() == "y":
            print("The first turn is RED")
            return True
            done = True
        elif user_answer.lower() == "n":
            return False
            done = True
        else:
            print("The answer is invalid, please try again.")
            continue
    
def _determine_turns(count:int)->str:
    '''determine the turn for the player'''
    turns = ""
    if count % 2 == 0:
        turns = "YELLOW"
    else:
        turns = "RED"
    return turns

def _game_processing()-> 'GameState':
    '''processing the game'''
    game_state = connectfour.new_game()
    count = 0
    while True:
        action = common.handle_input_action(game_state)
        try:
            if action.lower() == 'drop':
                game_state = common.each_drop(game_state)[0]
                common.print_board(game_state)
                print()
                turns = _determine_turns(count)
                print("Now is " +  turns + "'s turn.")
                count += 1
                if common.output_of_winner(game_state):
                    break
            else:
                game_state = common.each_pop(game_state)[0]
                common.print_board(game_state)
                print()
                turns = _determine_turns(count)
                print("Now is " +  turns + "'s turn.")
                count += 1
                if common.output_of_winner(game_state):
                    break
        except connectfour.InvalidMoveError:
            print("You cannot pop this point.\n" + "It is an invalid move\n" + "Please try again")
            pass
        except connectfour.GameOverError:
            pass

def _playing_process():
    '''play the game'''
    if _handle_user_answer1():
        _game_processing()
    else:
        print("Thank you! Bye-bye")
        
if __name__ == "__main__":
    _playing_process() 
