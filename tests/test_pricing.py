import unittest
from cinema import pricing


class TestPricing(unittest.TestCase):
    def test_no_discount(self):
        self.assertEqual(pricing.calculate(1, 1, 1)["final"], 1900)

    def test_student_discount(self):
        self.assertEqual(pricing.calculate(0, 2, 0)["student_discount"], 120)

    def test_group_discount(self):
        self.assertEqual(pricing.calculate(5, 0, 0)["final"], 3800)


if __name__ == "__main__":
    unittest.main()
