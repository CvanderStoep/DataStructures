import unittest
import is_bst_hard


class TestIsBSTHard(unittest.TestCase):
    def test_something(self):
        self.assertEqual(is_bst_hard.IsBinarySearchTree([]), True)
        self.assertEqual(is_bst_hard.IsBinarySearchTree([[2, 1, 2], [1, -1, -1], [3, -1, -1]]), True)
        self.assertEqual(is_bst_hard.IsBinarySearchTree([[1, 1, 2], [2, -1, -1], [3, -1, -1]]), False)
        self.assertEqual(is_bst_hard.IsBinarySearchTree([[2, 1, 2], [1, -1, -1], [2, -1, -1]]), True)
        self.assertEqual(is_bst_hard.IsBinarySearchTree([[2, 1, 2], [2, -1, -1], [3, -1, -1]]), False)
        self.assertEqual(is_bst_hard.IsBinarySearchTree([[2147483647, -1, -1]]), True)
        self.assertEqual(is_bst_hard.IsBinarySearchTree([[1, -1, 1], [2, -1, 2],
                                                         [3, -1, 3], [4, -1, 4], [5, -1, -1]]), True)
        self.assertEqual(is_bst_hard.IsBinarySearchTree([[4, 1, 2], [2, 3, 4], [6, 5, 6], [1, -1, -1],
                                                          [3, -1, -1], [5, -1, -1], [7, -1, -1]]), True)


if __name__ == '__main__':
    unittest.main()
