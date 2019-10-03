from quick_sort import quickSort
from selection_sort import do_selection_sort
import random
import time


# Driver program for quicksort program


def generate_list(size):
    arr = []
    for i in range(size):
        arr.append(random.randint(0, 100))
    return arr


def main():
    size = 100
    while size <= 1000000:
        print("Generating list...")
        arr = generate_list(size)
        print("Done.")
        print("Starting timer...")
        curr_time = time.time()
        print("Starting sort...")
        # quickSort(arr, 0, size - 1)
        do_selection_sort(arr)
        print("Done.")
        stop_time = time.time()
        print("Stopped timer.")
        taken = stop_time - curr_time
        # print(arr)
        print("{:<6} elements took {:<6f} seconds.".format(size, taken))
        size *= 10


if __name__ == '__main__':
    main()
