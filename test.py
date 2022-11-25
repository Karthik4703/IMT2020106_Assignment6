import unittest
from power import power
class Testpower(unittest.TestCase):
    def test_power1(self):
        result = power(1,5)
        self.assertEqual(result,1)
    def test_power2(self):
        result = power(2,3)
        self.assertEqual(result,8)
    def test_power3(self):
        result = power(3,4)
        self.assertEqual(result,81)
    def test_power4(self):
        result = power(4,2)
        self.assertEqual(result,15)
    def test_power5(self):
        result = power(5,3)
        self.assertEqual(result,25)

if __name__ == '__main__':
    unittest.main()
