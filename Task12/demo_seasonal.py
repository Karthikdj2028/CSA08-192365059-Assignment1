"""Show the seasonal rate and ten-day bonus examples."""

from milkrate_seasonal import rate_per_litre, volume_bonus, ten_day_settlement

print("April to June rate, fat 4.25 and SNF 8.63:")
print("Rs", format(rate_per_litre("4.25", "8.63", 4), ".2f"))

print("Regular season rate, fat 4.25 and SNF 8.63:")
print("Rs", format(rate_per_litre("4.25", "8.63", 7), ".2f"))

print("\nBonus for exactly 500 litres: Rs", format(volume_bonus("500"), ".2f"))
print("Bonus for 501 litres: Rs", format(volume_bonus("501"), ".2f"))

entries = [
    {"litres": "250.5", "fat": "3.5", "snf": "8.5"},
    {"litres": "250.5", "fat": "3.5", "snf": "8.5"},
]
result = ten_day_settlement(entries, 4)
print("\nExample ten-day settlement in April:")
print("Total litres:", result["litres"])
print("Milk amount: Rs", format(result["milk_total"], ".2f"))
print("Bonus: Rs", format(result["bonus"], ".2f"))
print("Final payment: Rs", format(result["total"], ".2f"))
