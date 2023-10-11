import unittest
import main
import calculator
import io
import sys

class TestMainProgram(unittest.TestCase):

    def test_get_float_input_valid(self):
        sys.stdin = io.StringIO('3.14\n')
        result = main.get_float_input("Enter a number: ")
        self.assertEqual(result, 3.14)

    def test_get_float_input_invalid(self):
        sys.stdin = io.StringIO('abc\n5.0\n')
        result = main.get_float_input("Enter a number: ")
        self.assertEqual(result, 5.0)

    def test_main_program(self):
        sys.stdin = io.StringIO('5.5\n3.0\ntest_results.json\n')
        main.main()

if __name__ == '__main__':
    unittest.main()
