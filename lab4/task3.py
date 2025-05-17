from random import randint


class Tic_Tac_Toe():
    def __init__(self):
        self.game_map = list(i for i in range(1, 10))

    def start_game(self):
        while True:
            print(
                f'{self.game_map[0]} {self.game_map[1]} {self.game_map[2]} \n{self.game_map[3]} {self.game_map[4]} {self.game_map[5]} \n{self.game_map[6]} {self.game_map[7]} {self.game_map[8]} \n ')
            print('Займите любую цифру')
            a = int(input())
            if a in self.game_map:
                self.game_map[int(a) - 1] = 'O'
            # Прописать условие выигрыша
            check_robot_turn = 0
            while check_robot_turn == 0:
                robot_turn = randint(1, 10)
                if self.game_map[robot_turn - 1] != ('O' or 'X'):
                    self.game_map[robot_turn - 1] = 'X'
                    check_robot_turn = 1


new_game = Tic_Tac_Toe()
new_game.start_game()
