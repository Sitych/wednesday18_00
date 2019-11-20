x1 = 0
x2 = 1
x3 = 0
while x3 < 1000:
    x3 = x2 + x1
    x1= x2
    x2 = x3
print(x3)
