# 8-a8.py
"""Simple exception handling example."""
while True:
    try:    # bu bloğu çalıştırmayı dene
        number1 = int(input("Enter numerator: "))
        number2 = int(input("Enter denominator: "))
        result = number1 / number2      
    except ZeroDivisionError: # ZeroDivisionError hatası çıkarsa
        print("Attempted to divide by zero")
    except ValueError:  # ValueError hatası çıkarsa
        print("You must enter two integers")
    else:   # hata çıkmazsa
        print(f"{number1:.3f} / {number2:.3f} = {result:.3f}")
        break