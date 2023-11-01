"""Señas de Identificación"""
from tkinter import *

root = Tk()
root.title("Registro Señas de Identificación")

# create a label and input field with tkinter of name,
# date of born, sex, phone number, address, civil status, nationality.
name_label = Label(root, text="Peso:")
name_label.grid(row=0, column=0, padx=10, pady=10)
name_entry = Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=10)

dob_label = Label(root, text="Altura:")
dob_label.grid(row=1, column=0, padx=10, pady=10)
dob_entry = Entry(root)
dob_entry.grid(row=1, column=1, padx=10, pady=10)

skin_label = Label(root, text="Piel:")
skin_label.grid(row=2, column=0, padx=10, pady=10)
skin_entry = Entry(root)
skin_entry.grid(row=2, column=1, padx=10, pady=10)

skin_color_label = Label(root, text="Color de piel:")
skin_color_label.grid(row=3, column=0, padx=10, pady=10)
skin_color_entry = Entry(root)
skin_color_entry.grid(row=3, column=1, padx=10, pady=10)

hair_label = Label(root, text="Cabello:")
hair_label.grid(row=4, column=0, padx=10, pady=10)
hair_entry = Entry(root)
hair_entry.grid(row=4, column=1, padx=10, pady=10)

eyes_color_label = Label(root, text="Color de ojos:")
eyes_color_label.grid(row=5, column=0, padx=10, pady=10)
eyes_color_entry = Entry(root)
eyes_color_entry.grid(row=5, column=1, padx=10, pady=10)

other_features_label = Label(root, text="Otras Características:")
other_features_label.grid(row=6, column=0, padx=10, pady=10)
other_features_entry = Entry(root)
other_features_entry.grid(row=6, column=1, padx=10, pady=10)

# create a button to command of function to save
#  the data in a python dictionary and show it in a label


def save_data():
    """Create a dictionary"""
    criminal_data = {
        "Peso": name_entry.get(),
        "Altura": dob_entry.get(),
        "Piel": skin_entry.get(),
        "Color de Piel": skin_color_entry.get(),
        "Cabello": hair_entry.get(),
        "Ojos": eyes_color_entry.get(),
        "Otras caracteristicas": other_features_entry.get()
    }
    for key, value in criminal_data.items():
        display_label.config(text=display_label.cget(
            "text") + f"{key}: {value}\n")


save_button = Button(root, text="Guardar", command=save_data)
save_button.grid(row=7, column=0, padx=10, pady=10)

# create a label to display the saved data
display_label = Label(root, text="")
display_label.grid(row=7, column=1, padx=10, pady=10)

root.mainloop()
