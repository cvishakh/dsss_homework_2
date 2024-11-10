import unittest
from math_quiz import get_random_int, get_random_operation, calculate


class TestMathGame(unittest.TestCase):

    def test_get_random_int(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = get_random_int(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_get_random_operation(self):
        """
        Check if get_random_operation returns a valid operator: +, -, or *.
        """
        for _ in range(1000):  # Test a large number of random operations
            operator = get_random_operation()
            self.assertIn(operator, ['+', '-', '*'], f"Invalid operator: {operator}")


    def test_calculate(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (5, 3, '-', '5 - 3', 2),  #5 - 3 = 2
                (5, 3, '*', '5 * 3', 15), #5 * 3 = 15
                (1, 1, '+', '1 + 1', 2),  #1 + 1 = 2
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                expression, result = calculate(num1, num2, operator)
                self.assertEqual(expression, expected_problem, f"Expected: {expected_problem}, Got: {expression}")
                self.assertEqual(result, expected_answer, f"Expected result: {expected_answer}, Got: {result}")
                

if __name__ == "__main__":
    unittest.main()