def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

test_number = int(input())
for i in range(test_number):
    num1,num2= map(int,input().split())
    y=[num1,num2]

    y.sort()
    
    print(y[0]*y[1]//gcd(y[1], y[0]))
        