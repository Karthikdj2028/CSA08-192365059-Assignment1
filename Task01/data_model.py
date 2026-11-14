"""Task 1: Identify the data used by the milk payment calculator."""

# Inputs recorded for every delivery
farmer_id = "F001"       # text: an ID may contain letters or leading zeroes
litres = 10.0             # fractional number: milk can be measured in parts of a litre
fat = 3.5                 # fractional percentage
snf = 8.5                 # fractional percentage
shift = "AM"              # text: AM or PM

# Values that remain fixed during the original rate-card run
BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30
REFERENCE_FAT = 3.5
REFERENCE_SNF = 8.5
MIN_FAT = 2.0
MAX_FAT = 7.0

# Example calculation
fat_steps = round((fat - REFERENCE_FAT) / 0.1)
snf_steps = round((snf - REFERENCE_SNF) / 0.1)
rate = BASE_RATE + fat_steps * FAT_STEP_VALUE + snf_steps * SNF_STEP_VALUE
amount = round(litres * rate, 2)

print("INPUT DATA")
print("Farmer ID:", farmer_id)
print("Litres:", litres)
print("Fat %:", fat)
print("SNF %:", snf)
print("Shift:", shift)
print("\nCALCULATED OUTPUT")
print("Fat steps:", fat_steps)
print("SNF steps:", snf_steps)
print("Rate per litre: Rs", format(rate, ".2f"))
print("Amount: Rs", format(amount, ".2f"))

print("\nVALIDATION RULES")
print("Litres must be greater than zero.")
print("Fat must be between 2.0% and 7.0% inclusive.")
print("SNF must not be negative. An upper limit must be confirmed with the co-operative.")
print("Shift must be AM or PM.")
print("Farmer ID must not be blank.")

print("\nASSUMPTIONS")
print("One entry represents one farmer's delivery in one shift.")
print("A ten-day payment combines all valid entries for one farmer.")
print("The nearest 0.1 percentage-point step is used.")
