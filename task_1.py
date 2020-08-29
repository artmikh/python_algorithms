"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).
Идея доработки: если за проход по списку не совершается ни одной сортировки, то завершение
Обязательно сделайте замеры времени обеих реализаций

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""

import random
import timeit

def bubble_sort_upd(orig_list):
    n = 1
    count = 0
    while n < len(orig_list):
        for i in range(len(orig_list)-n):
            if orig_list[i] < orig_list[i+1]:
                orig_list[i], orig_list[i+1] = orig_list[i+1], orig_list[i]
                count += 1
        if count == 0:
            break
        n += 1
    return orig_list, f'Количество всплываний пузырьков = {count}'


original_list = [random.randint(-100, 100) for i in range(1000)]
copy_list = original_list.copy()

# print(bubble_sort_upd(copy_list))
# print(bubble_sort_upd(copy_list))

"""Чтобы сработала доработка по проходу без всплывания(т.е. уже остортированному списку),
делаю замеры не с копией списка, а с оригиналом, а потом еще раз уже с отсортированным"""

print(timeit.timeit("bubble_sort_upd(original_list)", setup="from __main__ import bubble_sort_upd, original_list", number=100))
print(timeit.timeit("bubble_sort_upd(original_list)", setup="from __main__ import bubble_sort_upd, original_list", number=100))

# Доработка по завершению без всплытия ни одного пузырька скорости не прибавляет воообще, 
# т.к. в рандомном списке не может быть уже отсортированного списка
# более того, всегда получается примерно 250000 всплытий пузырьков (т.е. перестановок)

# результат
"""
1.973841191
0.22173413400000008
"""