"""Exportar Datos"""
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from .util.persona import get_personas,get_persona, get_complices_arresto
from .util.ocurrencia_de_arresto import get_arresto

img = None
ButtonImg = None
ButtonSig = None
ButtonAdd = None
ButtonBorrar = None
icono_grande = None
icono_chico = None

class PersonasArresto(tk.Tk):
    """Página de exportación de datos"""

    def __init__(self, edit=False, arresto_id=0):
        super().__init__()
        self.edit = edit
        self.arresto_id = arresto_id
        self.inicializar_gui()

    def inicializar_gui(self):
        """Configurar la interfaz gráfica"""
        self.title('Exportar Datos')
        self.geometry("1000x750")
        self.resizable(0, 0)

        bg_file = './src/img/select_implicado_complice.png'
        sig_file = './src/img/sig_button.png'
        add_file = './src/img/select_arresto_btn/agregar_btn.png'
        borrar_file = './src/img/select_arresto_btn/eliminar_btn.png'
        back_file = './src/img/back_button.png'

        global icono_grande
        icono_grande = tk.PhotoImage(file='./src/img/icon-32.png')

        global icono_chico
        icono_chico = tk.PhotoImage(file='./src/img/icon-16.png')

        self.iconphoto(False, icono_grande, icono_chico)

        global img
        img = tk.PhotoImage(file=bg_file)

        global ButtonSig
        ButtonSig = tk.PhotoImage(file=sig_file)
        
        global ButtonImg
        ButtonImg = tk.PhotoImage(file=back_file)

        global ButtonAdd
        ButtonAdd = tk.PhotoImage(file=add_file)

        global ButtonBorrar
        ButtonBorrar = tk.PhotoImage(file=borrar_file)

        self.fondo = tk.Canvas(self, width=1000, height=750)
        self.fondo.create_image(0, 0, image=img, anchor='nw')
        self.fondo.pack()
        
        if self.edit:
            implicado = get_arresto(self.arresto_id)[0][7]
            complices = get_complices_arresto(self.arresto_id)
            
        self.combostyle = ttk.Style()

        self.combostyle.theme_create('combostyle', parent='alt',
                                settings={'TCombobox':
                                          {'configure':
                                           {'selectbackground': '#EFA11A',  # Color al seleccionar una opcion
                                            'fieldbackground': '#EFA11A',  # Color del fondo
                                            'background': '#EFA11A',  # color de la flechita
                                            # tipo de fuente
                                            'font': ('Cascadia Code Normal', 16),
                                            'foreground': 'white',  # color de la fuente
                                            'borderwidth': '0',
                                            'highlightthickness': '0'  # borde
                                            }}}
                                )
        # ATTENTION: this applies the new style 'combostyle' to all ttk.Combobox
        self.combostyle.theme_use('combostyle')
        personas = list()
        personas_data = get_personas()    
        for i in range(len(personas_data)):
            personas.append(personas_data[i][0])
        self.implicado_entry = ttk.Combobox(
            state="readonly",
            values=personas,
            font=("Cascadia Code Normal", 16),
        )
        if self.edit:
            implicado_index = personas.index(implicado)
            self.implicado_entry.current(implicado_index)
        else:
            self.implicado_entry.current(0)
        self.implicado_entry.place(x=240, y=180, height=31, width=210)
        self.implicado_entry.pack
        
        self.combostyle.theme_use('combostyle')
        self.complice_entry = ttk.Combobox(
            state="readonly",
            values=personas,
            font=("Cascadia Code Normal", 16),
        )
        self.complice_entry.current(0)
        self.complice_entry.place(x=240, y=230, height=31, width=210)
        self.complice_entry.pack
        
        self.style_tree = ttk.Style()
        self.style_tree.theme_use("clam")
        self.style_tree.configure("Treeview", background="#01060a", fieldbackground="#01060a", foreground="white",font=("Cascadia Code Normal", 16))
        self.style_tree.map('Treeview',
            background=[('selected', 'white')],
            fieldbackground=[('selected', '#01060a')],
            foreground=[('selected', '#01060a')]
        )
        self.style = ttk.Style()
        self.style.configure("Treeview.Heading", background="black", foreground="white",font=("Cascadia Code Normal", 16))
        columns = ('Cedula', 'Nombre', 'Apellido')
        self.tree = ttk.Treeview(self, show='headings', columns=columns)
        
        self.tree.column('Cedula', width=115, minwidth=115, stretch=False)
        self.tree.column('Nombre',width=232, minwidth=232, stretch=False)
        self.tree.column('Apellido',width=233, minwidth=233, stretch=False)
        
        self.tree.heading('Cedula', text='Cedula')
        self.tree.heading('Nombre', text='Nombre')
        self.tree.heading('Apellido', text='Apellido')
        
        self.tree.place(x=85,y=295.1,height=250,width=583.2)
        #Scrollbar
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.place(x=668.2,y=295.1,height=250,width=13.8)
        if self.edit:
            for i in range(len(complices)):
                self.tree.insert('', tk.END, values=complices[i])       
         
        self.btn_add = tk.Button(
            bd=0, image=ButtonAdd, activebackground='#01060a',command=self.add_complice)
        self.btn_add.place(x=480, y=230, height=31, width=140)

        self.btn_borrar = tk.Button(
            bd=0, image=ButtonBorrar, activebackground='#01060a', command=self.delete_complice)
        self.btn_borrar.place(x=700, y=404, height=31, width=140)

        self.btn_next = tk.Button(
            bd=0, image=ButtonSig, activebackground='black',command=self.save_data)
        self.btn_next.place(x=716, y=575, height=79, width=235)
        
        self.btn_back = tk.Button(
            bd=0, image=ButtonImg, activebackground='#021118', command=self.back_to_menu)
        self.btn_back.place(x=75, y=87.3, height=53, width=95)
 
    def add_complice(self):        
        global complice
        complice = str(self.complice_entry.get())
        complice_in_tree = self.is_complice_in_tree(complice)
        if complice_in_tree:  
            messagebox.showwarning('Complice Invalido',
                f'La persona de cedula {complice} ya esta agregada.')
        else:
            complice_data = get_persona(complice)
            self.tree.insert('', tk.END, 
                            values=(complice_data[0][0],complice_data[0][1],complice_data[0][2]))
            
    def is_complice_in_tree(self,complice_id):
        personas_in_tree = list()
        treeIDs = self.tree.get_children()
        for item in treeIDs:
            personas_in_tree.append(str(self.tree.item(item)["values"][0]))
        print('Personas Agregadas:',personas_in_tree)
        if complice_id in personas_in_tree:
            return True
        else:
            return False
        
        
    def delete_complice(self):
        # Get the selected item
        selected_item = self.tree.selection()[0]
        # Delete the selected item
        self.tree.delete(selected_item)
    
    def save_data(self):
        implicado_id = self.implicado_entry.get()
        persona_in_tree = self.is_complice_in_tree(implicado_id)
        if persona_in_tree:
            messagebox.showwarning('Implicado Invalido',
                f'El implicado no puede ser un complice.')
            return
    
        implicado = str(implicado_id)
        treeIDs = self.tree.get_children()
        lista = []
        for item in treeIDs:
            lista.append(str(self.tree.item(item)["values"][0]))
        complices = lista
        print('Implicado:',implicado)
        print('Complices:',complices)
        
        from pages.arresto_condena import FormularioArresto
        self.destroy()
        FormularioArresto(implicado,complices,edit=self.edit,arresto_id=self.arresto_id)
            
    def back_to_menu(self):
        """Volver al menu"""
        if self.edit:
            from pages.show_arrestos import MostrarArrestos
            self.destroy()
            MostrarArrestos()
        else:
            from main import MenuApp
            self.destroy()
            MenuApp()

def main():
    """Renderizar la aplicacion"""
    app = PersonasArresto()
    app.mainloop()


if __name__ == '__main__':
    main()