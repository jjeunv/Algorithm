N=int(input()) #사진틀의 개수
num=int(input()) #추천 개수

prelist=[0]*N
rec=[1001]*N
time=[1001]*N
student=list(map(int, input().split()))
t=0


def time_compare():
    timemin = min(time)

    for i in range(N-1):
        if time[i] == timemin:
            return i
   
    return -1
            

            

def blank(idx):
    for i in range(N-1):
        if prelist[i] == 0 or prelist[i] == idx:
            return i
    return -1

def rec_compare():
    minVlaue = min(rec)
    for i in range(N-1):




for i in range(len(student)):
    if not student[i] in prelist:
        index = blank()
        if index != -1:
            prelist[index]=student[i]
            rec[index] += 1
            t+=1
            time[index] = t
        else :
            
            prelist[time_compare()]=student[i]
            t+=1
            time[time_compare()]=t

    else:
        time[prelist.index(student[i])]+=1

prelist.sort()
print(prelist)
        




