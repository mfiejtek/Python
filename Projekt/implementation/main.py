from RedBlackTree import RedBlackTree

if __name__ == "__main__":
    bst = RedBlackTree()
    
    elements = [10, 20, 30, 40, 50, 25]
    
    print("Wstawiam elementy:", elements)
    for el in elements:
        bst.insert(el)

    print("\nStruktura drzewa:")
    bst.print_tree()