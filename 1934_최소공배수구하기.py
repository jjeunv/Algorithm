test_number = int(input())
for i in range(test_number):
    num1,num2= map(int,input().split())
    y=[num1,num2]

    y.sort()
    
    for i in range(1,y[0] + 1):
        if (y[1]*i)%y[0]==0:
            print(y[1]*i)
            break
        