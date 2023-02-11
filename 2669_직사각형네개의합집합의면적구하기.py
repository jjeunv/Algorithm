array = [[0 for j in range(100)] for i in range(100)]

for i in range(4):
    num1,num2,num3,num4 = map(int, input().split())
    num2 = 99-num2 
    num4 = 99-num4   
    for j in range(num1, num3) :
        for k in range(num4+1, num2+1):
            array[k][j] = 1

count = 0

for i in array :
    for j in i :
        if j == 1 :
            count += 1
    

print(count)