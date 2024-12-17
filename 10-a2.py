# 10-a2.py
"""Collections Egzersiz 2"""

# Aşağıdaki tablodaki verileri uygun veri yapısı kullanarak
# program içerisinde tutun.
# Daha sonra tablo şeklinde ekrana yazdırın.

# Element      Symbol    Atomic Number    Melting point (K)    Boiling point (K)
# Hydrogen     H         1                14                   20
# Helium       He        2                1                    4
# Lithium      Li        3                453                  1603
# Beryllium    Be        4                1560                 2742
# Boron        B         5                2349                 4200
# Carbon       C         6                3915                 3915
# Nitrogen     N         7                63                   77

elements = [
  {
    "element": "Hydrogen",
    "symbol": "H",
    "atomic_number": 1,
    "melting_point": 14,
    "boiling_point": 20
  },
  {
    "element": "Helium",
    "symbol": "He",
    "atomic_number": 2,
    "melting_point": 1,
    "boiling_point": 4
  },
  {
    "element": "Lithium",
    "symbol": "Li",
    "atomic_number": 3,
    "melting_point": 453,
    "boiling_point": 1603
  },
  {
    "element": "Beryllium",
    "symbol": "Be",
    "atomic_number": 4,
    "melting_point": 1560,
    "boiling_point": 2742
  },
  {
    "element": "Boron",
    "symbol": "B",
    "atomic_number": 5,
    "melting_point": 2349,
    "boiling_point": 4200
  },
  {
    "element": "Carbon",
    "symbol": "C",
    "atomic_number": 6,
    "melting_point": 3915,
    "boiling_point": 3915
  },
  {
    "element": "Nitrogen",
    "symbol": "N",
    "atomic_number": 7,
    "melting_point": 63,
    "boiling_point": 77
  },
]
# Element      Symbol    Atomic Number    Melting point (K)    Boiling point (K)
print(f"{"Element":<13}{"Symbol":<10}{"Atomic Number":<17}{"Melting point (K)":<21}{"Boiling point (K)":<17}")
for el in elements:
  print(f"{el["element"]:<13}{el["symbol"]:<10}{el["atomic_number"]:<17}{el["melting_point"]:<21}{el["boiling_point"]:<17}")
