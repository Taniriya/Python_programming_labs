# Читаем числа из файла data.txt построчно
f = open('data.txt')
mas = [int(f.readline().strip()) for i in range(10)]
# Создаем новый файл, в который запишем результы
ans = open('result.txt', 'w')
# Построчно записываем результы
ans.writelines('Сумма: ' + str(sum(mas)) + '\n')
ans.writelines('Среднее: ' + str(sum(mas)//len(mas)) + '\n')
ans.writelines('Максимум: ' + str(max(mas)) + '\n')
ans.writelines('Минимум: ' + str(min(mas)) + '\n')
