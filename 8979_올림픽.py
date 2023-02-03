N, K = map(int, input().split())
arr=[]
for i in range(N):
    arr.append(list(map(int,input().split())))
    arr=sorted(arr, key=lambda x: (-x[1], -x[2], -x[3]))

for i in range(N):
    if arr[i][0] == K:
        nation = i

count=0
for i in range(N):
    if arr[nation][1:] == arr[i][1:]:
        count+=1

print(nation+1-count+1)



                
        


        
 
for i in arr:
    for j in i:
        print(j, end=" ")
    print()


