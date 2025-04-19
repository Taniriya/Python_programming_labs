from random import randint



def set_balance(a):
    with open('balance.txt', 'w', encoding='utf-8') as f:
        f.writelines(str(a))

def save_balance(a):
    with open('balance.txt', 'w', encoding='utf-8') as f:
        f.writelines(str(a))

def get_balance():
    with open('balance.txt', 'r') as f:
        return int(f.readline().strip())


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


new_game1 = Point_21()
new_game1.start_game(10)
