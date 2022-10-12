print("***Welcome to the Tip Calculator!")
bill = float(input("What was the total bill? €\n"))
tip = int(input("What percentage tip would you like to give?\n"))
people = int(input("How many people to split the bill?\n"))

tip_calc = (bill * (tip / 100))
bill_per_person = (bill + tip_calc) / people

bill_per_person = round(bill_per_person, 2)
total_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay € {total_amount}.")
