# 8-a5.py
"""Using nested control statements to analyze examination results."""

# öğrencilerin sınav sonuçlarını kullanıcıdan al (10 tane). eğer 1 girerse
# geçti, 2 girerse kaldı demek olsun.
# kullanıcıdan gelen girdi 1 ise passes sayacını 1 arttır. 
# kullanıcıdan gelen girdi 2 ise failures sayacını 1 arttır. 
# sonuçları yazdır:
# Passed: geçen sayısı
# Failed: kalan sayısı
# eğer geçen kişi sayısı 8'den büyükse "Bonus to Instructor" yazdır.

passes = 0
failures = 0

# range(10) --> [0, 1, 2, ..., 9]
for i in range(10):
    result = int(input("Enter result (1=pass, 2=fail): "))
    if result == 1:
        passes += 1
        # passes = passes + 1
    if result == 2:
        failures += 1
print("Passed: ", passes)
print("Failed: ", failures)