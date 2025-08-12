import calendar

# Program to generate a calendar for a given month and year

# Take input from user
year = int(input("Enter year (e.g. 2025): "))
month = int(input("Enter month (1-12): "))

# Validate month
if 1 <= month <= 12:
    # Display the calendar
    print("\nCalendar for", calendar.month_name[month], year)
    print(calendar.month(year, month))
else:
    print("Invalid month! Please enter a value between 1 and 12.")
