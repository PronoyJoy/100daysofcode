# sourcery skip: avoid-builtin-shadow
import random
array = list(map(int,input().split()))
print(array)

#selection sort works in index
min = 0
for i in range(len(array)-1):
    min = i

    for j in range(i+1,len(array)):

        if array[j] < array[i] :
            min = j 
            if i !=j :
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
print(array)