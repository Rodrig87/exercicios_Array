a = [2, 5, 4, 2, 8, 5, 2]
b = [0, 0, 0, 0, 0, 0, 0]

for x in range(7):
    b[6-x] = a[x]
print(b)
