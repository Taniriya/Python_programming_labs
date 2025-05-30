import pandas as pd


# Читаем файл
data = pd.read_csv('students.csv', sep=',')
# Находим студентов с баллом выше 80
print(data[data['Score'] > 80])
# Сортируем студентов по убыванию балла
print(data.sort_values(by='Score', ascending=False))
print(data[data['Age'] == data['Age'].max()])
print(data[data['Age'] == data['Age'].min()])