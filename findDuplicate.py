que = [[1, 1, 3, 2], [9, 8, 8, 1], [0, 4, 5, 0, 0, 1, 4]]

for i in que:
    y = []
    for j in i:
        if i.count(j) > 1:
            if j not in y:
                print(j, " -> ", i.count(j))
                y.append(j)
