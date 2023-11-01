"""Registro del Complices"""
from tkinter import *
from tkinter.ttk import Combobox

root = Tk()
root.title("Registro Complices")

# create a label and input field with tkinter of name,
# date of born, sex, phone number, address, civil status, nationality.
name_label = Label(root, text="Nombre:")
name_label.grid(row=0, column=0, padx=10, pady=10)
name_entry = Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=10)

dob_label = Label(root, text="Fecha de nacimiento:")
dob_label.grid(row=1, column=0, padx=10, pady=10)
dob_entry = Entry(root)
dob_entry.grid(row=1, column=1, padx=10, pady=10)


sex_label = Label(root, text="Sexo:")
sex_label.grid(row=2, column=0, padx=10, pady=10)

combo = Combobox(
    state="readonly",
    values=["M", "F"]
)
combo.grid(row=2, column=1, padx=10, pady=10)

phone_label = Label(root, text="Número de teléfono:")
phone_label.grid(row=3, column=0, padx=10, pady=10)
phone_entry = Entry(root)
phone_entry.grid(row=3, column=1, padx=10, pady=10)

address_label = Label(root, text="Dirección:")
address_label.grid(row=4, column=0, padx=10, pady=10)
address_entry = Entry(root)
address_entry.grid(row=4, column=1, padx=10, pady=10)

civil_status_label = Label(root, text="Estado civil:")
civil_status_label.grid(row=5, column=0, padx=10, pady=10)
civil_status_entry = Combobox(
    state="readonly",
    values=["Casado", "Soltero"]
)
civil_status_entry.grid(row=5, column=1, padx=10, pady=10)

nationality_label = Label(root, text="Nacionalidad:")
nationality_label.grid(row=6, column=0, padx=10, pady=10)
nationality_entry = Entry(root)
nationality_entry.grid(row=6, column=1, padx=10, pady=10)

alias_label = Label(root, text="Alias:")
alias_label.grid(row=7, column=0, padx=10, pady=10)
alias_entry = Entry(root)
alias_entry.grid(row=7, column=1, padx=10, pady=10)

# create a button to command of function to save
#  the data in a python dictionary and show it in a label


def save_data():
    """Create a dictionary"""
    criminal_data = {
        "Nombre": name_entry.get(),
        "Fecha de nacimiento": dob_entry.get(),
        "Sexo": combo.get(),
        "Número de teléfono": phone_entry.get(),
        "Dirección": address_entry.get(),
        "Estado civil": civil_status_entry.get(),
        "Nacionalidad": nationality_entry.get(),
        "Alias": alias_entry.get()
    }
    for key, value in criminal_data.items():
        display_label.config(text=display_label.cget(
            "text") + f"{key}: {value}\n")


save_button = Button(root, text="Guardar", command=save_data)
save_button.grid(row=8, column=0, padx=10, pady=10)

# create a label to display the saved data
display_label = Label(root, text="")
display_label.grid(row=8, column=1, padx=10, pady=10)

root.mainloop()
