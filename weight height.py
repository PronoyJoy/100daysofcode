# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

BMI = weight / height**2
#u can use round method
print(int(BMI))
print(round(BMI,2))
# u can use flow division using '//' which makes int

if BMI < 18.5:
    print('you are underweight')

if BMI > 18.5 and BMI<25:
    print('they have a normal weight')
if BMI >25 and BMI<30:
    print(' they are slightly overweight')