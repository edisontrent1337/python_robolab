#!/usr/bin/env python3
def compare(a, b):
    if a == b:
        print('a and b are equal in value')
    if a is b:
        print('a and b point to the same object')
    else:
        print('a and b are different objects')
compare(1,1)
compare([1], [1])
compare('hello', 'hello')
a = 'hello'
b = 'h'
c = 'ello'
b = b + c
compare(a, b)
