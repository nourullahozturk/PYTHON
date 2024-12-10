# 10-a1.py
"""Collections Egzersiz 1: Reverse each word of a string"""

# verilen stringdeki kelimeleri tersine çevirin
# örneğin "My Name is Jessa" stringi için
# cevap "yM emaN si asseJ" olmalı.

str1 = "My Name is Jessa"

words = str1.split(" ")

reversed_words = [word[::-1] for word in words]
print(reversed_words)

reversed_str1 = " ".join(reversed_words)
print(reversed_str1)

# 3 parametreli slicing
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(mylist[2:8:2])  # 3.parametre adım sayısı