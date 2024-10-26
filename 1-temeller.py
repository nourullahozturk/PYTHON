# yorum satırı # ile yapılır.

"""
bu da bir yorum satiridir. " yerine ' de kullanilabilir
"""

# değişken tanımlama
x = 'hello'   # string
y = 5   # int
z = True    # bool
k = 0.5     # float
l = [1, 2, 3]   # list

# shift + alt + down arrow --> satır kopyalama
# ctrl + d --> çoklu seçme
print(x)
print(x)
print(x)
print(x)
print(x)

# multiple variable assignment (çoklu değişken ataması)
x, y, z = "Orange", "Red", "Green"
print(x, y, z)

# unpacking list (liste açma)
x, y, z = ["apple", "banana", "cherry"]

# string concatenation (string birleştirme)
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

# casting (tür değiştirme)
# str(), int(), bool()
x = 5
print(x, type(x))
x = str(x)
print(x, type(x))

a = "Hello, World!"
print(len(a))
b = input("girdi: ")
print(b)