"""Registro del Criminal"""
from tkinter import *

root = Tk()
root.title("Registro Condena")

# create a label and input field with tkinter of name,
# date of born, sex, phone number, address, civil status, nationality.
date_label = Label(root, text="Fecha:")
date_label.grid(row=0, column=0, padx=10, pady=10)
date_entry = Entry(root)
date_entry.grid(row=0, column=1, padx=10, pady=10)

reason_label = Label(root, text="Motivo:")
reason_label.grid(row=1, column=0, padx=10, pady=10)
reason_entry = Entry(root)
reason_entry.grid(row=1, column=1, padx=10, pady=10)

judgment_label = Label(root, text="Sentencia:")
judgment_label.grid(row=2, column=0, padx=10, pady=10)
judgment_entry = Entry(root)
judgment_entry.grid(row=2, column=1, padx=10, pady=10)

# create a button to command of function to save
#  the data in a python dictionary and show it in a label


def save_data():
    """Create a dictionary"""
    criminal_data = {
        "Fecha": date_entry.get(),
        "Motivo": reason_entry.get(),
        "Sentencia": judgment_entry.get()
    }
    for key, value in criminal_data.items():
        display_label.config(text=display_label.cget(
            "text") + f"{key}: {value}\n")


save_button = Button(root, text="Guardar", command=save_data)
save_button.grid(row=4, column=0, padx=10, pady=10)

# create a label to display the saved data
display_label = Label(root, text="")
display_label.grid(row=4, column=1, padx=10, pady=10)

root.mainloop()
