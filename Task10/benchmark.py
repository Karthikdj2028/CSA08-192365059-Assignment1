"""Task 10: Compare float and Decimal totals for different data sizes."""

from decimal import Decimal
import time
import sys


def add_float(values):
    """Add payment strings as float values."""
    total = 0.0
    for value in values:
        total = total + float(value)
    return total


def add_decimal(values):
    """Add payment strings as Decimal values."""
    total = Decimal("0.00")
    for value in values:
        total = total + Decimal(value)
    return total


print("Python version:", sys.version.split()[0])
print("Object sizes (bytes):")
print("float:", sys.getsizeof(33.40))
print("Decimal:", sys.getsizeof(Decimal("33.40")))
print("integer paise:", sys.getsizeof(3340))

print("\nCOUNT | FLOAT TOTAL | DECIMAL TOTAL | DIFFERENCE | FLOAT TIME | DECIMAL TIME")

for count in (300, 6000, 150000):
    payments = ["33.40"] * count

    start = time.perf_counter()
    float_total = add_float(payments)
    float_time = time.perf_counter() - start

    start = time.perf_counter()
    decimal_total = add_decimal(payments)
    decimal_time = time.perf_counter() - start

    difference = decimal_total - Decimal(str(float_total))
    print(count, "|", format(float_total, ".10f"), "|", decimal_total,
          "|", difference, "|", format(float_time, ".6f"),
          "|", format(decimal_time, ".6f"))

# Compare rounding each line with rounding only after adding all lines.
small_payments = [Decimal("0.005"), Decimal("0.005"), Decimal("0.005")]
rounded_each_line = Decimal("0.00")
for payment in small_payments:
    rounded_each_line = rounded_each_line + payment.quantize(Decimal("0.01"), rounding="ROUND_HALF_UP")

rounded_at_end = sum(small_payments).quantize(Decimal("0.01"), rounding="ROUND_HALF_UP")
print("\nRound each small payment:", rounded_each_line)
print("Round only the final total:", rounded_at_end)
