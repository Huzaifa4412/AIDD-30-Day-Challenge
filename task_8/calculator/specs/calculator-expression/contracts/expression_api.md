# API Contract for Expression Evaluation

This document defines the interface for the expression evaluation functionality.

## Function: `evaluate_expression`

### Description:
Evaluates a given mathematical expression string and returns the numerical result.

### Signature (Conceptual):
`evaluate_expression(expression: str) -> float`

### Parameters:
- `expression` (string, required):
    - **Description**: The mathematical expression to be evaluated.
    - **Example**: `"1 + 2 * (3 - 4) / 5"`

### Returns:
- `float`:
    - **Description**: The numerical result of the evaluated expression.
    - **Example**: `0.6` (for the example expression `"1 + 2 * (3 - 4) / 5"`)

### Errors:
- `InvalidExpressionError`:
    - **Description**: Raised when the input `expression` is syntactically incorrect (e.g., unbalanced parentheses, invalid characters, consecutive operators).
    - **Example**: `"1 + (2 - 3"` or `"1 @ 2"`
- `DivisionByZeroError`:
    - **Description**: Raised when the expression attempts to perform a division by zero.
    - **Example**: `"1 / (5 - 5)"`
