# CSA08-192365059-Assignment1

**Assignment:** Payment Calculator for a Village Milk Co-operative  
**Course:** CSA08 – Python Programming  
**Student:** Karthikeyan S  
**Register Number:** 192365059  
**Nature:** Individual  
**Platform:** macOS  
**Python command:** `python3`  
**Python version used:** Python 3.13.15

**GitHub repository:** https://github.com/Karthikdj2028/CSA08-192365059-Assignment1

## About this project

This assignment uses beginner-friendly Python: variables, named constants, if/else, loops, lists, tuples, dictionaries, functions, try/except, simple assert tests and the Decimal module. It does not require classes, constructors or third-party libraries.

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

Each task folder contains its Python source or written analysis, a task README and an `evidence/` directory with execution evidence.

## Python and libraries

- Python 3.13.15 on macOS, run with `python3`.
- No third-party packages are required.
- Standard-library modules used include `decimal`, `math`, `sys`, `time` and `unittest`.
- `requirements.txt` is included as requested; no external packages are needed.

## Setup on Mac

Open the project folder in VS Code and select **Terminal → New Terminal**. Make sure the terminal is in the folder containing this README.

```bash
python3 --version
git --version
pwd
```

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

Task05 and the interactive Task09 calculator request keyboard input. Task05 accepts a decimal point (for example `8.5`); try invalid entries such as `eight` and `8,5` to observe the error handling.

For Task02, the assignment also asks for an interactive Python session:

```bash
python3
```

At the `>>>` prompt, enter the type and arithmetic expressions listed in the assignment. Type `exit()` when finished.

## Evidence and report

The task-specific screenshots and supporting files are stored in the corresponding `TaskXX/evidence/` folders. Task08 also includes its flowchart. Task11 is a written evaluation, so its main deliverable is `Task11/design_decision.md`, not a separate Python program.

Two evidence items should be checked before final portal submission:

1. Task02: add a dedicated screenshot of the actual interactive `>>>` interpreter session. The current `task02_types_interpreter.png` is the script output, not the interactive prompt.
2. Task05: the committed screenshot shows a valid data entry. Add a second screenshot showing rejection of invalid text (such as `eight` or `8,5`) followed by a successful correction.

Task10 includes the Mac benchmark and cache comparison screenshots. Timings depend on the local computer and Python build.

## Commit history

Each task was committed and pushed separately, as required. The final Git log showed Task01 through Task12 as separate commits, the branch `main` up to date with `origin/main`, and a clean working tree.

## Final submission checks

- [x] Repository name is `CSA08-192365059-Assignment1`.
- [x] Repository is public.
- [x] Python version 3.13.15 is recorded.
- [x] Tasks01–Task12 are present.
- [x] Each task has a separate commit.
- [x] Task10 benchmark and cache measurements are recorded in the evidence and report.
- [ ] Add the dedicated Task02 interactive interpreter screenshot.
- [ ] Add the Task05 invalid-input screenshot if the faculty expects the invalid attempt to be shown in evidence.
- [ ] Enter the GitHub URL on the report cover page and submission portal.

**Submission repository URL:** https://github.com/Karthikdj2028/CSA08-192365059-Assignment1

## Note about Task07

The assignment explicitly requires `if __name__ == "__main__":`. This simple check runs the sample table only when `milkrate.py` is run directly. When another script imports it, the sample table is not printed, but its functions can still be called. No `__init__.py`, class or constructor is needed.
