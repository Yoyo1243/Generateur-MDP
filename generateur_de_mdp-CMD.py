# !/usr/bin/python3
# modules
from termcolor import cprint
import random
import string
import os
import time

# variables
caractrer = string.ascii_letters + string.digits + string.punctuation
caractrer_no_symboles = string.ascii_letters + string.digits
colors = ['grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan']
logo = """
  ____             __        __            _
 |  _ \ __ _ ___ __\ \      / /__  _ __ __| |
 | |_) / _` / __/ __\ \ /\ / / _ \| '__/ _` |
 |  __/ (_| \__ \__  \ V  V / (_) | | | (_| |
 |_|   \__,_|___/___/ \_/\_/ \___/|_|  \__,_|\n"""

# fonction
def main():
    os.system("clear")
    cprint(logo, f'{random.choice(colors)}', attrs=['bold'])
    print(' 1: mot de passe avec symbole \n 2: mot de passe sans symbole\n 3: annuler\n')
    answer = input(" 1, 2 ou 3 ➜ ")

    if answer == '1':
        password_symbol()
    if answer == '2':
        password_no_symbol()
    if answer == '3':
        leave()
    else:
        cprint(" Pas la bonne valeur, 1/2/3", 'red', attrs=['bold'])
        time.sleep(1)
        os.system("clear")
        main()

def password_symbol():
    password = ''
    os.system("clear")
    cprint(logo, f'{random.choice(colors)}', attrs=['bold'])
    time.sleep(0.5)

    leght_password = int(input(" Longeur mot de passe : "))
    for i in range(leght_password):
        password += random.choice(caractrer)
    print(f'\n {password}\n')
    exit()

def password_no_symbol():
    password = ''
    os.system("clear")
    cprint(logo, f'{random.choice(colors)}', attrs=['bold'])
    time.sleep(0.5)
    leght_password = int(input("Longeur mot de passe : "))
    for i in range(leght_password):
        password += random.choice(caractrer_no_symboles)
    print(f'\n{password}\n')
    exit()

def leave():
    os.system("clear")
    cprint(logo, f'{random.choice(colors)}', attrs=['bold'])
    time.sleep(0.5)
    print("Vous allez quitter ...")
    time.sleep(1)
    os.system("clear")
    cprint(logo, f'{random.choice(colors)}', attrs=['bold'])
    time.sleep(0.5)
    print("[                    ] 0% ")
    time.sleep(0.5)
    os.system("clear")
    cprint(logo, f'{random.choice(colors)}', attrs=['bold'])
    print("[=====               ] 25%")
    time.sleep(0.5)
    os.system("clear")
    cprint(logo, f'{random.choice(colors)}', attrs=['bold'])
    print("[==========          ] 50%")
    time.sleep(0.5)
    os.system("clear")
    cprint(logo, f'{random.choice(colors)}', attrs=['bold'])
    print("[===============     ] 75%")
    time.sleep(0.5)
    os.system("clear")
    cprint(logo, f'{random.choice(colors)}', attrs=['bold'])
    print("[====================] 100%")
    time.sleep(1.75)
    os.system("clear")
    exit()


if __name__ == "__main__":
    main()