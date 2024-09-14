import tkinter as tk
from tkinter import ttk

class SimpleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicación GUI Básica")

        # Etiqueta
        self.label = tk.Label(root, text="Ingrese información:")
        self.label.pack(pady=10)

        # Campo de texto
        self.text_entry = tk.Entry(root)
        self.text_entry.pack(pady=5)

        # Botón Agregar
        self.add_button = tk.Button(root, text="Agregar", command=self.add_info)
        self.add_button.pack(pady=5)

        # Botón Limpiar
        self.clear_button = tk.Button(root, text="Limpiar", command=self.clear_info)
        self.clear_button.pack(pady=5)

        # Lista para mostrar datos
        self.info_list = tk.Listbox(root)
        self.info_list.pack(pady=10, fill=tk.BOTH, expand=True)

    def add_info(self):
        info = self.text_entry.get()
        if info:
            self.info_list.insert(tk.END, info)
            self.text_entry.delete(0, tk.END)

    def clear_info(self):
        self.info_list.delete(0, tk.END)
        self.text_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleApp(root)
    root.mainloop()
