#!/usr/bin/python3
def remove_char_at(str, n):
    new = ''
    r = 0
    for c in str:
        if r != n:
            new += str[r]
        r += 1
    return new
