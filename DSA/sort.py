def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


print(bubble_sort([56, 1, 2, 3, 34, 2]))


def insertion_sort(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1
        while current < arr[j] and j >= 0:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current
    return arr


print(insertion_sort([56, 1, 2, 3, 34, 2]))


def selection_sort(arr):
    for i in range(len(arr) - 1):
        min = i
        for j in range(i, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr


print(selection_sort([56, 1, 2, 3, 34, 2]))


def quick_sort(arr):
    if len(arr) < 2:
        return arr
    mid = arr[len(arr) // 2]
    left = [x for x in arr if x < mid]
    pivot = [x for x in arr if x == mid]
    right = [x for x in arr if x > mid]
    return quick_sort(left) + pivot + quick_sort(right)


print(quick_sort([56, 1, 2, 3, 34, 2]))


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            k += 1
            i += 1
        while j < left(right):
            arr[k] = right[j]
            k += 1
            j += 1

    return arr


print(merge_sort([56, 1, 2, 3, 34, 2]))


