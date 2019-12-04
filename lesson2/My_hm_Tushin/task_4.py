mec = int(input())
day = int(input())
if mec >= 13:
    print('error')
    
if mec == 12 and day <= 31:
    print(365 - 6 * 31 - 4 * 30 - 28 - day)

if mec == 11 and day <= 30:
    print(365 - 6 * 31 - 3 * 30 - 28 - day)

if mec == 10 and day <= 31:
    print(365 - 5 * 31 - 3 * 30 - 28 - day)

if mec == 9 and day <= 30:
    print(365 - 5 * 31 - 2 * 30 - 28 - day)

if mec == 8 and day <= 31:
    print(365 - 4 * 31 - 2 * 30 - 28 - day)
    
if mec == 7 and day <= 31:
    print(365 - 3 * 31 - 2 * 30 - 28 - day)
    
if mec == 6 and day <= 30:
    print(365 - 3 * 31 - 1 * 30 - 28 - day)
    
if mec == 5 and day <= 31:
    print(365 - 2 * 31 - 1 * 30 - 28 - day)
    
if mec == 4 and day <= 30:
    print(365 - 2 * 31 - 0 * 30 - 28 - day)
    
if mec == 3 and day <= 31:
    print(365 - 1 * 31 - 0 * 30 - 28 - day)

if mec == 2 and day <= 28:
    print(365 - 1 * 31 - 0 * 30 - day)
    
if mec == 1 and day <= 31:
    print(365 - day)
    

    

    

