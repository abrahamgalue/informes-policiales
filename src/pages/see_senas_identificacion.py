"""Ver persona"""
import tkinter as tk
from tkinter import ttk
from pages.util.senas_de_identificacion import get_seña
datos_arresto = []
img = None
ButtonImg = None
ButtonSig = None
icono_grande = None
icono_chico = None
ButtonVer=None


class SeeSenas(tk.Tk):
    """Página de exportación de datos"""

    def __init__(self,persona_id,complice,arresto,arresto_id):
        super().__init__()
        self.persona_id = persona_id
        self.complice = complice
        self.arresto = arresto
        self.arresto_id = arresto_id
        self.inicializar_gui()

    def inicializar_gui(self):
        """Configurar la interfaz gráfica"""
        self.title('Exportar Datos')
        self.geometry("1000x750")
        self.resizable(0, 0)

        bg_file = './src/img/senas_see.png'
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

        senas_data = get_seña(self.persona_id)
        
        p_text = tk.StringVar()
        p_text.set(senas_data[0][0])
        self.peso_text = tk.Entry(
            self,background="white", font=("Cascadia Code Normal", 16), fg="#EFA11A",textvariable=p_text,state='readonly')
        self.peso_text.config(bd=0)
        self.peso_text.place(x=203.1, y=334.9, height=31, width=210)
        self.peso_text.lift()
        #altura
        a_text = tk.StringVar()
        a_text.set(senas_data[0][1])
        self.altura_text = tk.Entry(
            self,background="white", font=("Cascadia Code Normal", 16), fg="#EFA11A",textvariable=a_text,state='readonly')
        self.altura_text.config(bd=0)
        self.altura_text.place(x=203.1, y=394.9, height=31, width=210)
        self.altura_text.lift()

        #cabello
        C_text = tk.StringVar()
        C_text.set(senas_data[0][3])
        self.Cabello_text = tk.Entry(
            self,background="white", font=("Cascadia Code Normal", 16), fg="#EFA11A",textvariable=C_text,state='readonly')
        self.Cabello_text.config(bd=0)
        self.Cabello_text.place(x=203.1, y=454.9, height=31, width=210)
        self.Cabello_text.lift()

        #color de piel
        cp_text = tk.StringVar()
        cp_text.set(senas_data[0][2])
        self.color_piel_text = tk.Entry(
            self,background="white", font=("Cascadia Code Normal", 16), fg="#EFA11A",textvariable=cp_text, state='readonly')
        self.color_piel_text.config(bd=0)
        self.color_piel_text.place(x=725.8, y=334.9, height=31, width=210)
        self.color_piel_text.lift()
        #ojos
        o_text = tk.StringVar()
        o_text.set(senas_data[0][5])
        self.ojos_text = tk.Entry(
            self,background="white", font=("Cascadia Code Normal", 16), fg="#EFA11A",textvariable=o_text, state='readonly')
        self.ojos_text.config(bd=0)
        self.ojos_text.place(x=725.8, y=394.9, height=31, width=210)
        self.ojos_text.lift()
        #color de cabello

        Cc_text = tk.StringVar()
        Cc_text.set(senas_data[0][4])
        self.color_cabello_text = tk.Entry(
            self,background="white", font=("Cascadia Code Normal", 16), fg="#EFA11A",textvariable=Cc_text, state='readonly')
        self.color_cabello_text.config(bd=0)
        self.color_cabello_text.place(x=725.8, y=454.9, height=31, width=210)
        self.color_cabello_text.lift()

        #OTRAS CARACTERISTICAS
        oc_text = tk.StringVar()
        if senas_data[0][6] == None:
            oc_text.set("Ninguna")
        else:
            oc_text.set(senas_data[0][6])
        self.otras_caracteristicas_text = tk.Entry(
            self,background="white", font=("Cascadia Code Normal", 16), fg="#EFA11A",textvariable=oc_text, state='readonly')
        self.otras_caracteristicas_text.config(bd=0)
        self.otras_caracteristicas_text.place(x=370.4, y=514.9, height=31, width=565.4)
        self.otras_caracteristicas_text.lift()

        self.btn_back = tk.Button(
            bd=0, image=ButtonImg, activebackground='#021118', command=self.back_to_persona)
        self.btn_back.place(x=75, y=87.3, height=53, width=95)

    def back_to_persona(self):
        """Volver al menu"""
        from pages.see_persona import SeePersona
        self.destroy()
        SeePersona(persona_id=self.persona_id,complice=self.complice, arresto=self.arresto, 
                   arresto_id=self.arresto_id)


def main():
    """Renderizar la aplicacion"""
    app = SeeSenas()
    app.mainloop()


if __name__ == '__main__':
    main()
