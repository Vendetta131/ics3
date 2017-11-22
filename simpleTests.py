import unittest


def absolute(a):
    return abs(a)


class TestCalculation(unittest.TestCase):
    positive_input = 5
    correct_result_for_positive_input = 5
    negative_input = -5
    correct_result_for_negative_input = 5

    def test_abs_returns_correct_numer_for_positive_input(self):
        # act
        result = absolute(self.positive_input)

        # check result
        self.assertEqual(result, self.correct_result_for_positive_input, "expected result for postive input to be {}".format(self.positive_input))

    def test_abs_returns_correct_number_for_negative_input(self):
        result = absolute(self.negative_input)

        self.assertEqual(result, self.correct_result_for_negative_input, "expected result for negative input to be {}".format(self.negative_input))


class Calculator:
    # expected to return sum of a and b
    def add(self, a, b):
        return a + b

    # expected to return difference of a and b
    def diff(self, a, b):
        return a - b

    # expected to return multiplication of a and b
    def multiply(self, a, b):
        return a * b

    # expected to return division of a and b
    def div(self, a, b):
        return a / b


class CalculatorTests(unittest.TestCase):
    def setUp(self):
        self.instance = Calculator()

    def test_add(self):
        result = self.instance.add(3, 5)
        self.assertEqual(result, 8, "expected result to be {}".format(8))

    def test_diff(self):
        result = self.instance.diff(7, 2)
        self.assertEqual(result, 5, "expected result to be {}".format(5))

    def test_multiply(self):
        result = self.instance.multiply(5, 7)
        self.assertEqual(result, 35, "expected result to be {}".format(35))

    def test_div(self):
        result = self.instance.div(18, 3)
        self.assertEqual(result, 6, "expect result to be {}".format(6))


if __name__ == '__main__':
    unittest.main()

