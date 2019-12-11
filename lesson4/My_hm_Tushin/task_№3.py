x = int(input())
def grafik(x):
    if x <= -12:
        return(-(x**2))
    if x > -12 and x < 0:
        return(x**4)
    if x >= 0:
        return(x - 2)
print(grafik(x))
