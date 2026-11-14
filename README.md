# CSA08-192365059-Assignment1

**Assignment:** Payment Calculator for a Village Milk Co-operative  
**Course:** CSA08 – Python Programming  
**Student:** Karthikeyan S  
**Register Number:** 192365059  
**Nature:** Individual  
**Platform:** macOS  
**Python command:** `python3`  
**Python version:** Enter the exact version printed by `python3 --version` on your Mac.

**GitHub repository:** https://github.com/Karthikdj2028/CSA08-192365059-Assignment1

## About this project

This assignment is written using beginner-friendly Python: variables, named constants, if/else, loops, lists, tuples, dictionaries, functions, try/except, simple assert tests and the Decimal module. It does not require classes, constructors or third-party libraries.

There is one folder for each task:

| Folder | Work |
|---|---|
| Task01 | Problem analysis, values, constants and validation rules |
| Task02 | Types, operators, floating-point behaviour and Decimal |
| Task03 | Variables, constants and dynamic typing |
| Task04 | Expressions, precedence and rounding |
| Task05 | Input, conversion and invalid input handling |
| Task06 | Functions, parameters, return values and scope |
| Task07 | A simple rate module and importing it |
| Task08 | Pseudocode, flowchart and hand trace |
| Task09 | Original calculator and simple assert tests |
| Task10 | Float/Decimal totals, timing and dictionary lookup |
| Task11 | Final design recommendation and complexity analysis |
| Task12 | Seasonal rate cards and ten-day bonus |

Each task contains its own README and an `evidence/` folder. Add your own screenshots after you execute the task.

## Setup on Mac

Open the project folder in VS Code and select **Terminal → New Terminal**. Make sure the terminal is in the folder containing this README.

```bash
python3 --version
git --version
pwd
```

No third-party packages need to be installed. The project uses only Python's standard library. `requirements.txt` is included as requested.

## Run each task

Run commands from the project root folder:

| Task | Command |
|---|---|
| 01 | `python3 Task01/data_model.py` |
| 02 | `python3 Task02/types_exploration.py` |
| 02 | `python3 Task02/decimal_totals.py` |
| 02 | `python3 Task02/memory_sizes.py` |
| 03 | `python3 Task03/constants.py` |
| 04 | `python3 Task04/expressions.py` |
| 05 | `python3 Task05/input_validation.py` |
| 06 | `python3 Task06/functions_demo.py` |
| 07 | `python3 Task07/milkrate.py` |
| 07 | `python3 Task07/demo_import.py` |
| 08 | `python3 Task08/hand_trace.py` |
| 09 | `python3 Task09/test_calculator.py` |
| 09 | `python3 Task09/milk_calculator.py` |
| 10 | `python3 Task10/benchmark.py` |
| 10 | `python3 Task10/cache_demo.py` |
| 11 | Read `Task11/design_decision.md` |
| 12 | `python3 Task12/demo_seasonal.py` |
| 12 | `python3 Task12/test_seasonal.py` |

Task05 and the interactive Task09 calculator request keyboard input. For Task05, enter valid values and also try inputs such as `eight` and `8,5` to see how invalid values are handled.

For Task02, capture an interactive Python session as well:

```bash
python3
```

At the `>>>` prompt, enter the type and arithmetic expressions listed in the assignment. Type `exit()` when finished.

## Evidence and report

1. Execute each task yourself.
2. Compare its output with the assignment's expected output.
3. Capture the terminal using **Shift + Command + 4** on Mac.
4. Save the screenshot inside the matching task's `evidence/` folder.
5. Record your own timings from Task10 in the report. They vary between computers.
6. Enter the exact Python version and this repository link on the report cover page.
7. Use `EVIDENCE_CHECKLIST.md` to check every screenshot requirement.

The evidence folders contain placeholder notes only. They do not contain fabricated screenshots.

## Commit each task separately

After completing a task and saving its evidence, commit that task separately. Example:

```bash
git add Task01
git commit -m "feat(task01): document milk payment data model"
git push origin main
```

Repeat with Task02 through Task12, using the task-specific folders. At the end:

```bash
git status
git log --oneline
```

The assignment requires at least one commit for each task. Do not upload all tasks in one final commit.

## Final submission checks

- [ ] Python version recorded.
- [ ] All 12 tasks executed.
- [ ] Genuine screenshots saved in every evidence folder.
- [ ] Task10 timings measured on your Mac and entered in the report.
- [ ] Separate commits for all 12 tasks pushed to GitHub.
- [ ] Repository is public, or faculty has been added as a collaborator.
- [ ] The GitHub URL appears on the report cover page and submission portal.

**Submission repository URL:** https://github.com/Karthikdj2028/CSA08-192365059-Assignment1

## Note about Task07

The assignment explicitly requires `if __name__ == "__main__":`. This simple check runs the sample table only when `milkrate.py` is run directly. When another script imports it, the sample table is not printed, but its functions can still be called. No `__init__.py`, class or constructor is needed.