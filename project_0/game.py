import numpy as np
'''Функция угадывает загаданное число'''
def game_core(number):
    count = 1
    predict = 50 # всегда начинает угадывать с середины диапазона
    min = 0  # минимальное число диапазона
    max = 101 # максимальное число диапазона
    while number != predict:  # если не угадали, делим оставшийся диапазон пополам
        count += 1
        if number > predict:
            min = predict
            predict = min + ((max - min) // 2)
        elif number < predict:
            max = predict
            predict = min + ((max - min) // 2)
    return(count) # выход из цикла, если угадали

'''Запускаем функцию 1000 раз'''
predict_count = 0
for i in range(1000):
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    number = np.random.randint(1, 101) # Случайным образом загадывается число.
    predict_count += game_core(number) # Сумма всех попыток.
print(f"Ваш алгоритм угадывает число в среднем за {int(predict_count / i)} попыток")