#!/usr/bin/env python2.7
#to use - edit stringToCipher to encrypted string
import string
import collections

def rotate(rotateString, number):
    upper = collections.deque(string.ascii_uppercase)
    lower = collections.deque(string.ascii_lowercase)

    upper.rotate(number)
    lower.rotate(number)

    upper = ''.join(list(upper))
    lower = ''.join(list(lower))

    return rotateString.translate(string.maketrans(string.ascii_uppercase, upper)).translate(string.maketrans(string.ascii_lowercase, lower))


stringToCipher = "efgfoe uif fbtu xbmm pg uif dbtumf"
print('\n')
for i in range(26):
    print(i, rotate(stringToCipher, i))
