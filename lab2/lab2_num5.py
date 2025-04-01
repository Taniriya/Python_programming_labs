# Создаем список от 1 до 20 и выводим
data = [a for a in range(1, 21)]
print(*data)
# Создаем список с четными числами из списка data с помощью лямбды и filter 
data_even = list(filter(lambda x: x%2==0, data))
print(*data_even)
# Создаем список с числами+10 из списка data с помощью лямбды и map
data_plus_ten = list(map(lambda x: x+10, data))
print(*data_plus_ten)
# Создаем список с числами из списка data в обратном порядке с помощью лямбды и sorted
data_reversed = sorted(data, key=lambda x: x, reverse=True)
print(*data_reversed)
