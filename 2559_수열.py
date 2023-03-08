N, k =map(int,input().split())
arr=list(map(int,input().split()))

maxList= []
maxList.append(sum(arr[:k]))


for j in range(N-1):
    if j + k -1 < N-1:
        maxList.append(maxList[j]-arr[j]+arr[j+k])


print(max(maxList))