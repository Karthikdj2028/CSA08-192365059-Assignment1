"""Task 8: Show a simple hand trace for three milk deliveries."""

BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30

entries = [
    (10, 3.5, 8.5),
    (8.5, 4.2, 8.7),
    (12, 3.1, 8.3),
]

total = 0.0
print("LITRES  FAT  SNF  RATE  AMOUNT  RUNNING TOTAL")

for entry in entries:
    litres = entry[0]
    fat = entry[1]
    snf = entry[2]

    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)
    rate = BASE_RATE + fat_steps * FAT_STEP_VALUE + snf_steps * SNF_STEP_VALUE
    amount = litres * rate
    total = total + amount

    print(f"{litres:6.2f} {fat:4.1f} {snf:4.1f} {rate:6.2f} {amount:8.2f} {total:14.2f}")

print("TEN-DAY TOTAL: Rs", format(total, ".2f"))
