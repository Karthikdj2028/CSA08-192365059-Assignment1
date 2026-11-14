"""Task 12: Simple assert tests for seasonal rates and the bonus."""

from decimal import Decimal
from milkrate_seasonal import rate_per_litre, volume_bonus, ten_day_settlement

# Summer base rate is Rs 32.00. Regular base rate is Rs 30.00.
assert rate_per_litre("3.5", "8.5", 4) == Decimal("32.00")
print("PASS: April to June base rate")
assert rate_per_litre("3.5", "8.5", 7) == Decimal("30.00")
print("PASS: regular season base rate")

# Example readings have two decimal places.
assert rate_per_litre("4.25", "8.63", 4) == Decimal("35.90")
assert rate_per_litre("4.25", "8.63", 7) == Decimal("33.50")
print("PASS: two-decimal analyser readings in both seasons")

# Python round() uses ties-to-even for exact half-step values.
assert rate_per_litre("3.45", "8.55", 7) == Decimal("30.00")
print("PASS: exact half-step follows Python round()")

# Exactly 500 L gets no bonus; 501 L gets 50 paise for all 501 L.
assert volume_bonus("500") == Decimal("0.00")
print("PASS: 500 litres gets no bonus")
assert volume_bonus("501") == Decimal("250.50")
print("PASS: 501 litres gets bonus on all litres")

# Two deliveries for one farmer add to 501 L.
entries = [
    {"litres": "250.5", "fat": "3.5", "snf": "8.5"},
    {"litres": "250.5", "fat": "3.5", "snf": "8.5"},
]
result = ten_day_settlement(entries, 4)
assert result["litres"] == Decimal("501.0")
assert result["bonus"] == Decimal("250.50")
assert result["total"] == Decimal("16282.50")
print("PASS: ten-day total and bonus")

print("All Task 12 checks passed.")
