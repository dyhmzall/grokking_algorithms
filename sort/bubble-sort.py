import random
import timeit


def bubble_sort(lst):
    """
    Сортировка пузырьком
    Сложность алгоритма O(n^2)
    """

    n = 1

    while n < len(lst):
        for i in range(len(lst) - n):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]

        n += 1

    return lst


lst_10 = random.sample(range(10), 10)
lst_100 = random.sample(range(100), 100)
lst_1000 = random.sample(range(1000), 1000)

print(bubble_sort(lst_10))
print(bubble_sort(lst_100))
print(bubble_sort(lst_1000))

print(timeit.timeit('bubble_sort(lst_10[:])', globals=globals(), number=1000))
print(timeit.timeit('bubble_sort(lst_100[:])', globals=globals(), number=1000))
print(timeit.timeit('bubble_sort(lst_1000[:])', globals=globals(), number=1000))

"""
Результаты замеров:

0.0081257
0.3877926
41.2713665
"""
