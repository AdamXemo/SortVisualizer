import random
import time

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
            arr[j+1], arr[j] = arr[j], arr[j+1]
            yield {"values": arr.copy(),
                   "highlight": [j, j+1]}
            j -= 1


def shell_sort(arr):
    gaps = [701, 301, 132, 57, 23, 10, 4, 1]
    for gap in gaps:
        for i in range(1, len(arr)):
            j = i
            while j-gap >= 0:
                yield {"values": arr.copy(),
                       "highlight": [j-gap, j]}

                if arr[j-gap] <= arr[j]:
                    break

                arr[j-gap], arr[j] = arr[j], arr[j-gap]
                yield {"values": arr.copy(),
                       "highlight": [j-gap, j]}
                j -= gap


def merge(arr, start1, end1, start2, end2):
    if start1 > end1 or start2 > end2:
        return

    yield {"values": arr.copy(),
           "highlight": [start1, start2]}

    if arr[start2] < arr[start1]:
        arr.insert(start1, arr.pop(start2))
        yield {"values": arr.copy(),
               "highlight": [start1, start1+1]}
        yield from merge(arr, start1+1, end1+1, start2+1, end2)
    else:
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


def heap_sort(arr):
    start = len(arr) // 2
    end = len(arr)
    while end > 0:
        if start > 0:
            start -= 1
        else:
            end -= 1
            arr[0], arr[end] = arr[end], arr[0]
            yield {"values": arr.copy(),
                   "highlight": [0, end]}

        while (child := 2*start + 1) < end:
            if child + 1 < end and arr[child+1] > arr[child]:
                child = child+1

            if arr[start] < arr[child]:
                arr[start], arr[child] = arr[child], arr[start]
                yield {"values": arr.copy(),
                       "highlight": [start, child]}
                start = child
            else:
                break

def bogo_sort(arr):
    for _ in range(1000):
        random.shuffle(arr)
        yield {"values": arr.copy(),
               "highlight": random.sample(range(len(arr)-1), len(arr) // 5)}
        