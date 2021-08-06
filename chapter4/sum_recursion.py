def sum_recursion(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr.pop() + sum_recursion(arr)


print(sum_recursion([1, 2, 3, 4, 5, 6]))
