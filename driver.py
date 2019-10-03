from quick_sort import *
import random
import time


# Driver program for quicksort program


def generate_list(size):
    li = []
    for i in range(size):
        li.append(random.randint(0, 100))
    return li


def main():
    size = eval(input("Enter list size:\n"))
    li = generate_list(size)
    curr_time = time.time()
    quickSort(li, 0, size - 1)
    stop_time = time.time()
    taken = stop_time - curr_time
    print(taken)


if __name__ == '__main__':
    main()
