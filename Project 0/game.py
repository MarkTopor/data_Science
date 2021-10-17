"""guess the number"""

import numpy as np

number = np.random.randint(1,101) #загадываем число

#количество попыток
count = 0

while True:
    count += 1
    predict_number = int(input("Guess the number from 1 to 100: "))
    
    if predict_number > number:
        print("число должно быть меньше")
    elif predict_number < number:
        print("число должно быть больше")
    else:
        print(f'вы угадали! это число = {number} за {count} попыток')
        break #конец игры
