print('Welcome to the calcu1ator.')
bill = float(input('What was the total bill? /$'))
people = int(input('How many people to split the bill? '))
tip = int(input('What percentage you would you like to give? 10, 12, or 15?'))



tip = bill * (tip/100)

bill += tip

total = bill /people

print('each person should pay: $',round(total,2)),
