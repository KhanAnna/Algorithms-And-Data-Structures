from array import array
import random
import numpy

import os
import sys

file_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(file_dir + "/src")
print(file_dir)
from bubble_sort import bubble_sort_v1

def generate_array(low, high, size) -> array:
    _array = numpy.random.randint(low, high, size)
    return _array

def print_array(array) -> None:
    print(str(array))

def main() -> int:
    while True:
        try:
            low, high, size = map(int, input("Input low, high borders and size of array: ").split())
            break
        except ValueError:
            print("Oops! That was no valid number. Try again.")

    array_test = generate_array(low, high, size)
    print("Initial array")
    print_array(array_test)
    bubble_sort_v1(array_test)
    print("Sorted array")
    print_array(array_test)

main()