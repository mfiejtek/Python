from fracs import *
import unittest

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(add_frac([3,4],[2,5]), [23,20])
        self.assertEqual(add_frac([-1,6],[1,2]), [1,3])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(sub_frac([5, 4], [2, 4]), [3, 4])
        self.assertEqual(sub_frac([1, 3], [2, 3]), [-1, 3])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([1,2],[1,3]), [1,6])
        self.assertEqual(mul_frac([3,5],[10,9]), [2,3])
        self.assertEqual(mul_frac([-2,7],[3,4]), [-3,14])

    def test_div_frac(self):
        self.assertEqual(div_frac([1,2],[1,3]), [3,2])
        self.assertEqual(div_frac([3,4],[2,5]), [15,8])
        self.assertEqual(div_frac([-2,7],[3,4]), [-8,21])

    def test_is_positive(self):
        self.assertTrue(is_positive([2,5]))
        self.assertTrue(is_positive([1,2]))
        self.assertFalse(is_positive([-1,2]))
        self.assertFalse(is_positive([1,-2]))

    def test_is_zero(self):
        self.assertTrue(is_zero(self.zero))
        self.assertTrue(is_zero([0,5]))
        self.assertFalse(is_zero([1,2]))

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([1,2],[3,4]), -1)
        self.assertEqual(cmp_frac([2,3],[2,3]), 0)
        self.assertEqual(cmp_frac([5,2],[2,3]), 1)
    

    def test_frac2float(self):
        self.assertEqual(frac2float([3,4]), 0.75)
        self.assertEqual(frac2float([5,2]), 2.5)
        self.assertEqual(frac2float([-1,8]), -0.125)

if __name__ == "__main__":
    unittest.main()
