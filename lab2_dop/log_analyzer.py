status_200 = 0
total_size_in_bytes = 0
unique_ip = set()
logs = []

# Читаем файл
with open('server_logs.txt', 'r') as f:
    for line in f:
        # Берём значения из каждой строки и записываем в logs
        date, time, ip, method, url, status, size = map(str, line.strip()[1:-2].split('] ['))
        logs.append([date, time, ip, method, url, status, size])
        # Находим все запросы со статусом 200
        if int(status) == 200:
            status_200 += 1
        # Находим общее объём в байтах
        total_size_in_bytes += int(size)
        # Записываем каждое уникальное значение
        unique_ip.add(ip)


total_size = ''
types_of_sizes = ['байт', 'Кб', 'Мб', 'Гб']
# Записываем объём с нужной единицой измерения
for i in range(4):
    if i == 0:
        total_size = str(total_size_in_bytes) + ' ' + types_of_sizes[i]
    elif total_size_in_bytes > 1024**i:
        a = total_size_in_bytes / (1024 ** i)
        # Записываем с точностью до одной цифры после запятой
        total_size = str((int(a) + ((a-int(a))//0.1)*0.1)) + ' ' + types_of_sizes[i]


# Записываем анализ логов в отдельный файл
with open('log_analysis.txt', 'w', encoding="utf-8") as f:
    f.writelines(f'Успешных запросов: {status_200}' + '\n')
    f.writelines(f'Общий объём: {total_size}' + '\n')
    f.writelines(f'Уникальных ip: {len(unique_ip)}' + '\n')


# Сортируем по последним добавленным логам
logs_sorted = sorted(logs, key=lambda x: x, reverse=True)
# Выводим 10 последних
for i in range(10):
    print(logs_sorted[i])
