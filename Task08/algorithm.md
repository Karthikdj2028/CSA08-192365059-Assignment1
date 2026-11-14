# Task 08 – Algorithm plan

## Problem-solving stages

1. **Understand:** identify the farmer, delivery, rate references, validation limits and settlement period.
2. **Plan:** write pseudocode and a flowchart before coding; decide how invalid entries are handled.
3. **Write:** translate the approved algorithm into functions using `Decimal` for money.
4. **Test:** check normal values, boundaries, invalid data, hand calculations and larger input sizes.

## ALGORITHM CALCULATE_ONE_PAYMENT

```text
START
    INPUT farmer_id, litres, fat, snf, shift
    SET valid TO TRUE
    IF farmer_id is empty THEN
        SET valid TO FALSE
        OUTPUT "invalid farmer ID"
    ENDIF
    IF litres is not a finite number OR litres <= 0 THEN
        SET valid TO FALSE
        OUTPUT "invalid quantity"
    ENDIF
    IF fat is not a finite number OR fat < 2.0 OR fat > 7.0 THEN
        SET valid TO FALSE
        OUTPUT "invalid fat percentage"
    ENDIF
    IF snf is not a finite number OR snf < 0 THEN
        SET valid TO FALSE
        OUTPUT "invalid SNF percentage"
    ENDIF
    IF shift is not AM or PM THEN
        SET valid TO FALSE
        OUTPUT "invalid shift"
    ENDIF
    IF valid THEN
        SET fat_steps TO nearest whole 0.1% step from 3.5%
        SET snf_steps TO nearest whole 0.1% step from 8.5%
        SET rate TO 30.00 + fat_steps * 0.40 + snf_steps * 0.30
        SET amount TO litres * rate
        OUTPUT rate and unrounded delivery amount
    ELSE
        OUTPUT "entry rejected; do not add it to the settlement"
    ENDIF
END
```

## ALGORITHM CALCULATE_TEN_DAY_TOTAL

```text
START
    SET total TO 0.00
    FOR each valid entry belonging to the farmer in the ten-day period
        SET entry_amount TO the payment for that entry
        SET total TO total + entry_amount
    ENDFOR
    OUTPUT total rounded to two decimal places
END
```

## Flowchart

The editable Mermaid source is in `flowchart.mmd`. Preview it in a Mermaid-compatible Markdown viewer or GitHub. Capture a screenshot of the rendered flowchart for the report.

## Hand trace – five sample entries

The required three-entry trace is shown below; Tasks 09 and 10 also use five entries.

| Entry | Litres | Fat | SNF | Fat steps | SNF steps | Rate (Rs/L) | Amount (Rs) | Running total (Rs) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 10.00 | 3.5 | 8.5 | 0 | 0 | 30.00 | 300.00 | 300.00 |
| 2 | 8.50 | 4.2 | 8.7 | 7 | 2 | 33.40 | 283.90 | 583.90 |
| 3 | 12.00 | 3.1 | 8.3 | -4 | -2 | 27.80 | 333.60 | 917.50 |

## Alternative: store a list or use a running total

Both approaches take **O(n)** time to process n entries. Storing all entries requires **O(n)** additional space, but supports audit, correction, reprinting, grouping by farmer, and later analysis. A running total requires **O(1)** extra space and is suitable for a streaming total when entries never need to be revisited. For this co-operative, retain transaction records and also maintain a running subtotal for efficiency.
