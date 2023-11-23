"""Ver persona"""
import tkinter as tk
from tkinter import ttk
from .util.persona import get_persona, get_arrestos_complice
from .util.ocurrencia_de_arresto import get_arrestos_implicado

datos_arresto = []
img = None
ButtonImg = None
ButtonSig = None
icono_grande = None
icono_chico = None
ButtonVer=None


class SeePersona(tk.Tk):
    """Página de exportación de datos"""

    def __init__(self,persona_id,persona=False,complice=False,arresto=False, arresto_id = 0, implicado = False):
        super().__init__()
        self.persona_id = persona_id
        self.complice = complice
        self.arresto = arresto
        self.arresto_id = arresto_id
        self.persona = persona
        self.implicado = implicado
        self.inicializar_gui()

    def inicializar_gui(self):
        """Configurar la interfaz gráfica"""
        self.title('Exportar Datos')
        self.geometry("1000x750")
        self.resizable(0, 0)

        
        
        if self.persona and self.implicado == False and self.complice == False:
            bg_file = './src/img/persona_see.png'
        elif self.arresto:
            bg_file = './src/img/persona_see_2.png'
        elif self.complice:
            bg_file = './src/img/complice_see.png'
        elif self.implicado:
            bg_file = './src/img/implicado_see.png'          

        sig_file = './src/img/see_persona_btn/senas_btn.png'
        back_file = './src/img/back_button.png'
        ver_file= './src/img/see_persona_btn/ver_btn.png'

        global icono_grande
        icono_grande = tk.PhotoImage(file='./src/img/icon-32.png')

        global icono_chico
        icono_chico = tk.PhotoImage(file='./src/img/icon-16.png')

        self.iconphoto(False, icono_grande, icono_chico)

        global img
        img = tk.PhotoImage(file=bg_file)

        global ButtonImg
        ButtonImg = tk.PhotoImage(file=back_file)

        global ButtonSig
        ButtonSig=tk.PhotoImage(file=sig_file)

        global ButtonVer
        ButtonVer=tk.PhotoImage(file=ver_file)

        self.fondo = tk.Canvas(self, width=1000, height=750)
        self.fondo.create_image(0, 0, image=img, anchor='nw')
        self.fondo.pack()

        persona_data = get_persona(self.persona_id)
        
        c_text = tk.StringVar()
        c_text.set(persona_data[0][0])
        self.cedula_text = tk.Entry(
            self,background="white", font=("Cascadia Code Normal", 16), fg="#EFA11A",textvariable=c_text,state='readonly')
        self.cedula_text.config(bd=0)
        self.cedula_text.place(x=206.9, y=160, height=31, width=210)
        self.cedula_text.lift()

        n_text = tk.StringVar()
        n_text.set(persona_data[0][1])
        self.nombre_text = tk.Entry(
            self,background="white", font=("Cascadia Code Normal", 16), fg="#EFA11A",textvariable=n_text,state='readonly')
        self.nombre_text.config(bd=0)
        self.nombre_text.place(x=207.9, y=220, height=31, width=210)
        self.nombre_text.lift()

        ap_text = tk.StringVar()
        ap_text.set(persona_data[0][2])
        self.apellido_text = tk.Entry(
            self,background="white", font=("Cascadia Code Normal", 16), fg="#EFA11A",textvariable=ap_text,state='readonly')
        self.apellido_text.config(bd=0)
        self.apellido_text.place(x=207.7, y=280, height=31, width=210)
        self.apellido_text.lift()

        al_text = tk.StringVar()
        al_text.set(persona_data[0][8])
        self.alias_text = tk.Entry(
            self,background="white", font=("Cascadia Code Normal", 16), fg="#EFA11A",textvariable=al_text, state='readonly')
        self.alias_text.config(bd=0)
        self.alias_text.place(x=206.7, y=340, height=31, width=210)
        self.alias_text.lift()

        sex_text = tk.StringVar()
        sex_text.set(persona_data[0][4])
        self.sexo_text = tk.Entry(
            self,background="white", font=("Cascadia Code Normal", 16), fg="#EFA11A",textvariable=sex_text, state='readonly')
        self.sexo_text.config(bd=0)
        self.sexo_text.place(x=207.9, y=400, height=31, width=210)
        self.sexo_text.lift()

        naci_text = tk.StringVar()
        naci_text.set(persona_data[0][3])
        self.nacimiento_text = tk.Entry(
            self,background="white", font=("Cascadia Code Normal", 16), fg="#EFA11A",textvariable=naci_text, state='readonly')
        self.nacimiento_text.config(bd=0)
        self.nacimiento_text.place(x=259.5, y=460, height=31, width=210)
        self.nacimiento_text.lift()

        nd_text = tk.StringVar()
        nd_text.set(persona_data[0][7])
        self.nacionalidad_text = tk.Entry(
            self,background="white", font=("Cascadia Code Normal", 16), fg="#EFA11A",textvariable=nd_text, state='readonly')
        self.nacionalidad_text.config(bd=0)
        self.nacionalidad_text.place(x=646.9, y=400, height=31, width=304.3)
        self.nacionalidad_text.lift()

        t_text = tk.StringVar()
        t_text.set(persona_data[0][5])
        self.telefono_text = tk.Entry(
            self,background="white", font=("Cascadia Code Normal", 16), fg="#EFA11A",textvariable=t_text, state='readonly')
        self.telefono_text.config(bd=0)
        self.telefono_text.place(x=646.9, y=460, height=31, width=304.3)
        self.telefono_text.lift()

        d_text = tk.StringVar()
        d_text.set(persona_data[0][6])
        self.direccion_text = tk.Entry(
            self,background="white", font=("Cascadia Code Normal", 16), fg="#EFA11A",textvariable=d_text, state='readonly')
        self.direccion_text.config(bd=0)
        self.direccion_text.place(x=231.5, y=520, height=31, width=719.6)
        self.direccion_text.lift()

        self.btn_senas= tk.Button(
            bd=0, image=ButtonSig, activebackground='#021118', command=self.to_senas)
        self.btn_senas.place(x=716.1, y=575.5, height=79, width=235)

        self.btn_back = tk.Button(
            bd=0, image=ButtonImg, activebackground='#021118', command=self.back_to_show)
        self.btn_back.place(x=75, y=87.3, height=53, width=95)
           
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
            
        if self.arresto != True and self.persona != True:    
            #combobox
            
            arrestos= list()
            if self.complice:
                self.arrestos_data = get_arrestos_complice(self.persona_id)
            elif self.implicado:
                self.arrestos_data = get_arrestos_implicado(self.persona_id)
            
            if self.arrestos_data == []:
                arrestos = ["No hay"]
            else:
                for i in range(len(self.arrestos_data)):
                    arrestos.append(self.arrestos_data[i][1])      
            self.arrestos_box = ttk.Combobox(
                state="readonly",
                values=arrestos,
                font=("Cascadia Code Normal", 16),
            )
            self.arrestos_box.current(0)
            self.arrestos_box.place(x=231.5, y=580, height=31, width=210)
            self.arrestos_box.pack
            
            self.btn_ver= tk.Button(
            bd=0, image=ButtonVer, activebackground='#021118', command=self.to_arresto)
            self.btn_ver.place(x=451.6, y=580, height=31, width=139.8)
            
        elif self.persona and self.implicado == False and self.complice == False:
            self.combostyle.theme_use('combostyle')
            arrestos_implicado= list()
            
            self.arrestos_implicado_data = get_arrestos_complice(self.persona_id)
            
            
            if self.arrestos_implicado_data == []:
                arrestos_implicado = ["No hay"]
            else:
                for i in range(len(self.arrestos_implicado_data)):
                    arrestos_implicado.append(self.arrestos_implicado_data[i][1])      
            self.arrestos_implicado_box = ttk.Combobox(
                state="readonly",
                values=arrestos_implicado,
                font=("Cascadia Code Normal", 16),
            )
            self.arrestos_implicado_box.current(0)
            self.arrestos_implicado_box.place(x=113.5, y=615, height=31, width=210)
            self.arrestos_implicado_box.pack
            
            self.btn_ver_implicado= tk.Button(
            bd=0, image=ButtonVer, activebackground='#021118', command=self.to_arresto_implicado)
            self.btn_ver_implicado.place(x=144.4, y=670, height=31, width=139.8)

            arrestos_complice= list()
            self.arrestos_complice_data = get_arrestos_implicado(self.persona_id)
            
            if self.arrestos_complice_data == []:
                arrestos_complice = ["No hay"]
            else:
                for i in range(len(self.arrestos_complice_data)):
                    arrestos_complice.append(self.arrestos_complice_data[i][1])      
            self.arrestos_complice_box = ttk.Combobox(
                state="readonly",
                values=arrestos_complice,
                font=("Cascadia Code Normal", 16),
            )
            self.arrestos_complice_box.current(0)
            self.arrestos_complice_box.place(x=414.8, y=616, height=31, width=210)
            self.arrestos_complice_box.pack
            
            self.btn_ver_complice= tk.Button(
            bd=0, image=ButtonVer, activebackground='#021118', command=self.to_arresto_complice)
            self.btn_ver_complice.place(x=446.4, y=671, height=31, width=139.8)
                
    def back_to_show(self):
        """Volver al menu"""
        if self.persona:
            from pages.show_persona import MostrarPersonas
            self.destroy()
            MostrarPersonas()
        if self.arresto and self.complice:
            from pages.see_arresto import SeeArresto
            self.destroy()
            SeeArresto(arresto_id=self.arresto_id)
        elif self.arresto:
            from pages.see_arresto import SeeArresto
            self.destroy()
            SeeArresto(arresto_id=self.arresto_id)
        elif self.complice:
            from pages.show_complice import MostrarComplice
            self.destroy()
            MostrarComplice()
        elif self.implicado:
            from pages.show_implicado import MostrarImplicados
            self.destroy()
            MostrarImplicados()
            
    def to_senas(self):
        from pages.see_senas_identificacion import SeeSenas
        self.destroy()
        SeeSenas(persona_id=self.persona_id, complice=self.complice,
                 arresto=self.arresto,arresto_id=self.arresto_id,persona=self.persona, implicado=self.implicado)
    
    def to_arresto(self):
        from pages.see_arresto import SeeArresto
        index_id = self.arrestos_box.current()
        arresto = self.arrestos_data[index_id][0]
        self.destroy()
        SeeArresto(persona_id=self.persona_id, complice=self.complice,
                 persona=False,arresto_id=arresto,implicado=self.implicado)
    def to_arresto_implicado(self):
        from pages.see_arresto import SeeArresto
        index_id = self.arrestos_implicado_box.current()
        arresto = self.arrestos_implicado_data[index_id][0]
        self.destroy()
        SeeArresto(persona_id=self.persona_id, complice=self.complice,
                 persona=True,arresto_id=arresto)
        
    def to_arresto_complice(self):
        from pages.see_arresto import SeeArresto
        index_id = self.arrestos_complice_box.current()
        arresto = self.arrestos_complice_data[index_id][0]
        self.destroy()
        SeeArresto(persona_id=self.persona_id, complice=self.complice,
                 persona=True,arresto_id=arresto)

def main():
    """Renderizar la aplicacion"""
    app = SeePersona()
    app.mainloop()


if __name__ == '__main__':
    main()
