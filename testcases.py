import unittest
import functions

class Lab3TestCases(unittest.TestCase):
    def test_double_one(self):
        result = functions.double(2)
        expected = 4
        self.assertEqual(expected, result)

    def test_double_two(self):
        result = functions.double(3)
        expected = 6
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()

# No, if test_double_one came back okay, that does mean the function is okay.
# They answer just happened to be the same, we got lucky