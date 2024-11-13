# 8-a3.py
"""Class average program for fixed number of grades"""
# grades: 98, 76, 71, 87, 83, 90, 57, 79, 82, 94

grades = [98, 76, 71, 87, 83, 90, 57, 79, 82, 94]

total = 0

for grade in grades:
    total += grade

print("Average is", total / len(grades))