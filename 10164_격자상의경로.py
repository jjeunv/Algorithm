N, M, K = map(int, input().split())
road = [[0 for j in range(M)] for i in range(N)]

for j in range(M) :
    a = 1
    for i in range(N) :
        road[i][j] = a
        a += 1
        print(a)




for i in road :
    for j in i :
        print(j, end=' ')
    print()