class Student:
    '''
    Класс Student имеет слудующие атрибуты:
    - name (строка)
    - student_id (строка/число)
    - grades (список чисел)
    И методы:
    - add_grade(grade) - добавляет оценку с валидацией (0-10)
    - get_average() - возвращает средний балл
    - display_info() - красиво выводит информацию о студенте
    '''
    def __init__(self, name: str, student_id: int, grades: list):
        self.__name = name
        self.__student_id = student_id
        self.__grades = grades
    def add_grade(self, grade: int):
        if 0 <= grade <= 10:
            self.__grades.append(grade)
    def get_average(self):
        if self.__grades != []:
            return f'Ваш средний балл: {sum(self.__grades)/len(self.__grades)}'
    def display_info(self):
        return f'Имя: {self.__name};\nНомер студента: {self.__student_id};\nОценки: {self.__grades}'


if __name__ == '__main__':
    Tanya = Student('Таня', 1, [5, 7])
    Dan = Student('Дэн', 2, [])
    print(Student.__doc__)
    print(Dan.get_average())
    Tanya.add_grade(int(9))
    print(Tanya.get_average())
    print(Tanya.display_info())
