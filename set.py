# Set
buah = {"apel", "pisang", "mangga"}
print(buah) # output = {"apel", "pisang", "mangga"}

angka_duplikat = {1, 1, 2, 5, 3, 5}
print(angka_duplikat) # output = {1, 2, 3, 5}

# Access set items
print("Anggur" in buah)
print("Anggur" not in buah)

# Add set items
huruf = {"a", "b", "c", "d"}
angka = {1, 2, 3, 4}
huruf.add("e")
huruf.update(angka) # add items from variable in the argument
print(huruf)

# Remove set items
huruf1 = {"a", "b", "c", "d"}
huruf1.remove("a")
huruf1.discard("b")
print(huruf1)

# Loop set
for x in huruf:
     print(x)

# Join set
#The union() and update() methods joins all items from both sets.
set1 = {1, 2, 3, 4}
set2 = {"a", "b", "c"}
set3 = set1.union(set2) # or using set1 | set2
print(set3)

#The intersection() method keeps ONLY the duplicates.
setIntersection1 = {1, 2, 3, 4}
setIntersection2 = {"a", "b", "c", 4}
setIntersection3 = setIntersection1.intersection(setIntersection2) # or using setIntersection1 & setDifference2
print(setIntersection3) # output = {4}

#The difference() method keeps the items from the first set that are not in the other set(s).
setDifference1 = {"Pisang", "Pepaya", "Apple"}
setDifference2 = {"Google", "Yahho", "Bing", "Apple"}
setIntersection3 = setDifference1.difference(setDifference2) # or using setDifference1 - setDifference2
print(setIntersection3)

#The symmetric_difference() method keeps all items EXCEPT the duplicates.
setSymmetricDiffrerence1 = {"Apple", "Banana", "Cherry"}
setSymmetricDiffrerence2 = {"Google", "Apple", "Yahho", "DuckDuckGo"}
setSymmetricDiffrerence3 = setSymmetricDiffrerence1.symmetric_difference(setSymmetricDiffrerence2) # or using setSymmetricDiffrerence1 ^ setSymmetricDiffrerence2
print(setSymmetricDiffrerence3)
