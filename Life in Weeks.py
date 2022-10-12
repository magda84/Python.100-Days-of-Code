# Don't change the code below 👇
age = input("What is your current age?\n")
# Don't change the code above 👆

# Write your code below this line 👇

# 1 year = 365 days, 52 weeks and 12 months

max_days = 90

days_left = (max_days * 365) - (int(age) * 365)
weeks_left = (max_days * 52) - (int(age) * 52)
months_left = (max_days * 12) - (int(age) * 12)

print(f"You have {days_left} days, {weeks_left} weeks and {months_left} months left.")