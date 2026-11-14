"""Task 6: Divide the milk calculation into simple functions."""

from decimal import Decimal

BASE_RATE = Decimal("30.00")
FAT_STEP_VALUE = Decimal("0.40")
SNF_STEP_VALUE = Decimal("0.30")


def rate_per_litre(fat, snf):
    """Return the rate per litre for the given fat and SNF values."""
    fat_steps = round((fat - Decimal("3.5")) / Decimal("0.1"))
    snf_steps = round((snf - Decimal("8.5")) / Decimal("0.1"))
    rate = BASE_RATE + fat_steps * FAT_STEP_VALUE + snf_steps * SNF_STEP_VALUE
    return rate


def payout(litres, fat, snf):
    """Return the amount for one delivery."""
    rate = rate_per_litre(fat, snf)
    amount = litres * rate
    return amount


def ten_day_total(entries):
    """Add all delivery amounts in a list and round the final total."""
    total = Decimal("0.00")
    for entry in entries:
        total = total + payout(entry[0], entry[1], entry[2])
    return total.quantize(Decimal("0.01"))


# Sample entries use (litres, fat, snf) tuples.
entries = [
    (Decimal("10"), Decimal("3.5"), Decimal("8.5")),
    (Decimal("8.5"), Decimal("4.2"), Decimal("8.7")),
]

for entry in entries:
    rate = rate_per_litre(entry[1], entry[2])
    amount = payout(entry[0], entry[1], entry[2])
    print("Rate: Rs", format(rate, ".2f"), "Amount: Rs", format(amount, ".2f"))

print("Ten-day total: Rs", format(ten_day_total(entries), ".2f"))
print("Function docstring:", rate_per_litre.__doc__)
