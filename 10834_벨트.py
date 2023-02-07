M = int(input()) # 벨트의 개수
direction = 0 # 바퀴의 회전 방향
rpm = 0 # 분당 회전수

dirArray = [0, 1] * 501
index = 0

first, second, belt = map(int,input().split())

if belt == 0 :
        direction = dirArray[index]
else :
        direction = dirArray[index+1]
        index+=1


for i in range(M-1) :
    a, b, c = map(int, input().split())
    if a == second :
        rpm = b
        first = a 
        second = b     
      
    else :
        b = b * (second // a) 
        a = second
        rpm = b
        
        first = a 
        second = b

    if c == 0 :
        direction = dirArray[index]
    else :
        direction = dirArray[index+1]
        index+=1

print (direction, rpm)

    
