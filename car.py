#!/usr/bin/env python3
class Car:
    wheels = 4 # class variable shared by all instances
    def __init__(self, manufacturer, doors, hp): # constructor with arguments
        self.manufacturer = manufacturer
        self.doors = doors
        self.hp = hp
    def __repr__(self): # string representation of this classe's objects
        return f'{self.wheels} wheeled car {self.manufacturer} with {self.doors} doors and {self.hp} horsepower'
    # functions of the class
    def updateEngine(self, hp):
        self.hp = hp
        print(f'Updated car to {self.hp} hp')
    def drive(self, start, destination):
      print(f'Car drives from {start} to {destination}')
