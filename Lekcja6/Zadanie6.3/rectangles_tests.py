import unittest
from rectangles import Rectangle

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

if __name__ == "__main__":
    unittest.main()