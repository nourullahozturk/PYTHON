# 9-collections.py
"""
Python Collections (Arrays)

There are four collection data types in the Python programming language:

  - List is a collection which is ordered and changeable. Allows duplicate members.
  - Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
  - Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
  - Dictionary is a collection which is ordered** and changeable. No duplicate members.

*Set items are unchangeable, but you can remove and/or add items whenever you like.
**As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

Ordered dediğimiz, yani diziye bir eleman eklenirse sona ekleniyor. elemanların bir sırası var yani. Elemanlara
sıra numarası(index) ile erişilebiliyor.
Sadece Setler unordered'dır. Elemanların hangi sırada olacağından emin olamazsınız. Setleri, matematikteki
kümelerin bilgisayardaki karşılığı olarak düşünebilirsiniz.
Setlerin elemanlarına index numarası ile ulaşamazsınız, örn. mySet[0] işe yaramaz. Elemanların bir sırası yok çünkü.
"""

# Lists
# Veri tutmak ve manipüle etmek için kullanırız. 
data = [23, 45, 12, 67, 34]
data.append(89)  # Add an item
data.remove(45)  # Remove an item

# List Comprehesion
# Mevcut bir listenin elemanlarından yeni bir liste oluşturmak için
# kullanırız. Daha kısa bir yazım sağlar. Bunu kullanmazsak döngü ve
# if else kullanarak da aynı şeyi yapabiliriz.

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
print(fruits)

# list comprehension kullanmadan:
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)

# list comprehension kullanarak:
newlist = [x for x in fruits if "a" in x]
print(newlist)

# içerisinde a olan elemanları al yeni bir listeye koy
# bu elemanlardan içerisinde n olan varsa sonuna ! koy
newlist = [x+"!" if "n" in x else x for x in fruits if "a" in x]

# içerisinde a olan elemanları al yeni bir listeye koy bu elemanlardan
# içerisinde n olan varsa sonuna ! koy, içinde g olan varsa sonuna ? koy
for x in fruits:
  if "a" in x:
    if "n" in x:
      newlist.append(x+"!")
    else:
      if "g" in x:
        newlist.append(x+"?")
      else:
        newlist.append(x)

newlist = [x+"!" if "n" in x else x+"?" if "g" in x else x for x in fruits if "a" in x]


#################################################

# Reference Types

# In Python, all values are objects. That means all the types
# are reference types.

# Python'da bütün değerler bir objedir.
# list, number, string, bool vs hepsi birer objedir. Örnek objeler:
# [1,2,3], 5, "hello", true, {"id": 123}, (4, 5)
# objeler değişkenlere atandığında objenin kendisi
# değişkene atanmaz. O objenin adresine işaret eden bir pointer değişkene atanır.
# değişkeni kullanmak istediğimizde python, adresteki değeri döndürür.

# Örneğin:
#################################################
thislist = [1, 2, 3, 4]
print(hex(id(thislist)), thislist)

list2 = thislist # güya kopyaladık

list2.append(5)
print("list2:", hex(id(list2)) , list2)
print("thislist:", hex(id(thislist)), thislist)

#################################################

# Aşağıdaki basit türlerde de aynı durum geçerlidir.

# Numeric 
# String 
# Boolean
# Null and None

x = 5
print("x:", hex(id(x)), x)
y = x
print("y:", hex(id(y)), y)
y += 1
print("y:", hex(id(y)), y)
print("x:", hex(id(x)), x)

# Basit türler haricindeki veri türlerini kopyalamak
# istediğimiz zaman dikkatli olacağız. copy() metodu veya diğer
# yöntemleri kullanacağız.

# liste kopyalama

mylist = thislist.copy()
mylist = list(thislist)
mylist = thislist[:]
mylist = [x for x in thislist]


###################################################################

# Dictionaries
# Diğer diziler eleman olarak tek bir değer tutarken Sözlükler anahtar:değer ikilisi
# tutar.
# JSON dosyalarındaki anahtar:değer içeren verileri program içerisinde tutmak için kullanışlıdır. 
record = {
  "id": 1,
  "name": "John Doe",
  "email": "johndoe@example.com",
  "age": 30
}
print(record["age"])
print(record["name"])
print(record["email"])
# print(record["xyz"])
record["city"] = "New York"
print(record)
record["city"] = "Los Angelos"
print(record)

# Bir dizideki elemanların sıklığını(frekansını) bulmak için idealdir.
elements = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
frequency = {}
for item in elements:
  # .get metodu: item anahtarının sözlükteki değerini al, öyle bir anahtar yoksa 0 döndür.
  frequency[item] = frequency.get(item, 0) + 1

print(frequency)
###################################################################

# Tuples
# Değiştirilemez (sabit) verileri tutmak için kullanırız.
days = ("pzt", "sal", "çar", "per", "cum", "cmt", "pzr")
# days[0] = "mon"

# Ayrıca tupleları dictionary içerisinde key olarak kullanabiliriz. Liste ile bu mümkün değildir.
locations = {
  ("Paris", "France"): "Eiffel Tower",
  ("New York", "USA"): "Statue of Liberty",
  ("Marseille", "France"): "Château d'If",
  ("Valon Brabant", "Belgium"): "Waterloo",
  ("Brugelette", "Belgium"): "Pairi Daiza",
}

print(locations[("Paris", "France")])

###################################################################

# Sets
# unique verileri gruplamak için kullanırız. sıra önemli değildir.
student_id = {112, 114, 116, 118, 115}
# print(student_id[0])

vowel_letters = {"a", "e", "o", "u", "i"}
vowelCount = 0
for letter in "jonas":
  if letter in vowel_letters:
    vowelCount += 1

# Setleri bir listedeki duplikasyonları kaldırmak için kullanabiliriz
my_list = [1, 2, 2, 3, 4, 4, 5]
my_set = set(my_list)
my_list = list(my_set)
print(my_list)

# Setler üzerinde birleşim, kesişim, fark işlemleri uygulayabiliriz.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

new_set = set1.union(set2)
print(new_set)
new_set = set1.intersection(set2)
print(new_set)
new_set = set1.difference(set2)
print(new_set)

# Bir elemanın bir dizideki mevcutluğunu kontrol etmenin en verimli
# yolu Set kullanmaktır. (due to their underlying hash table implementation)
prohibited_items = {"knife", "gun", "drug"}
item = "knife"
if item in prohibited_items:
  print(f"{item} is prohibited")