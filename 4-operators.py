# aritmetik, atama, karşılaştırma, mantıksal, ... operatörleri

# aritmetik: + - * / % // **
print(12 + 3 * 5 / 2 + 4 ** 2)

# atama: =, +=, -=, *=, ...
x = 4
x += 3
print(x)
# x = x + 3

# karşılaştırma: >, <, >=, <=, ==, !=
x = 5
y = 10
z = 5
print(x > y)
print(x < y)

# mantıksal: and, or, not
# or --> bir tanesi bile doğruysa sonuç doğru
# and --> bir tanesi bile yanlışsa sonuç yanlış
print(1 > 0 or 1 < 0)
print(1 > 0 and 1 < 0)

# diğerleri
# iki değerin eşitliğini kontrol etmek: is, is not
print(type(10) is int)
print(type(10) is not int)

# bir şey bir şeyin içerisinde var mı kontrol etmek: in, not in
print(10 in [1, 2, 3, 4, 5])
print("a" in "merhaba")
print(1 in range(1, 10))
print(10 in range(1, 10))
# range(1, 10) ---> [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(2**3**2)
print(2**(3**2))

# Booleans
# python'daki her değer True veya False şeklinde yorumlanabilir.
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

print(2 ** 3 + 12 == 20 and "hello" != "merhaba")

print(2 ** 3 + 12 == (20 and "hello") != "merhaba")
# print(20 and "hello")

# print(20 == "hello" != "merhaba")
# print(20 == "hello" and "hello" != "merhaba")


# Short Circuiting (and, or)
print("---- OR ----")
print(3 or "hello")
print('' or "hello")
print(True or 0)
print(None or 0)

print(None or 0 or '' or "Hello" or 23)
# ilk karşılaştığı True değeri döndür.
# sona kadar True bir değerle karşılaşmazsan sonuncusunu döndür.

print("---- AND ----")
print(0 and "hello")
print(7 and "hello")

print("hello" and 23 and None and "merhaba")
# ilk karşılaştığı False değeri döndür.
# sona kadar False bir değerle karşılaşmazsan sonuncusunu döndür.

# örnek
hasDrivingLicense = False
if (hasDrivingLicense):
  print("Sarah can start driving 🚗")

hasDrivingLicense and print("Sarah can start driving 🚗")

# Chaining Comparison Operators (karşılaştırma operatörlerini zincirleme)
x = 5
y = 10
if 1 < x < 10:
  print("x is between 1 and 10")
if 1 < x and x < 10:
  print("x is between 1 and 10")
if x < y < 20:
  print("x is less then y and y is less than 20")
if x < y and y < 20:
  print("x is less then y and y is less than 20")


# ternary operator
# Syntax: true_value if condition else false_value
a = 10
b = 20
min = "a is minimum" if a < b else "b is minimum"
# "a is minimum" stringini döndür; eğer a b'den küçükse,
# değilse "b is minimum" değerini döndür.
print(min)

print("Both are equal" if a == b else "a is greater"
      if a > b else "b is greater")

# Örnek
print("Sarah can start driving 🚗" if hasDrivingLicense else "Sarah can't drive")