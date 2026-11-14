"""Task 10: Compare calculating a rate repeatedly with dictionary lookup."""

import time

BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30


def calculate_rate(fat, snf):
    """Calculate the rate for one fat and SNF pair."""
    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)
    return BASE_RATE + fat_steps * FAT_STEP_VALUE + snf_steps * SNF_STEP_VALUE


# There are many entries, but only three different pairs.
pairs = [(4.2, 8.7), (3.5, 8.5), (3.1, 8.3), (4.2, 8.7)] * 10000

start = time.perf_counter()
uncached_rates = []
for pair in pairs:
    rate = calculate_rate(pair[0], pair[1])
    uncached_rates.append(rate)
uncached_time = time.perf_counter() - start

start = time.perf_counter()
rate_table = {}
cached_rates = []
for pair in pairs:
    if pair not in rate_table:
        rate_table[pair] = calculate_rate(pair[0], pair[1])
    cached_rates.append(rate_table[pair])
cached_time = time.perf_counter() - start

print("Number of entries:", len(pairs))
print("Different fat/SNF pairs:", len(rate_table))
print("Without dictionary lookup:", format(uncached_time, ".6f"), "seconds")
print("With dictionary lookup:", format(cached_time, ".6f"), "seconds")
print("Both results are equal:", uncached_rates == cached_rates)
print("Extra dictionary space is O(k), where k is the number of different pairs.")
