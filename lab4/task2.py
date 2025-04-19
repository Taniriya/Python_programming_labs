from random import randint


class Point_21():
    def __init__(self):
        self.player_cards = list(randint(2, 12) for i in range(2))
        self.robot_cards = [randint(2, 12)]

    def start_game(self):
        while sum(self.player_cards) <= 21:
            print(f'Ваша нынешняя сумма: {sum(self.player_cards)}')
            print(f'Сумма оппонента: {sum(self.robot_cards)}')
            print('Чтобы взять карту введите: 1; чтобы остановиться введите: 0')
            player_ans = input('Ваш ответ:')
            try:
                if int(player_ans) == 1:
                    new_card = randint(2, 12)
                    self.player_cards.append(new_card)
                    print(f'Вы вытянули карту со значением: {new_card}')
                if sum(self.robot_cards) < 17:
                    self.robot_cards.append(randint(2, 12))
                if sum(self.robot_cards) == 21:
                    print('Вы проиграли, у оппонента 21 балл')
                    break
                elif sum(self.robot_cards) > 21:
                    print(f'Вы выиграли, у оппонента перебор')
                    break
                if int(player_ans) == 0:
                    if sum(self.player_cards) > sum(self.robot_cards):
                        print(f'Вы выиграли, у оппонента {sum(self.robot_cards)}, у вас {sum(self.player_cards)}')
                    elif sum(self.player_cards) < sum(self.robot_cards):
                        print(f'Вы проиграли, у оппонента {sum(self.robot_cards)}, у вас {sum(self.player_cards)}')
                    else:
                        print(f'Ничья!')
                    break
            except ValueError:
                print('Неверное значение!')
        else:
            print('Вы проиграли, перебор')


new_game1 = Point_21()
new_game1.start_game()
