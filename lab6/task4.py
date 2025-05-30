import pandas as pd


# Читаем файл
data = pd.read_csv('students.csv', sep=',')
# Вывод средного балла
print(data.groupby('Group')['Score'].mean())
# Вывод медианного возраста
print(data.groupby('Group')['Age'].median())
# добавление нового столбца Passed
data['Passed'] = data['Score'].apply(lambda score: 1 if score >= 60 else 0)
print(data)