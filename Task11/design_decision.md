# Task 11 – Recommend and defend the final design

## Recommendation

I recommend keeping the simple function-based design and improving the money calculation by using Python's `Decimal` type. This is a **modify** decision, not a complete redesign.

## Types and rounding

- Farmer ID: `str`, because an ID is a label and can contain letters or leading zeroes.
- Litres, fat and SNF: `Decimal`, because they can contain decimal places.
- Shift: `str`, restricted to `AM` or `PM`.
- Rate and payment: `Decimal`, so money is not added as an inaccurate binary float.
- Step count: use Python's `round()` to choose the nearest whole 0.1% step. For an exact half-step, Python uses ties-to-even (for example, `round(7.5)` is `8`). This behaviour should be explained and approved by the co-operative.
- Final ten-day bank amount: use `Decimal` and round once to two decimal places (paisa) after adding one farmer's delivery amounts. The program uses `ROUND_HALF_UP` for the final money amount, so the bank-rounding rule is stated clearly.

## Rate revision

The rate values are named constants in one module. If the rate changes, edit those values in one place, rerun the tests and commit the change. For seasonal prices, use a simple dictionary selected by month, as shown in Task 12.

## Time and space

For `n` delivery entries, the calculator visits each entry once, so the calculation takes O(n) time. If all entries are saved in a list, the list uses O(n) space. Keeping only a running total uses O(1) extra space, but does not retain the delivery history. A co-operative should keep the entries for checking and audit purposes.

The Task 10 script measures 300, 6,000 and 150,000 sample payments on the student's own computer. The measured times should be copied from that actual run into the assignment report. The arithmetic is linear and these data sizes are manageable for a basic Python program, but a real district union should use a database, backups, access controls and duplicate-entry checks.

## Limitations

1. The assignment gives a fat range of 2.0% to 7.0%, but does not give the highest allowed SNF value. This solution rejects negative SNF and assumes the co-operative will confirm the upper limit.
2. The solution uses the nearest 0.1% step. The co-operative must approve how exact halfway readings are rounded.
3. This is a learning program. It does not include a database, login system, audit history or bank-file integration.
4. Benchmark times depend on the computer and Python version.

## Alternative: read rate values from a JSON file

A JSON file could store the base rate and fat/SNF step values. At program start, Python would read the file once and use those values during calculations. Reading a small file takes O(k) time and O(k) space for `k` settings. It is slightly slower at startup, but a rate revision can be made by editing the file instead of changing Python code. The program must check that the file contains valid values.
