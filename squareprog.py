import math

cases= int(input())
l1 = []
l2 = []
flag = 0

for x in range(0, cases):
    q = int(input())
    l1.append(q)
    flag = 0
    if(q < 0):
        q = -q

        for y in range(q, 1, -1):
            for z in range(q-1, 1, -1):
                w = math.pow(y, 2) - math.pow(z, 2)
                if(w == q):
                    l2.append(y)
                    l2.append(z)
                    flag = 1
                    break
            
                if(flag == 1):
                    break
            if(flag == 1):
                break
        if(flag == 0):
            l2.append(-1)
            
            
        
for x in range(0, len(l2), 2):
    if(l2[x] != -1):
        print(l2[x], end = " ")
        print(l2[x+1])
        
    elif(l2[x] == -1):
        print(l2[x])
        x = x - 1


