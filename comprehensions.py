#!/usr/bin/env python3
# list comprehension
myList = [i for i in range(0, 10)]

# all squares
squareList = [i*i for i in range(0,10)]

# filtered squares
filteredSquares = [i for i in squareList if i % 2 == 0]
