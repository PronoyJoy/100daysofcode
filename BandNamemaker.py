print('Welcome to the calcu1ator.')
bill = float(input('What was the total bill? /$'))
people = int(input('How many people to split the bill? '))
tip = float(input('What percentage you would you like to give? 10, 12, or 15?'))

pay = (bill/people)

total = pay+tip

print('each person should pay: $',total)
