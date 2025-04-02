# Импортируем модуль для работы с регулярными выражениями
import re


# Читаем файл text.txt
data = open('text.txt').read()
# Находим email адреса
mails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,6}\b", data)
# Находим номера телефонов
phones = re.findall(r"\+7-\w{3}-\w{3}-\w{2}-\w{2}", data)
# Находим слова начинающиеся с заглавной буквы
capital = re.findall(r"\b[A-ZА-Я]\w*", data)
# Записываем результаты в файлы
with open('emails.txt', 'w') as f:
	for i in mails:
		f.writelines(str(i) + '\n')
with open('phones.txt', 'w') as f:
	for i in phones:
		f.writelines(str(i) + '\n')
with open('capital_words.txt', 'w') as f:
	for i in capital:
		f.writelines(str(i) + '\n')
