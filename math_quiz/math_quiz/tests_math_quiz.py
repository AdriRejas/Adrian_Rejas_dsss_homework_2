import unittest
from math_quiz import generate_random_integer, choose_operator, calculate_answer

class TestMathGame(unittest.TestCase):

    def test_generate_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_choose_operator(self):
        # Test if the operator is randomly selected from the allowed list of operators
        for _ in range(1000):  # Testing multiple times to ensure randomness
            operator = choose_operator()
            self.assertIn(operator, ['+', '-', '*'], f"Expected one of '+', '-', or '*' but got {operator}")

    def test_calculate_answer(self):
        # Test cases to check if the answer calculation is correct for different operators
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (5, 2, '-', '5 - 2', 3),
            (5, 2, '*', '5 * 2', 10),
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = calculate_answer(num1, num2, operator)
            self.assertEqual(problem, expected_problem, f"Expected problem '{expected_problem}' but got '{problem}'")
            self.assertEqual(answer, expected_answer, f"Expected answer {expected_answer} but got {answer}")


if __name__ == "__main__":
    unittest.main()

