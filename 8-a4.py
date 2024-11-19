# 8-a4.py
"""Class average program for abritrary number of grades."""

# Kullanıcıdan girdi al.
# Girdi -1 den farklı oldu sürece
# girdileri topla
# Eğer -1 ise döngüyü sonlandır
# ortalamayı hesapla ve yazdır

total = 0
grade_counter = 0
grade = int(input("Enter grade, -1 to end: "))

while grade != -1:
    total += grade
    grade_counter += 1
    grade = int(input("Enter grade, -1 to end: "))

if grade_counter != 0:  # ilk girdi -1 olduğu durumda
    print(total / grade_counter)