def shaker_sort_basic(arr):
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1

    while swapped:
        swapped = False

        # Forward pass
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        # Break if sorted
        if not swapped:
            break

        swapped = False

        end = end - 1

        # Backward pass
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        start = start + 1

    return arr

# List comprehensions with 'any' function

def shaker_sort_any(arr):
    n = len(arr)
    start, end = 0, n - 1

    while True:
        # Forward pass
        forward_indices = range(start, end)
        forward_swaps = [(i, i + 1) for i in forward_indices if arr[i] > arr[i + 1]]
        for i, j in forward_swaps:
            arr[i], arr[j] = arr[j], arr[i]

        # Break if sorted
        if not forward_swaps:
            break

        # Backward pass
        backward_indices = range(end - 1, start - 1, -1)
        backward_swaps = [(i, i + 1) for i in backward_indices if arr[i] > arr[i + 1]]
        for i, j in backward_swaps:
            arr[i], arr[j] = arr[j], arr[i]

        start, end = start + 1, end - 1

    return arr

#----
#
# to sort based on specific attribute, use the 'key' param
#
#----

from functools import reduce
from itertools import groupby

class MyObject:
    def __init__(self, value):
        self.value = value

def shaker_sort_with_tools(arr):
    n = len(arr)

    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    def forward_pass():
        nonlocal arr
        groups = groupby(range(n - 1), key=lambda i: arr[i].value > arr[i + 1].value)
        for is_greater, indices in groups:
            if is_greater:
                indices = list(indices)
                swap(indices[0], indices[-1])

    def backward_pass():
        nonlocal arr
        groups = groupby(range(n - 1, 0, -1), key=lambda i: arr[i - 1].value > arr[i].value)
        for is_greater, indices in groups:
            if is_greater:
                indices = list(indices)
                swap(indices[-1], indices[0])

    while True:
        forward_pass()
        backward_pass()
        if not any(arr[i].value > arr[i + 1].value for i in range(n - 1)):
            break

    return arr

# Example usage:
my_objects = [MyObject(5), MyObject(3), MyObject(8), MyObject(4), MyObject(2), MyObject(1)]
sorted_objects = shaker_sort(my_objects, key=lambda x: x.value)
print([obj.value for obj in sorted_objects])


