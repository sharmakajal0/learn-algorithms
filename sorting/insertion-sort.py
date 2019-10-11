#!/usr/bin/env python

from sys import argv

# Algorithm
def insertion_sort(A): # A is the input parameter as well as output parameter
    for j in range(1, len(A)):
        key = A[j]
        
        i = j - 1

        while (i >= 0 and key < A[i] ):
            A[i + 1] = A[i]
            i -= 1

        A[i + 1] = key

# Input
# A = list(map(int, input().split()))
# => Get input from command line

# $ python insertion-sort.py 4 3 2 5 6 1
# 1 2 3 4 5 6

def main(args):
    print('arguments to program =>', ' '.join(args))
    # A = list(map(int, args))
    A = list(map(int, input().split(" ")))

    # print('A before sorting =>', ' '.join(map(str, A)))

    insertion_sort(A)

    # print('A after sorting =>', ' '.join(map(str, A)))

if __name__ == "__main__":
    main(argv[1:])
