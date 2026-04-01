_This project has been created as part of the 42 curriculum by pabdalla_

# Garden Guardian - Data Engineering for Smart Agriculture

## Evaluator Instructions

### Running the scripts
Replace with necessary values
```bash
python3 {exercise.py}
# or directly if the shebang is set:
./{exercise_path.py}
```

### Checking code standards
```bash
flake8      # style linter
mypy ./     # type checker
```

---

## Overview

This project builds resilient data pipelines for a smart agricultural monitoring system using Python.
It focuses on exception handling and defensive programming, teaching how to gracefully manage
sensor failures, invalid data, and real-world pipeline errors across a series of exercises.

---

## Concepts Covered

- Catching and handling exceptions with `try` / `except` blocks
- Raising exceptions with `raise` to signal invalid states
- Differentiating between built-in exception types (`ValueError`, `TypeError`, `ZeroDivisionError`, `FileNotFoundError`)
- Creating custom exception hierarchies through class inheritance
- Guaranteeing resource cleanup with `finally` blocks
- Type hints and code standards with `mypy` and `flake8`

---

## Key Python Concepts

### Basic Exception Handling
- `try` wraps code that might fail
- `except ExceptionType` catches a specific error and lets you handle it gracefully
- The program continues running after a caught exception
- Use the base `Exception` class to catch any error, or name a specific type for precision

### Raising Exceptions
- Use `raise ExceptionType("message")` to signal that something has gone wrong
- You can raise built-in exceptions (e.g., `ValueError`) or your own custom ones
- Raising an exception stops the current function and propagates the error up the call stack

### Multiple Exception Types
- A single `try` block can have multiple `except` clauses, one per error type
- You can also catch several types at once with a tuple: `except (ValueError, TypeError)`
- Python has different exception types because different problems require different responses

### Custom Exceptions
- Define a custom exception by inheriting from `Exception` or another exception class
- Custom exceptions make errors more descriptive and domain-specific
- Inheritance lets you group related errors: catching a parent class catches all its children

```python
class GardenError(Exception):
    pass

class PlantError(GardenError):
    pass

class WaterError(GardenError):
    pass
```

### Finally Block
- The `finally` block always executes, whether an exception was raised or not
- Used to release resources (close files, shut down systems) that must always be cleaned up
- Even if an `except` block returns early, `finally` still runs before the function exits

---

## Exercise Summary

| Exercise | File | Concepts |
|----------|------|----------|
| 0 | `ex0/ft_first_exception.py` | Basic `try/except`, catching a `ValueError` |
| 1 | `ex1/ft_raise_exception.py` | `raise`, validating data ranges |
| 2 | `ex2/ft_different_errors.py` | Multiple exception types, catching several at once |
| 3 | `ex3/ft_custom_errors.py` | Custom exception classes, exception inheritance |
| 4 | `ex4/ft_finally_block.py` | `finally` block, guaranteed resource cleanup |

---