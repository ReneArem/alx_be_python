import unittest
from test_simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        # Add more assertions to thoroughly test the add method.

# Remember to write additional test methods for subtract, multiply, and divide
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(-8, 4), -12)
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(5, 3), 15)
        self.assertEqual(self.calc.multiply(-4, 4), -16)
    def test_division(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        try:
            self.assertEqual(self.calc.divide(1, 0), )
        except ZeroDivisionError as e:
            print(f"Error {e}")
        except TypeError as e:
            print(f"{e} is not of the correct type")

if _name_ == "_main_":
    unittest.main()