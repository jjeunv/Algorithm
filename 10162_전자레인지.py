T = int(input())
A, B, C = 300, 60, 10
aCount, bCount, cCount = 0, 0, 0

aCount = T // A
bCount = (T % A) // B
cCount = ((T % A) % B) // C

if ((T % A) % B) % C == 0 :
    print(aCount, bCount, cCount)

else :
    print(-1)

