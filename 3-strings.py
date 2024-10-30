# strings
# string bir dizidir
# dizi birden çok elemanı olan veri kümesine verilen genel addır.
# dizi örnekleri: string, list, tuple, range, ...
# dizi indexlenebilir, dönülebilir, içerisinde bir elemanın varlığı sorgulanabilir, ...

# string indexleme
a = "Hello, World!"
print(a[5])   # indexler her zaman 0'dan başlar

# looping through a string (string dönme)
for harf in a:
  print(harf)

# string uzunluğu
print(len(a))

# check string
txt = "Hepimiz birimiz, birimiz hepimiz için"
print("birimiz" in txt)
print("birimiz" not in txt)

if "birimiz" in txt:
  print('string "birimiz" txt içerisinde var')

# slicing strings
print(a[2:5])   # başlangıç indisi dahil, bitiş indisi dahil değil
print(a[2:])
print(a[:5])

# string methods
a = "Hello, World!"
# a = a.upper()
print(a.upper())
print(a.lower())
print(a.replace("H", "J"))
print(a.replace("o", "J"))
print(a.split(","))
a = "    Hello,    World!      "
print(a.strip())
print(a.lstrip())
print(a.rstrip())
# bu methodlar orijinal nesneyi değiştirmez

