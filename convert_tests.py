import unittest
from keyboard import str_to_float


class TestConversionFunctions(unittest.TestCase):
   def test_str_to_float_valid(self):
       self.assertEqual(str_to_float("3.5"), 3.5)
       self.assertEqual(str_to_float("0"), 0.0)
       self.assertEqual(str_to_float("-2.3"), -2.3)


   def test_str_to_float_invalid(self):
       self.assertIsNone(str_to_float("abc"))
       self.assertIsNone(str_to_float(""))
       self.assertIsNone(str_to_float("1.2.3"))




if __name__ == '__main__':
   unittest.main()

