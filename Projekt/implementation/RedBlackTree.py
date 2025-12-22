"""Implementacja drzewa czerwono-czarnego (Red-Black Tree).

Klasa dostarcza metody do wstawiania i usuwania elementów oraz pomocnicze
operacje potrzebne do utrzymania własności drzewa.
"""

from implementation.Node import BLACK, RED, Node

class RedBlackTree:
    """Struktura drzewa czerwono-czarnego z operacjami modyfikującymi.

    Atrybuty:
        TNULL: sentinel reprezentujący puste potomki (czarny)
        root: korzeń drzewa
    """
    def __init__(self):
        self.TNULL = Node(0)
        self.TNULL.color = BLACK
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL

    def left_rotate(self, x):
        """Wykonuje lewą rotację wokół węzła x.

        Używane przy przywracaniu równowagi drzewa.
        """
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x
        
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        """Wykonuje prawą rotację wokół węzła x.

        Używane przy przywracaniu równowagi drzewa.
        """
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x
        
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        
        y.right = x
        x.parent = y


    def fix_insert(self, k):
        """Naprawia własności drzewa po wstawieniu węzła k.

        Przywraca właściwości drzewa czerwono-czarnego poprzez odpowiednie
        rotacje i zmiany kolorów węzłów.
        """
        while k.parent.color == RED:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left

                if u.color == RED:
                    u.color = BLACK
                    k.parent.color = BLACK
                    k.parent.parent.color = RED
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)

                    k.parent.color = BLACK
                    k.parent.parent.color = RED
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right

                if u.color == RED:
                    u.color = BLACK
                    k.parent.color = BLACK
                    k.parent.parent.color = RED
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)

                    k.parent.color = BLACK
                    k.parent.parent.color = RED
                    self.right_rotate(k.parent.parent)

            if k == self.root:
                break

        self.root.color = BLACK

    def insert(self, key):
        """Wstawia wartość `key` do drzewa.

        Tworzy nowy węzeł i wstawia go zgodnie z własnością BST,
        a następnie wywołuje `fix_insert` w celu przywrócenia
        własności czerwono-czarnych.
        """
        node = Node(key)
        node.parent = None
        node.val = key
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = RED

        y = None
        x = self.root

        while x != self.TNULL:
            y = x
            if node.val < x.val:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y is None:
            self.root = node
        elif node.val < y.val:
            y.left = node
        else:
            y.right = node

        if node.parent is None:
            node.color = BLACK
            return

        if node.parent.parent is None:
            return

        self.fix_insert(node)
    
    # --- METODY POMOCNICZE DO USUWANIA ---

    def rb_transplant(self, u, v):
        """Zastępuje poddrzewo węzła `u` poddrzewem `v`.

        Używane wewnętrznie przy usuwaniu węzłów.
        """
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def minimum(self, node):
        """Zwraca węzeł o najmniejszej wartości w poddrzewie `node`."""
        while node.left != self.TNULL:
            node = node.left
        return node

    def fix_delete(self, x):
        """Naprawia własności drzewa po usunięciu węzła wskazywanego przez x.

        Operacja przywraca równowagę drzewa poprzez rotacje i zmiany kolorów.
        """
        while x != self.root and x.color == BLACK:
            if x == x.parent.left:
                w = x.parent.right

                if w.color == RED:
                    w.color = BLACK
                    x.parent.color = RED
                    self.left_rotate(x.parent)
                    w = x.parent.right

                if w.left.color == BLACK and w.right.color == BLACK:
                    w.color = RED
                    x = x.parent
                else:
                    if w.right.color == BLACK:
                        w.left.color = BLACK
                        w.color = RED
                        self.right_rotate(w)
                        w = x.parent.right

                    w.color = x.parent.color
                    x.parent.color = BLACK
                    w.right.color = BLACK
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left

                if w.color == RED:
                    w.color = BLACK
                    x.parent.color = RED
                    self.right_rotate(x.parent)
                    w = x.parent.left

                if w.right.color == BLACK and w.left.color == BLACK:
                    w.color = RED
                    x = x.parent
                else:
                    if w.left.color == BLACK:
                        w.right.color = BLACK
                        w.color = RED
                        self.left_rotate(w)
                        w = x.parent.left

                    w.color = x.parent.color
                    x.parent.color = BLACK
                    w.left.color = BLACK
                    self.right_rotate(x.parent)
                    x = self.root

        x.color = BLACK

    # --- GŁÓWNA METODA USUWANIA ---

    def delete_node(self, val):
        """Usuń węzeł o wartości `val` z drzewa."""
        return self._delete_node_helper(self.root, val)

    def _delete_node_helper(self, node, key):
        """Pomocnicza implementacja usuwania.

        Znajduje węzeł o danym kluczu, usuwa go zachowując własność BST,
        a następnie wywołuje `fix_delete` jeśli było to konieczne.
        """
        z = self.TNULL
        while node != self.TNULL:
            if node.val == key:
                z = node
            if node.val <= key:
                node = node.right
            else:
                node = node.left

        if z == self.TNULL:
            return False

        y = z
        y_original_color = y.color
        x = None

        # Standardowe usuwanie BST
        if z.left == self.TNULL:
            x = z.right
            self.rb_transplant(z, z.right)
        elif z.right == self.TNULL:
            x = z.left
            self.rb_transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.rb_transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self.rb_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color

        if y_original_color == BLACK:
            self.fix_delete(x)
        
        return True
    
    # --- WYSZUKIWANIE ---

    def search(self, k):
        """Publiczna metoda wyszukiwania."""
        return self._search_tree_helper(self.root, k)

    def _search_tree_helper(self, node, key):
        """Rekurencyjne przeszukiwanie drzewa."""
        if node == self.TNULL or key == node.val:
            return node

        if key < node.val:
            return self._search_tree_helper(node.left, key)
        
        return self._search_tree_helper(node.right, key)
