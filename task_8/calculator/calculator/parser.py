
class InvalidExpressionError(Exception):
    """Custom exception for invalid mathematical expressions."""
    pass

class DivisionByZeroError(Exception):
    """Custom exception for division by zero errors."""
    pass

def tokenize(expression: str) -> list[str]:
    """
    Tokenizes a mathematical expression string.
    e.g., "1 + 2 * (3 - 4)" -> ["1", "+", "2", "*", "(", "3", "-", "4", ")"]
    """
    tokens = []
    current_number = []
    i = 0
    while i < len(expression):
        char = expression[i]
        if char.isspace():
            i += 1
            continue
        elif char.isdigit() or char == '.':
            while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                current_number.append(expression[i])
                i += 1
            tokens.append("".join(current_number))
            current_number = []
            continue
        elif char in "+-*/()":
            tokens.append(char)
        else:
            raise InvalidExpressionError(f"Invalid character in expression: {char}")
        i += 1
    return tokens

# Operator precedence
precedence = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2
}

def shunting_yard(tokens: list[str]) -> list[str]:
    """
    Converts a list of infix tokens to Reverse Polish Notation (RPN) using the Shunting-yard algorithm.
    """
    output_queue = []
    operator_stack = []

    for token in tokens:
        if token.isdigit() or (token[0] == '-' and token[1:].isdigit()) or (token.replace('.', '', 1).isdigit()): # Number
            output_queue.append(token)
        elif token in "+-*/": # Operator
            while (operator_stack and operator_stack[-1] != '(' and
                   precedence.get(operator_stack[-1], 0) >= precedence.get(token, 0)):
                output_queue.append(operator_stack.pop())
            operator_stack.append(token)
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':
            while operator_stack and operator_stack[-1] != '(':
                output_queue.append(operator_stack.pop())
            if not operator_stack or operator_stack[-1] != '(':
                raise InvalidExpressionError("Mismatched parentheses")
            operator_stack.pop() # Pop the '('
        else:
            raise InvalidExpressionError(f"Unknown token: {token}")

    while operator_stack:
        if operator_stack[-1] == '(':
            raise InvalidExpressionError("Mismatched parentheses")
        output_queue.append(operator_stack.pop())
    return output_queue

def evaluate_rpn(rpn_tokens: list[str]) -> float:
    """
    Evaluates a list of tokens in Reverse Polish Notation (RPN).
    """
    stack = []

    for token in rpn_tokens:
        if token.replace('.', '', 1).isdigit() or (token[0] == '-' and token[1:].replace('.', '', 1).isdigit()):
            stack.append(float(token))
        elif token in "+-*/":
            if len(stack) < 2:
                raise InvalidExpressionError("Invalid RPN expression")
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == '+':
                stack.append(operand1 + operand2)
            elif token == '-':
                stack.append(operand1 - operand2)
            elif token == '*':
                stack.append(operand1 * operand2)
            elif token == '/':
                if operand2 == 0:
                    raise DivisionByZeroError("Division by zero")
                stack.append(operand1 / operand2)
        else:
            raise InvalidExpressionError(f"Unknown token in RPN: {token}")

    if len(stack) != 1:
        raise InvalidExpressionError("Invalid RPN expression")
    return stack[0]

