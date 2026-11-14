# CSA08-192365059-Assignment1

**Assignment:** Payment Calculator for a Village Milk Co-operative  
**Course:** CSA08 – Python Programming  
**Student:** Karthikeyan S  
**Register number:** 192365059  
**Nature:** Individual  
**Platform:** macOS  
**Python command:** `python3`  
**Python version:** Fill in the exact version shown by `python3 --version` on the Mac used for this submission.

**GitHub repository:** https://github.com/Karthikdj2028/CSA08-192365059-Assignment1

> Work through the tasks individually. Run every program on your own Mac, compare the output with the assignment's expected output, save your own screenshots in the relevant `evidence/` directory, and commit each task separately. Do not mark a task complete until it has been executed and evidenced.

## Project overview

This repository contains separate task folders for Tasks 01–12. Tasks 01–08 analyse the data, explore Python types and operators, define constants, validate input, organise functions/modules and plan the algorithm. Tasks 09–11 implement and evaluate the original rate card. Task 12 adapts the design for two-decimal analyser readings, seasonal rate cards and the ten-day volume bonus.

## Python and library versions

- **Python:** Run `python3 --version` and enter the exact output here and on the report cover.
- **Third-party packages:** None.
- **Standard-library modules used:** `dataclasses`, `decimal`, `math`, `sys`, `time` and `unittest`. These are distributed with Python.
- **Local modules:** `Task07/milkrate.py`, `Task09/milk_calculator.py` and `Task12/milkrate_seasonal.py` are files in this repository, not third-party packages.
- **requirements.txt:** No third-party dependencies are needed. Keep this file as requested by the assignment.

## macOS setup

Open the extracted repository folder in VS Code. Choose **Terminal → New Terminal**. Confirm that the terminal is in the repository root (the directory containing this README).

Check the tools:

```bash
python3 --version
git --version
pwd
```

Optional: create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 --version
```

No third-party package installation is required. If you use the virtual environment, continue to use `python3` in the commands below.

## Repository map, run commands and expected result notes

Run commands from the repository root folder.

| Task | Command / file to use | Result to check |
|---|---|---|
| Task 01 | `python3 Task01/data_model.py` | Prints the input, output, constants, data types, validation rules and assumptions for one delivery and a ten-day settlement. |
| Task 02 | `python3 Task02/types_exploration.py`, `python3 Task02/decimal_totals.py`, and `python3 Task02/memory_sizes.py` | Shows Python types/operators, float total versus exact Decimal total, and `sys.getsizeof()` measurements. Also capture a real `>>>` interpreter session using `python3`. |
| Task 03 | `python3 Task03/constants.py` | Shows named rate constants, dynamic reassignment and swapping values. |
| Task 04 | `python3 Task04/expressions.py` | Shows step-count expressions, operator-precedence examples, unexpected floating-point results and round/int/floor comparisons. |
| Task 05 | `python3 Task05/input_validation.py` | Interactive: accepts valid decimal text, rejects values such as `8,5` or `eight`, and prints aligned output. |
| Task 06 | `python3 Task06/functions_demo.py` | Demonstrates calculation functions, returned values, docstrings and local scope. |
| Task 07 | `python3 Task07/milkrate.py` and `python3 Task07/demo_import.py` | Direct execution prints the expected three-row rate/payment table; the second script imports and calls the module without printing its demonstration table on import. |
| Task 08 | `python3 Task08/hand_trace.py`; read `Task08/algorithm.md` and open `Task08/flowchart.png` | Prints the three-entry hand trace and running total; the Markdown file contains pseudocode and complexity comparison, and the PNG is the flowchart. |
| Task 09 | `python3 -m unittest discover -s Task09 -v` | Runs original-calculator tests, including normal values, fat boundaries, invalid values, five-entry hand total and round-once settlement. |
| Task 10 | `python3 Task10/benchmark.py` and `python3 Task10/cache_demo.py` | Prints float/Decimal totals, local timings, object sizes, rounding-policy comparison and cached/uncached rate results. Record your own timings. |
| Task 11 | Read `Task11/design_decision.md` | Gives the final recommendation, limitations, scale analysis and JSON rate-card alternative. Add your own Task09/10 evidence to defend it. |
| Task 12 | `python3 Task12/demo_seasonal.py` and `python3 -m unittest discover -s Task12 -v` | Demonstrates April–June and regular rates, exactly 500 L/no bonus, 501 L/all-litre bonus and seasonal tests. |

Task05 is interactive. Enter the requested values in the terminal. It accepts decimal points (for example `8.5`), not decimal commas (`8,5`). Task08 is primarily an algorithm/flowchart task; `hand_trace.py` provides an executable trace for evidence.

## Task-by-task workflow

1. Open the project root in VS Code and use its integrated terminal.
2. Run only the current task using the command above.
3. Read the task's code and understand what each important line does.
4. Compare actual output with the assignment's expected output.
5. Capture the terminal using **Shift + Command + 4** (or **Shift + Command + 5**) and save it under that task's `evidence/` directory.
6. Update the report with your own results, screenshots and benchmark measurements.
7. Commit the task before starting the next one.

## Evidence policy

The `evidence/` directories contain placeholder notes, not completed screenshots. Add genuine screenshots from your own Mac, your own benchmark output and the required Git history. Do not present sample output as if it were a screenshot of your own execution.

See [EVIDENCE_CHECKLIST.md](EVIDENCE_CHECKLIST.md) for the per-task screenshot list and [REPORT_COMPLETION_NOTES.md](REPORT_COMPLETION_NOTES.md) for report placeholders that must be completed.

## GitHub workflow (macOS)

Check the repository remote:

```bash
git remote -v
```

If `origin` is not set, add it:

```bash
git remote add origin https://github.com/Karthikdj2028/CSA08-192365059-Assignment1.git
```

If `origin` already exists but points elsewhere, correct it:

```bash
git remote set-url origin https://github.com/Karthikdj2028/CSA08-192365059-Assignment1.git
```

Check status and branch:

```bash
git status
git branch --show-current
```

If this is a brand-new local Git repository, use `main` as the branch:

```bash
git branch -M main
```

After finishing each task, stage and commit it separately. Example for Task01:

```bash
git add Task01
git commit -m "feat(task01): document milk payment data model"
git push -u origin main
```

For each later task, replace `Task01` and the commit message with the relevant task. The suggested commit messages below can be used. If Git asks you to authenticate, complete the browser sign-in or credential prompt.

## Suggested commit sequence

```bash
git add README.md .gitignore requirements.txt EVIDENCE_CHECKLIST.md REPORT_COMPLETION_NOTES.md
git commit -m "docs: create assignment repository structure"

git add Task01 && git commit -m "feat(task01): document milk payment data model"
git add Task02 && git commit -m "feat(task02): explore Python types and decimal money"
git add Task03 && git commit -m "feat(task03): define named rate constants"
git add Task04 && git commit -m "feat(task04): implement and analyse payment expressions"
git add Task05 && git commit -m "feat(task05): validate and convert clerk input"
git add Task06 && git commit -m "feat(task06): organise calculations into functions"
git add Task07 && git commit -m "feat(task07): create and import milkrate module"
git add Task08 && git commit -m "docs(task08): add payment algorithm and flowchart"
git add Task09 && git commit -m "feat(task09): implement and test milk calculator"
git add Task10 && git commit -m "test(task10): benchmark float and Decimal totals"
git add Task11 && git commit -m "docs(task11): defend final calculator design"
git add Task12 && git commit -m "feat(task12): add seasonal rates and volume bonus"

git add .
git commit -m "docs: add execution evidence and final report"
git push origin main
```

The first documentation commit is only needed if you have not already committed the starter files. Do not repeat it if it already exists. Run `git status` before committing and `git log --oneline` to verify your history.

## Before submitting

- [ ] Replace the Python version placeholder with the exact output of `python3 --version`.
- [ ] Run every task on your Mac and compare the output with the stated expected result.
- [ ] Save genuine screenshots in every task's `evidence/` folder.
- [ ] Record Task10's own measurements (do not copy example timings).
- [ ] Complete the Word report's GitHub link, Python version, test results, timing values and evidence references.
- [ ] Ensure commits are separate and pushed.
- [ ] Confirm the repository is public, or invite the faculty as a collaborator if private.
- [ ] Submit this repository URL on the portal and print it on the report cover:

  https://github.com/Karthikdj2028/CSA08-192365059-Assignment1
