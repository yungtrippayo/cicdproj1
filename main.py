class TicTacToe:
    def __init__(self):
        self.board = [' '] * 9
        self.current_player = 'X'

    def print_board(self):
        print(f'{self.board[0]} | {self.board[1]} | {self.board[2]}')
        print('---------')
        print(f'{self.board[3]} | {self.board[4]} | {self.board[5]}')
        print('---------')
        print(f'{self.board[6]} | {self.board[7]} | {self.board[8]}')

    def check_win(self):
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                          (0, 3, 6), (1, 4, 7), (2, 5, 8),
                          (0, 4, 8), (2, 4, 6)]

        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] != ' ':
                return self.board[condition[0]]
        if ' ' not in self.board:
            return 'Draw'
        return False

    def get_move(self):
        while True:
            move = input(f'Player {self.current_player}, enter your move (1-9): ')
            if not move.isdigit() or int(move) < 1 or int(move) > 9 or self.board[int(move) - 1] != ' ':
                print('Invalid move. Try again.')
            else:
                return int(move) - 1

    def play(self):
        while True:
            self.print_board()
            move = self.get_move()
            self.board[move] = self.current_player
            result = self.check_win()
            if result:
                self.print_board()
                if result == 'Draw':
                    print('The game is a draw.')
                else:
                    print(f'Player {self.current_player} wins!')
                break
            self.current_player = 'O' if self.current_player == 'X' else 'X'


if __name__ == '__main__':
    game = TicTacToe()
    game.play()
