import random
import timeit


def insert_sort(lst):
    """
    Сортировка вставками
    Сложность алгоритма O(n^2)
    """

    for i in range(len(lst)):
        j = i
        current = lst[j]
        while j > 0 and current < lst[j - 1]:
            lst[j] = lst[j - 1]
            j -= 1

        lst[j] = current

    return lst


lst_10 = random.sample(range(10), 10)
lst_100 = random.sample(range(100), 100)
lst_1000 = random.sample(range(1000), 1000)

print(insert_sort(lst_10))
print(insert_sort(lst_100))
print(insert_sort(lst_1000))

print(timeit.timeit('insert_sort(lst_10[:])', globals=globals(), number=1000))
print(timeit.timeit('insert_sort(lst_100[:])', globals=globals(), number=1000))
print(timeit.timeit('insert_sort(lst_1000[:])', globals=globals(), number=1000))

"""
Результаты замеров:

0.0017843000000000026
0.015083899999999997
0.1520953
"""
