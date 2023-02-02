dish=input()
dish_list=list(dish)
height=10

for i in range(1,len(dish_list)):
        if dish_list[i-1]==dish_list[i]:
            height+=5
        else : height+=10


print(height)

