# 8-a9.py
"""A Number Guessing Game"""
# 1 ve 100 arasında rastgele bir sayı seç 
# kullanıcıdan girdi al (Guess the number between 1 and 100:)
# eğer girdi seçilen sayıdan küçükse:
# Too low!
# eğer girdi seçilen sayıdan büyükse:
# Too high!
# aynıysa
# Congratulations! You guessed the number.
# hata kontrollerini yapmayı unutmayın.

import random, sys
number_to_guess = random.randint(1, 100)
while True:
    try:
        guess = int(input("Guess the number between 1 and 100: "))
        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print("Congratulations! You guess the number.")
            # sys.exit()
            break
    except ValueError:
        print("Please enter a valid number")