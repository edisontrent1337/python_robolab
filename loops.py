#!/usr/bin/env python3
# for loop
def pingpongFor(duration):
    for i in range(0, duration):
        if i % 2 == 0:
            print('PING')
        else:
            print('PONG')
# while loop
def pingpongWhile(duration):
    i = 0
    while i is not duration:
        if i % 2 == 0:
            print('PING')
        else:
            print('PONG')
        i += 1
