def count_recursion(arr):
    if len(arr) == 0:
        return 0
    else:
        arr.pop()
        return 1 + count_recursion(arr)


print(count_recursion([1, 2, 3, 4, 5, 6]))
