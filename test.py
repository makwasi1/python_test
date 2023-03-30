# as the code grows you can put all the tests into a single folder
# its convetion test_*.py for all test files
# how to run with verbose flag python -m unittest -v test

import unittest

from my_sum import sum

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 4]
        result = sum(data)
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()