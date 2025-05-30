import pandas as pd


# Читаем файл
data = pd.read_csv('students.csv', sep=',')
# Выводим первые 5 строк
print(data.head())
# Выводим информацию о данных:
# кол-во строк и столбцов, имена столбцов, типы данных и использование памяти
print(data.info())
# Выводим статистику числовых столбцов:
# count, mean, std (стандартное отклонение), min, max, процентили
print(data.describe())
# Выводим средний балл студентов
print(data['Score'].mean())
# Выводим кол-во студентов в каждой группе
print(data.groupby('Group').count())