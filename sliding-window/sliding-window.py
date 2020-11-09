#!/usr/bin/env python

def compress(search, look_ahead):
    search_length = len(search)
    look_ahead_length = len(look_ahead)

    if(search_length == 0):
        return(0, 0, look_ahead[0])

    best_length = 0
    best_offset = 0
    buffer = search + look_ahead
    search_pointer = search_length
    for i in range(0, search_length):
        length = 0
        offset = 1
        while buffer[i + length] == buffer[search_pointer + length]:
            length += 1
            print(len(buffer))
            if search_pointer + length == len(buffer):
                length -= 1
            if i + length >= search_pointer:
                break
        if length > best_length:
            best_offset = i + offset
            best_length = length
    return (best_offset, best_length, buffer[search_pointer+best_length])

INPUT_STRING = input()
input_string = list(INPUT_STRING)

search_iterator = 0
iterator = 0
max_search = int(input("Enter the size of search buffer"))
max_look_ahead = int(input("\nEnter the size of look ahead buffer"))
print()
count = 1
while(iterator < len(input_string)):
    search = input_string[search_iterator:iterator]
    look_ahead = input_string[iterator:iterator+max_look_ahead]
    (offset, match_length, character) = compress(search, look_ahead)
    print("%d = <%d, %d, c(%s)>" %(count, offset, match_length, character))
    iterator = iterator + match_length + 1
    search_iterator = iterator - max_search
    count += 1
    if search_iterator < 0:
        search_iter = 0
