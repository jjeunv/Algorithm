N=int(input()) #사진틀의 개수
num=int(input()) #추천 개수

student=list(map(int, input().split()))
photos = [0] * N
rec = [0] * 101
time = [0] * 101

def imHere(myIndex):
    if myIndex in photos:
        return True
    else:
        return False

def blank():
    for i in range(N):
        if photos[i] == 0:
            return i
    return -1


def minRec():
    recCount = 1001
    recIndex = -1
    minTime = 1001
    for i in range(N):
        if rec[photos[i]] == recCount and time[photos[i]] < time[photos[recIndex]]:
            recIndex = i
            recCount = rec[photos[i]]
        elif rec[photos[i]] < recCount:
            recIndex = i
            recCount = rec[photos[i]]
    return recIndex


for i in range(len(student)):
    if imHere(student[i]):
        time[student[i]] = i
        rec[student[i]] += 1
    elif blank() != -1:
        time[student[i]] = i
        rec[student[i]] = 1
        photos[blank()] = student[i]
    else:
        idx = minRec()
        time[photos[idx]] = 1001
        rec[photos[idx]] = 0
        time[student[i]] = i
        rec[student[i]] = 1
        photos[idx] = student[i]

    

photos.sort()
for student in photos:
    if student != 0:
        print(student,end=" ")

