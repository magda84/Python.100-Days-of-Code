print("***Welcome to the Tip Calculator!")
bill = float(input("What was the total bill? €\n"))
tip = int(input("What percentage tip would you like to give?\n"))
people = int(input("How many people to split the bill?\n"))

tip_calc = (bill * (tip / 100))
total_bill = (bill + tip_calc) / people

total_bill = round(total_bill, 2)

print(f"Each person should pay € {total_bill}.")
