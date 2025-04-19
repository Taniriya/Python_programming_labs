class Person:
    '''Базовый класс Person с атрибутами name, age'''
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

class Teacher(Person):
    '''
    Дочерний класс Teacher с дополнительными атрибутами:
    - subject (преподаваемый предмет)
    - students (список объектов Student)
    И методами:
    - add_student() - добавляет студентов
    - remove_student() - удаляет студентов по имени
    - list_students() - выводит список студентов
    '''
    def __init__(self, name: str, age: int, subject: list, students: list):
        super().__init__(name, age)
        self.__subject = subject
        self.__students = students
    def add_students(self, name):
        self.__students.append(name)
    def remove_student(self, name):
        self.__students.remove(name)
    def list_students(self):
        return f'Ваши студенты: {self.__students}'


if __name__ == '__main__':
    teacher_Jack = Teacher('Джек', 27, [], [])
    print(Person.__doc__)
    print(Teacher.__doc__)
    teacher_Jack.add_students('Оля')
    print(teacher_Jack.list_students())
    teacher_Jack.remove_student('Оля')
    print(teacher_Jack.list_students())

