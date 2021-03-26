year = int(input("Input a year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"So the year {year} is a leap year")
        else:
            print(f"So the year {year} is a not leap year")
    else:
        print(f"So the year {year} is a leap year")
else:
    print(f"So the year {year} is a not leap year")