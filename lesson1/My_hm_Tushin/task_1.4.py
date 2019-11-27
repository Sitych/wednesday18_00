x0 = 1
x1 = 1
i = 0
s = 0
while s < 1000:
    s = x0 + x1
    x0 = x1
    x1 = s
    i = i + 1
print(x1)
