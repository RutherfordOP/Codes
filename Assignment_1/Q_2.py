def list_checker(L):
    if len(L) < 3:
        return 1
    else:
        return 0

def rang_calci(L):
    max = L[0]
    i = 0
    for i in range(1,len(L)):
        if L[i] > max:
            max = L[i]
        else:
            continue 
    min = L[0]
    for j in range(1,len(L)):
        if L[j] < min:
            min = L[j]
        else:
            continue
    rang = max-min
    return rang

#__main__
L = []
k = 0
size = int(input("Enter the number of elements you want in the list: "))
for k in range (0,size):
    t = int(input("Enter the element: "))
    L.append(t)
if list_checker(L) == 1:
    print("Elements less than 3.Bye")
    exit 
else:
    ans = rang_calci(L)
    print("The range is: ",ans)