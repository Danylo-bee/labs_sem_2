import unittest
from red_black_priority import RedBlackTreePriorityQueue

class TestRedBlackPriorityQueue(unittest.TestCase):
    def setUp(self):
        self.pq = RedBlackTreePriorityQueue()

    def test_insert_and_view_queue(self):
        self.pq.insert("Task 1", 5)
        self.pq.insert("Task 2", 3)
        self.pq.insert("Task 3", 8)
        self.pq.insert("Task 4", 6)

        expected = [("Task 3", 8), ("Task 4", 6), ("Task 1", 5), ("Task 2", 3)]
        self.assertEqual(self.pq.view_queue(), expected)

    def test_remove_highest_priority(self):
        self.pq.insert("Task A", 10)
        self.pq.insert("Task B", 20)
        self.pq.insert("Task C", 5)

        highest = self.pq.extract_max()
        self.assertEqual(highest, ("Task B", 20))

        expected = [("Task A", 10), ("Task C", 5)]
        self.assertEqual(self.pq.view_queue(), expected)

    def test_remove_until_empty(self):
        self.pq.insert("One", 1)
        self.pq.insert("Two", 2)
        self.pq.insert("Three", 3)

        self.assertEqual(self.pq.extract_max(), ("Three", 3))
        self.assertEqual(self.pq.extract_max(), ("Two", 2))
        self.assertEqual(self.pq.extract_max(), ("One", 1))


        self.assertEqual(self.pq.view_queue(), [])

    def test_remove_from_empty(self):
        self.assertIsNone(self.pq.extract_max())

    def test_view_empty_queue(self):
        self.assertEqual(self.pq.view_queue(), [])

if __name__ == "__main__":
    unittest.main()
