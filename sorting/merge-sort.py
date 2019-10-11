#!/usr/bin/env python

from sys import argv

def merge(left: list, right: list, level):
    '''
    Merge two sorted list into one list
    '''
    length_of_a: int = len(left)
    length_of_b: int = len(right)

    # print('left(level=%d)' % level, left)
    # print('right(level=%d)' % level, right)

    i = 0 # Pointer to current element of left being accessed
    j = 0 # Pointer to current element of right being accessed

    merged_list: list = []

    while i < length_of_a and j < length_of_b: # length_of_a + length_of_b = len(left) + len(right)
        if left[i] < right[j]:
            merged_list.append(left[i])
            i += 1
        else:
            merged_list.append(right[j])
            j += 1

    while i < length_of_a: # length_of_a
        merged_list.append(left[i])
        i += 1
    while j < length_of_b: # length_of_b
        merged_list.append(right[j])
        j += 1

    # print('merged_list(level=%d)' % level, merged_list) # This list should be sorted and should contain all elements of A and B

    return merged_list

# n = len(A)
def merge_sort(A, level = 0): # T(len(A)) = T(n)
    # print('-'*16, 'merge_sort(level=%d) start'%level, '-'*16)
    # print('A(level=%d)' % level, A)
    array_size = len(A)
    
    if array_size < 2:
        return A

    mid = array_size // 2

    left = A[0:mid]
    right = A[mid:]
    
    # print('going to level %d' % (level+1))
    left = merge_sort(left, level + 1) # T(len(left)) = T(n / 2)
    # print('back to level %d' % (level))
    # print('going to level %d' % (level+1))
    right = merge_sort(right, level + 1) # T(len(right)) = T(n / 2)
    # print('back to level %d' % (level))
    
    sorted_A = merge(left, right, level) # len(left) + len(right) = n
    # print('sorted_A(level=%d)' % level, sorted_A)
    # print('-'*16, 'merge_sort(level=%d) end'%level, '-'*16)
    return sorted_A

# T(n) = T(n/2) + T(n/2) + n
#      = 2 * T(n/2) + n

    
def main(args):

    # A = list(map(int, args))
    A = list(map(int, input().split(" ")))
    sorted_A = merge_sort(A)
    # print('='*32)
    # print('A', A)
    # print('='*16)
    # print('sorted_A', sorted_A)
    # print('='*32)

if __name__ == "__main__":
    main(argv[1:])
