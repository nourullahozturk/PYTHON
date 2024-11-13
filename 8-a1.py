# 8-a1.py
"""Comparing integers using if statements and comparison operatos."""

print("İki sayı gir, aralarındaki ilişkiyi söyleyeyim.")

# kullanıcıdan iki sayı al. değişkenlerde tut
# eğer sayı1 sayı2 ile eşit ise "sayı1, sayı2 ile eşittir" yazdır
# eğer sayı1 sayı2 ile eşit değilse "sayı1, sayı2 ile eşit değildir" yazdır
# eğer sayı1 sayı2 den küçük ise "sayı1, sayı2 den küçüktür" yazdır
# eğer sayı1 sayı2 den büyük ise "sayı1, sayı2 den büyüktür" yazdır
# eğer sayı1 sayı2 den küçük veya eşit ise "sayı1, sayı2 den küçük veya eşittir" yazdır
# eğer sayı1 sayı2 den büyük veya eşit ise "sayı1, sayı2 den büyük veya eşittir" yazdır

# İpucu: kullancıdan input() fonksiyonu ile girdi alabilirsiniz

number1 = int(input("İlk sayıyı giriniz: "))
number2 = int(input("İkinci sayıyı giriniz: "))

if number1 == number2:
    # print(str(number1) + ", " + str(number2) + "'e eşittir.")
    print(f"{number1}, {number2}'e eşittir.")
if number1 != number2:
    print(str(number1) + ", " + str(number2) + "'e eşit değildir.")
if number1 > number2:
    print(str(number1) + ", " + str(number2) + "'den büyüktür.")
if number1 < number2:
    print(str(number1) + ", " + str(number2) + "'den küçüktür.")
if number1 >= number2:
    print(str(number1) + ", " + str(number2) + "'den büyük veya ona eşittir.")
if number1 <= number2:
    print(str(number1) + ", " + str(number2) + "'den küçük veya ona eşittir.")