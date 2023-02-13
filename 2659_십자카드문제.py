N = list(map(int,input().split()))
num1 = N[0]*1000 + N[1]*100 + N[2]*10 + N[3]
num2 = N[1]*1000 + N[2]*100 + N[3]*10 + N[0]
num3 = N[2]*1000 + N[3]*100 + N[0]*10 + N[1]
num4 = N[3]*1000 + N[0]*100 + N[1]*10 + N[2]
num = min(num1,num2,num3,num4)

def circle(num) :
    N = []
    N.append(num // 1000) 
    N.append((num % 1000) // 100) 
    N.append(((num % 1000) % 100) // 10) 
    N.append(((num % 1000) % 100) % 10) 

    num1 = N[0]*1000 + N[1]*100 + N[2]*10 + N[3]
    num2 = N[1]*1000 + N[2]*100 + N[3]*10 + N[0]
    num3 = N[2]*1000 + N[3]*100 + N[0]*10 + N[1]
    num4 = N[3]*1000 + N[0]*100 + N[1]*10 + N[2]
    number = min(num1,num2,num3,num4)

    
    if num == number :
        return True
    else : return False


count = 1
compare = 1111

for i in range(10000) :
    
    if ((compare % 1000) % 100) % 10 == 0 :
        compare += 1
        continue
    
    elif ((compare % 1000) % 100) // 10 == 0 :
        compare += 10
        continue

    elif ((compare % 1000) // 100) == 0 :
        compare += 100
        continue

    elif (compare // 1000) == 0 :
        compare += 1000
        continue

    if circle(compare) :
        if compare == num :
            print(count)
            break
        else :
            count += 1
            compare += 1
            print(compare, count)
    
    else :
        compare += 1
