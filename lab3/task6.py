class Temperature():
    '''
    Класс Temperature с приватным атрибутом:
    - celsius
    - Геттером/сеттером через @property с валидацией
    - Динамическим свойством fahrenheit
    '''
    def __init__(self):
        self.__celsius = 20
    @property
    def current_temperature(self):
        return self.__celsius
    @current_temperature.setter
    def current_temperature(self, new_temp):
        if -100 >= new_temp >= 200:
            self.__celsius = new_temp
        else:
            print('Temperature is too high/low')
    def fahrenheit(self):
        return (self.__celsius*9/5)+32


if __name__ == '__main__':
    temp = Temperature()
    temp.current_temperature = 60
    print(temp.current_temperature)
    print(temp.fahrenheit())
    temp.current_temperature = 600

