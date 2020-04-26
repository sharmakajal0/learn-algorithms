#!/usr/bin/env python

class Sliding_Window:
    def __init__(self, window_size= 20):
        self.window_size = window_size
        self.input_string = ''

    def compress(self, input_string):
        '''
        sliding window algorithm(
            window_size: The total size of the window which is the sum of Search buffer size and look ahead buffer size,
            Search_buffer_size: The size of the buffer which is used to search the character which is to be encoded,
            Look_ahead_buffer_size: The size of the buffer which is used to look at the character,
            Input_string: the string which is to be encoded.
        ):
        1. Initialize:-
            Look_ahead_buffer = Input_string[0:Look_ahead_buffer_size]
            Search_buffer = []

        2. Compress:-
            While(len(input) > 0):
                Find Best Match()
                if not found:
                    print(<0, 0, c(look_ahead_buffer[j])>)
                else:
                    print(<i, l, c(look_ahead_buffer[j+1])>)
        while input is not empty... Do
            prefix = longest prefix of input that begins in window
            if prefix exists then 
                i = distance of the start of prefix
                l = length of prefix
                c = character following prefix in input
            else:
                i = 0
                l = 0
                c = first char of input
            end if
        output(i, l, c)
        s = pop l + 1 chars from the front of input
            discard l + 1 chars from the front of window
            append s to back of window
        repeat
        '''
        look_ahead_buffer = input_string[0:look_ahead_buffer_size]
        search_buffer = ''
        i = 0
        # while(len(search_buffer) > 0):
            
            

if __name__ == "__main__":
    object = Sliding_Window()
    window_size = int(input("Input Window Size: "))
    search_buffer_size = int(input("\nSearch Buffer Size: "))
    input_string = input("\nInput String: ")
    look_ahead_buffer_size = window_size - search_buffer_size
    print("\nWindow Size: ", window_size, "\nsearch Buffer: ", search_buffer_size, "\nLook ahead buffer size: ", look_ahead_buffer_size, "\ninput_string: ", input_string, )
