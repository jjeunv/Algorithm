N =int(input())

array = []
count = 0

num1, num2, num3 = 0, 0, 0

for i in range(1, N) :
    num1 = i
    for j in range(1, N-i) :
        if N - num1 > 0 :
            num2 = j
        for k in range(1, N-j) :
            if num1+num2+k == N :
                num3 =k
                arr = []
                arr.append(num1)
                arr.append(num2)
                arr.append(num3)
                arr.sort()
                if arr[2] < (arr[0] +arr[1]) :
                    arr = tuple(arr)
                    array.append(arr)

array.sort()
array =set(array)


           
print(len(array))
           
                



        

