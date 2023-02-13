
N = int(input()) 
arr = [] 
count = [0] * N

for i in range(N) :
    arr.append(list(map(int, input().split())))
    count[i] = [0] * N

for i in arr:
    for j in i :
        print(j, end=' ')
    print()

for i in range(5) :
    for j in range(N):
        for k in range(j+1 , N):
            if arr[j][i] == arr[k][i]:
                count[j][k] = 1
                count[k][j] = 1

num = []
for s in count:
    num.append(s.count(1))