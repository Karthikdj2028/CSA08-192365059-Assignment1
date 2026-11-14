"""Task 2: Compare the size of a few Python number objects."""

import sys
from decimal import Decimal

print("Sizes can differ between Python versions and computers.")
print("float object:", sys.getsizeof(33.40), "bytes")
print("Decimal object:", sys.getsizeof(Decimal("33.40")), "bytes")
print("integer paise object:", sys.getsizeof(3340), "bytes")

# Store Rs 33.40 as 3,340 paise (an integer)
amount_in_paise = 3340
print("3340 paise = Rs", format(amount_in_paise / 100, ".2f"))
