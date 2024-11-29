def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                yield arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            arr[j] = key
            yield arr
            j -= 1


def merge(arr1, arr2):
    if arr1 == []:
        return arr2
    elif arr2 == []:
        return arr1
    elif arr1[0] < arr2[0]:
        return [arr1[0]] + merge(arr1[1:], arr2)
    else:
        return [arr2[0]] + merge(arr1, arr2[1:])


def merge_sort(arr):
    if len(arr) == 1:
        return arr

    middle = len(arr) // 2

    return merge(
        merge_sort(arr[:middle]),
        merge_sort(arr[middle:]))


if __name__ == "__main__":
    import random

    arr = random.sample(range(10), 10)
    print(arr)

    sorted_arr = insertion_sort(arr)
    print(sorted_arr)
