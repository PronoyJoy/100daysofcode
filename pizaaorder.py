S = 15

M = 20

L=  25

P_Small = 2

P_Medium_large = 3

cheese = 1

payment = 0

size = input('Welcome to pizza deliveries! \n What Size Pizza Do You want ? : S, M or L ')

if size == 'S':
    payment += 15

elif size == 'M':
    payment += 20

elif size == 'L':
    payment += 25

else:
    print('enter correct !')


pep = input('Do You want Pepporoni? Y or N ')

if pep == 'Y' and size == 'S':
    payment += 2
elif pep == 'Y' and size in ['M', 'L']:
    payment += 3
else:
    print('no pepporoni')

cheese = input('Do you want cheese? Y or N ')

if cheese == 'Y':
    payment += 1

print('total payment:$',payment)

