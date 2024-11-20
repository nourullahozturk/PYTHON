# 8-a7.py
"""Roll a six-sided die 6,000,000 times."""
import random

# her bir zar yüzü için bir sayaç oluştur
# 6 milyon kere zar at. her seferinde sonuca göre
# ilgili sayacı arttır. Aşağıdaki tabloyu 
# kendi sayac değerlerinizle yazdırın:

# Face    Frequency
#    1       100000
#    2       100000
#    3       100000
#    4       100000
#    5       100000
#    6       100000

frequecy1 = 0
frequecy2 = 0
frequecy3 = 0
frequecy4 = 0
frequecy5 = 0
frequecy6 = 0

for roll in range(6_000_000):
    face = random.randint(1, 6)

    if face == 1:
        frequecy1 +=1
    if face == 2:
        frequecy2 += 1
    if face == 3:
        frequecy3 += 1
    if face == 4:
        frequecy4 += 1
    if face == 5:
        frequecy5 += 1
    if face == 6:
        frequecy6 += 1

print(f"Face{"Frequency":>13}")
print(f"{"1":>4}{frequecy1:>13}")
print(f"{"2":>4}{frequecy2:>13}")
print(f"{"3":>4}{frequecy3:>13}")
print(f"{"4":>4}{frequecy4:>13}")
print(f"{"5":>4}{frequecy5:>13}")
print(f"{"6":>4}{frequecy6:>13}")