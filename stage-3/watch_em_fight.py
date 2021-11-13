import random
from time import sleep

COMPUTER = 'easy'
USER = 'user'
PLAYER_1 = 'X'
PLAYER_2 = 'O'
BOARD_SIDES = '|'
BOARD_TOP_BOTTOM = '-' * 9


class Board:
    def __init__(self) -> None:
        self.cell = [' ']
    
    def initial_board(self):
        board = [self.cell * 3 for _ in range(3)]

        return board
    
    @staticmethod
    def print_board(cells):
        print('\n' + BOARD_TOP_BOTTOM)
        for i in range(0, 3):
            print(f'{BOARD_SIDES} {cells[i][0]} {cells[i][1]} {cells[i][2]} {BOARD_SIDES}')
        print(BOARD_TOP_BOTTOM + '\n')
    
    @staticmethod
    def add_move_to_board(cell, coordinates, player):
        cell[coordinates[0]][coordinates[1]] = player

        return cell[coordinates[0]][coordinates[1]]


class Player:
    def __init__(self, player, cell) -> None:
        self.player = player
        self.moves = []
        self.cell = cell
    
    def get_user_coordinates(self):
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

                if self.cell[moves[0]][moves[1]] == PLAYER_1 or self.cell[moves[0]][moves[1]] == PLAYER_2:
                    print('\nThis cell is occupied! Choose another one!\n')
                    continue
            break
        return moves
    
    def get_computer_coordinates(self):
        while True:
            coordinate_1 = random.randint(0, 2)
            coordinate_2 = random.randint(0, 2)
            coordinates = [coordinate_1, coordinate_2]

            if self.cell[coordinate_1][coordinate_2] == PLAYER_1 or self.cell[coordinate_1][coordinate_2] == PLAYER_2:
                continue
            break
        return coordinates


def start_or_end():
    while True:
        prompt = 'Input command:\n$ '
        command = input(prompt).lower().split()

        if len(command) == 3 and command[0] == 'start' and (
            (command[1] == USER or command[1] == COMPUTER) and 
            (command[2] == USER or command[2] == COMPUTER)):
            return command[1], command[2]
        elif command[0] == 'exit':
            exit(0)
        else:
            print('Bad parameters!')
            continue


def get_coordinates_player1(players, cells):
    player1 = Player(PLAYER_1, cells)
    
    if players[0] == COMPUTER:
        return player1.get_computer_coordinates()
        
    elif players[0] == USER:
        return player1.get_user_coordinates()



def get_coordinates_player2(players, cells):
    player2 = Player(PLAYER_2, cells)

    if players[1] == COMPUTER:
        return player2.get_computer_coordinates()
    elif players[1] == USER:
        return player2.get_user_coordinates()


def get_results(board, cell, player):
    if ((cell[0][0] == player and cell[1][0] == player and cell[2][0] == player) or
            (cell[0][1] == player and cell[1][1] == player and cell[2][1] == player) or
            (cell[0][2] == player and cell[1][2] == player and cell[2][2] == player) or
            (cell[0][0] == player and cell[1][1] == player and cell[2][2] == player) or
            (cell[2][0] == player and cell[1][1] == player and cell[0][2] == player) or
            (cell[0][0] == player and cell[0][1] == player and cell[0][2] == player) or
            (cell[1][0] == player and cell[1][1] == player and cell[1][2] == player) or
            (cell[2][0] == player and cell[2][1] == player and cell[2][2] == player)):
        board.print_board(cell)
        return '%s wins!' % player

    elif all(c == PLAYER_1 or c == PLAYER_2 for char in cell for c in char):
        board.print_board(cell)
        return 'Draw!'

    return board.print_board(cell)


def print_board(cells):
    print('\n' + BOARD_TOP_BOTTOM)
    for i in range(0, 3):
        print(f'{BOARD_SIDES} {cells[i][0]} {cells[i][1]} {cells[i][2]} {BOARD_SIDES}')
    print(BOARD_TOP_BOTTOM + '\n')


def play_game(players):
    board = Board()
    cells = board.initial_board()
    board.print_board(cells)
    while True:
        player1_coordinates = get_coordinates_player1(players, cells)
        player1_move = board.add_move_to_board(cells, player1_coordinates, PLAYER_1)

        if players[0] == COMPUTER:
            print('making move level "easy"')
        
        x_result = get_results(board, cells, player1_move)

        if x_result == 'X wins!' or x_result == 'Draw!':
            return x_result

        player2_coordinates = get_coordinates_player2(players, cells)
        player2_move = board.add_move_to_board(cells, player2_coordinates, PLAYER_2)

        if players[1] == COMPUTER:
            print('making move level "easy"')

        o_result = get_results(board, cells, player2_move)

        if o_result == 'O wins!' or o_result == 'Draw!':
            return o_result


def main():
    while True:
        players = start_or_end()
        print(play_game(players))

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\n[!!] Detected CTRL+C! Exiting game....')
        sleep(1)
    except Exception as e:
        print(e)
    finally:
        print('GOODBYE!')
