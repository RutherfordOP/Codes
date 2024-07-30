L = [2,7,4,1,3,6]
def sum_ten(x,y):
    if x + y == 10:
        return 1
    else:
        return 0

i = 0
j = 0
count = 0
for i in range (0, len(L)):
    for j in range(0, len(L)):
        if sum_ten(L[i],L[j]) == 1:
            count += 1
        else:
            continue 

print("The number of elements with sum as 10 is:", count)