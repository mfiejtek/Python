import unittest
from rectangles import Rectangle
from points import Point

class TestFractions(unittest.TestCase):
    def test_init_invalid(self):
        with self.assertRaises(ValueError):
            Rectangle(2, 2, 1, 1)
        with self.assertRaises(ValueError):
            Rectangle(0, 0, 0, 5)
        with self.assertRaises(ValueError):
            Rectangle(-1, -1, -2, -2)

    def test_str(self):
        self.assertEqual(str(Rectangle(-1,-1,1,1)), "[(-1, -1), (1, 1)]")
        self.assertEqual(str(Rectangle(2,3,4,5)), "[(2, 3), (4, 5)]")
        self.assertEqual(str(Rectangle(1,11,2,12)), "[(1, 11), (2, 12)]")

    def test_repr(self):
        self.assertEqual(repr(Rectangle(-1,-1,1,1)), "Rectangle(-1, -1, 1, 1)")
        self.assertEqual(repr(Rectangle(2,3,4,5)), "Rectangle(2, 3, 4, 5)")
        self.assertEqual(repr(Rectangle(1,11,2,12)), "Rectangle(1, 11, 2, 12)")

    def test_eq(self):
        self.assertTrue(Rectangle(-1,-1,1,1) == Rectangle(-1,-1,1,1))
        self.assertTrue(Rectangle(1,1,2,2) == Rectangle(1,1,2,2))
        self.assertFalse(Rectangle(1,1,2,3) == Rectangle(1,1,2,4))
    
    def test_ne(self):
        self.assertFalse(Rectangle(-1,-1,1,1) != Rectangle(-1,-1,1,1))
        self.assertFalse(Rectangle(1,1,2,2) != Rectangle(1,1,2,2))
        self.assertTrue(Rectangle(1,1,2,3) != Rectangle(1,1,2,4))
    
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
    
    def test_intersection(self):
        rect1 = Rectangle(0,0,4,4)
        rect2 = Rectangle(2,2,6,6)
        self.assertEqual(rect1.intersection(rect2), Rectangle(2,2,4,4))
        
        rect1 = Rectangle(0,0,2,2)
        rect2 = Rectangle(3,3,5,5)
        self.assertIsNone(rect1.intersection(rect2))
        
        rect1 = Rectangle(-1,-1,1,1)
        rect2 = Rectangle(-2,-2,0,0)
        self.assertEqual(rect1.intersection(rect2), Rectangle(-1,-1,0,0))

    def test_cover(self):
        rect1 = Rectangle(0,0,4,4)
        rect2 = Rectangle(2,2,6,6)
        self.assertEqual(rect1.cover(rect2), Rectangle(0,0,6,6))
        
        rect1 = Rectangle(0,0,2,2)
        rect2 = Rectangle(3,3,5,5)
        self.assertEqual(rect1.cover(rect2), Rectangle(0,0,5,5))
        
        rect1 = Rectangle(-1,-1,1,1)
        rect2 = Rectangle(-2,-2,0,0)
        self.assertEqual(rect1.cover(rect2), Rectangle(-2,-2,1,1))

    def test_make4(self):
        rect = Rectangle(0,0,4,4)
        quads = rect.make4()
        expected = (Rectangle(0,0,2,2), Rectangle(2,0,4,2),
                    Rectangle(0,2,2,4), Rectangle(2,2,4,4))
        self.assertEqual(quads, expected)
        
        rect = Rectangle(-2,-2,2,2)
        quads = rect.make4()
        expected = (Rectangle(-2,-2,0,0), Rectangle(0,-2,2,0),
                    Rectangle(-2,0,0,2), Rectangle(0,0,2,2))
        self.assertEqual(quads, expected)
        
        rect = Rectangle(1,1,5,5)
        quads = rect.make4()
        expected = (Rectangle(1,1,3,3), Rectangle(3,1,5,3),
                    Rectangle(1,3,3,5), Rectangle(3,3,5,5))
        self.assertEqual(quads, expected)


if __name__ == "__main__":
    unittest.main()