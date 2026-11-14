"""Task 3: Use named constants and demonstrate dynamic typing."""

BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30
REFERENCE_FAT = 3.5
REFERENCE_SNF = 8.5

print("Rate constants:")
print("Base rate:", BASE_RATE)
print("Fat step value:", FAT_STEP_VALUE)
print("SNF step value:", SNF_STEP_VALUE)
print("Reference fat:", REFERENCE_FAT)
print("Reference SNF:", REFERENCE_SNF)

# Python variables can refer to values of different types.
value = 10
print("\nvalue =", value, "type:", type(value))
value = "ten"
print("value =", value, "type:", type(value))

# Multiple assignment can swap two values.
a = 5
b = 10
print("\nBefore swapping:", a, b)
a, b = b, a
print("After swapping:", a, b)
