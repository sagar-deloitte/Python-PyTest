list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
finalList = []
for i in range(2):
    for j in range(2):
        element = list1[i] + list2[j]
        finalList.append(element)
print(finalList)
