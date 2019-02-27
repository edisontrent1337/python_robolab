# imports the class Car from the file car.py
from car import Car

# returns a new Car instance
def sellBMW():
    return Car("BMW", 5, 300)

# modifies instance variable of a given car
def upgradeCar(car):
    # calling an instance function and accessing instance variables
    car.updateEngine(car.hp + 100)
    return car
