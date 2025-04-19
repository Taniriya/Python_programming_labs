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
        self.name = name
        self.student_id = student_id
        self.grades = grades
    def add_grade(self, grade: int):
        if 0 <= grade <= 10:
            self.grades.append(grade)
    def get_average(self):
        if self.grades != []:
            return f'Ваш средний балл: {sum(self.grades)/len(self.grades)}'
    def display_info(self):
        return f'Имя: {self.name};\nНомер студента: {self.student_id};\nОценки: {self.grades}'

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
        super().__init__(name=name, age=age)
        self.subject = subject
        self.students = students
    def add_students(self, name):
        self.students.append(name)
    def remove_student(self, name):
        self.students.remove(name)
    def list_students(self):
        return f'Ваши студенты: {self.students}'

class Assistant(Student, Teacher):
    '''
    Дочерний класс Assistant с дополнительным методом:
    - help_student() - Ассистент помогает ученику найти учителя
    '''
    def __init__(self, student_name: str, teacher_name: str, student_id: int, grades: list, age: int, subject: list, students: list):
        Student.__init__(self, name=student_name, student_id=student_id, grades=grades)
        Teacher.__init__(self, name=teacher_name, age=age, subject=subject, students=students)
        self.name_stu = student_name
        self.name_tea = teacher_name
    def help_student(self):
        print(f'Ассистент помогает {self.name_stu} найти {self.name_tea}')

if __name__ == '__main__':
    assis = Assistant('Таня', 'Джек', 1, [5, 7], 27, [], ['Таня'])
    assis.add_students('Оля')
    print(assis.list_students())
    assis.help_student()