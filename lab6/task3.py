import pandas as pd


# Читаем файл
data = pd.read_csv('students_with_gaps.csv', sep=',')
# Проверяем, есть ли пропуски в данных
print(data.isnull().sum())
# Заполняем пропуски в столбце Score средним значением
new_data = data.fillna(value={'Score': data['Score'].mean()})
# Удаляем строки с пропусками в остальных столбцах
newest_data = new_data.dropna()
