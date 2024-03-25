import time
import random

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
            print("Merging:", arr)
            time.sleep(0.1)

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
            print("Merging:", arr)
            time.sleep(0.1)

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
            print("Merging:", arr)
            time.sleep(0.1)

def main():
    array = [random.randint(50, 500) for _ in range(10)]

    print("Unsorted array:", array)
    merge_sort(array)
    print("Sorted array:", array)

if __name__ == "__main__":
    main()

