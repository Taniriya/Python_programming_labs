class BankAccount():
    '''
    Класс BankAccount с приватными атрибутами:
    - balance
    - transactions
    и публичными методами:
    - deposit() - положить средства на счёт
    - withdraw() - забрать средства со счёта
    - balance() через @property
    '''
    def __init__(self):
        self.__balance = 0
        self.__transactions = []
    @property
    def balance(self):
        return self.__balance
    def deposit(self, money):
        self.__balance += money
        self.__transactions.append('DEPOSIT: ' + str(money))
    def withdraw(self, money):
        if money <= self.__balance:
            self.__balance -= money
            self.__transactions.append('WITHDRAW: ' + str(money))
        else:
            print('Not enough money on balance, only: '+str(self.__balance))


if __name__ == '__main__':
    new_bank = BankAccount()
    print(new_bank.balance)
    new_bank.deposit(1000)
    print(new_bank.balance)
    new_bank.withdraw(900)
    print(new_bank.balance)
    new_bank.withdraw(900)