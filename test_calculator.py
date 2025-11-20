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
        self.assertEqual(sub(5,3),2)
        self.assertEqual(sub(-5,-3),-2)
        self.assertEqual(sub(0,7),-7)


    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0,10)

    def test_logarithm(self):
        self.assertAlmostEqual(log(10,100),2)
        self.assertAlmostEqual(log(2,8),3)
        self.assertAlmostEqual(log(5,1),0)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            log(0,10)

    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()