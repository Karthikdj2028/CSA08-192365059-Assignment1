"""Task 2: Compare float and Decimal when adding payments."""

from decimal import Decimal

# 1,000 payments of Rs 33.40 and three adjustments of Rs 0.10
payments = ["33.40"] * 1000 + ["0.10"] * 3


def total_float(items):
    """Add the amounts using float."""
    total = 0.0
    for amount in items:
        total = total + float(amount)
    return total


def total_decimal(items):
    """Add decimal text values exactly using Decimal."""
    total = Decimal("0.00")
    for amount in items:
        total = total + Decimal(amount)
    return total


def total_decimal_from_float(items):
    """Show what happens when Decimal receives a float value."""
    total = Decimal("0.00")
    for amount in items:
        total = total + Decimal(float(amount))
    return total


print("float :", total_float(payments))
print("Decimal:", total_decimal(payments))
print("Decimal(float(amount)):", total_decimal_from_float(payments))
print("0.1 + 0.2 == 0.3 ->", 0.1 + 0.2 == 0.3)
print("Decimal comparison ->", Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))
