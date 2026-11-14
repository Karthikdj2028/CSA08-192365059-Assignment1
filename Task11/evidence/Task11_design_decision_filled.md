# Task 11 – Recommend and defend the final design

**Student:** Karthikeyan S  
**Register number:** 192365059  
**Course:** CSA08 – Python Programming

## 1. Final recommendation

I recommend **modifying and retaining the simple function-based calculator**. I would not redesign the whole program. The program can remain beginner-friendly and use named constants, lists, dictionaries, loops and functions. I recommend using `Decimal` for litres, rate values and money calculations so that binary floating-point errors do not affect the bank payment.

## 2. Types and rounding rule

- Farmer ID and shift are strings. A farmer ID can contain letters or leading zeroes. Shift is `AM` or `PM`.
- Litres, fat percentage, SNF percentage, rate and payment should be represented with `Decimal` values created from input strings.
- The number of 0.1% steps is the nearest whole step, calculated with `round()`. Python uses ties-to-even for an exact halfway value. The co-operative should approve this rule and it should be documented.
- Money should be added as `Decimal`, not `float`.
- Keep the exact delivery amounts during the ten-day calculation and round the farmer's final ten-day total once to two decimal places using `ROUND_HALF_UP`. This gives one clearly stated bank-rounding rule.

## 3. Evidence from my execution

I ran the Task 09 tests on my Mac. The output showed 11 PASS checks, including standard rate, readings above and below standard, fat limits, invalid quantity, invalid fat, invalid shift, text quantity and the five-entry hand total of **Rs 1,213.50**.

My Task 10 benchmark was run using Python 3.13.15 on my Mac. The payment used in the benchmark was Rs 33.40 for every entry. The measured results were:

| Number of payments | Float total (Rs) | Decimal total (Rs) | Decimal minus float (Rs) | Float time (s) | Decimal time (s) |
|---:|---:|---:|---:|---:|---:|
| 300 | 10,019.9999999999 | 10,020.00 | 5.6E-11 | 0.000010 | 0.000029 |
| 6,000 | 200,399.9999999785 | 200,400.00 | 2.148E-8 | 0.000149 | 0.000561 |
| 150,000 | 5,010,000.0000008428 | 5,010,000.00 | -8.43E-7 | 0.003629 | 0.013143 |

The measured object sizes on this Python installation were 24 bytes for a float, 120 bytes for a Decimal and 28 bytes for an integer. These are the sizes of individual objects reported by `sys.getsizeof()`, not the total memory used by a full list of payments.

The benchmark shows that `Decimal` took longer than `float` in this small arithmetic test, but its totals remained exact to the paisa. Even at 150,000 entries, the measured calculation time was about 0.013 seconds for Decimal in this run. These timings are specific to my Mac and Python version; file, database and network operations are not included.

The rounding test also showed why one policy must be selected. Rounding three small payments of Rs 0.005 separately gave Rs 0.03, while adding them first and rounding the final total gave Rs 0.02. Since the co-operative pays one ten-day amount to each farmer, I recommend adding the unrounded Decimal delivery amounts first and rounding the final ten-day amount once. The co-operative must approve this policy before real payments are made.

## 4. Rate revisions

For the original rate card, keep the base rate, fat step value, SNF step value and reference percentages together as named constants in one module. A rate revision then requires changing one place, rerunning the tests and committing the change.

For the seasonal requirement in Task 12, a small dictionary can hold the rate values for each season. A function selects the correct rate card based on the month. The bonus is calculated separately from the farmer's total ten-day litres.

## 5. Time and space complexity

For `n` delivery entries, the calculator processes each entry once. Therefore, the calculation takes **O(n) time**.

- If every delivery is stored in a list for later checking, the list uses **O(n) space**.
- If only a running total is kept, the calculation needs **O(1) extra space**, but the individual delivery history is not retained.
- For a co-operative, retaining the entries is useful for checking, correcting mistakes and audit purposes. A real district union should store the records in a database and maintain backups, access controls and duplicate-entry checks.

The measured 150,000-entry calculation completed in about 0.013143 seconds for Decimal arithmetic on my Mac. This supports using a simple loop for the assignment's district-union example. It does not prove that a complete real-world district system will take that long, because database access, file writing, validation and multiple users add extra work.

## 6. Limitations

1. The assignment specifies a fat range of 2.0% to 7.0%, but it does not specify the maximum SNF value. The current program rejects negative SNF; the co-operative must provide the upper limit.
2. The nearest-step rule and Python's ties-to-even behaviour for exact half-steps must be approved by the co-operative.
3. This is a learning calculator. It does not include a database, login system, audit history, backup service or bank-file integration.
4. Benchmark timings depend on the computer, Python version and data used.

## 7. Alternative: load the rate card from a JSON file

Instead of writing the rate values in a Python module, the co-operative could store them in a small JSON file:

```json
{
  "base_rate": "30.00",
  "fat_step": "0.40",
  "snf_step": "0.30"
}
```

The program can read the file once when it starts:

```python
import json
from decimal import Decimal

with open("rate_card.json", "r") as file:
    rate_data = json.load(file)

BASE_RATE = Decimal(rate_data["base_rate"])
FAT_STEP_VALUE = Decimal(rate_data["fat_step"])
SNF_STEP_VALUE = Decimal(rate_data["snf_step"])

print("Rate card loaded:", BASE_RATE, FAT_STEP_VALUE, SNF_STEP_VALUE)
```

If the file contains `k` rate settings, reading and storing them takes **O(k) time** and **O(k) space** at startup. For a small rate card, this cost is very small. The benefit is that an authorised person can revise the JSON values without editing or redistributing the Python program. The program must still check that the file exists and that the values are valid numbers. A backup/default rate card should be available if the file is missing or damaged.

## 8. Conclusion

I recommend retaining the simple function-based design and modifying it to use `Decimal` for accurate money calculations, one documented rounding rule, centralised rate values and input validation. The Task 09 tests and Task 10 measurements support this decision. For future rate revisions, a JSON rate-card file is a useful improvement because it separates rate data from calculation code. The design is suitable for demonstrating the assignment's 150,000-entry scale, while a real district-union system would also need database storage, backups, audit records and access controls.

## Evidence files to attach

- `../Task09/evidence/task09_test_results.png` – the passing calculation and validation checks.
- `../Task10/evidence/task10_benchmark_output.png` – float/Decimal totals, object sizes and execution times.
- `../Task10/evidence/task10_cache_results.png` – rate lookup comparison, after running the cache demonstration.
- `evidence/task11_design_decision.png` – screenshot of this completed written recommendation in the editor or Markdown preview.
