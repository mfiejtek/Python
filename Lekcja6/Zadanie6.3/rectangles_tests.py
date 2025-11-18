import unittest
from rectangles import Rectangle
from points import Point

class TestFractions(unittest.TestCase):
    def test_str(self):
        self.assertEqual(str(Rectangle(-1,-1,1,1)), "[(-1, -1), (1, 1)]")
        self.assertEqual(str(Rectangle(-2,3,4,5)), "[(-2, 3), (4, 5)]")
        self.assertEqual(str(Rectangle(3,1,2,10)), "[(3, 1), (2, 10)]")

    def test_repr(self):
        self.assertEqual(repr(Rectangle(-1,-1,1,1)), "Rectangle(-1, -1, 1, 1)")
        self.assertEqual(repr(Rectangle(2,3,4,5)), "Rectangle(2, 3, 4, 5)")
        self.assertEqual(repr(Rectangle(1,11,12,-10)), "Rectangle(1, 11, 12, -10)")

    def test_eq(self):
        self.assertTrue(Rectangle(-1,-1,1,1) == Rectangle(-1,-1,1,1))
        self.assertTrue(Rectangle(-1,-1,1,1) == Rectangle(1,1,-1,-1))
        self.assertFalse(Rectangle(-1,1,1,1) == Rectangle(1,-1,1,1))
    
    def test_ne(self):
        self.assertFalse(Rectangle(-1,-1,1,1) != Rectangle(-1,-1,1,1))
        self.assertFalse(Rectangle(-1,-1,1,1) != Rectangle(1,1,-1,-1))
        self.assertTrue(Rectangle(-1,1,1,1) != Rectangle(1,-1,1,1))
    
    def test_center(self):
        self.assertEqual(Rectangle(-1,-1,1,1).center(), Point(0, 0))
        self.assertEqual(Rectangle(0,0,4,6).center(), Point(2, 3))
        self.assertEqual(Rectangle(-3,5,3,11).center(), Point(0, 8))

    def test_area(self):
        self.assertEqual(Rectangle(-1,-1,1,1).area(), 4)
        self.assertEqual(Rectangle(0,0,4,6).area(), 24)
        self.assertEqual(Rectangle(-3,5,3,11).area(), 36)
        
    def test_move(self):
        rect = Rectangle(-1,-1,1,1)
        rect.move(2,3)
        self.assertEqual(rect, Rectangle(1,2,3,4))
        
        rect = Rectangle(0,0,4,6)
        rect.move(-1,-2)
        self.assertEqual(rect, Rectangle(-1,-2,3,4))
        
        rect = Rectangle(-3,5,3,11)
        rect.move(0,-5)
        self.assertEqual(rect, Rectangle(-3,0,3,6))


if __name__ == "__main__":
    unittest.main()