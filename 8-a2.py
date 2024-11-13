# 8-a2.py
"""Find the minimum of three values."""

# kullanıcıdan 3 sayı al. bunların minimumunu yazdır.
# min() fonksiyonu kullanmayınız.

number1 = int(input("Enter first integer: "))
number2 = int(input("Enter second integer: "))
number3 = int(input("Enter third integer: "))

# 1.yöntem
minimum = number1   # 1.sayıyı minimum seçtik
if number2 < minimum:   # 2.sayı minimumdan küçükse
    minimum = number2   # yeni minimum 2.sayı olsun
if number3 < minimum:
    minimum = number3

# 2.yöntem
if number1 < number2 and number1 < number3:
    minimum = number1
if number2 < number1 and number2 < number3:
    minimum = number2
if number3 < number1 and number3 < number2:
    minimum = number3

print("Minimum value is", minimum)
