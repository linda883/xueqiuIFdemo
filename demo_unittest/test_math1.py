from parameterized import parameterized_class
import unittest


@parameterized_class([
   {"a": 3, "expected": 2},
   {"b": 5, "expected": -4},
])
class TestMathClassDict(unittest.TestCase):
    a = 1
    b = 1

    def test_subtract(self):
        self.assertEqual(self.a - self.b, self.expected)



