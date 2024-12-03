def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            yield {"values": arr.copy(),
                   "highlight": [j, j+1]}


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            arr[j] = key
            yield {"values": arr.copy(),
                   "highlight": [j, j+1]}
            j -= 1


def merge(arr, start1, end1, start2, end2):
    if start1 > end1 or start2 > end2:
        return
    if arr[start2] < arr[start1]:
        yield {"values": arr.copy(),
               "highlight": [start1, start2]}
        arr.insert(start1, arr.pop(start2))
        yield {"values": arr.copy(),
               "highlight": [start1, start1+1]}
        yield from merge(arr, start1+1, end1+1, start2+1, end2)
    else:
        yield {"values": arr.copy(),
               "highlight": [start1, start2]}
        yield from merge(arr, start1+1, end1, start2, end2)


def merge_sort(arr, start=0, end=-1):
    end %= len(arr)

    if end - start == 0:
        return

    middle = (start+end) // 2

    yield from merge_sort(arr, start, middle)
    yield from merge_sort(arr, middle+1, end)

    yield from merge(arr, start, middle, middle+1, end)


def quick_sort(arr, start=0, end=-1):
    end %= len(arr)

    if end <= start:
        return

    pivot = arr[(start+end) // 2]
    i = start-1
    j = end+1
    while True:
        while True:
            i += 1
            if arr[i] >= pivot:
                break
            yield {"values": arr.copy(),
                   "highlight": [i, j-1]}

        while True:
            j -= 1
            if arr[j] <= pivot:
                break
            yield {"values": arr.copy(),
                   "highlight": [i, j]}

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
            yield {"values": arr.copy(),
                   "highlight": [i, j]}
        else:
            break

    yield from quick_sort(arr, start, j)
    yield from quick_sort(arr, j+1, end)
