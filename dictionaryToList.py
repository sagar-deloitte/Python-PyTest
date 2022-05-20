originalList = {"HuEx": [1, 3, 4], "is": [7, 6], "best": [4, 5]}
convertedList = []
for i in originalList:
    temp = [i]
    for j in originalList[i]:
        temp.append(j)
    convertedList.append(temp)
print(convertedList)
