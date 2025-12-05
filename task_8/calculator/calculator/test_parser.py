
import unittest
from calculator.parser import tokenize, shunting_yard, evaluate_rpn, InvalidExpressionError, DivisionByZeroError

class TestParser(unittest.TestCase):

    # Test Tokenization
    def test_tokenize_basic(self):
        self.assertEqual(tokenize("1 + 2"), ["1", "+", "2"])
        self.assertEqual(tokenize("10 * (2.5 - 0.5)"), ["10", "*", "(", "2.5", "-", "0.5", ")"])

    def test_tokenize_whitespace(self):
        self.assertEqual(tokenize("  1   +   2  "), ["1", "+", "2"])

    def test_tokenize_invalid_char(self):
        with self.assertRaises(InvalidExpressionError):
            tokenize("1 $ 2")

    # Test Shunting-yard Algorithm
    def test_shunting_yard_basic(self):
        self.assertEqual(shunting_yard(tokenize("3 + 4 * 2 / (1 - 5)")), ["3", "4", "2", "*", "1", "5", "-", "/", "+"])
        self.assertEqual(shunting_yard(tokenize("5 * (6 + 2)")), ["5", "6", "2", "+", "*"])

    def test_shunting_yard_precedence(self):
        self.assertEqual(shunting_yard(tokenize("2 + 3 * 4")), ["2", "3", "4", "*", "+"])
        self.assertEqual(shunting_yard(tokenize("2 * 3 + 4")), ["2", "3", "*", "4", "+"])

    def test_shunting_yard_mismatched_parentheses(self):
        with self.assertRaises(InvalidExpressionError):
            shunting_yard(tokenize(" (1 + 2 "))
        with self.assertRaises(InvalidExpressionError):
            shunting_yard(tokenize(" 1 + 2) "))

    # Test RPN Evaluation
    def test_evaluate_rpn_basic(self):
        self.assertEqual(evaluate_rpn(["3", "4", "+"]), 7.0)
        self.assertEqual(evaluate_rpn(["3", "4", "2", "*", "+"]), 11.0)
        self.assertEqual(evaluate_rpn(["10", "2.5", "0.5", "-", "*", "2", "/"]), 10.0)

    def test_evaluate_rpn_division_by_zero(self):
        with self.assertRaises(DivisionByZeroError):
            evaluate_rpn(["1", "0", "/"])

    def test_evaluate_rpn_invalid_expression(self):
        with self.assertRaises(InvalidExpressionError):
            evaluate_rpn(["1", "+"])
        with self.assertRaises(InvalidExpressionError):
            evaluate_rpn(["1", "2", "3", "+"])

if __name__ == '__main__':
    unittest.main()
