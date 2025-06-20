def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):

        min_idx = i

        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[j], arr[min_idx] = arr[min_idx], arr[j]

    return arr




    # TODO: Implement selection sort

