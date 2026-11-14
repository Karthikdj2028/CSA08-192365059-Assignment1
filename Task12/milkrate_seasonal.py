"""Task 12: Seasonal rate calculator with a ten-day volume bonus."""

from decimal import Decimal, ROUND_HALF_UP

CENT = Decimal("0.01")
BONUS_LIMIT = Decimal("500")
BONUS_RATE = Decimal("0.50")


def get_rate_card(month):
    """Return the rate values for the selected month as a dictionary."""
    if month < 1 or month > 12:
        raise ValueError("Month must be from 1 to 12")
    if month >= 4 and month <= 6:
        rate_card = {
            "base_rate": Decimal("32.00"),
            "fat_step": Decimal("0.45"),
            "snf_step": Decimal("0.30"),
            "season": "April to June",
        }
    else:
        rate_card = {
            "base_rate": Decimal("30.00"),
            "fat_step": Decimal("0.40"),
            "snf_step": Decimal("0.30"),
            "season": "Regular season",
        }
    return rate_card


def rate_per_litre(fat, snf, month):
    """Calculate the rate per litre for the month."""
    fat = Decimal(str(fat))
    snf = Decimal(str(snf))
    if fat < Decimal("2.0") or fat > Decimal("7.0"):
        raise ValueError("Fat must be between 2.0 and 7.0")
    if snf < 0:
        raise ValueError("SNF cannot be negative")
    card = get_rate_card(month)

    # round() chooses the nearest whole 0.1 percentage-point step.
    # For an exact halfway value, Python round() uses ties-to-even.
    fat_steps = round((fat - Decimal("3.5")) / Decimal("0.1"))
    snf_steps = round((snf - Decimal("8.5")) / Decimal("0.1"))

    rate = card["base_rate"] + fat_steps * card["fat_step"] + snf_steps * card["snf_step"]
    return rate.quantize(CENT, rounding=ROUND_HALF_UP)


def payout(litres, fat, snf, month):
    """Return the amount for one milk delivery."""
    litres = Decimal(str(litres))
    if litres <= 0:
        raise ValueError("Litres must be greater than zero")
    rate = rate_per_litre(fat, snf, month)
    return litres * rate


def volume_bonus(total_litres):
    """Give 50 paise per litre only when the ten-day quantity is above 500 L."""
    total_litres = Decimal(str(total_litres))
    if total_litres > BONUS_LIMIT:
        bonus = total_litres * BONUS_RATE
    else:
        bonus = Decimal("0.00")
    return bonus.quantize(CENT, rounding=ROUND_HALF_UP)


def ten_day_settlement(entries, month):
    """Return milk total, bonus and final amount for one farmer's entries."""
    total_litres = Decimal("0.00")
    milk_total = Decimal("0.00")

    for entry in entries:
        litres = Decimal(str(entry["litres"]))
        fat = Decimal(str(entry["fat"]))
        snf = Decimal(str(entry["snf"]))
        total_litres = total_litres + litres
        milk_total = milk_total + payout(litres, fat, snf, month)

    milk_total = milk_total.quantize(CENT, rounding=ROUND_HALF_UP)
    bonus = volume_bonus(total_litres)
    final_total = milk_total + bonus

    result = {
        "litres": total_litres,
        "milk_total": milk_total,
        "bonus": bonus,
        "total": final_total.quantize(CENT, rounding=ROUND_HALF_UP),
    }
    return result
