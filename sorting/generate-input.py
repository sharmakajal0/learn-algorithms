#!/usr/bin/env python

from sys import argv
from random import randint

filename = argv[1]
N = int(argv[2])

input_array = [str(randint(0, 100000)) for i in range(N)]
# print(input_array)

with open(filename, 'w') as f:
    f.write(' '.join(input_array))

