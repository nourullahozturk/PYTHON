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

# list comprehension kullanmadan:


# list comprehension kullanarak:


# içerisinde a olan elemanları al yeni bir listeye koy
# bu elemanlardan içerisinde n olan varsa sonuna ! koy


# içerisinde a olan elemanları al yeni bir listeye koy bu elemanlardan
# içerisinde n olan varsa sonuna ! koy, içinde g olan varsa sonuna ? koy


# newlist'in her bir elemanı için;
# eğer elemanın sonunda "!" karakteri varsa bu karakteri kaldır.
# eğer elemanın sonunda "!" karakteri yoksa sonuna "?" ekle.
# mevcut listeyi güncelle.


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



#################################################

# Aşağıdaki basit türlerde de aynı durum geçerlidir.

# Numeric 
# String 
# Boolean
# Null and None



###################################################################

# Dictionaries
# Diğer diziler eleman olarak tek bir değer tutarken Sözlükler anahtar:değer ikilisi
# tutar.
# JSON dosyalarındaki anahtar:değer içeren verileri program içerisinde tutmak için kullanışlıdır. 


# Bir dizideki elemanların sıklığını(frekansını) bulmak için idealdir.
elements = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']


###################################################################

# Tuples
# Değiştirilemez (sabit) verileri tutmak için kullanırız.


# Ayrıca tupleları dictionary içerisinde key olarak kullanabiliriz. Liste ile bu mümkün değildir.
locations = {
  ("Paris", "France"): "Eiffel Tower",
  ("New York", "USA"): "Statue of Liberty",
  ("Marseille", "France"): "Château d'If",
  ("Valon Brabant", "Belgium"): "Waterloo",
  ("Brugelette", "Belgium"): "Pairi Daiza",
}

###################################################################

# Sets
# unique verileri gruplamak için kullanırız. sıra önemli değildir.


# Setleri bir listedeki duplikasyonları kaldırmak için kullanabiliriz


# Setler üzerinde birleşim, kesişim, fark işlemleri uygulayabiliriz.


# Bir elemanın bir dizideki mevcutluğunu kontrol etmenin en verimli
# yolu Set kullanmaktır. (due to their underlying hash table implementation)