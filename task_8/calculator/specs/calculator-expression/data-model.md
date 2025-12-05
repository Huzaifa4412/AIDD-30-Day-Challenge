# Data Model for Calculator Expression

## Entity: Expression

### Fields:
- `value` (string): The raw mathematical expression input by the user.
- `tokens` (list of strings/enums): The expression broken down into individual tokens (numbers, operators, parentheses).
- `rpn_tokens` (list of strings/enums): The tokens of the expression converted to Reverse Polish Notation (RPN) using the Shunting-yard algorithm.
- `result` (float): The numerical outcome of the evaluated expression.

### Relationships:
- None (Expression is a self-contained entity for calculation).

### Validation Rules:
- **Balanced Parentheses**: Ensure all opening parentheses have a corresponding closing parenthesis.
- **Valid Operators**: Only `+`, `-`, `*`, `/` are allowed. No other symbols.
- **Valid Numbers**: Numbers can be integers or decimals. Handle negative numbers correctly.
- **Syntax Correctness**: Prevent consecutive operators (e.g., `++`, `*/`) or invalid starting/ending tokens.
- **Division by Zero**: Detect and flag division by zero attempts during evaluation.

### State Transitions:
- Not applicable (expression evaluation is a stateless operation).
