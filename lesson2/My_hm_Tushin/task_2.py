a = []
n = 10
from random import randrange
n = 10
a = [randrange(1, 10) for i in range(n)]
print(a)
for i in range(0, len(a)):
    if i % 2 == 0:
        print(a[i])
