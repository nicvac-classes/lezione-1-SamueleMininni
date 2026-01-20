#!/usr/bin/env python3
# NOTE: it is recommended to use this even if you don't understand the following code.

import sys

# uncomment the two following lines if you want to read/write from files
sys.stdin = open('input0.txt')
sys.stdout = open('output.txt', 'w')

N = int(input().strip())

B = 0


# INSERT YOUR CODE HERE
for i in range(1, N+1):
    B += i

print(B)

sys.stdout.close()
