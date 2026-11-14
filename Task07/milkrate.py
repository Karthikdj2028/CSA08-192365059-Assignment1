"""Rate card and functions for the village milk co-operative."""

BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30


def rate_per_litre(fat, snf):
    """Calculate and return the rate per litre."""
    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)
    rate = BASE_RATE + fat_steps * FAT_STEP_VALUE + snf_steps * SNF_STEP_VALUE
    return round(rate, 2)


def payout(litres, fat, snf):
    """Calculate and return the payment for one delivery."""
    rate = rate_per_litre(fat, snf)
    amount = litres * rate
    return round(amount, 2)


# This block runs only when this file is executed directly.
# It does not run when another Python file imports milkrate.
if __name__ == "__main__":
    sample_entries = [
        (10, 3.5, 8.5),
        (8.5, 4.2, 8.7),
        (12, 3.1, 8.3),
    ]

    for entry in sample_entries:
        litres = entry[0]
        fat = entry[1]
        snf = entry[2]
        rate = rate_per_litre(fat, snf)
        amount = payout(litres, fat, snf)
        print(f"{litres:5} L fat {fat} snf {snf} rate {rate:6.2f} pay {amount:8.2f}")
