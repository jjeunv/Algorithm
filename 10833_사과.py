N = int(input())
sum = 0

for i in range(N) :
    student, apple = map(int, input().split())
    sum += (apple % student)

print(sum)