#!/usr/bin/env python3
from car import Car
# creating a new car instance using the constructor
mercedes = Car('Mercedes Benz A-Klasse', 5, 230)
 # calling a function on a car instance
mercedes.drive('Dresden', 'Berlin')

bmw = Car('BMW 3er', 5, 250) # a different car
print(bmw) # uses __repr__ to generate string representation
print(bmw.doors) # accessing instance variables
