numArray=[]
num1, num2=map(int,input().split())
numArray.append(num1)
numArray.append(num2)


def reverse(num) :
    first = num // 100
    second = (num % 100) // 10
    third = num % 10
    revNumber = (third * 100) + (second * 10) + first
    return revNumber

for i in range(2) :
    numArray[i] = reverse(numArray[i])

if numArray[0] > numArray[1] :
    print(numArray[0]) 

else : print(numArray[1])