import random
import timeit


def select_sort(lst):
    """
    Сортировка выбором
    Сложность алгоритма O(n^2)
    """

    for i in range(len(lst)):
        min_index = i
        for j in range(i + 1, len(lst)):
            if lst[min_index] > lst[j]:
                min_index = j

        if min_index != i:
            lst[min_index], lst[i] = lst[i], lst[min_index]

    return lst


lst_10 = random.sample(range(10), 10)
lst_100 = random.sample(range(100), 100)
lst_1000 = random.sample(range(1000), 1000)

print(select_sort(lst_10))
print(select_sort(lst_100))
print(select_sort(lst_1000))

print(timeit.timeit('select_sort(lst_10[:])', globals=globals(), number=1000))
print(timeit.timeit('select_sort(lst_100[:])', globals=globals(), number=1000))
print(timeit.timeit('select_sort(lst_1000[:])', globals=globals(), number=1000))

"""
Результаты замеров:

0.007398700000000008
0.3179064
33.2881737
"""
