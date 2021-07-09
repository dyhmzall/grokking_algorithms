def binary_search(items, item):
    low = 0
    high = len(items) - 1

    while low <= high:
        mid = int((low + high) / 2)
        guess = items[mid]

        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1  # отнимаем единицу, поскольку текущее значение items[mid] не равно item
        else:
            low = mid + 1  # прибавляем единицу, поскольку текущее значение items[mid] не равно item

    return None


# проверка алгоритма
my_list = list(range(0, 100, 2))

print(my_list)
print('search:', 20, 'index:', binary_search(my_list, 20))
print('search:', 40, 'index:', binary_search(my_list, 40))
print('search:', 60, 'index:', binary_search(my_list, 60))
print('search:', 76, 'index:', binary_search(my_list, 76))
