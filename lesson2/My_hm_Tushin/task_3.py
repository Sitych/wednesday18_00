a = [] 
n = int(input())  
for i in range(n):  
    new_element = int(input()) 
    a.append(new_element)  
print(a)
for i in range(0,n):
    if i == 0:
        b = a[i+1] + a[n-1]
    if i >= 1 and i <= n-2:
        b = a[i-1] + a[i+1]
    if i == n-1:
        b = a[i-1] + a[0]
    print(b)
