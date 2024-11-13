# 8-a5.py
"""Using nested control statements to analyze examination results."""

# öğrencilerin sınav sonuçlarını kullanıcıdan al. eğer 1 girerse
# geçti, 2 girerse kaldı demek olsun.
# kullanıcıdan 10 tane girdi al.
# kullanıcıdan gelen girdi 1 ise passes sayacını 1 arttır. 
# kullanıcıdan gelen girdi 2 ise failures sayacını 1 arttır. 
# sonuçları yazdır:
# Passed: geçen sayısı
# Failed: kalan sayısı
# eğer geçen kişi sayısı 8'den büyükse "Bonus to Instructor" yazdır.

passes = 0
failures = 0

# range(10) --> 0'dan 10'a kadar (10dahil değil) bir range nesnesi
# döndürür [0, 1, 2, ..., 9]
for i in range(10): # 10 defa dönen bir döngü
    result = int(input("Enter result (1=pass, 2=fail): "))
    if result == 1:
        passes += 1     # geçen sayısını 1 arttır
    if result == 2:
        failures += 1   # kalan sayısını 1 arttır

print("Passed: ", passes)
print("Failed: ", failures)