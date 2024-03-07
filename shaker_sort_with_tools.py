
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


