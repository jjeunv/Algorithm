N = int(input()) #지방의 수
budget = list(map(int, input().split())) #예산 요청 금액
M = int(input()) #총 예산

budget.sort()

totalBudget=sum(budget) #예산 요청금액의 총 합

average = M // N # 총 예산의 평균
mod = M  % N
sum = 0
count = 0



if M >= totalBudget :
    print(budget[N-1])

elif budget[0] > average :
    print(average)

else :
    for i in range(N -1) :
        if budget[i] <= average:
            sum += average - budget[i]
            count += 1
            
    sum = sum + average * (N-count) + mod
    print(sum // (N-count))

