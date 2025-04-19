from random import randint
import datetime as dt


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

new_game = Guess_the_number(5, 10, 1000)
new_game.cheat_get_num()
new_game.start_game()
with open('results.txt', 'w', encoding='utf-8') as f:
    for i in new_game.get_logs():
        f.writelines(f'{i} \n')
