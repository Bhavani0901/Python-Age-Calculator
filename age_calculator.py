from datetime import date
from calendar import monthrange

print("===== AGE CALCULATOR =====")

try:
    dob_input = input("Enter your date of birth (DD-MM-YYYY): ")

    # Convert the entered date into day, month and year
    day, month, year = map(int, dob_input.split("-"))
    dob = date(year, month, day)

    # Get today's date
    today = date.today()

    # Do not allow a future date of birth
    if dob > today:
        print("Error: Date of birth cannot be in the future.")

    else:
        # Initial age calculation
        years = today.year - dob.year
        months = today.month - dob.month
        days = today.day - dob.day

        # Adjust days when the current day is before the birth day
        if days < 0:
            months -= 1

            # Find the previous month and year
            if today.month == 1:
                previous_month = 12
                previous_year = today.year - 1
            else:
                previous_month = today.month - 1
                previous_year = today.year

            # Add the number of days in the previous month
            days += monthrange(previous_year, previous_month)[1]

        # Adjust months when the current month is before the birth month
        if months < 0:
            years -= 1
            months += 12

        print("\nYour exact age is:")
        print("Years :", years)
        print("Months:", months)
        print("Days  :", days)

except ValueError:
    print("Invalid input. Please enter a valid date in DD-MM-YYYY format.")
