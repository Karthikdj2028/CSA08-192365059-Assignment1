"""Task 4: Demonstrate rate expressions, operators and rounding."""

import math

BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30

fat = 4.2
snf = 8.7
fat_steps = round((fat - 3.5) / 0.1)
snf_steps = round((snf - 8.5) / 0.1)
rate = BASE_RATE + fat_steps * FAT_STEP_VALUE + snf_steps * SNF_STEP_VALUE
amount = round(8.5 * rate, 2)

print("Fat steps:", (fat - 3.5) / 0.1, "rounded to", fat_steps)
print("SNF steps:", (snf - 8.5) / 0.1, "rounded to", snf_steps)
print("Rate per litre: Rs", format(rate, ".2f"))
print("Amount: Rs", format(amount, ".2f"))

print("\nThree or more surprising results:")
print("(4.2 - 3.5) / 0.1 =", (4.2 - 3.5) / 0.1)
print("0.1 + 0.2 == 0.3 ->", 0.1 + 0.2 == 0.3)
print("round(2.675, 2) =", round(2.675, 2))
print("-7 // 2 =", -7 // 2)

fat = 3.1
steps = (fat - 3.5) / 0.1
print("\nFor fat = 3.1:")
print("Raw steps:", steps)
print("round():", round(steps))
print("int():", int(steps))
print("floor():", math.floor(steps))
print("Rate using round():", BASE_RATE + round(steps) * FAT_STEP_VALUE)
print("Rate using int():", BASE_RATE + int(steps) * FAT_STEP_VALUE)
print("Rate using floor():", BASE_RATE + math.floor(steps) * FAT_STEP_VALUE)

print("\nComparison chaining:")
print("2.0 <= 4.2 <= 7.0 ->", 2.0 <= 4.2 <= 7.0)
print("Fat valid and SNF non-negative ->", 2.0 <= 4.2 <= 7.0 and 8.7 >= 0)
