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