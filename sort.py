def swap(arr, i, j):
    yield {"values": arr.copy(),
           "highlight": [i, j]}
    arr[i], arr[j] = arr[j], arr[i]


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            yield from swap(arr, j, j+1)


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            arr[j] = key
            yield from swap(arr, j, j+1)
            j -= 1


def merge(arr, start1, end1, start2, end2):
    if start1 > end1 or start2 > end2:
        return
    if arr[start2] < arr[start1]:
        yield from swap(arr, start1, start2)
        arr.insert(start1, arr.pop(start2))
        yield from swap(arr, start1, start1+1)
        yield from merge(arr, start1+1, end1+1, start2+1, end2)
    else:
        yield from swap(arr, start1, start2)
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
            yield from swap(arr, i, j-1)

        while True:
            j -= 1
            if arr[j] <= pivot:
                break
            yield from swap(arr, i, j)

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
            yield from swap(arr, i, j)
        else:
            break

    yield from quick_sort(arr, start, j)
    yield from quick_sort(arr, j+1, end)


def heap_sort(arr):
    start = len(arr) // 2
    end = len(arr)
    while end > 0:
        if start > 0:
            start -= 1
        else:
            end -= 1
            arr[0], arr[end] = arr[end], arr[0]
            yield from swap(arr, 0, end)

        while (child := 2*start + 1) < end:
            if child + 1 < end and arr[child+1] > arr[child]:
                child = child+1

            if arr[start] < arr[child]:
                arr[start], arr[child] = arr[child], arr[start]
                yield from swap(arr, start, child)
                start = child
            else:
                break
