import unittest
from board import find_board_size
 
class TestMinBoardSize(unittest.TestCase):
    ''' Тест функції find_board_size'''
    def test_given_cases(self):
        self.assertEqual(find_board_size(10, 2, 3), 9)
    def test_large_case(self):
        self.assertEqual(find_board_size(2, 1000000000, 999999999), 1999999998)
    def test_idk_how_name_it(self):
        self.assertEqual(find_board_size(4, 1, 1), 2)

if __name__ == "__main__":
    unittest.main()
