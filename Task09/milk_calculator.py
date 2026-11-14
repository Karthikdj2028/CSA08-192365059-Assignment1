"""Task 9: A beginner-friendly milk payment calculator using Decimal."""

from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

BASE_RATE = Decimal("30.00")
FAT_STEP_VALUE = Decimal("0.40")
SNF_STEP_VALUE = Decimal("0.30")
MIN_FAT = Decimal("2.0")
MAX_FAT = Decimal("7.0")
CENT = Decimal("0.01")


def make_decimal(value, field_name):
    """Convert input text to Decimal and reject invalid numbers."""
    try:
        number = Decimal(str(value).strip())
    except InvalidOperation:
        raise ValueError(field_name + " must be a number")
    if not number.is_finite():
        raise ValueError(field_name + " must be a finite number")
    return number


def validate_entry(farmer_id, litres, fat, snf, shift):
    """Check one delivery and return its values in a dictionary."""
    farmer_id = str(farmer_id).strip()
    shift = str(shift).strip().upper()
    litres = make_decimal(litres, "Litres")
    fat = make_decimal(fat, "Fat")
    snf = make_decimal(snf, "SNF")

    if farmer_id == "":
        raise ValueError("Farmer ID cannot be blank")
    if litres <= 0:
        raise ValueError("Litres must be greater than zero")
    if fat < MIN_FAT or fat > MAX_FAT:
        raise ValueError("Fat must be between 2.0 and 7.0")
    if snf < 0:
        raise ValueError("SNF cannot be negative")
    if shift != "AM" and shift != "PM":
        raise ValueError("Shift must be AM or PM")

    entry = {
        "farmer_id": farmer_id,
        "litres": litres,
        "fat": fat,
        "snf": snf,
        "shift": shift,
    }
    return entry


def rate_per_litre(fat, snf):
    """Calculate the rate per litre from fat and SNF readings."""
    fat = make_decimal(fat, "Fat")
    snf = make_decimal(snf, "SNF")
    fat_steps = round((fat - Decimal("3.5")) / Decimal("0.1"))
    snf_steps = round((snf - Decimal("8.5")) / Decimal("0.1"))
    rate = BASE_RATE + fat_steps * FAT_STEP_VALUE + snf_steps * SNF_STEP_VALUE
    return rate.quantize(CENT, rounding=ROUND_HALF_UP)


def payout(litres, fat, snf):
    """Calculate one delivery amount without rounding away extra precision."""
    litres = make_decimal(litres, "Litres")
    if litres <= 0:
        raise ValueError("Litres must be greater than zero")
    rate = rate_per_litre(fat, snf)
    return litres * rate


def ten_day_total(entries):
    """Add one farmer's deliveries and round once for the bank payment."""
    total = Decimal("0.00")
    for entry in entries:
        amount = payout(entry["litres"], entry["fat"], entry["snf"])
        total = total + amount
    return total.quantize(CENT, rounding=ROUND_HALF_UP)


def main():
    """Read one farmer's entries until DONE and display the ten-day total."""
    entries = []
    print("Ksheera Milk Co-operative")
    print("Enter DONE as Farmer ID when all entries are entered.")

    while True:
        farmer_id = input("Farmer ID (or DONE): ").strip()
        if farmer_id.upper() == "DONE":
            break

        litres = input("Litres: ")
        fat = input("Fat %: ")
        snf = input("SNF %: ")
        shift = input("Shift (AM/PM): ")

        try:
            entry = validate_entry(farmer_id, litres, fat, snf, shift)
            entries.append(entry)
            rate = rate_per_litre(entry["fat"], entry["snf"])
            amount = payout(entry["litres"], entry["fat"], entry["snf"])
            print("Rate per litre: Rs", format(rate, ".2f"))
            print("Delivery amount: Rs", format(amount, ".2f"))
        except ValueError as error:
            print("Entry rejected:", error)

    if len(entries) > 0:
        # Make a list of each farmer ID without using advanced features.
        farmer_ids = []
        for entry in entries:
            if entry["farmer_id"] not in farmer_ids:
                farmer_ids.append(entry["farmer_id"])

        # Calculate a separate ten-day total for each farmer.
        for farmer_id in farmer_ids:
            one_farmer_entries = []
            for entry in entries:
                if entry["farmer_id"] == farmer_id:
                    one_farmer_entries.append(entry)
            total = ten_day_total(one_farmer_entries)
            print(f"Farmer {farmer_id}: ten-day total Rs {total:.2f}")
    else:
        print("No valid entries were entered.")


if __name__ == "__main__":
    main()
