import unittest
import random

from implementation.RedBlackTree import RedBlackTree
from implementation.Node import RED, BLACK

class TestRedBlackTree(unittest.TestCase):

    def setUp(self):
        """Uruchamiane przed każdym testem. Tworzy czyste drzewo."""
        self.bst = RedBlackTree()

    def _validate_rbt_properties(self, node):
        """
        Pomocnicza metoda rekurencyjna weryfikująca poprawność drzewa RBT.
        Zwraca 'czarną wysokość' węzła, jeśli poddrzewo jest poprawne.
        Rzuca błąd (AssertionError), jeśli zasady są złamane.
        """
        # Baza rekurencji: jeśli dotarliśmy do TNULL (liścia)
        if node == self.bst.TNULL:
            # TNULL jest zawsze czarny
            self.assertEqual(node.color, BLACK, "TNULL musi być czarny")
            return 1  # Liczymy czarną wysokość jako 1 dla TNULL
        
        # 1. Sprawdź konflikt Czerwony-Czerwony
        if node.color == RED:
            self.assertNotEqual(node.parent.color, RED, f"Błąd: Węzeł {node.val} jest CZERWONY i ma CZERWONEGO rodzica")
            self.assertNotEqual(node.left.color, RED, f"Błąd: Węzeł {node.val} jest CZERWONY i ma CZERWONE lewe dziecko")
            self.assertNotEqual(node.right.color, RED, f"Błąd: Węzeł {node.val} jest CZERWONY i ma CZERWONE prawe dziecko")

        # 2. Sprawdź poprawność relacji BST
        if node.left != self.bst.TNULL:
            self.assertTrue(node.left.val <= node.val, f"Błąd BST: Lewe dziecko {node.left.val} > Rodzic {node.val}")
        if node.right != self.bst.TNULL:
            self.assertTrue(node.right.val >= node.val, f"Błąd BST: Prawe dziecko {node.right.val} < Rodzic {node.val}")

        # 3. Rekurencja dla dzieci i obliczanie Czarnej Wysokości
        left_black_height = self._validate_rbt_properties(node.left)
        right_black_height = self._validate_rbt_properties(node.right)

        # 4. Sprawdź, czy czarna wysokość jest taka sama dla obu ścieżek
        self.assertEqual(left_black_height, right_black_height, 
                         f"Naruszenie czarnej wysokości w węźle {node.val}: L={left_black_height}, R={right_black_height}")

        # Zwróć wysokość dla rodzica 
        return left_black_height + (1 if node.color == BLACK else 0)

    def validate_tree(self):
        """Wrapper uruchamiający walidację od korzenia."""
        if self.bst.root == self.bst.TNULL:
            return
        
        # Korzeń musi być czarny
        self.assertEqual(self.bst.root.color, BLACK, "Korzeń musi być CZARNY")
        self._validate_rbt_properties(self.bst.root)

    # --- TESTY WŁAŚCIWE ---

    def test_empty_tree(self):
        self.assertEqual(self.bst.root, self.bst.TNULL)

    def test_simple_insert(self):
        """Sprawdza proste wstawienie i kolorowanie korzenia"""
        self.bst.insert(10)
        self.assertEqual(self.bst.root.val, 10)
        self.assertEqual(self.bst.root.color, BLACK) # Korzeń zawsze czarny
        self.validate_tree()

    def test_insert_rotation_case(self):
        """Wstawianie posortowanych danych (wymusza rotacje w lewo)"""
        data = [10, 20, 30, 40, 50]
        for val in data:
            self.bst.insert(val)
            self.validate_tree()
        
        self.assertEqual(self.bst.root.val, 20)
        self.assertEqual(self.bst.root.left.val, 10)
        self.assertEqual(self.bst.root.right.val, 40)

    def test_reverse_insert(self):
        """Wstawianie odwrotnie posortowanych danych (wymusza rotacje w prawo)"""
        data = [50, 40, 30, 20, 10]
        for val in data:
            self.bst.insert(val)
            self.validate_tree()

    def test_delete_leaf(self):
        """Usuwanie liścia (czerwonego i czarnego)"""
        self.bst.insert(10)
        self.bst.insert(5)  
        self.bst.insert(15) 
        self.validate_tree()

        self.bst.delete_node(5)
        self.validate_tree()
        # Sprawdzamy czy zniknął
        self.assertEqual(self.bst.root.left, self.bst.TNULL)

    def test_delete_root(self):
        """Usuwanie korzenia"""
        self.bst.insert(20)
        self.bst.insert(10)
        self.bst.insert(30)
        
        self.bst.delete_node(20)
        self.validate_tree()
        self.assertNotEqual(self.bst.root.val, 20) # Stary korzeń zniknął
        self.assertEqual(self.bst.root.color, BLACK) # Nowy korzeń jest czarny

    def test_delete_complex(self):
        """Bardziej złożony scenariusz usuwania"""
        elements = [10, 20, 30, 40, 50, 60, 70, 80]
        for el in elements:
            self.bst.insert(el)
        
        # Usuwamy węzeł ze środka
        self.bst.delete_node(40) 
        self.validate_tree()
        
        # Usuwamy węzeł powodujący dużo rebalansowania
        self.bst.delete_node(20)
        self.validate_tree()

    def test_large_random_dataset(self):
        """1000 losowych liczb, wstawianie i usuwanie"""
        data = list(range(1000))
        random.shuffle(data)
        
        # 1. Wstawianie
        for val in data:
            self.bst.insert(val)
        
        self.validate_tree() # Sprawdź poprawność całego dużego drzewa
        
        # 2. Usuwanie losowych 200 elementów
        to_delete = data[:200]
        for val in to_delete:
            self.bst.delete_node(val)
            # Sprawdzanie przy każdym kroku
            self.validate_tree()
        
        self.validate_tree()

if __name__ == '__main__':
    unittest.main()