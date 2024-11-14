import tkinter as tk
from criptare import *
from decriptare import *
from tkinter import filedialog
from tkinter import messagebox
custom_font = ("Times New Roman", 12)
def hex_string_to_matrix(input):
    if all(c in "0123456789ABCDEFabcdef" for c in input):
        # Convertim hex stringul în reprezentare bytes
        hex_bytes = bytes.fromhex(input)
        # Convertim fiecare byte în număr întreg
        elements = [int(byte) for byte in hex_bytes]
    else:
        # Convertim stringul în bytes
        string_bytes = input.encode()
        # Convertim bytes în reprezentare hex
        hex_string = string_bytes.hex()
        # Convertim hex stringul în reprezentare bytes
        hex_bytes = bytes.fromhex(hex_string)
        # Convertim fiecare byte în număr întreg
        elements = [int(byte) for byte in hex_bytes]

    matrix = [elements[i:i+4] for i in range(0, len(elements), 4)]
    transposed_matrix = [[row[i] for row in matrix] for i in range(4)]
    return transposed_matrix


def criptare():
    if len(entry_text.get())!=len(entry_key.get()):
        messagebox.showinfo("Pop-up", "Cheia si plaintext-ul trebuie sa aiba aceeasi lungime!")
    elif len(entry_text.get())!=32 or len(entry_key.get())!=32:
        messagebox.showinfo("Pop-up", "Cheia si plaintext-ul trebuie sa aiba o lungime de 128 biti, adica 32 de caractere!")
    else:
        text = hex_string_to_matrix(entry_text.get())
        key = hex_string_to_matrix(entry_key.get())
        key_expanded=key_expansion(key)
        encrypted_message = cipher(text, 10, key_expanded)
        encrypted_message_transposed = [[encrypted_message[j][i] for j in range(len(encrypted_message))] for i in range(len(encrypted_message[0]))]
        encrypted_hex_string = ''.join([''.join(['{:02X}'.format(element) for element in column]) for column in encrypted_message_transposed])
        grouped_encrypted_hex_string = ' '.join([encrypted_hex_string[i:i+8] for i in range(0, len(encrypted_hex_string), 8)])
        label_encrypted.config(text=grouped_encrypted_hex_string, font=('Times New Roman',12))

def decriptare():
    if len(entry_textd.get())!=len(entry_keyd.get()):
        messagebox.showinfo("Pop-up", "Cheia si plaintext-ul trebuie sa aiba aceeasi lungime!")
    elif len(entry_textd.get())!=32 or len(entry_keyd.get())!=32:
        messagebox.showinfo("Pop-up", "Cheia si plaintext-ul trebuie sa aiba o lungime de 128 biti, adica 32 de caractere!")
    else:
        textd = hex_string_to_matrix(entry_textd.get())
        keyd = hex_string_to_matrix(entry_keyd.get())
        key_expanded=key_expansiond(keyd)
        decrypted_message = invcipher(textd, 10, key_expanded)
        decrypted_message_transposed = [[decrypted_message[j][i] for j in range(len(decrypted_message))] for i in range(len(decrypted_message[0]))]
        decrypted_hex_string = ''.join([''.join(['{:02X}'.format(element) for element in column]) for column in decrypted_message_transposed])
        grouped_decrypted_hex_string = ' '.join([decrypted_hex_string[i:i+8] for i in range(0, len(decrypted_hex_string), 8)])
        label_decrypted.config(text=grouped_decrypted_hex_string,font=('Times New Roman',12))

def din_fisier_criptare():
    nume_fisier = filedialog.askopenfilename()
    with open(nume_fisier, "r") as file:
        plaintext=file.readline().strip()
        cheia=file.readline().strip()

    entry_text.delete(0,tk.END)
    entry_text.insert(0,plaintext)

    entry_key.delete(0,tk.END)
    entry_key.insert(0,cheia)

def din_fisier_decriptare():
    nume_fisier = filedialog.askopenfilename()
    with open(nume_fisier, "r") as file:
        plaintext=file.readline().strip()
        cheia=file.readline().strip()

    entry_textd.delete(0,tk.END)
    entry_textd.insert(0,plaintext)

    entry_keyd.delete(0,tk.END)
    entry_keyd.insert(0,cheia)

# Crearea ferestrei principale
root = tk.Tk()
root.title("AES")
root.geometry("800x600")

#criptare
label_info = tk.Label(root, text="Criptare:", font=custom_font)
label_info.pack(pady=(70,0))

text_intro=tk.Label(root, text="Introduceti textul:")
text_intro.pack()
entry_text = tk.Entry(root, width=50)
entry_text.pack()

text_key=tk.Label(root, text="Introduceti cheia:")
text_key.pack()
entry_key = tk.Entry(root, width=50)
entry_key.pack()

# Adăugarea unui buton
button_criptare = tk.Button(root, text="Criptare mesaj", command=criptare)
button_criptare.place(x=300,y=220)
#buton pentru incarcare din fisier
button_fisier = tk.Button(root, text="Incarcare Fisier", command=din_fisier_criptare)
button_fisier.place(x=410,y=220)

label_encrypted = tk.Label(root, text="Mesajul dupa criptare:")
label_encrypted.pack(pady=(5,10))

#decriptare
label_info1 = tk.Label(root, text="Decriptare:", font=custom_font)
label_info1.pack(pady=(50,0))

text_introd=tk.Label(root, text="Introduceti textul pentru decriptat:")
text_introd.pack()
entry_textd = tk.Entry(root, width=50)
entry_textd.pack()

text_keyd=tk.Label(root, text="Introduceti cheia:")
text_keyd.pack()
entry_keyd = tk.Entry(root, width=50)
entry_keyd.pack()

# Adăugarea unui buton
button_decriptare = tk.Button(root, text="Decriptare mesaj", command=decriptare)
button_decriptare.place(x=300,y=410)

#buton pentru incarcare din fisier
button_fisier1 = tk.Button(root, text="Incarcare Fisier", command=din_fisier_decriptare)
button_fisier1.place(x=410,y=410)

label_decrypted = tk.Label(root, text="Mesajul dupa decriptare:")
label_decrypted.pack(pady=(5,10))
# Menținerea ferestrei deschise
root.mainloop()


