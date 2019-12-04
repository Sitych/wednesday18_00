a = int(input())
b = int(input())
n = 10
from random import randrange
c = [randrange(a, b+1) for i in range(n)]
print(c)
