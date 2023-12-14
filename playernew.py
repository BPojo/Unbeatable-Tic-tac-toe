import math
import random

class Participant:
    def __init__(self, token):
        self.token = token

    def make_move(self, game):
        pass

class UserPlayer(Participant):
    def __init__(self, token):
        super().__init__(token)

    def make_move(self, game):
        valid_cell = False
        cell = None
        while not valid_cell:
            move = input(self.token + '\'s turn. Input move (1-9): ')
            try:
                cell = int(move)
                if cell not in game.possible_moves():
                    raise ValueError
                valid_cell = True
            except ValueError:
                print('Cell is in use, please try another one')
        return cell

class AIPlayer(Participant):
    def __init__(self, token):
        super().__init__(token)

    def make_move(self, game):
        if len(game.possible_moves()) == 9:
            cell = random.choice(game.possible_moves())
        else:
            cell = self.minimax(game, self.token)['position']
        return cell

    def minimax(self, state, player):
        max_player = self.token  
        other_player = 'O' if player == 'X' else 'X'

        if state.winner == other_player:
            return {'position': None, 'score': 1 * (state.count_vacant_cells() + 1) if other_player == max_player else -1 * (state.count_vacant_cells() + 1)}
        elif not state.vacant_cells_exists():
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}  
        else:
            best = {'position': None, 'score': math.inf}  
        for possible_move in state.possible_moves():
            state.execute_move(possible_move, player)
            sim_score = self.minimax(state, other_player)  

            state.revoke_move(possible_move)
            sim_score['position'] = possible_move  

            if player == max_player:  
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best
