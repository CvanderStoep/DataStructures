import unittest
import max_sliding_window as ms


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(ms.max_sliding_window([2, 7, 3, 1, 5, 2, 6, 2], 4),
                         ms.max_sliding_window_naive([2, 7, 3, 1, 5, 2, 6, 2], 4))
        self.assertEqual(ms.max_sliding_window([1], 1),
                         ms.max_sliding_window_naive([1], 1))


if __name__ == '__main__':
    unittest.main()
