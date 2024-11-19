# 8-a8.py
"""Simple exception handling example."""
while True:
    try:
        number1 = int(input("Enter numerator: "))
        number2 = int(input("Enter denomenator: "))
        result = number1 / number2
    except ValueError:
        print("You must enter two integers")
    except ZeroDivisionError:
        print("Attempted to divide by zero")
    else:
        print(f"{number1:.3f} / {number2:.3f} = {result:.3f}")
        break