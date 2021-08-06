def max_recursion(arr):
    if len(arr) == 0:
        return 0
    else:
        item_cur = arr.pop()
        item_recursion = max_recursion(arr)

        if item_cur > item_recursion:
            return item_cur
        else:
            return item_recursion


print(max_recursion([5, 10, 2, 3]))
