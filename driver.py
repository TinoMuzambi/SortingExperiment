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
    sizes = []
    sizes.append(100)
    sizes.append(1000)
    sizes.append(5000)
    sizes.append(10000)
    sizes.append(50000)
    for i in sizes:
        #print("Generating list...")
        arr = generate_list(i)
        #print("Done.")
        #print("Starting timer...")
        curr_time = time.time()
        #print("Starting sort...")
        # quickSort(arr, 0, size - 1)
        do_selection_sort(arr)
        #print("Done.")
        stop_time = time.time()
        #print("Stopped timer.")
        taken = stop_time - curr_time
        # print(arr)
        print("{:<6} elements took {:<3.6f} seconds.".format(i, taken))


if __name__ == '__main__':
    main()
