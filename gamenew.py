import math
import time
from playernew import UserPlayer, AIPlayer

class TTTGame:
    def __init__(self):
        self.board = self.make_board()
        self.winner = None

    def make_board(self):
        board = {
            1: ' ', 2: ' ', 3: ' ',
            4: ' ', 5: ' ', 6: ' ',
            7: ' ', 8: ' ', 9: ' ',
        }
        return board

    def print_board(self):
        print("CURRENT GAME BOARD")
        print(' ' + self.board[1] + ' | ' + self.board[2] + ' | ' + self.board[3] + ' ')
        print('---+---+---')
        print(' ' + self.board[4] + ' | ' + self.board[5] + ' | ' + self.board[6] + ' ')
        print('---+---+---')
        print(' ' + self.board[7] + ' | ' + self.board[8] + ' | ' + self.board[9] + ' ')

    def execute_move(self, cell, symbol):
        if self.board[cell] == ' ':
            self.board[cell] = symbol
            if self._check_victory(cell, symbol):
                self.winner = symbol
            return True
        return False

    def _check_victory(self, cell, symbol):
        row_idx = (cell - 1) // 3
        col_idx = (cell - 1) % 3
        row = [self.board[i*3 + col_idx + 1] for i in range(3)]
        col = [self.board[row_idx*3 + i + 1] for i in range(3)]
        diag1 = [self.board[i] for i in [1, 5, 9]]
        diag2 = [self.board[i] for i in [3, 5, 7]]

        return all(val == symbol for val in row) or all(val == symbol for val in col) or all(val == symbol for val in diag1) or all(val == symbol for val in diag2)

    def vacant_cells_exists(self):
        return ' ' in self.board.values()

    def count_vacant_cells(self):
        return len([cell for cell in self.board.values() if cell == ' '])

    def possible_moves(self):
        return [idx for idx, val in self.board.items() if val == ' ']

    def revoke_move(self, cell):
        self.board[cell] = ' '
        self.winner = None

def initiate_game(game, player_x, player_o, print_game=True):
    if print_game:
        game.print_board()

    symbol = 'X'
    while game.vacant_cells_exists():
        if symbol == 'X':
            cell = player_x.make_move(game)
        else:
            cell = player_o.make_move(game)

        if game.execute_move(cell, symbol):
            if print_game:
                print(symbol + f' makes a move to cell {cell}')
                game.print_board()
                print('')
            if game.winner:
                if print_game:
                    print(symbol + ' wins!')
                return symbol

            symbol = 'O' if symbol == 'X' else 'X'

        time.sleep(0.8)

    if print_game:
        print('It\'s a tie.')

if __name__ == '__main__':
    print(' 1 | 2 | 3 ')
    print('---+---+---')
    print(' 4 | 5 | 6 ')
    print('---+---+---')
    print(' 7 | 8 | 9 ')
    print("\n")
    player_x = UserPlayer('X')
    player_o = AIPlayer('O')
    t = TTTGame()
    initiate_game(t, player_x, player_o, print_game=True)


