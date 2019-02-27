#!/usr/bin/env python3
a = 0
b = 0
while True:
    if a is not b:
        print(f'a was {a} and b was {b}')
        break
    else:
        a += 1
        b += 1
