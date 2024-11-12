"""
Python Collections (Arrays)

There are four collection data types in the Python programming language:

  - List is a collection which is ordered and changeable. Allows duplicate members.
  - Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
  - Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
  - Dictionary is a collection which is ordered** and changeable. No duplicate members.

*Set items are unchangeable, but you can remove and/or add items whenever you like.
**As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
"""

import os

mylist = ["apple", "banana", "cherry", "carrot"]
print(len(mylist))
list1 = ["abc", 34, True, 40, "male"]

print(range(1,10)) # 1, 2, 3, ..., 9 ama range türünde
print(range(10)) # 0, 2, 3, ..., 9 ama range türünde
print(list(range(1,10)))
print(list(range(10)))

# aynı stringler gibi indexlenebilir, slice edilebilir.
print(mylist[0])
print(mylist[1:3])
# içerisinde bir eleman var mı kontrol edilebilir.
print("Yes, apple is in the list" if "apple" in mylist else "No, apple is not in the list")


# liste elemanı değiştirme
thislist = ["apple", "banana", "cherry"]
# tek elemanı değiştirme
thislist[0] = "carrot"
# çoklu eleman değiştirme
thislist[1:3] = ["watermelon"]
print(thislist)
# insert(): istediğimiz yere eleman yerleştirme 
thislist.insert(1, "tomato")
print(thislist)
# append(): listenin sonuna eleman ekleme
thislist.append("karambola")
print(thislist)
# extend(): iki listeyi(herhangi bir dizi de olur) birleştirme
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
# thislist.extend("merhaba")
print(thislist)

# remove(): istediğimiz bir elemanı kaldırma
thislist.remove("carrot")
print(thislist)
# pop(): sondan eleman kaldırma
thislist.pop()
print(thislist)
thislist.pop(1)
print(thislist)
# del keywordü ile eleman kaldırma
del thislist[0]
print(thislist)
# listeyi temizleme/boşaltma
thislist.clear()
print(thislist)
# listeyi silme
del thislist

# os.system("cls")

# Liste dönme

# elemanları dönme
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x) 

# index dizisi ile liste dönme
# range bir dönülebilir nesne oluşturur: bu örnekte range(3) --> [0, 1, 2]
for i in range(len(thislist)):
  print(thislist[i])

# while ile liste dönme
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

# List Comprehesion
# List comprehension offers a shorter syntax when you want to create a
# new list based on the values of an existing list.

# Syntax: newlist = [expression for item in iterable if condition == True]
# Eğer şart sağlanırsa dizinin her elemanı için expression çalıştırılacak
# expression'ın döndürdüğü değer bir listeye eklenecek
# expression: değer döndüren bir ifade demektir. örn. 5 + 2, 2 == 3, "Mad", 4, True, ... 

# Egzersiz:
# Asagidaki liste elemanlarindan icinde a harfi bulunan
# elemanlari ayri bir listeye alalim.
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

#################################################

#...

#################################################

# sort lists
# sort(): listeyi alfabetik veya sayısal olarak sıralar
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
# sayılar için default olarak küçükten büyüğe sıralar
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
# büyükten küçüğe sıralamak için reverse argümanını True yapmalısınız 
thislist.sort(reverse = True)
print(thislist)

# Customizing Sort Function
def myfunc(n):
  return abs(n - 50)
# 100, 50, 65, 82, 23
# 50 0 15 32 27 return edilen değerler sort edilecek
# 0 15 27 32 50 bu sonucların sırasına göre dizinin elemanlarını sırala

thislist = [100, 50, 65, 82, 23]
# sort fonksiyonu listenin elemanlarını tek tek myfunc fonksiyonuna arguman olarak verir
thislist.sort(key = myfunc)
print(thislist)

# Örnek: Case-insensitive sort
thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort()
# print(thislist)
thislist.sort(key = str.lower)
print(thislist)

# listenin elemanlarını tersine sırala. alfabeden bağımsız.
thislist = ["banana", "Orange", 15, "Kiwi", "cherry", 3]
thislist.reverse()
print(thislist)

print("thislist[::-1] ", thislist[::-1])

# 3 parametreli slicing.
mystr = "Hello, World!"
print(mystr[1:7:2])

mylist = [1,2,3,4,6,7,8]
print(mylist[-6:-1:2])

mytuple = (1,2,3,4,5,6,7)
print(mytuple[-4:-1:2])

print(mystr[::])
print(mystr[::-1])
print(mystr[::1])
print(list(range(5, -1, -1)))

# list kopyalama

# Çoğu dilde, primitive ve reference type ayrımı vardır. Primitive
# hafızada obje olarak tutulmayan, bir classtan türetilmemiş
# türlere denir.

# In Python, all values are objects. That means all the types
# are reference types. Objeler değişkenlere atandığında aslında
# değişkene bir pointer(objeye işaret eden) atanır. 
# Yalnız, bu davranış aşağıdaki basit türler için geçerli değildir: 

# Numeric 
# String 
# Boolean
# Null and None

# Yukarıdaki türler hariç diğer türleri bir değişkene koyduğunuzda
# aslında değişkene bu objelerin bir pointerı koyulur.

#################################################

#...

#################################################

# copy() metodu ile kopyalama
mylist = thislist.copy()
print(mylist)
# list() metodu ile kopyalama
mylist2 = list(thislist)
print(mylist2)
# slicing ile kopyalama
mylist3 = thislist[:]
print(mylist3)

# join lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

# + operatörü kullanarak
list3 = list1 + list2
print(list3)

# döngü ve append() kullanarak
for x in list2:
  list1.append(x)

# extend() kullanarak
list1.extend(list2)