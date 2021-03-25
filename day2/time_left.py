age = input("What is your current age?")
years_left = float(90) - float(age)
days_left = years_left * 365
weeks_left = years_left * 52
months_left = years_left * 12
print(f"Assuming you live to 90 years old, you have {round(days_left)} days, {round(weeks_left)} weeks, and {round(months_left)} months left.")