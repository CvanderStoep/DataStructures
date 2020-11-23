import unittest
import check_brackets


class TestCheckBrackets(unittest.TestCase):
    def test_something(self):
        self.assertEqual(check_brackets.find_mismatch('[]'), "Success")
        self.assertEqual(check_brackets.find_mismatch('{}[]'), "Success")
        self.assertEqual(check_brackets.find_mismatch('[{}]'), "Success")
        self.assertEqual(check_brackets.find_mismatch('[](){}'), "Success")
        self.assertEqual(check_brackets.find_mismatch('{[}'), (3, False))
        self.assertEqual(check_brackets.find_mismatch('[[]}]{}'), (4, False))
        self.assertEqual(check_brackets.find_mismatch('foo(bar[i);'), (10, False))

if __name__ == '__main__':
    unittest.main()
