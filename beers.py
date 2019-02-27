#!/usr/bin/env python3
def orderBeer(age, beersHad):
    if age < 16:
        print(f'Get outta here. You are only {age} y.o.')
    elif beersHad > 5:
        print(f'Go home! You are drunk, you had {beersHad} beers dude.')
    else:
        beersHad += 1
        print(f'Here is your beer. Enjoy!')
    return beersHad
