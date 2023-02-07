aCard = list(map(int, input().split()))
bCard = list(map(int, input().split()))
aScore = 0
bScore = 0
lastWinner = ' '

for i in range(10) :
    if aCard[i] > bCard[i] :
        aScore += 3
        lastWinner = 'A'

    elif aCard[i] == bCard[i] :
        aScore += 1
        bScore += 1
        

    else :
        bScore += 3
        lastWinner = 'B'

print(aScore, bScore)

if aScore > bScore :
    print('A')
    
elif aScore == bScore :
    if lastWinner == ' ':
        print('D')
    else :
        print(lastWinner)

else :
    print('B')        

