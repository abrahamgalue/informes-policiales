"""Exportar Datos"""
import tkinter as tk
from tkinter import ttk
datos_arresto = []
img = None
ButtonImg = None
ButtonVer = None
ButtonEditar = None
ButtonBorrar = None
icono_grande = None
icono_chico = None

class ExportarDatos(tk.Tk):
    """Página de exportación de datos"""

    def __init__(self):
        super().__init__()
        
        
        self.inicializar_gui()

    def inicializar_gui(self):
        """Configurar la interfaz gráfica"""
        self.title('Exportar Datos')
        self.geometry("1000x750")
        self.resizable(0, 0)

        bg_file = './src/img/arrestos_show.png'
        ver_file = './src/img/show_btn/ver_btn.png'
        editar_file = './src/img/show_btn/editar_btn.png'
        borrar_file = './src/img/show_btn/borrar_btn.png'
        back_file = './src/img/back_button.png'

        global icono_grande
        icono_grande = tk.PhotoImage(file='./src/img/icon-32.png')

        global icono_chico
        icono_chico = tk.PhotoImage(file='./src/img/icon-16.png')

        self.iconphoto(False, icono_grande, icono_chico)

        global img
        img = tk.PhotoImage(file=bg_file)

        global ButtonImg
        ButtonImg = tk.PhotoImage(file=back_file)

        global ButtonVer
        ButtonVer = tk.PhotoImage(file=ver_file)

        global ButtonEditar
        ButtonEditar = tk.PhotoImage(file=editar_file)

        global ButtonBorrar
        ButtonBorrar = tk.PhotoImage(file=borrar_file)

        self.fondo = tk.Canvas(self, width=1000, height=750)
        self.fondo.create_image(0, 0, image=img, anchor='nw')
        self.fondo.pack()
        
        style_tree = ttk.Style()
        style_tree.configure("Treeview", background="#01060a", fieldbackground="#01060a", foreground="white",font=("Cascadia Code", 16))
        columns = ('Id', 'Fecha', 'Delito','Nacimiento','Cedula')
        tree = ttk.Treeview(self, show='headings', columns=columns)
        
        tree.column('Id', width=95, minwidth=95, stretch=False)
        tree.column('Fecha',width=197, minwidth=197, stretch=False)
        tree.column('Delito',width=309, minwidth=309, stretch=False)
        tree.column('Cedula',width=282, minwidth=282, stretch=False)
        
        
        tree.place(x=55,y=192,height=358.6,width=883.2)
        tree.heading('Cedula', text='')
        #Scrollbar
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.place(x=938.2,y=192,height=358.6,width=13.8)
        
        
        from util.ocurrencia_de_arresto import get_arrestos
        arresto_data = get_arrestos()    
        for i in range(len(arresto_data)):
            tree.insert('', tk.END, values=(arresto_data[i][0],arresto_data[i][1],arresto_data[i][4],arresto_data[i][7]))
        # self.list_implicados = tk.Listbox()
        # self.list_implicados.insert(0, "Python")
        # self.list_implicados.place(x=55,y=192,height=358.6,width=883.2)
         
        self.btn_ver = tk.Button(
            bd=0, image=ButtonVer, activebackground='#01060a')
        self.btn_ver.place(x=230.4, y=580, height=92, width=151)

        self.btn_editar = tk.Button(
            bd=0, image=ButtonEditar, activebackground='#01060a')
        self.btn_editar.place(x=424.4, y=580, height=92, width=151)

        self.btn_borrar = tk.Button(
            bd=0, image=ButtonBorrar, activebackground='#01060a')
        self.btn_borrar.place(x=618.6, y=580, height=92, width=151)

        self.btn_back = tk.Button(
            bd=0, image=ButtonImg, activebackground='#021118', command=self.back_to_menu)
        self.btn_back.place(x=75, y=87.3, height=53, width=95)

    def back_to_menu(self):
        """Volver al menu"""
        from main import MenuApp
        self.destroy()
        MenuApp()


def main():
    """Renderizar la aplicacion"""
    app = ExportarDatos()
    app.mainloop()


if __name__ == '__main__':
    main()