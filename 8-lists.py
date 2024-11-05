mylist = ["apple", "banana", "cherry", "carrot"]
print(len(mylist))
list1 = ["abc", 34, True]

print(range(1, 10))
print(list(range(1, 10)))

# aynı stringler gibi indexlenebilir, slice edilebilir
print(mylist[0])
print(mylist[1:3])
# içerisinde bir eleman var mı kontrol edilebilir
print("Yes, apple is in the list" if "apple" in mylist else \
      "No, apple is not in the list")

# liste elemanı değiştirme
thislist = ["apple", "banana", "cherry"]
# tek eleman değiştirme
thislist[0] = "carrot"
# çoklu eleman değiştirme
thislist[1:3] = ["watermelon"]
print(thislist)
# insert(): istediğimiz yere bir eleman yerleştirme
thislist.insert(1, "tomato")
print(thislist)
# append(): listenin sonuna eleman ekleme
thislist.append("karambola")
print(thislist)
# extend(): iki listeyi (herhangi bir dizi de olur) birleştirme
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# remove(): istediğimiz bir elemanı kaldırma
thislist.remove("carrot")
print(thislist)
# pop(): sondan bir eleman kaldırma
thislist.pop()
print(thislist)
# del keywordü ile eleman kaldırma
del thislist[0]
print(thislist)
# listeyi temizlemek için
thislist.clear()
print(thislist)
# liste silme
del thislist