N = int(input())
paper = [[0 for _ in range(10)] for _ in range(10)]

for i in range(1,N +1 ) :
    x, y, width, height = map (int, input().split())
    for j in range(x, x+ width) :
        for k in range(y, y+ height) :
            paper[j][k] = i

for i in paper :
    for j in i:
        print(j, end= ' ')
    print()        

arrCount = [0] * N

for j in range(N) :
    for i in range(10) :
        number = paper[i][0:]
        arrCount[j] += number.count(j)

for i in range(N) :
    print(arrCount[i], '\n')