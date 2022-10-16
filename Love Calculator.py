# Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# Don't change the code above 👆

# Write your code below this line 👇

# Input to lowercase

name1 = name1.lower()
name2 = name2.lower()

# Convert all characters to lowercase

a = name1.count("t")
b = name1.count("r")
c = name1.count("u")
d = name1.count("e")
e = name1.count("l")
f = name1.count("o")
g = name1.count("v")
h = name1.count("e")

a1 = name2.count("t")
b1 = name2.count("r")
c1 = name2.count("u")
d1 = name2.count("e")
e1 = name2.count("l")
f1 = name2.count("o")
g1 = name2.count("v")
h1 = name2.count("e")

# Score calculation - conversion from str to int.

percentage1 = (a+b+c+d+e+f+g+h)
percentage2 = (a1+b1+c1+d1+e1+f1+g1+h1)
print(f"Your score is {percentage1}{percentage2}")
love_score = str(percentage1) + str(percentage2)
love_score_as_int = int(love_score)

if love_score_as_int < 10 or love_score_as_int > 90:
    print(f"Your score is {love_score_as_int}, you go together like coke and mentos.")

elif 40 < love_score_as_int < 50:
    print(f"Your love score is {love_score_as_int}, you are alright together.")

else:
    print(f"Your score is {love_score_as_int}.")
