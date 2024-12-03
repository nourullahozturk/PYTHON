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