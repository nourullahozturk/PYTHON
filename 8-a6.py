# 8-a6.py
"""A Dice-Rolling Game"""

# Bir zar atma programı yazınız.
# örnek girdi ve çıktılar:

# Roll the dice? (y/n):
# > y
# You rolled (5, 6)

# Roll the dice? (y/n):
# > n
# Thanks for playing!

# Roll the dice? (y/n):
# > 5
# Invalid choice!

# Bu programı şu şekilde güncelleyiniz:
# kullanıcı ne kadar zar atacağını önceden belirlesin.

import random

rollCount = int(input("How many dice do you want to roll?: "))

i = 0
while i < rollCount:
    print("Roll the dice? (y/n)")
    answer = input()
    if answer == "y":
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        print(f"You rolled ({die1}, {die2})")
    elif answer == "n":
        print("Thanks for playing!")
        break   
    else:
        print("Invalid choice!")
    i += 1