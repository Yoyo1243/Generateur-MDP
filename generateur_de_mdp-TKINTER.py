# modules
from tkinter import *
from random import randint, choice
import string

# fonction
def gen_psw():
    psw_min = 6
    psw_max = 12
    all_chars = string.ascii_letters + string.punctuation + string.digits

    password = "".join(choice(all_chars) for x in range(randint(psw_min,psw_max)))
    password_input.delete(0, END)
    password_input.insert(0, password)  
        
        
    
# fenetre
window = Tk()

# personaliser
window.title("Mon app")
window.geometry("480x360")
window.minsize(480, 360)
window.config(background='grey')

# frame
frame = Frame(window, bd='1', bg='grey')
frame.pack(expand=YES)

# texte
titre = Label(frame, text='Whello', bg='grey', font=("", 40))
titre.pack(expand=YES)

# input
password_input = Entry(frame, bg='grey')
password_input.pack()

# bouton
button_generate_password = Button(frame, text="Générer", font=('', 25), bg='grey', fg='white', relief=SUNKEN, command=gen_psw)
button_generate_password.pack(pady=10, fill=X)

# afficher
window.mainloop()