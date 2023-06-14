
strs = ["flower","flow","flo","fl"]

min = len(strs[0])
min_index = 0


for index,i in enumerate(strs):
    # print(type(len(i)),type(min))
    if len(i) < min:
        min = len(i) 
        min_index = index

print(min_index)

for i in range(min_index):
    
    
