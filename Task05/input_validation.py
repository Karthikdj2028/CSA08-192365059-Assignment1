"""Task 5: Read values and handle incorrect input using try/except."""

import math


def read_number(prompt):
    """Keep asking until the user enters a number."""
    while True:
        text = input(prompt).strip()
        try:
            number = float(text)
            if math.isfinite(number):
                return number
            print("Enter a finite number.")
        except ValueError:
            print("Invalid number. Enter a number such as 8.5.")


def main():
    """Read one entry and display it neatly."""
    farmer_id = input("Farmer ID: ").strip()
    while farmer_id == "":
        print("Farmer ID cannot be blank.")
        farmer_id = input("Farmer ID: ").strip()

    shift = input("Shift (AM/PM): ").strip().upper()
    while shift != "AM" and shift != "PM":
        print("Enter AM or PM.")
        shift = input("Shift (AM/PM): ").strip().upper()

    litres = read_number("Litres: ")
    while litres <= 0:
        print("Litres must be greater than zero.")
        litres = read_number("Litres: ")

    fat = read_number("Fat % (2.0 to 7.0): ")
    while fat < 2.0 or fat > 7.0:
        print("Fat must be between 2.0 and 7.0.")
        fat = read_number("Fat % (2.0 to 7.0): ")

    snf = read_number("SNF %: ")
    while snf < 0:
        print("SNF cannot be negative.")
        snf = read_number("SNF %: ")

    print("\n{:<12}{:>12}".format("FIELD", "VALUE"))
    print("{:<12}{:>12}".format("Farmer ID", farmer_id))
    print("{:<12}{:>12}".format("Shift", shift))
    print("{:<12}{:>12.2f}".format("Litres", litres))
    print("{:<12}{:>12.2f}".format("Fat %", fat))
    print("{:<12}{:>12.2f}".format("SNF %", snf))


if __name__ == "__main__":
    main()
