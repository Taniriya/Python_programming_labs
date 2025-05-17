from random import randint


def check_winner(game_map):
    if game_map[0] == game_map[1] == game_map[2] == 'O' or \
            game_map[3] == game_map[4] == game_map[5] == 'O' or \
            game_map[6] == game_map[7] == game_map[8] == 'O' or \
            game_map[0] == game_map[3] == game_map[6] == 'O' or \
            game_map[1] == game_map[4] == game_map[7] == 'O' or \
            game_map[2] == game_map[5] == game_map[8] == 'O' or \
            game_map[0] == game_map[4] == game_map[8] == 'O' or \
            game_map[2] == game_map[4] == game_map[6] == 'O':
        return 1
    elif game_map[0] == game_map[1] == game_map[2] == 'X' or \
            game_map[3] == game_map[4] == game_map[5] == 'X' or \
            game_map[6] == game_map[7] == game_map[8] == 'X' or \
            game_map[0] == game_map[3] == game_map[6] == 'X' or \
            game_map[1] == game_map[4] == game_map[7] == 'X' or \
            game_map[2] == game_map[5] == game_map[8] == 'X' or \
            game_map[0] == game_map[4] == game_map[8] == 'X' or \
            game_map[2] == game_map[4] == game_map[6] == 'X':
        return 2
    else:
        return 0

class Tic_Tac_Toe():
    def __init__(self):
        self.game_map = list(i for i in range(1, 10))

    def start_game(self):
        while check_winner(self.game_map) == 0:
            print(
                f'{self.game_map[0]} {self.game_map[1]} {self.game_map[2]} \n{self.game_map[3]} {self.game_map[4]} {self.game_map[5]} \n{self.game_map[6]} {self.game_map[7]} {self.game_map[8]} \n ')
            print('Займите любую цифру')
            try:
                a = int(input())
                if a in self.game_map:
                    self.game_map[int(a) - 1] = 'O'
                check_robot_turn = 0
                while check_robot_turn == 0:
                    robot_turn = randint(1, 9)
                    if self.game_map[robot_turn - 1] != ('O' or 'X'):
                        self.game_map[robot_turn - 1] = 'X'
                        check_robot_turn = 1
            except ValueError:
                print('Неверное значение!')
        else:
            if check_winner(self.game_map) == 1:
                print('Вы победили')
            elif check_winner(self.game_map) == 2:
                print('Вы проиграли')

new_game = Tic_Tac_Toe()
new_game.start_game()