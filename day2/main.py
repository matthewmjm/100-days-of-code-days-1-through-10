print("Welcome to the tip calculator!")
total_bill = input("What was the exact amount of the total bill? $")
tip_percentage = input("What percentage tip would you like to give (as a whole number with no decimal point)? 10, 12, or 15? ")
party_size = input("How many people to split the bill? ")
tip_amount = float(total_bill) * (float(tip_percentage) / 100)
grand_total_bill = float(total_bill) + tip_amount
bill_per_person = round(grand_total_bill / int(party_size), 2)
bill_per_person_formatted = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${bill_per_person_formatted}")