s = input()
new = ''
new += s[0].upper()

for i in range(1,len(s)):
    
    
   
    if s[i-1] == ' ':
        new = new + s[i].upper()

    else:
        new = new + s[i]
    

print(new)
