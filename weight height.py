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