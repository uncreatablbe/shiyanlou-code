def is7(n):
    if(n % 7 == 0):
        return True
    for i in range(len(str(n))):
        if(str(n)[i] == '7'):
            return True

for i in range(1,101):
    if(is7(i)):
        continue
    print(i)
