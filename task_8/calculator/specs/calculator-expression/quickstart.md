# Quickstart Guide for Calculator Expression Evaluator

This guide provides a quick overview of how to use the calculator expression evaluator.

## 1. Prerequisites

- Python 3.x installed.

## 2. Running the Evaluator

To evaluate a mathematical expression, run the main script from your terminal and pass the expression as an argument (or interactively, depending on final implementation).

### Example Usage (Command Line):

Assuming the main script is `main.py` in the project root:

```bash
python main.py "1 + 2 * (3 - 4) / 5"
```

### Expected Output:

```
Result: 0.6
```

### Error Handling:

- **Invalid Expression**:

  ```bash
  python main.py "1 + (2 - 3"
  ```
  Expected Output:
  ```
  Error: Invalid Expression: Unbalanced parentheses
  ```

- **Division by Zero**:

  ```bash
  python main.py "1 / (2 - 2)"
  ```
  Expected Output:
  ```
  Error: Division By Zero
  ```
