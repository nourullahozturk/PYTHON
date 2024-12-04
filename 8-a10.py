# 8-a10.py
"""The Zig-Zag Game"""
# ekrana * karakterleriyle zigzag şekli yazdırın:
# ********
#  ********
#   ********
#    ********
#   ********
#  ********
# ********
#  ********
#   ********
# Program Ctrl + C ile durdurulana kadar bu şekilde yazdırmaya devam etsin.
# hard kodlama yapmayın. Başa eklenen max boşluk sayısı ve satırdaki
# yıldız miktarı kolayca değiştirilebilir olmalı. 

import time
MAX_INDENT = 20
LINE_LENGTH = 8
indent = 0
indentIncreasing = True
try:
    while True:
        print(" " * indent, end="")
        print("*" * LINE_LENGTH)
        time.sleep(0.5)
        if indentIncreasing:
            indent = indent + 1
            if indent == MAX_INDENT:
                indentIncreasing = False
        else:
            indent = indent - 1
            if indent == 0:
                indentIncreasing = True
except KeyboardInterrupt:
    print("Thanks for playing!")

