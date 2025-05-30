import pandas as pd


# Читаем файл
data = pd.read_csv('students.csv', sep=',')
# Находим студентов с баллом выше 80
print(data[data['Score'] > 80])
# Сортируем студентов по убыванию балла
print(data.sort_values(by='Score', ascending=False))
# Выводим студентов с максимальным возрастом
print(data[data['Age'] == data['Age'].max()])
# И минимальным
print(data[data['Age'] == data['Age'].min()])
