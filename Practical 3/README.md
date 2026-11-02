# Practical 3 — Control Flow & Utility Functions

**Course:** MCA Semester I — Python Programming (Unit I / CO1)
**Name:** Rushikesh Laxman Hadawale
**Roll No.:** 54

A menu-driven CLI calculator built with conditionals, loops, `break`/`continue`,
reusable functions, default arguments, `*args`, `**kwargs`, `lambda` and scope.

## Files

| File | Purpose |
|------|---------|
| `utility.py` | Main calculator program |
| `extensions.py` | Extension tasks B–E |
| `output.txt` | Terminal output from testing all cases |
| `screenshots/` | Terminal screenshots |

## How to run

```
python3 -m venv .venv
source .venv/bin/activate
python utility.py
python extensions.py
```

## Menu

1 Add · 2 Subtract · 3 Multiply · 4 Divide · 5 Show summary · 6 Average of three numbers · 0 Exit

## Concepts used

| Concept | Where |
|---------|-------|
| `if / elif / else` | Operation selection in `main()` and `calculate()` |
| `while` | Repeats the menu; `get_number()` repeats until the input is valid |
| `break` | Option 0 exits the menu loop |
| `continue` | Skips back to the menu after invalid choice, summary, average, or divide-by-zero |
| Reusable functions | `show_menu`, `get_number`, `add`, `calculate`, `average`, `show_summary`, `main` |
| Default arguments | `calculate(a, b, operation="+")`, `get_number(prompt=...)` |
| `*args` | `add(*args)`, `average(*numbers)` |
| `**kwargs` | `show_summary(**kwargs)` |
| `lambda` | `format_result = lambda value: f"{value:.2f}"` |
| Scope | `history` is local to `main()`; parameters are local to their functions |

## Technical justification

I put the number input in a separate `get_number()` function that loops with
`while True` and `try/except ValueError` until the user types a valid number.
This keeps the validation in one place, so every operation gets the same
protection without repeating code, and a typo such as a letter does not crash
the program. For division, I handle `ZeroDivisionError` in `main()` and use
`continue` so the user sees a clear message and returns to the menu instead of
the program stopping.
