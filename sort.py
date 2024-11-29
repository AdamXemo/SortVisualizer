
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] >  arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

if __name__ == "__main__":
    import random

    arr = random.sample(range(10), 10)
    print(arr)

    sorted_arr = bubble_sort(arr)
    print(sorted_arr)