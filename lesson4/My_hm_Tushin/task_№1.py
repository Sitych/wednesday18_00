x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
def distance(x1, y1, x2, y2):
    return (((x2-x1)**2 + (y2-y1)**2)**0.5)
print(distance(x1, y1, x2, y2))
