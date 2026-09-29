import unittest
from cinema import auth


class TestAuth(unittest.TestCase):
    def test_hash_is_repeatable(self):
        self.assertEqual(auth.hash_password("abc", "s"), auth.hash_password("abc", "s"))

    def test_salt_changes_hash(self):
        self.assertNotEqual(auth.hash_password("abc", "s1"), auth.hash_password("abc", "s2"))


if __name__ == "__main__":
    unittest.main()
