# Импортируем модуль для работы с регулярными выражениями
import re


# Читаем файл text.txt
data = open('text.txt').read()
# С помощью регулярных выражентй находим даты в формате dd.mm.yyyy
date = re.findall(r'\d\d\.\d\d\.\d{4}', data)
new_date = []
# Переводим даты в формат yyyy-mm-dd и сохраняем в список new_date
for i in date:
	day, month, year = map(str, i.split('.'))
	new_date.append(f'{year}-{month}-{day}')
# Сортируем даты от раннего к позднему
new_date.sort(key=lambda x: "".join(x.split('-')))
# Выводим результат
print(*new_date)
