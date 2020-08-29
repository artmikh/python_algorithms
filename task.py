""" В этом задании сделал замеры и сравнение всех сортировок
Результаты в конце"""

import timeit
import random


# Сортировка методом пузырька
def bubble_sort_upd(orig_list):
    n = 1
    count = 0
    while n < len(orig_list):
        for i in range(len(orig_list)-n):
            if orig_list[i] < orig_list[i+1]:
                orig_list[i], orig_list[i+1] = orig_list[i+1], orig_list[i]
                count = 1
        if count == 0:
            break
        n += 1
    return orig_list

# Сортировка методом слияния
def merge_sort(alist):

    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1

# Сортировка методом Гном
def gnome_sort(sort_list):
    i = 1
    while i < len(sort_list):
        if not i or sort_list[i - 1] <= sort_list[i]:
            i += 1
        else:
            sort_list[i], sort_list[i - 1] = sort_list[i - 1], sort_list[i]
            i -= 1
    return sort_list

# Стандартная сортировка №1
def reverse_sort(lst_obj):
    ordered_list = sorted(lst_obj)
    return ordered_list

# Стандартная сортировка №2
def reverse2_sort(lst_obj):
    lst_obj.sort()
    return lst_obj

# Быстрая сортировка
def my_calc(lst_obj):
    def quick_sort(lst_obj):
        if len(lst_obj) <= 1:
            return lst_obj
        else:
            q = random.choice(lst_obj)
            L = []
            M = []
            R = []
            for elem in lst_obj:
                if elem < q:
                    L.append(elem)
                elif elem > q:
                    R.append(elem)
                else:
                    M.append(elem)
            return quick_sort(L) + M + quick_sort(R)
    return quick_sort

# Сортировка вставками
def insertion_sort(lst_obj):
    for i in range(len(lst_obj)):
        v = lst_obj[i]
        j = i

        while (lst_obj[j-1] > v) and (j > 0):

            lst_obj[j] = lst_obj[j-1]
            j = j - 1

        lst_obj[j] = v
    return lst_obj

# Сортировка выбором
def selection_sort(lst_obj):
    for i in range(len(lst_obj)):
        idx_min = i
        for j in range(i+1, len(lst_obj)):
            if lst_obj[j] < lst_obj[idx_min]:
                idx_min = j

        tmp = lst_obj[idx_min]
        lst_obj[idx_min] = lst_obj[i]
        lst_obj[i] = tmp

    return lst_obj

# Сортировка шейкерная
def cocktail_sort(lst_obj):
    left = 0
    right = len(lst_obj) - 1
    while left <= right:
        for i in range(left, right):
            if lst_obj[i] > lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        right -= 1
        for i in range(right, left, -1):
            if lst_obj[i-1] > lst_obj[i]:
                lst_obj[i], lst_obj[i-1] = lst_obj[i-1], lst_obj[i]
        left += 1
    return lst_obj

original_list = [random.randint(-100, 100) for i in range(1000)]
bubble_list = original_list.copy()
merge_list = original_list.copy()
gnome_list = original_list.copy()
standart1_list = original_list.copy()
standart2_list = original_list.copy()
quick_list = original_list.copy()
insert_list = original_list.copy()
select_list = original_list.copy()
coctail_list = original_list.copy()

print('Пузырьком - ', timeit.timeit("bubble_sort_upd(bubble_list)", setup="from __main__ import bubble_sort_upd, bubble_list", number=100))
print('Слиянием - ', timeit.timeit("merge_sort(merge_list)", setup="from __main__ import merge_sort, merge_list", number=100))
print('Гном - ', timeit.timeit("gnome_sort(gnome_list)", setup="from __main__ import gnome_sort, gnome_list", number=100))
print('Стандарт 1 - ', timeit.timeit("reverse_sort(standart1_list)", setup="from __main__ import reverse_sort, standart1_list", number=100))
print('Стандарт 2 - ', timeit.timeit("reverse2_sort(standart2_list)", setup="from __main__ import reverse2_sort, standart2_list", number=100))
print('Быстрая - ', timeit.timeit("my_calc(quick_list)", setup="from __main__ import my_calc, quick_list", number=100))
print('Вставки - ', timeit.timeit("insertion_sort(insert_list)", setup="from __main__ import insertion_sort, insert_list", number=100))
print('Выбором - ', timeit.timeit("selection_sort(select_list)", setup="from __main__ import selection_sort, select_list", number=100))
print('Шейкерная - ', timeit.timeit("cocktail_sort(coctail_list)", setup="from __main__ import cocktail_sort, coctail_list", number=100))


"""
Судя по замерам, самой быстрой сортировкой оказалась 'Быстрая'
Странно, почему ее не сделали стандарной?

Пузырьком -   0.9787003959999998
Слиянием -    7.627589752999999
Гном -        2.9210276439999996
Стандарт 1 -  0.036309955000000116
Стандарт 2 -  0.004918871000000102
Быстрая -     0.0018345520000000448
Вставки -     1.3970408510000007
Выбором -    48.853364137
Шейкерная -  60.34705307200001
"""