print("Welcome to the tip calculator!")
total_bill = input("What was the total bill? ")
tip_percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")
party_size = input("How many people to split the bill? ")
tip_amount = float(total_bill) * float(tip_percentage)
grand_total_bill = float(total_bill) + tip_amount
print(grand_total_bill)