# Programlama, bilgisayarın icra(execute) edebilmesi için, 
# problemlerin çözümünü bilgisayara açıklama sanatıdır.

import math

PI = math.pi
r = float(input("r: "))
alan = PI * r ** 2

print(alan)

for r in range(1, 101):
    alan = PI * r ** 2
    print("r: " + str(r) + " alan: " + str(alan))

# Aslında bir programın yaptığı tek şey girdi almak ve çıktı üretmektir

# Program, girdileri içerisinde tutabilmek için veri yapılarına ihtiyaç
# duyacaktır.

# Program yazmak için gereken yapılar:
# data structures (veri yapıları: string, int, bool, ...)
# arithmetic and comparison operators (aritmetik ve karşılaştırma operatörleri)
# selection (seçim yapısı: if else)
# iteration (döngüler: for, while)
# text and numeric input and output (text ve numerik girdi ve çıktılar)
# organize your code with functions (fonksiyonlar)