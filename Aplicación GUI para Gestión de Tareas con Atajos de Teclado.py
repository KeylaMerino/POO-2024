import tkinter as tk
from tkinter import messagebox

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Tareas")

        # Campo de entrada para las tareas
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)
        self.task_entry.bind("<Return>", self.add_task)

        # Lista de tareas
        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=50, height=10)
        self.task_listbox.grid(row=1, column=0, padx=10, pady=10)

        # Botones
        self.add_button = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=10)

        self.complete_button = tk.Button(root, text="Completar Tarea", command=self.complete_task)
        self.complete_button.grid(row=1, column=1, padx=10)

        self.delete_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.grid(row=2, column=1, padx=10)

        # Atajos de teclado
        self.root.bind("<c>", self.complete_task)
        self.root.bind("<Delete>", self.delete_task)
        self.root.bind("<Escape>", lambda event: root.quit())

    # Función para añadir tarea
    def add_task(self, event=None):
        task = self.task_entry.get()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Entrada Vacía", "No puedes añadir una tarea vacía")

    # Función para completar tarea
    def complete_task(self, event=None):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            task = self.task_listbox.get(selected_task_index)
            if not task.startswith("[COMPLETADA]"):
                self.task_listbox.delete(selected_task_index)
                self.task_listbox.insert(selected_task_index, f"[COMPLETADA] {task}")
        except IndexError:
            messagebox.showwarning("Selecciona una tarea", "Por favor selecciona una tarea para completar")

    # Función para eliminar tarea
    def delete_task(self, event=None):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_task_index)
        except IndexError:
            messagebox.showwarning("Selecciona una tarea", "Por favor selecciona una tarea para eliminar")

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
