# 11-conways.py
"""Conway's Game of Life"""

# İki boyutlu bir tabloda canlı hücrelerin hareketlerini/yaşamlarını
# simüle eden bir program yazınız.
# tablomuzu oluşturmak için liste listesi kullanın.
# "#" canlı hücreleri, " " ise ölü hücreleri temsil etsin.
# başlangıçta tabloya rastgele yaşayan veya ölü hücre yerleştirin.
# örnek:
# [
#   ["#", " ", " ", "#", " "]
#   ["#", " ", "#", "#", " "]
#   [" ", "#", " ", "#", " "]
#   ["#", " ", "#", " ", "#"]
#   [" ", "#", "#", " ", "#"]
# ]
# Daha sonra bir oyun döngüsü içerisinde
# önce mevcut tabloyu yazdırın
# sonra oyun kurallarına göre yeni tabloyu oluşturun
#
# oyun kuralları:
# --> 2 veya 3 tane komşusu olan yaşayan hücreler hayatta kalır.
# komşu derken hücrenin etrafındaki(sol-üst, üst, sağ-üst, sağ, sağ-alt, alt, sol-alt, sol)
# yaşayan hücreler kastedilmektedir.
# örneğin aşağıdaki hücrenin(ortadaki) komşu sayısı 2 dir:
# [" ", " ", "#",
#  " ", "#", " ",
#  " ", "#", " "]
# --> 3 komşusu olan ölü hücreler canlanır. Yukarıdaki tablonun sonraki aşaması:
# [" ", " ", " ",
#  " ", "#", "#",
#  " ", " ", " "]
# --> Diğer hepsi ölür veya ölü kalmaya devam eder.
#
# Hint: Add a 1-second pause to reduce flickering (use time module)

import random, copy, time

WIDTH = 60
HEIGHT = 20

# tablo oluştur.
cells = [
 [" ", " ", "#"],
 [" ", "#", " "],
 [" ", "#", " "],
 [" ", "#", " "]
]

# Dynamically create 2D-list and fill it randomly
nextCells = []
for x in range(WIDTH):
    column = []
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append(" ")
        else:
            column.append("#")
    nextCells.append(column)

while True:
    print("-----------------------------------")
    currentCells = copy.deepcopy(nextCells)

    # Print the cells
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end="")
        print()
    
    # Calculate next cells based on the game rules
    for x in range(WIDTH):
        for y in range(HEIGHT):
            leftCoord = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT

            numNeighbours = 0
            if currentCells[leftCoord][aboveCoord] == "#":
                numNeighbours += 1
            if currentCells[x][aboveCoord] == "#":
                numNeighbours += 1
            if currentCells[rightCoord][aboveCoord] == "#":
                numNeighbours += 1
            if currentCells[rightCoord][y] == "#":
                numNeighbours += 1
            if currentCells[rightCoord][belowCoord] == "#":
                numNeighbours += 1
            if currentCells[x][belowCoord] == "#":
                numNeighbours += 1
            if currentCells[leftCoord][belowCoord] == "#":
                numNeighbours += 1
            if currentCells[leftCoord][y] == "#":
                numNeighbours += 1

            # Apply game rules
            if currentCells[x][y] == "#" and (numNeighbours == 2 or numNeighbours == 3):
                nextCells[x][y] = "#"
            elif currentCells[x][y] == " " and numNeighbours == 3:
                nextCells[x][y] = "#"
            else:
                nextCells[x][y] = " "
    
    time.sleep(0.2)

