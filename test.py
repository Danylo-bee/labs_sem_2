import unittest
from KMP import KMP

class TestKMP(unittest.TestCase):
    def test_found(self):
        self.assertEqual(KMP("abcxabcdabxabcdabcdabcy", "abcdabcy"), 15)

    def test_not_found(self):
        self.assertIsNone(KMP("abcdefgh", "xyz"))

    def test_empty_needle(self):
        self.assertEqual(KMP("abcde", ""), 0)

    def test_empty_haystack(self):
        self.assertIsNone(KMP("", "abc"))

    def test_both_empty(self):
        self.assertEqual(KMP("", ""), 0)

    def test_needle_longer_than_haystack(self):
        self.assertIsNone(KMP("abc", "abcd"))

    def test_multiple_occurrences(self):
        self.assertEqual(KMP("ababababca", "abababca"), 2)

if __name__ == '__main__':
    unittest.main()
