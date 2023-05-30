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
