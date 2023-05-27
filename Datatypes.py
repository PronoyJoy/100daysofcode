# 🚨 Don't change the code below 👇
# sourcery skip: avoid-builtin-shadow
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
first = int(two_digit_number[0])
second = int(two_digit_number[1])

sum = first + second

print( f"{two_digit_number[0]} + {two_digit_number[1]} = {sum}")
print(sum)