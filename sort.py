
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] >  arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                yield arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

if __name__ == "__main__":
    import random

    arr = random.sample(range(10), 10)
    print(arr)

    sorted_arr = insertion_sort(arr)
    print(sorted_arr)