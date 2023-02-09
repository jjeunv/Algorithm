A = int(input())
B = int(input())
C = int(input())

countArray = [0]*10

number = A * B * C

numLength = len(str(number))

a = 10 ** (numLength - 1)
countArray[number // a] += 1

for i in range(numLength - 1) :
   
    countArray[(number % a) // (a // 10)] += 1
    number = number % a
    a = a // 10

for i in countArray :
    print(i)


