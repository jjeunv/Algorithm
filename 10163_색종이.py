N = int(input()) #색종이의 장수 

squre = [[0 for j in range(10)] for i in range (10)]

for i in range(1, N + 1) :
    x, y, w, h = map(int,input().split())
    for j in range(y, y + h) : 
        squre[j][x:x+w] = [i] * w
     
arr = [0] * (N + 1)

for k in squre :
    for j in k :
        arr[j] += 1

for i in range(1, N+1) :
    print(arr[i])
        
