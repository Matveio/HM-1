from random import randint
from time import sleep

class cat:

    
    def __init__(self):

        self.Health = 100
        self.sleepchance = 50
        self.meowchance = 3

    def meow(self):
        print('meow')
        sleep(0.1)
        print(f'Health: {self.Health} -> {self.Health + 10}')
        self.Health += 10

    def catsleep(self):
        print('sleeping')
        sleep(10)
        print('sleep has end')
        print(f'Health: {self.Health} -> {self.Health + 50}')
        self.Health += 50


Cat = cat()
whiles = 0
while True:
    sleep(1)
    if whiles < 20 and Cat.Health <= 200:
        if randint(1, Cat.meowchance) == 2:
            Cat.meow()
        if randint(1, Cat.sleepchance) == 36:
            Cat.catsleep()

        whiles += 1

        print(whiles)

        if Cat.Health >= 200:
            print('your cat has won')
            break
        if whiles >= 20:
            print('your cat got old')
            break
