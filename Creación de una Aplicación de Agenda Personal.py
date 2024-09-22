import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry 

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("600x400")

        # Frame para la lista de eventos
        self.frame_lista = tk.Frame(self.root)
        self.frame_lista.pack(pady=10, padx=10, fill="both", expand=True)

        # TreeView para mostrar los eventos
        self.tree = ttk.Treeview(self.frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack(fill="both", expand=True)

        # Frame para la entrada de nuevos eventos
        self.frame_entrada = tk.Frame(self.root)
        self.frame_entrada.pack(pady=10, padx=10)

        # Etiquetas y campos de entrada
        tk.Label(self.frame_entrada, text="Fecha:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_fecha = DateEntry(self.frame_entrada, width=15, background='darkblue',
                                    foreground='white', borderwidth=2, date_pattern='yyyy-mm-dd')
        self.entry_fecha.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.frame_entrada, text="Hora:").grid(row=1, column=0, padx=5, pady=5)
        self.entry_hora = tk.Entry(self.frame_entrada, width=15)
        self.entry_hora.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.frame_entrada, text="Descripción:").grid(row=2, column=0, padx=5, pady=5)
        self.entry_descripcion = tk.Entry(self.frame_entrada, width=40)
        self.entry_descripcion.grid(row=2, column=1, padx=5, pady=5)

        # Frame para los botones
        self.frame_botones = tk.Frame(self.root)
        self.frame_botones.pack(pady=10)

        # Botones
        self.btn_agregar = tk.Button(self.frame_botones, text="Agregar Evento", command=self.agregar_evento)
        self.btn_agregar.grid(row=0, column=0, padx=10)

        self.btn_eliminar = tk.Button(self.frame_botones, text="Eliminar Evento", command=self.eliminar_evento)
        self.btn_eliminar.grid(row=0, column=1, padx=10)

        self.btn_salir = tk.Button(self.frame_botones, text="Salir", command=self.root.quit)
        self.btn_salir.grid(row=0, column=2, padx=10)

    def agregar_evento(self):
        fecha = self.entry_fecha.get()
        hora = self.entry_hora.get()
        descripcion = self.entry_descripcion.get()

        if fecha and hora and descripcion:
            self.tree.insert('', 'end', values=(fecha, hora, descripcion))
            self.limpiar_campos()
        else:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")

    def eliminar_evento(self):
        selected_item = self.tree.selection()
        if selected_item:
            self.tree.delete(selected_item)
        else:
            messagebox.showwarning("Advertencia", "Seleccione un evento para eliminar.")

    def limpiar_campos(self):
        self.entry_fecha.set_date("")
        self.entry_hora.delete(0, 'end')
        self.entry_descripcion.delete(0, 'end')


if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()


