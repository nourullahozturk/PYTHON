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

import random, time, copy

WIDTH = 60
HEIGHT = 20

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
    print("-----------------------")
    currentCells = copy.deepcopy(nextCells)

    # tabloyu yazdır
    for y in range(HEIGHT): # 3
        for x in range(WIDTH): # 4
            print(currentCells[x][y], end="")
        print()

    # oyun kurallarına göre bir sonraki tabloyu hesapla
    for x in range(WIDTH):
        for y in range(HEIGHT):

            leftCoord = (x - 1) % WIDTH # leftCoord her zaman [0, WIDTH-1] arasında olur
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
            if currentCells[leftCoord][y] == "#":
                numNeighbours += 1
            if currentCells[rightCoord][y] == "#":
                numNeighbours += 1
            if currentCells[leftCoord][belowCoord] == "#":
                numNeighbours += 1
            if currentCells[x][belowCoord] == "#":
                numNeighbours += 1
            if currentCells[rightCoord][belowCoord] == "#":
                numNeighbours += 1
            
            # bir sonraki tabloda mevcut hücrenin yaşayıp
            # yaşamayacağına oyun kurallarına göre karar ver
            if currentCells[x][y] == "#" and (numNeighbours == 2 or numNeighbours == 3):
                nextCells[x][y] = "#"   # yaşamaya devam eder
            elif currentCells[x][y] == " " and numNeighbours == 3:
                nextCells[x][y] = "#"   # canlanır
            else:
                nextCells[x][y] = " "   # ölür, veya ölü kalmaya devam eder
    time.sleep(1)  