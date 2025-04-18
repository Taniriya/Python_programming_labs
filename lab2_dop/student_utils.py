def get_top_students(students, amount):
    # Сортируем студентов по баллам
    students_sorted = sorted(students, key=lambda x: x['Средний балл'], reverse=True)
    ans = []
    # Вносим студентов в список с удобным форматом для вывода
    for i in students_sorted:
        ans.append(i['Имя'] + ' - ' + str(i['Средний балл']))
    # Если ввели слишком большое значение
    if amount > len(ans):
        amount = len(ans)
    # Выводим только топ лучших
    return ans[:amount]

def get_average_age(students):
    # Создаём список с возрастами
    ans = [d.get('Возраст') for d in students if 'Возраст' in d]
    # Находим средний возраст
    a = sum(ans)/len(ans)
    # Выводим в удобном для вывода формате с точностью до одной цифры после запятой
    return 'Средний возраст: ' + str(int(a) + ((a - int(a)) // 0.1) * 0.1)

def filter_by_grade(students, grade):
    # Создаём список со средними баллами
    mas = [d.get('Средний балл') for d in students if 'Средний балл' in d]
    # Создаём список с отфильтрованными значениями
    ans = list(filter(lambda x: x>grade, mas))
    # Выводим в удобном для вывода формате
    return f'C баллом > {grade}: {len(ans)} студентов'