# CSA08-192365059-Assignment1

**Assignment:** Payment Calculator for a Village Milk Co-operative  
**Course:** CSA08 – Python Programming  
**Student:** Karthikeyan S  
**Register number:** 192365059  
**Nature:** Individual  
**Python version used:** FILL AFTER RUNNING `python --version` (Python 3.10 or later is required)

> Replace the GitHub link after creating the repository. Do not claim that a task is complete until you have run it and saved your own evidence.

**GitHub repository:** `https://github.com/<YOUR-USERNAME>/CSA08-192365059-Assignment1`

## Project overview

This repository contains separate task folders for Tasks 01–12. Tasks 01–08 analyse the data, explore Python types and operators, define constants, validate input, organise functions/modules and plan the algorithm. Tasks 09–11 implement and evaluate the original rate card. Task 12 adapts the design for two-decimal analyser readings, seasonal rate cards and the ten-day volume bonus.

## Python and library versions

- **Python:** Record the exact version printed by `python --version` on the computer used for this submission.
- **Third-party packages:** None.
- **Standard-library modules used:** `dataclasses`, `decimal`, `math`, `sys`, `time` and `unittest`. These are distributed with the installed Python interpreter; they do not have separate package versions to pin.
- **Local modules:** `Task07/milkrate.py`, `Task09/milk_calculator.py` and `Task12/milkrate_seasonal.py` are files in this repository, not installable third-party packages.
- **requirements.txt:** No third-party dependencies are needed. Keep this file in the repository as the assignment requests.

Check your exact version:

```bash
python --version
```

On some systems use `python3 --version` instead, then replace the placeholder near the top of this README and on the report cover.

## Repository map, run commands and expected result notes

Run commands from the repository root folder.

| Task | Command / file to use | Result to check |
|---|---|---|
| Task 01 | `python Task01/data_model.py` | Prints the input, output, constants, data types, validation rules and assumptions for one delivery and a ten-day settlement. |
| Task 02 | `python Task02/types_exploration.py` and `python Task02/decimal_totals.py` and `python Task02/memory_sizes.py` | Shows Python types/operators, the float total versus exact Decimal total, and `sys.getsizeof()` measurements for float, Decimal and integer paise. Also capture a real `>>>` interpreter session. |
| Task 03 | `python Task03/constants.py` | Shows named rate constants, dynamic reassignment and swapping values. |
| Task 04 | `python Task04/expressions.py` | Shows step-count expressions, operator-precedence examples, unexpected floating-point results and round/int/floor comparisons. |
| Task 05 | `python Task05/input_validation.py` | Interactive: accepts valid decimal text, rejects values such as `8,5` or `eight`, and prints aligned output. |
| Task 06 | `python Task06/functions_demo.py` | Demonstrates calculation functions, their returned values, docstrings and local scope. |
| Task 07 | `python Task07/milkrate.py` and `python Task07/demo_import.py` | Direct execution prints the expected three-row rate/payment table; importing from the second script prints its own call without the module's demonstration table. |
| Task 08 | `python Task08/hand_trace.py`; read `Task08/algorithm.md` and open `Task08/flowchart.png` | Prints the three-entry hand trace and running total (Rs 917.50); the Markdown file contains the pseudocode and complexity comparison, and the PNG is the flowchart. |
| Task 09 | `python -m unittest discover -s Task09 -v` | Runs the original-calculator tests, including normal values, fat boundaries, invalid values, five-entry hand total and round-once settlement. |
| Task 10 | `python Task10/benchmark.py` and `python Task10/cache_demo.py` | Prints float/Decimal totals, local timing measurements, object sizes, a rounding-policy comparison and cached/uncached rate results. Record your own timings. |
| Task 11 | Read `Task11/design_decision.md` | Gives the final recommendation, limitations, scale analysis and JSON rate-card alternative. Add your own Task 09/10 evidence to defend it. |
| Task 12 | `python Task12/demo_seasonal.py` and `python -m unittest discover -s Task12 -v` | Demonstrates April–June and regular rates, exact 500 L/no bonus, 501 L/all-litre bonus and the seasonal tests. |

Task05 is interactive. Run it in a terminal and enter the requested values. It accepts decimal points (for example `8.5`), not decimal commas (`8,5`). Task08 is primarily an algorithm/flowchart task; `hand_trace.py` provides an executable trace for evidence.

## Recommended workflow

1. Create the GitHub repository with the exact name shown above.
2. Download and extract this project folder.
3. Open the extracted folder in VS Code or another editor.
4. Run one task at a time using the commands in the table.
5. Compare the output with the assignment's expected output and the report guide.
6. Capture terminal screenshots after each task runs successfully. Save them in that task's `evidence/` folder.
7. Complete the measurement fields in the report using results from your own computer.
8. Commit each task separately. Do not make one final bulk commit.
9. Push the commits and add the faculty as a collaborator if the repository is private.
10. Paste the working repository URL into the cover page and submission portal.

## Evidence policy

The `evidence/` directories contain placeholder notes but no prefilled screenshots. Add genuine screenshots from your own terminal, your own benchmark output, and any required GitHub history screenshots. Do not paste sample output as though it were a screenshot of your execution.

## Suggested commit sequence

```bash
git add README.md .gitignore requirements.txt EVIDENCE_CHECKLIST.md REPORT_COMPLETION_NOTES.md
git commit -m "docs: create assignment repository structure"

git add Task01
git commit -m "feat(task01): document milk payment data model"

git add Task02
git commit -m "feat(task02): explore Python types and decimal money"

git add Task03
git commit -m "feat(task03): define named rate constants"

git add Task04
git commit -m "feat(task04): implement and analyse payment expressions"

git add Task05
git commit -m "feat(task05): validate and convert clerk input"

git add Task06
git commit -m "feat(task06): organise calculations into functions"

git add Task07
git commit -m "feat(task07): create and import milkrate module"

git add Task08
git commit -m "docs(task08): add payment algorithm and flowchart"

git add Task09
git commit -m "feat(task09): implement and test milk calculator"

git add Task10
git commit -m "test(task10): benchmark float and Decimal totals"

git add Task11
git commit -m "docs(task11): defend final calculator design"

git add Task12
git commit -m "feat(task12): add seasonal rates and volume bonus"

git add .
git commit -m "docs: add execution evidence and final report"
```

Run `git status` before every commit and `git log --oneline` to verify the history.
