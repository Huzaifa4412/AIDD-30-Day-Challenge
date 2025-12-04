
import sys
from calculator.parser import tokenize, shunting_yard, evaluate_rpn, InvalidExpressionError, DivisionByZeroError

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py \"<expression>\"")
        sys.exit(1)

    expression = sys.argv[1]

    try:
        tokens = tokenize(expression)
        rpn_tokens = shunting_yard(tokens)
        result = evaluate_rpn(rpn_tokens)
        print(f"Result: {result}")
    except (InvalidExpressionError, DivisionByZeroError) as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
