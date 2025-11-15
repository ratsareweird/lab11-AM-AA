import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######## Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(2, 7), 9)
        self.assertEqual(add(149, 463), 612)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(4, 3), 1)
        self.assertEqual(subtract(2, 7), -5)
        self.assertEqual(subtract(463, 100), 363)
    ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertAlmostEqual(multiply(.5, .85), .425)
        self.assertEqual(multiply(210, 0), 0)
        self.assertEqual(multiply(91, 210), 19110)

    def test_divide(self): # 3 assertions
        self.assertAlmostEqual(div(120,7), 17.142857142857142)
        self.assertEqual(div(210,2), 105)
        self.assertEqual(div(60,.4), 150)

    ##########################
    ####### Partner 2
    def test_divide_by_zero(self): # 1 assertion
        self.assertRaises(div(4, 0), ZeroDivisionError)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(2, 4), 2)
        self.assertEqual(logarithm(3, 27), 3)
        self.assertEqual(logarithm(2, 8), 3)



    def test_log_invalid_base(self): # 1 assertion
        self.assertRaises(logarithm(-5, -12), ValueError)

    ##########################
    ######## Partner 1
    def test_log_invalid_argument(self):
        self.assertRaises(logarithm(0,5), ValueError)# 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3,4), 5)
        self.assertAlmostEqual(hypotenuse(8,10), 12.80624847486569)
        self.assertAlmostEqual(hypotenuse(10,10), 14.142135623730951)

    def test_sqrt(self): # 3 assertions
        self.assertRaises(square_root(-10), ValueError)
        self.assertEqual(square_root(25), 5)
        self.assertAlmostEqual(square_root(10), 3.1622)


# Do not touch this
if __name__ == "__main__":
    unittest.main()