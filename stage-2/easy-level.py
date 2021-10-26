import random
from time import sleep

USER = 'X'
COMPUTER = 'O'
BOARD_SIDES = '|'
BOARD_TOP_BOTTOM = '-' * 9


def initial_board():
    cell = [' ']
    board = [cell * 3 for _ in range(3)]

    return board


def get_user_coordinates(cell):
    moves = []

    while True:        
        coordinates = input('Enter the coordinates:\n$ ')
        if ' ' in coordinates:
            coordinates = coordinates.replace(' ', '')
        try:
            coordinates_list = [int(i) for i in coordinates]
        except ValueError:
            print('\nYou should enter numbers!\n')
            continue

        if len(coordinates_list) > 2:
            print('\nCoordinates must be two numbers!\n')
            continue

        elif coordinates_list[0] > 3 or coordinates_list[1] > 3:
            print('\nCoordinates should be from 1 to 3!\n')
            continue  
            
        else:
            moves = [coordinates_list[i] - 1 for i in range(len(coordinates_list)) if len(coordinates_list) < 3]

            if cell[moves[0]][moves[1]] == USER or cell[moves[0]][moves[1]] == COMPUTER:
                print('\nThis cell is occupied! Choose another one!\n')
                continue
        break
    return moves


def get_computer_coordinates(cell):
    while True:
        coordinate_1 = random.randint(0, 2)
        coordinate_2 = random.randint(0, 2)
        coordinates = [coordinate_1, coordinate_2]

        if cell[coordinate_1][coordinate_2] == USER or cell[coordinate_1][coordinate_2] == COMPUTER:
            continue
        break
    return coordinates


def add_move_to_board(board, coordinates, player):
    board[coordinates[0]][coordinates[1]] = player
    
    return board[coordinates[0]][coordinates[1]] 

def get_results(cell, player):
        if ((cell[0][0] == player and cell[1][0] == player and cell[2][0] == player) or
                (cell[0][1] == player and cell[1][1] == player and cell[2][1] == player) or
                (cell[0][2] == player and cell[1][2] == player and cell[2][2] == player) or
                (cell[0][0] == player and cell[1][1] == player and cell[2][2] == player) or
                (cell[2][0] == player and cell[1][1] == player and cell[0][2] == player) or
                (cell[0][0] == player and cell[0][1] == player and cell[0][2] == player) or
                (cell[1][0] == player and cell[1][1] == player and cell[1][2] == player) or
                (cell[2][0] == player and cell[2][1] == player and cell[2][2] == player)): 
            print_board(cell)
            return '%s wins!' % player
        
        elif all(c == USER or c == COMPUTER for char in cell for c in char):
            print_board(cell)
            return 'Draw!'
        
        return print_board(cell)


def print_board(cells):
    print('\n' + BOARD_TOP_BOTTOM)
    for i in range(0, 3):
        print(f'{BOARD_SIDES} {cells[i][0]} {cells[i][1]} {cells[i][2]} {BOARD_SIDES}')
    print(BOARD_TOP_BOTTOM + '\n')


def main():
    cell = initial_board()
    print_board(cell)
    while True:
        user_coordinates = get_user_coordinates(cell)
        player = add_move_to_board(cell, user_coordinates, USER)
        x_result = get_results(cell, player)

        if x_result == 'X wins!' or x_result == 'Draw!':
            return x_result

        computer_coordinates = get_computer_coordinates(cell)
        computer = add_move_to_board(cell, computer_coordinates, COMPUTER)
        print('Making move level "easy"') 
        o_result = get_results(cell, computer)

        if o_result == 'O wins!' or o_result == 'Draw!':
            return o_result


if __name__ == '__main__':
    try:
        print(main())
    except KeyboardInterrupt:
        print('\n[!!] Detected CTRL+C! Exiting game....')
        sleep(1)
    except Exception as e:
        print(e)
    finally:
        print('GOODBYE!')
