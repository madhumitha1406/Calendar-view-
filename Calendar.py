import calendar

def display_calendar(year, month):
    """Displays the calendar for a given month and year."""
    try:
        year = int(year)
        month = int(month)
        cal = calendar.month(year, month)
        print(cal)
    except ValueError:
        print("Invalid input. Please enter numeric values for year and month.")
    except calendar.IllegalMonthError:
        print("Invalid month. Please enter a month between 1 and 12.")

def main():
    """Main function to get user input and disply the calendar."""
    while True:
        year = input("Enter year (or 'quit' to exit): ")
        if year.lower() == 'quit':
            break
        month = input("Enter month (1-12): ")
        display_calendar(year, month)

if __name__ == "__main__":
    main()