"""Exportar Datos"""
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
img = None
ButtonImg = None
ButtonVer = None
ButtonEditar = None
ButtonBorrar = None
icono_grande = None
icono_chico = None

class MostrarComplice(tk.Tk):
    """Página de exportación de datos"""

    def __init__(self):
        super().__init__()
        
        
        self.inicializar_gui()

    def inicializar_gui(self):
        """Configurar la interfaz gráfica"""
        self.title('Exportar Datos')
        self.geometry("1000x750")
        self.resizable(0, 0)

        bg_file = './src/img/complices_show.png'
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
        
        self.style_tree = ttk.Style()
        self.style_tree.theme_use("clam")
        self.style_tree.configure("Treeview", background="#01060a", fieldbackground="#01060a", foreground="white",font=("Cascadia Code Normal", 16))
        self.style_tree.map('Treeview',
            background=[('selected', 'white')],
            fieldbackground=[('selected', '#01060a')],
            foreground=[('selected', '#01060a')]
        )
        self.style = ttk.Style()
        self.style.configure("Treeview.Heading", background="#01060a", foreground="white",font=("Cascadia Code Normal", 16))
        self.style.map('Treeview.Heading',
            background=[('selected', '#01060a')],
            fieldbackground=[('selected', '#01060a')],
            foreground=[('selected', '#01060a')]
        )
        columns = ('Cedula', 'Nombre', 'Apellido','Nacimiento','Arrestos')
        self.tree = ttk.Treeview(self, show='headings', columns=columns)
        
        self.tree.column('Cedula', width=172, minwidth=172, stretch=False)
        self.tree.column('Nombre',width=169, minwidth=169, stretch=False)
        self.tree.column('Apellido',width=171, minwidth=171, stretch=False)
        self.tree.column('Nacimiento',width=218, minwidth=218, stretch=False)
        self.tree.column('Arrestos',width=154, minwidth=154, anchor=tk.CENTER, stretch=False)
        
        self.tree.place(x=55,y=192,height=358.6,width=883.2)
        self.tree.heading('Cedula', text='')
        #Scrollbar
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.place(x=938.2,y=192,height=358.6,width=13.8)
        
        
        from .util.persona import get_complices
        implicado_data = get_complices()    
        for i in range(len(implicado_data)):
            self.tree.insert('', tk.END, values=implicado_data[i])
                 
        self.btn_ver = tk.Button(
            bd=0, image=ButtonVer, activebackground='#01060a', command=self.see_complice)
        self.btn_ver.place(x=230.4, y=580, height=92, width=151)

        self.btn_editar = tk.Button(
            bd=0, image=ButtonEditar, activebackground='#01060a', command=self.edit_complice)
        self.btn_editar.place(x=424.4, y=580, height=92, width=151)

        self.btn_borrar = tk.Button(
            bd=0, image=ButtonBorrar, activebackground='#01060a', command=self.borrar_persona)
        self.btn_borrar.place(x=618.6, y=580, height=92, width=151)

        self.btn_back = tk.Button(
            bd=0, image=ButtonImg, activebackground='#021118', command=self.back_to_menu)
        self.btn_back.place(x=75, y=87.3, height=53, width=95)

    def back_to_menu(self):
        """Volver al menu"""
        from pages.visualize import VisualizePersona
        self.destroy()
        VisualizePersona()
        
    def get_complice_id(self):
        if len(self.tree.selection()) > 0:
            selected_item = self.tree.selection()[0]
            complice_id = self.tree.item(selected_item)['values'][0]
            print(complice_id)
            return complice_id
    
    def edit_complice(self):
        id = self.get_complice_id()
        if id == None:
            messagebox.showinfo(
            'Mensaje', f'Ninguna persona ha sido seleccionada.')
        else:
            from pages.criminal import FormularioCriminal
            self.destroy()
            FormularioCriminal(edit=True,persona_id=id, complice=True)
    
    def see_complice(self):
        id = self.get_complice_id()
        if id == None:
            messagebox.showinfo(
            'Mensaje', f'Ninguna persona ha sido seleccionada.')
        else:
            from pages.see_persona import SeePersona
            self.destroy()
            SeePersona(persona_id=id,complice=True)
    
    def borrar_persona(self):
        id = self.get_implicado_id()
        if id == None:
            messagebox.showinfo(
            'Mensaje', f'Ninguna persona ha sido seleccionada.')
        else:
            borrar = messagebox.askyesno('Mensaje', '¿Desea borrar a la persona?. Esto borrará toda su informacion y los arrestos en los que esta implicado.')
            if borrar:
                from pages.util.persona import delete_persona
                delete_persona(id)
                messagebox.showinfo(
                'Mensaje', f'La persona de id {id} ha sido borrada de forma satisfactoria.')
                self.destroy()
                MostrarComplice()

def main():
    """Renderizar la aplicacion"""
    app = MostrarComplice()
    app.mainloop()


if __name__ == '__main__':
    main()