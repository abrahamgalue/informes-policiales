"""Reseñas Policiales"""
import tkinter as tk
from pages.arresto import FormularioArresto


class MenuApp(tk.Tk):
    """Menu de Reseñas Policiales"""

    def __init__(self):
        super().__init__()

        self.inicializar_gui()

    def inicializar_gui(self):
        """Configurar la interfaz gráfica"""
        self.title('Reseñas Policiales')
        self.minsize(400, 400)
        self.resizable(0, 0)

        title_label = tk.Label(text='RESEÑAS POLICIALES')
        title_label.grid(row=0, column=3, pady=10)

        btn_registrar = tk.Button(
            text='Registrar Nuevo Caso', command=self.to_register)
        btn_registrar.grid(row=1, column=0)

        btn_view_logs = tk.Button(
            text='Ver Registros')
        btn_view_logs.grid(row=1, column=4)

    def to_register(self):
        """Create a new record"""
        self.destroy()
        FormularioArresto()

    def clean(self):
        """Limpiar los campos del formulario"""
        self.date_entry.delete(0, tk.END)
        self.judgment_entry.delete(0, tk.END)


def main():
    """Renderizar la aplicacion"""
    app = MenuApp()
    app.mainloop()


if __name__ == '__main__':
    main()
