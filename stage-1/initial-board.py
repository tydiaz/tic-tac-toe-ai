import re
from time import sleep

PLAYER_X = 'X'
PLAYER_O = 'O'
BOARD_SIDES = '|'
BOARD_TOP_BOTTOM = '-' * 9


def get_initial_state():
    pattern = r'[^XO_]+'
    while True:
        user_cell = input('Enter 9 symbols X/O/_:\n$ ').upper()

        if re.findall(pattern, user_cell):
            print('\nSymbols must be combination of X, O, _\n')
            continue
        break

    for _ in user_cell:
        if len(user_cell) == 9:
            user_cell = user_cell.replace('_', ' ')
            user_cell = [i for i in user_cell]
            cell_list = [user_cell[i:i + 3] for i in range(0, len(user_cell), 3)]

            return cell_list
        else:
            print('\nCell must contain 9 symbols!\n')
            return get_initial_state()


def get_coordinates(cell):
    moves = []

    print_board(cell)
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

            if cell[moves[0]][moves[1]] == PLAYER_X or cell[moves[0]][moves[1]] == PLAYER_O:
                print('\nThis cell is occupied! Choose another one!\n')
                continue
        break
    return moves


def add_move_to_board(cell, moves):
    x_count = [x for char in cell for x in char].count(PLAYER_X)
    o_count = [o for char in cell for o in char].count(PLAYER_O)

    if x_count > o_count:
        cell[moves[0]][moves[1]] = PLAYER_O

        print_board(cell)
        return cell[moves[0]][moves[1]]

    cell[moves[0]][moves[1]] = PLAYER_X

    print_board(cell)
    return cell[moves[0]][moves[1]]


def get_results(cell, move):
    if ((cell[0][0] == move and cell[1][0] == move and cell[2][0] == move) or
            (cell[0][1] == move and cell[1][1] == move and cell[2][1] == move) or
            (cell[0][2] == move and cell[1][2] == move and cell[2][2] == move) or
            (cell[0][0] == move and cell[1][1] == move and cell[2][2] == move) or
            (cell[2][0] == move and cell[1][1] == move and cell[0][2] == move) or
            (cell[0][0] == move and cell[0][1] == move and cell[0][2] == move) or
            (cell[1][0] == move and cell[1][1] == move and cell[1][2] == move) or
            (cell[2][0] == move and cell[2][1] == move and cell[2][2] == move)):
        return '%s wins!' % move
    elif all(c == PLAYER_X or c == PLAYER_O for char in cell for c in char):
        return 'Draw!'

    return 'Game not finished!'


def print_board(cells):
    print('\n' + BOARD_TOP_BOTTOM)
    print(f'{BOARD_SIDES} {cells[0][0]} {cells[0][1]} {cells[0][2]} {BOARD_SIDES}')
    print(f'{BOARD_SIDES} {cells[1][0]} {cells[1][1]} {cells[1][2]} {BOARD_SIDES}')
    print(f'{BOARD_SIDES} {cells[2][0]} {cells[2][1]} {cells[2][2]} {BOARD_SIDES}')
    print(BOARD_TOP_BOTTOM + '\n')


def main():
    cells = get_initial_state()
    user_moves = get_coordinates(cells)
    final_move = add_move_to_board(cells, user_moves)

    return get_results(cells, final_move)


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
