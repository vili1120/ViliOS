import os
import random
import time

def main(arg1=None, arg2=None):
    RUN = True
    number = random.randint(1, 50)
    while RUN:
        guess = int(input("Guess a number(1-50): "))

        if guess < number:
            print("Guess higher!\n")
        elif guess > number:
            print("Guess lower!\n")
        elif guess == number:
            print("You've won!")
            time.sleep(2.5)
            RUN = False
