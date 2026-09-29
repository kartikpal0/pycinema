import unittest
from cinema import seats


class TestSeats(unittest.TestCase):
    def test_seat_count(self):
        self.assertEqual(len(seats.ALL_SEATS), 100)

    def test_invalid_seat_rejected(self):
        self.assertFalse(seats.book("TestMovie", ["Z99"]))


if __name__ == "__main__":
    unittest.main()
