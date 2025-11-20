#https://github.com/anayamackle/lab11-RB-AM
#Partner 1: Anaya Mackle
#Partner 2: Ryan Buehler
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(-1,1),0)
        self.assertEqual(add(0,0),0)
        self.assertEqual(add(10.5,20.3),30.8)


    def test_subtract(self):
        self.assertEqual(subtract(5,3),2)
        self.assertEqual(subtract(-5,-3),-2)
        self.assertEqual(subtract(0,7),-7)


    ######## Partner 1
    def test_multiply(self):
        self.assertEqual(mul(3,7),21)
        self.assertEqual(mul(-4,5),-20)
        self.assertEqual(mul(2.5,4),10.0)

    def test_divide(self):
        self.assertEqual(div(5,20),4)
        self.assertEqual(div(3,9),3)
        self.assertEqual(div(-4,20),-5)

    ######## Partner 2
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0,10)

    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(10,100),2)
        self.assertAlmostEqual(logarithm(2,8),3)
        self.assertAlmostEqual(logarithm(5,1),0)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(0,10)

    
    ######## Partner 1
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(10,-8)

    def test_hypotenuse(self):
        self.assertEqual(hypotenuse(3,4),5)
        self.assertEqual(hypotenuse(5,12),13)
        self.assertEqual(hypotenuse(8,15),17)

    def test_sqrt(self):
        self.assertEqual(square_root(16),4)
        self.assertEqual(square_root(0),0)
        with self.assertRaises(ValueError):
            square_root(-9)

# Do not touch this
if __name__ == "__main__":
    unittest.main()