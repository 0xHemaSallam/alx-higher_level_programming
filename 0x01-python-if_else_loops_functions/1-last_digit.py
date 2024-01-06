#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
less = "and is less than 6 and not 0"
greater = "and is greater than 5"
zero = "and is 0"

if number < 0:
    last_digit = number % -10
else:
    last_digit = number % 10

if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} {greater}")
elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit} {zero}")
else:
    print(f"Last digit of {number} is {last_digit} {less}")
