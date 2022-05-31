import main
import unittest
from unittest.mock import patch
import sys

class ZybookTests(unittest.TestCase):
    def test_circleTest(self):
        self.assertEqual(78.5, main.circleArea(5), 'Circle function is not implmented correctly.')

    def test_riangleTest(self):
        self.assertEqual(21.0, main.triangleArea(6,7), 'Triangle function is not implemented correctly')

    def test_trapezoidTest(self):
        self.assertEqual(8.0, main.trapezoidArea(1,3,4), 'Trapezoid function is not implemented correctly')

    @patch('builtins.print')
    def test_printShapeInfoTest(self, mock_print):
        main.printShapeInfo('circle', 28.26)
        mock_print.assert_called_with('The area of this circle is 28.26cm\u00b2')

if __name__ == '__main__':
    unittest.main()