# This program counts vowels of your name

# 1. kullanıcıdan isim ve soyisim girmelerini iste
print("What's your name? e.g. John Doe")
myName = input()
firstname, lastname = myName.split(" ")
# 2. kullanıcıdan isim, soyisim al ve baş harflerini yazdır
print("Nice to meet you " + firstname[0].upper() + "." + lastname[0].upper())
# 3. kullanıcının ismindeki sesli harf sayısını yazdır
vowels = "aeuüıioöAEUÜIİOÖ"
vowelCount = 0
for letter in myName:
  if letter in vowels:
    vowelCount += 1
print(f"Your name has {vowelCount} vowels")
