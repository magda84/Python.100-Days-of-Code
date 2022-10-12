# Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# Don't change the code above 👆

# Write your code below this line 👇

bmi = round(int(weight) / float(height) ** 2)
print(bmi)

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you're \033[1munderweight\033[0m")

elif bmi < 25:
    print(f"Your BMI is {bmi}, you have \033[1mnormal weight\033[0m")

elif bmi < 30:
    print(f"Your BMI is {bmi}, you're \033[1moverweight\033[0m")

elif bmi < 35:
    print(f"Your BMI is {bmi}, you're \033[1mobese\033[0m")

else:
    print(f"Your BMI is {bmi}, you're \033[1mclinically obese\033[0m")
