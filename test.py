import unittest
from min_dist import min_distanse


class TestMST(unittest.TestCase):

    def test_connected_graph(self):
        edges = [
            (100, "K1", "K2"),
            (200, "K2", "K3"),
            (150, "K3", "K4"),
            (300, "K4", "K5"),
            (500, "K1", "K5"),
            (350, "K2", "K5"),
            (250, "K3", "K1"),
        ]
        expected_weight = 100 + 150 + 200 + 300  # 750
        total_weight, mst_edges = min_distanse(edges)
        self.assertEqual(total_weight, expected_weight)
        self.assertEqual(len(mst_edges), 4)

    def test_disconnected_graph(self):
        edges = [
            (100, "A", "B"),
            (200, "B", "C"),
            (300, "X", "Y"),
        ]
        total_weight, mst_edges = min_distanse(edges)
        self.assertEqual(total_weight, -1)
        self.assertEqual(mst_edges, [])

    def test_single_node(self):
        edges = []
        total_weight, mst_edges = min_distanse(edges)
        self.assertEqual(total_weight, -1)
        self.assertEqual(mst_edges, [])

    def test_minimal_graph(self):
        edges = [(42, "A", "B")]
        total_weight, mst_edges = min_distanse(edges)
        self.assertEqual(total_weight, 42)
        self.assertEqual(mst_edges, [(42, "A", "B")])


if __name__ == "__main__":
    unittest.main()
