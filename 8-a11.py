# 8-a11.py
"""A Rock, Paper, Scissors Game"""

# x Wins, y Losses, z Ties şeklinde skorları yazdır.
# kullanıcıdan bir hamle yapmasını iste yani bunu yazdır:
# 'Enter your move: (r)ock (p)aper (s)cissors or (q)uit'
# Kullanıcı r, p, s, veya q haricinde bir girdi girerse:
# 'Type one of r, p, s, or q.'
# şeklinde hata mesajı göster ve tekrar hamle iste.
# kullanıcı q girerse programdan çıkış yap.
# kullanıcı r, p, veya s girerse:
# Kullanıcının seçtiği hamleyi ekrana yazdır:
# 'ROCK versus...'
# veya
# 'PAPER versus...'
# veya
# 'SCISSORS versus...'
# ve daha sonra
# bilgisayara hamle yaptır (rastgele r,p, s den birini seç)
# Bilgisayarın yaptığı hamleyi yazdır:
# ROCK
# veya
# PAPER
# veya
# SCISSORS

# sonucu hesapla
# sonucu göster (win/loss/tie) ve skor değişkenlerini güncelle

import sys, random

wins = 0
losses = 0
ties = 0
moves = ("r", "p", "s")
while True:   # game loop
  print(f"{wins} Wins, {losses} Losses, {ties} Ties")
  print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")

  while True:   # player input loop
    playerMove = input()
    if playerMove == "r":
      print("ROCK versus...")
      break
    elif playerMove == "p":
      print("PAPER versus...")
      break
    elif playerMove == "s":
      print("SCISSORS versus...")
      break
    elif playerMove == "q":
      print("Goodbye!")
      sys.exit()
    else:
      print("Type one of r, p, s, or q.")
  
  # Bilgisayarın hamlesini ekrana yazdır
  computerMove = random.choice(moves)
  if computerMove == "r":
    print("ROCK")
  if computerMove == "p":
    print("PAPER")
  if computerMove == "s":
    print("SCISSORS")
  
  # Sonucu ekrana yazdır ve skorları güncelle
  if playerMove == computerMove:
    print("It's Tie!")
    ties += 1
  elif (playerMove == "r" and computerMove == "s") or \
       (playerMove == "p" and computerMove == "r") or \
       (playerMove == "s" and computerMove == "p"):
    print("You win!")
    wins += 1
  else:
    print("You lose!")
    losses += 1