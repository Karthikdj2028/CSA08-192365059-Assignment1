"""Task 9: Simple assert tests for the milk calculator."""

from decimal import Decimal
from milk_calculator import rate_per_litre, payout, ten_day_total, validate_entry

# Test 1: standard milk rate
assert rate_per_litre("3.5", "8.5") == Decimal("30.00")
print("PASS: standard rate")

# Test 2: fat and SNF above the standard
assert rate_per_litre("4.2", "8.7") == Decimal("33.40")
assert payout("8.5", "4.2", "8.7") == Decimal("283.900")
print("PASS: readings above standard")

# Test 3: fat and SNF below the standard
assert rate_per_litre("3.1", "8.3") == Decimal("27.80")
assert payout("12", "3.1", "8.3") == Decimal("333.600")
print("PASS: readings below standard")

# Test 4: lower and upper fat boundaries
assert rate_per_litre("2.0", "8.5") == Decimal("24.00")
assert rate_per_litre("7.0", "8.5") == Decimal("44.00")
print("PASS: fat boundaries")

# Test 5: invalid entries are rejected
try:
    validate_entry("F1", "-1", "3.5", "8.5", "AM")
    assert False, "Negative litres should be rejected"
except ValueError:
    print("PASS: negative litres rejected")

try:
    payout("-1", "3.5", "8.5")
    assert False, "Payout must also reject negative litres"
except ValueError:
    print("PASS: payout rejects negative litres")

try:
    validate_entry("F1", "10", "1.9", "8.5", "AM")
    assert False, "Fat below 2.0 should be rejected"
except ValueError:
    print("PASS: low fat rejected")

try:
    validate_entry("F1", "10", "7.1", "8.5", "AM")
    assert False, "Fat above 7.0 should be rejected"
except ValueError:
    print("PASS: high fat rejected")

try:
    validate_entry("F1", "10", "3.5", "8.5", "night")
    assert False, "Invalid shift should be rejected"
except ValueError:
    print("PASS: invalid shift rejected")

try:
    validate_entry("F1", "ten", "3.5", "8.5", "AM")
    assert False, "Text litres should be rejected"
except ValueError:
    print("PASS: text litres rejected")

# Test 6: five entries, total calculated by hand
entries = [
    {"litres": "10", "fat": "3.5", "snf": "8.5"},
    {"litres": "8.5", "fat": "4.2", "snf": "8.7"},
    {"litres": "12", "fat": "3.1", "snf": "8.3"},
    {"litres": "5", "fat": "2.0", "snf": "8.5"},
    {"litres": "4", "fat": "7.0", "snf": "8.5"},
]
assert ten_day_total(entries) == Decimal("1213.50")
print("PASS: five-entry hand total = Rs 1213.50")

print("All Task 9 checks passed.")
