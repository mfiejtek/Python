import tkinter as tk
from tkinter import messagebox
import sys
import os

# --- HACK NA IMPORTY ---
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
sys.path.append(project_root)
# -----------------------

from implementation.RedBlackTree import RedBlackTree
from implementation.Node import RED, BLACK

class RBTVisualizer:
    def __init__(self, root):
        self.tree = RedBlackTree()
        self.root = root
        self.root.title("Wizualizacja Red-Black Tree")
        
        self.width = 1000
        self.height = 600
        self.node_radius = 20
        self.y_dist = 60 

        self.main_frame = tk.Frame(root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(self.main_frame, width=self.width, height=self.height, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.controls_frame = tk.Frame(root, bg="#eee", pady=10)
        self.controls_frame.pack(fill=tk.X)

        tk.Label(self.controls_frame, text="Wartość:", bg="#eee").pack(side=tk.LEFT, padx=5)
        
        self.entry = tk.Entry(self.controls_frame)
        self.entry.pack(side=tk.LEFT, padx=5)
        self.entry.bind('<Return>', lambda event: self.add_node()) # Enter dodaje

        btn_insert = tk.Button(self.controls_frame, text="Dodaj (Insert)", command=self.add_node, bg="#ccffcc")
        btn_insert.pack(side=tk.LEFT, padx=5)

        btn_delete = tk.Button(self.controls_frame, text="Usuń (Delete)", command=self.delete_node, bg="#ffcccc")
        btn_delete.pack(side=tk.LEFT, padx=5)

        btn_clear = tk.Button(self.controls_frame, text="Wyczyść", command=self.clear_tree)
        btn_clear.pack(side=tk.RIGHT, padx=20)

        for val in [20, 15, 25, 10, 5, 1, 30]:
            self.tree.insert(val)
        self.draw_tree()

    def add_node(self):
        try:
            val = int(self.entry.get())
            self.tree.insert(val)
            self.entry.delete(0, tk.END)
            self.draw_tree()
        except ValueError:
            messagebox.showerror("Błąd", "Wprowadź liczbę całkowitą!")

    def delete_node(self):
        try:
            val_str = self.entry.get()
            if not val_str:
                return 
                
            val = int(val_str)
            
            success = self.tree.delete_node(val)
            
            if not success:
                messagebox.showerror("Błąd usuwania", f"Klucz {val} nie istnieje w drzewie!")
            else:
                self.entry.delete(0, tk.END)
                self.draw_tree()
                
        except ValueError:
            messagebox.showerror("Błąd", "Wprowadź poprawną liczbę całkowitą!")

    def clear_tree(self):
        self.tree = RedBlackTree()
        self.draw_tree()

    # --- LOGIKA RYSOWANIA ---

    def draw_tree(self):
        self.canvas.delete("all")
        if self.tree.root != self.tree.TNULL:
            self._draw_node_recursive(self.tree.root, self.width // 2, 40, self.width // 4)

    def _draw_node_recursive(self, node, x, y, x_offset):
        if node == self.tree.TNULL:
            return

        if node.left != self.tree.TNULL:
            next_x = x - x_offset
            next_y = y + self.y_dist
            self.canvas.create_line(x, y, next_x, next_y, width=2)
            self._draw_node_recursive(node.left, next_x, next_y, x_offset // 2)

        if node.right != self.tree.TNULL:
            next_x = x + x_offset
            next_y = y + self.y_dist
            self.canvas.create_line(x, y, next_x, next_y, width=2)
            self._draw_node_recursive(node.right, next_x, next_y, x_offset // 2)

        r = self.node_radius
        color = "red" if node.color == RED else "black"
        outline = "black"
                
        self.canvas.create_oval(x - r, y - r, x + r, y + r, fill=color, outline=outline, width=2)

        text_color = "white"
        self.canvas.create_text(x, y, text=str(node.val), fill=text_color, font=("Arial", 10, "bold"))

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1000x700") 
    app = RBTVisualizer(root)
    root.mainloop()