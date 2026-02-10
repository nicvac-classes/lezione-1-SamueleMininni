#!/usr/bin/env python3
# NOTE: it is recommended to use this even if you don't understand the following code.
import sys
sys.stdin = open('keyboardshift_input0.txt')
sys.stdout = open('output.txt', 'w')

# input data
N = int(input().strip())
S = input().strip()

alfabeto = {
    'q': 'w',
    'w': 'e',
    'e': 'r',
    'r': 't',
    't': 'y',
    'y': 'u',
    'u': 'i',
    'i': 'o',
    'o': 'p',
    'p': 'ò',

    'a': 's',
    's': 'd',
    'd': 'f',
    'f': 'g',
    'g': 'h',
    'h': 'j',
    'j': 'k',
    'k': 'l',
    'l': 'à',
    'à': 'è',

    'z': 'x',
    'x': 'c',
    'c': 'v',
    'v': 'b',
    'b': 'n',
    'n': 'm',
    'm': ','
}

stringaCorretta = ""
for i in range(len(S)):
    errato = S[i]
    stringaCorretta += alfabeto.get(errato, errato)

# insert your code here


print(stringaCorretta)  # print the result
