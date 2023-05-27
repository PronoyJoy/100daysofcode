age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age = int(age)
year = 365
week = 52
month = 12

days = (90*365) - (age *365)

weeks = (90*52) - (age * 52)

months = (90 *12) -(age *12)

print(f'You have {days} days, {weeks} weeks, and {months} months left.')