## Mengchen Xu 61281584 and Zhuoyue Lian 33822074
##
## project2_socket.py
## ICS 32 lab 7
## This module provides a set of functions that implement the project2_AI
## using sockets

import socket

def game_connect(host: str, port: int) -> 'connection':
    '''connect the game'''
    game_socket = socket.socket()
    game_socket.connect((host, port))
    game_socket_input = game_socket.makefile('r')
    game_socket_output = game_socket.makefile('w')
    return game_socket, game_socket_input, game_socket_output

def game_hello(connection:'connection',username:str):
    '''write hello to the server'''
    game_socket, game_socket_in, game_socket_out = connection
    answer = 'I32CFSP_HELLO ' + username
    _write_line(connection,answer)
    line=_read_line(connection)
    print(line)
    return line

def game_play(connection:'connection')->bool:
    '''play the game when the server is ready'''
    game_socket, game_socket_in, game_socket_out = connection
    _write_line(connection,'AI_GAME')    
    response=_read_line(connection).strip()
    print(response)
    return response=='READY'

def game_drop(connection:'connection',column:int):
    '''return the action of AI player'''
    m = "DROP "+str(column+1)
    _write_line(connection,m)
    answer1 = _read_line(connection)
    action = _read_line(connection)
    answer2 = _read_line(connection)
    return action

def game_pop(conection:'connection',column:int):
    '''return the action of AI player'''
    _write_line(connection,str(column+1))
    answer1 = _read_line(connection)
    action = _read_line(connection)
    answer2 = _read_line(connection)
    return action   
 
def close(connection: 'connection') -> None:
    '''close the connection'''
    game_socket, game_socket_input, game_socket_output = connection
    game_socket_input.close()
    game_socket_output.close()
    game_socket.close()

def _write_line(connection: 'connection', line: str) -> None:
    '''write the line to the server'''
    game_socket, game_socket_input, game_socket_output = connection
    game_socket_output.write(line + '\r\n')
    game_socket_output.flush()

def _read_line(connection: 'connection') -> str:
    '''read the line'''
    game_socket, game_socket_input, game_socket_output = connection
    return game_socket_input.readline()[:-1]
