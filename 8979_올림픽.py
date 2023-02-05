N, K = map(int, input().split())
arr=[]
for i in range(N):
    arr.append(list(map(int,input().split())))
    arr=sorted(arr, key=lambda x: (-x[1], -x[2], -x[3]))

for i in range(N):
    if arr[i][0] == K:

        nation = i

for i in range(N):
    if arr[nation][1:] == arr[i][1:]:
        print(i+1)
        break




 

