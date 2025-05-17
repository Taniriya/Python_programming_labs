from random import randint
import datetime as dt


def set_balance(a):
    with open('balance.txt', 'w', encoding='utf-8') as f:
        f.writelines(str(a))

def save_balance(a):
    with open('balance.txt', 'w', encoding='utf-8') as f:
        f.writelines(str(a))

def get_balance():
    with open('balance.txt', 'r') as f:
        return int(f.readline().strip())

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

class Point_21():
    def __init__(self):
        self.player_cards = list(randint(2, 11) for i in range(2))
        self.robot_cards = [randint(2, 11)]
        self.balance = get_balance()

    def start_game(self, bet):
        while sum(self.player_cards) <= 21:
            print(f'Ваша нынешняя сумма: {sum(self.player_cards)}')
            print(f'Сумма оппонента: {sum(self.robot_cards)}')
            print('Чтобы взять карту введите: 1; чтобы остановиться введите: 0')
            player_ans = input('Ваш ответ:')
            try:
                if int(player_ans) == 1:
                    new_card = randint(2, 11)
                    self.player_cards.append(new_card)
                    print(f'Вы вытянули карту со значением: {new_card}')
                if sum(self.robot_cards) < 17:
                    self.robot_cards.append(randint(2, 11))
                if sum(self.robot_cards) > 21:
                    print(f'Вы выиграли, у оппонента перебор')
                    self.balance += bet*2
                    break
                if int(player_ans) == 0:
                    while sum(self.robot_cards) < 17:
                        self.robot_cards.append(randint(2, 11))
                    if sum(self.robot_cards) > 21:
                        print(f'Вы выиграли, у оппонента перебор')
                        self.balance += bet * 2
                        break
                    if sum(self.player_cards) > sum(self.robot_cards):
                        print(f'Вы выиграли, у оппонента {sum(self.robot_cards)}, у вас {sum(self.player_cards)}')
                        self.balance += bet * 2
                    elif sum(self.player_cards) < sum(self.robot_cards):
                        print(f'Вы проиграли, у оппонента {sum(self.robot_cards)}, у вас {sum(self.player_cards)}')
                        self.balance -= bet
                    else:
                        print(f'Ничья!')
                    break
            except ValueError:
                print('Неверное значение!')
        else:
            print('Вы проиграли, перебор')
            self.balance -= bet
        save_balance(self.balance)

class Guess_the_number():
    def __init__(self, tries, lowest_num, biggest_num):
        self.number = randint(lowest_num, biggest_num+1)
        self.tries = tries
        self.logs = []
        self.range = f'от {lowest_num} до {biggest_num}'

    def cheat_get_num(self):
        print(self.number)

    def start_game(self):
        while self.tries > 0:
            try:
                print(f'Загадано число {self.range}')
                number = input("Введите число:")
                number = int(number)
                if number == self.number:
                    self.tries -= 1
                    self.logs.append(['WIN!', number, dt.datetime.now()])
                    print(f'Поздравляю, загаданное число: {number}')
                    break
                elif number > self.number:
                    self.tries -= 1
                    self.logs.append(['Bigger quess', number, dt.datetime.now()])
                    print(f'Загаданное число меньше {number}')
                elif number < self.number:
                    self.tries -= 1
                    self.logs.append(['Lower guess', number, dt.datetime.now()])
                    print(f'Загаданное число больше {number}')
            except ValueError:
                self.logs.append(['ValueError', number, dt.datetime.now()])
                print('Неверный ввод!')
        else:
            self.logs.append(['LOSE!', self.number, dt.datetime.now()])
            print(f'Вы проиграли, загаданное число: {self.number}')

    def get_logs(self):
        return self.logs

class Menu():
    def __init__(self):
        self.games_played = 0
    def start_menu(self):
        while True:
            print('Выберите игру:')
            print('1 - Отгадай число')
            print('2 - 21 Очко')
            print('3 - Крестики-Нолики')
            print('Введите любой другой символ, чтобы выйти из игры')
            try:
                game_chosen = int(input())
                if game_chosen == 1:
                    new_game = Guess_the_number(5, 1, 100)
                    new_game.start_game()
                elif game_chosen == 2:
                    new_game = Point_21()
                    new_game.start_game()
                elif game_chosen == 3:
                    new_game = Tic_Tac_Toe()
                    new_game.start_game()
                else:
                    break
            except ValueError:
                break


game = Menu()
game.start_menu()
