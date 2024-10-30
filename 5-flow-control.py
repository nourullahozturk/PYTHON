# Akış kontrolü yapıları:
# seçim yapıları (if else)
# döngüler (for, while)

# seçim yapısı (if else)
# Sytnax:
# if [şart]:
# --[if bloğu]
# elif [şart]:
# --[elif bloğu 1]
# elif [şart]:
# --[elif bloğu 2]
# ...
# else:
# --[else bloğu]

number = 1
if number == 1:
  print("number is 1")
elif number == 2:
  print("number is 2")
elif number == 3:
  print("number is 3")
else:
  print("number is something else")

# döngüler (for-in, while)

# for [değişken] in [dönülebilir nesne]:
# --[for bloğu]
for x in [1, 2, 3, 4]:
  print(x)

# while [şart]:
# --[while bloğu]

while number <= 10:
  print(number)
  number += 1
  # number = number + 1
print(number)

