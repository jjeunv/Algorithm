N, k =map(int,input().split())
arr=list(map(int,input().split()))

maximum = int(-10000000000000000000)
index =int(0)

for j in range(N-1):
    sum = int(0)
    index =j
    if j + k -1 <= N-1:
        
        for i in range(k) :
            sum = sum + arr[index]
            index +=1
        if sum>maximum :
            maximum = sum


print(maximum)