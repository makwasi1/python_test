# as the code grows you can put all the tests into a single folder
# its convetion test_*.py for all test files
# how to run with verbose flag python -m unittest -v test

import unittest

from my_sum import sum

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that user has a password
        """
        data = [1, 2, 3,5,6]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_list_int(self):
        """
        Test that user has provided valid email
        """
        data = [1, 2, 3,5,6]
        result = sum(data)
        self.assertEqual(result, 6)    

if __name__ == '__main__':
    unittest.main()