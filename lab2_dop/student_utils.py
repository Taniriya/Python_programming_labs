def get_top_students(students, amount):
    students_sorted = sorted(students, key=lambda x: x['Средний балл'], reverse=True)
    ans = []
    for i in students_sorted:
        ans.append(i['Имя'] + ' - ' + str(i['Средний балл']))
    return ans[:amount]

def get_average_age(students):
    ans = [d.get('Возраст') for d in students if 'Возраст' in d]
    a = sum(ans)/len(ans)
    return 'Средний возраст: ' + str(int(a) + ((a - int(a)) // 0.1) * 0.1)

def filter_by_grade(students, grade):
    ans = 0
    mas = [d.get('Средний балл') for d in students if 'Средний балл' in d]
    for i in mas:
        if i > grade:
            ans += 1
    return f'C баллом > {grade}: {ans} студентов'