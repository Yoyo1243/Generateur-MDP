# !/usr/bin/python3
# modules
from tkinter import *
from random import choice
import string

# variables
chars = string.ascii_letters + string.digits + string.punctuation

# fonction
def password_symbol():
    password = ''
    
    for i in range(int(value.get())):
        password += choice(chars)
    password_input.delete(0, END)
    password_input.insert(0, password)  


# fenetre
window = Tk()




# personaliser
window.title("Générateur De mot de passe")
window.geometry("450x300")
window.minsize(450, 300)
window.maxsize(450, 300)
window.config(background='grey')

# frame
frame = LabelFrame(window, padx=20, pady=20, bd='10', bg='grey')
frame.pack(fill="both", expand="yes")
#frame = Frame(window, bd='1', bg='grey')
# frame.pack(expand=YES)

frame3 = Frame(frame)
frame3.pack(side=RIGHT, padx=5, pady=5)

# roulette - nombre de caractère
value = IntVar()
scale = Scale(frame3, variable=value, from_=0, to=10)
scale.pack()

# texte
titre = Label(frame, text='Mot de passe', bg='grey', font=("", 25))
titre.pack(expand=YES)

# input
password_input = Entry(frame, bg='grey')
password_input.pack()

# bouton
button_generate_password = Button(frame, text="Générer", font=('', 30), bg='grey', relief=SUNKEN, command=password_symbol)
button_generate_password.pack(pady=10, fill=X)

# bouton 'stop'
stop = Button(window, text="STOP", font=('', 25), fg='red', relief=SUNKEN, command=window.quit)
stop.pack(padx=10, pady=10)

# afficher
window.mainloop()