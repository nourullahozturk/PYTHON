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

# face counters
frequency1 = 0
frequency2 = 0
frequency3 = 0
frequency4 = 0
frequency5 = 0
frequency6 = 0

# 6,000,000 defa zar at
# eğer 1 ise frequency1 sayacını 1 arttır.
# eğer 2 ise frequency2 sayacını 1 arttır.
# ...
# sonucları tablo şeklinde yazdır.

# range(4) --> [0, 1, 2, 3]
for roll in range(6_000_000):
    face = random.randrange(1, 7)

    # increment appropriate counter
    if face == 1:
        frequency1 += 1
    elif face == 2:
        frequency2 += 1
    elif face == 3:
        frequency3 += 1
    elif face == 4:
        frequency4 += 1
    elif face == 5:
        frequency5 += 1
    elif face == 6:
        frequency6 += 1

print(f"Face{"Frequency":>13}")
print(f"{"1":>4}{frequency1:>13}")
print(f"{"2":>4}{frequency2:>13}")
print(f"{"3":>4}{frequency3:>13}")
print(f"{"4":>4}{frequency4:>13}")
print(f"{"5":>4}{frequency5:>13}")
print(f"{"6":>4}{frequency6:>13}")
