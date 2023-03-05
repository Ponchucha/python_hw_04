# В фермерском хозяйстве в Карелии выращивают чернику.
# Она растет на круглой грядке, причем кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних.
# Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью,
# поэтому ко времени сбора на них выросло различное число ягод –
# на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод,
# которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.

import random

num_of_shrubs = int(input("Введите количество кустов: "))
shrubs = []

for i in range(num_of_shrubs):
    shrubs.append(random.randint(1, 10))
print(shrubs)

max_sum = shrubs[num_of_shrubs-1]+shrubs[0]+shrubs[1]
max_sum_index = 0
shrubs_sum = shrubs[num_of_shrubs - 2] + shrubs[num_of_shrubs - 1] + shrubs[0]

if shrubs_sum > max_sum:
    max_sum = shrubs_sum
    max_sum_index = (num_of_shrubs-1)

for i in range(1, num_of_shrubs-1):
    shrubs_sum = shrubs[i - 1] + shrubs[i] + shrubs[i + 1]
    if shrubs_sum > max_sum:
        max_sum = shrubs_sum
        max_sum_index = i
print(f"Максимальное количество ягод будет собрано с {max_sum_index+1 if max_sum_index < num_of_shrubs-1 else num_of_shrubs} куста и двух соседних")

