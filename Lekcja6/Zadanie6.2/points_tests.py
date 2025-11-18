from points import Point
import unittest

class TestPoint(unittest.TestCase): 
    def test_str(self):
        self.assertEqual(str(Point(1,2)), "(1, 2)")
        self.assertEqual(str(Point(2,3)), "(2, 3)")
        self.assertEqual(str(Point(-1,4)), "(-1, 4)")

    def test_repr(self):
        self.assertEqual(repr(Point(1,2)), "Point(1, 2)")
        self.assertEqual(repr(Point(2,3)), "Point(2, 3)")
        self.assertEqual(repr(Point(-1,4)), "Point(-1, 4)")
    
    def test_eq(self):
        self.assertTrue(Point(1,2) == Point(1,2))
        self.assertTrue(Point(2,4) == Point(2,4))
        self.assertFalse(Point(2,5) == Point(5,2))

    def test_ne(self):
        self.assertTrue(Point(2,1) != Point(1,2))
        self.assertTrue(Point(4,4) != Point(2,4))
        self.assertFalse(Point(2,5) != Point(2,5))
    
    def test_add(self):
        self.assertEqual(Point(1,2)+Point(2,3), Point(3,5))
        self.assertEqual(Point(2,4)+Point(4,5), Point(6,9))
        self.assertEqual(Point(-1,2)+Point(0,-3), Point(-1,-1))

    def test_sub(self):
        self.assertEqual(Point(1,2)-Point(2,3), Point(-1,-1))
        self.assertEqual(Point(2,4)-Point(4,5), Point(-2,-1))
        self.assertEqual(Point(-1,2)-Point(0,-3), Point(-1,5)) 
    
    def test_mul(self):
        self.assertEqual(Point(1,2)*Point(1,2), 5)
        self.assertEqual(Point(2,3)*Point(4,2), 14)
        self.assertEqual(Point(5,6)*Point(3,4), 39)
    
    def test_cross(self):
        self.assertEqual(Point(1,2).cross(Point(1,2)), 0)
        self.assertEqual(Point(2,3).cross(Point(4,2)), -8)
        self.assertEqual(Point(5,6).cross(Point(3,4)), 2)

    def test_length(self):
        self.assertEqual(Point(0,5).length(), 5)
        self.assertEqual(Point(6,0).length(), 6)
        self.assertEqual(Point(3,4).length(), 5)

    def test_hash(self):
        self.assertEqual(hash(Point(1,2)), hash((1,2)))
        self.assertEqual(hash(Point(3,2)), hash((3,2)))
        self.assertEqual(hash(Point(4,2)), hash((4,2)))

    


if __name__ == "__main__":
    unittest.main()