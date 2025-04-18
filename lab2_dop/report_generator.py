import student_utils as su


students = []
with open('students.csv', 'r', encoding='utf-8') as f:
    a, b, c = map(str, f.readline().strip().split(','))
    for line in f:
        name, age, score = map(str, line.strip().split(','))
        students.append({a:name, b:int(age), c:float(score)})

top_students = su.get_top_students(students, 5)
with open('report.txt', 'w', encoding='utf-8') as f:
    f.writelines('Топ студентов: \n')
    for i in top_students:
        f.writelines(f'{i} \n')
    f.writelines(su.get_average_age(students) + '\n')
    f.writelines(su.filter_by_grade(students, 4.0) + '\n')
