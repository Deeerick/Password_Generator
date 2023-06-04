# ----- Imports ----- #
from tkinter import *
from tkinter import ttk
from tkinter import messagebox 
from PIL import ImageTk, Image 
import random
import string

# ----- Styles ----- #
color_0 = "#000000"  # Preta
color_1 = "#feffff"  # branca
color_2 = "#f05a43"  # Laranja
color_3 = "#18bf15"  # Green

fundo_dark="#484f60"
fundo_claro = "#fff"
fundo = color_1

root = Tk()
root.title('')
root.geometry('300x360')
root.configure(bg=fundo)

# ----- Frames ----- #
frame_main = Frame(root, width=300, height=110, bg=fundo, pady=0, padx=0, relief="flat",)
frame_main.grid(row=0, column=0)

frame_box = Frame(root, width=300, height=220, bg=fundo, pady=0, padx=0, relief="flat",)
frame_box.grid(row=1, column=0)

# ----- Main Frame ----- #
style = ttk.Style(root)
style.theme_use("clam")

img_0 = Image.open('padlock.png')
img_0 = img_0.resize((30, 30), Image.ANTIALIAS)
img_0 = ImageTk.PhotoImage(img_0)

app_image = Label(frame_main, height=60, image=img_0, compound=LEFT, padx=10, pady=5, relief="flat", anchor="nw", font=('Ivy 16 bold'), bg=color_1, fg=color_2)
app_image.place(x=2, y=0)

app_name = Label(frame_main, text="Gerador de Senhas", width=20, height=1, padx=10, relief="flat", anchor="nw", font=('Ivy 16 bold'), bg=color_1, fg=color_0)
app_name.place(x=35, y=2)

app_line = Label(frame_main, text="", width=400, height=1, padx=0, relief="flat", anchor="nw", font=('Arial 1'), bg=color_0, fg=color_1)
app_line.place(x=0, y=35)

# ----- Função para Gerar Senha ----- #
def criar_senha():
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    numbers = '123456789'
    symbols = "[]{}()*;/,_-"

    global combinar

    # ----- Uppercase ----- #
    if variable_1.get() == uppercase:
        combinar = uppercase
    else:
        pass

    # ----- Lowercase ----- #
    if variable_2.get() == lowercase:
        combinar = combinar + lowercase
    else:
        pass

    # ----- Numbers ----- #
    if variable_3.get() == numbers:
        combinar = combinar + numbers
    else:
        pass

    # ----- Symbols ----- #
    if variable_4.get() == symbols:
        combinar = combinar + symbols
    else:
        pass

    # ----- Length ----- #
    length = int(spin.get())

    # ----- Password ----- #
    senha = "".join(random.sample(combinar, length))
    app_senha['text'] = senha

    # ----- Função para Criar a Senha ----- #
    def copiar_senha():
        info = senha
        frame_box.clipboard_clear()
        frame_box.clipboard_append(info)
        messagebox.showinfo("Sucesso","A senha foi copiada com sucesso") 

    buttom_copy = Button(frame_box, command=copiar_senha, text="Copiar", width=8, height=1, overrelief=SOLID, bg=color_3, fg=color_1, font=('Ivy 10 bold'), anchor="center", relief=RAISED )
    buttom_copy.grid(row=0, column=2, columnspan=2, sticky=NSEW, pady=10, padx=1)

# ----- Caracters ----- #
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
numbers = '123456789'
symbols = "[]{}()*;/,_-"

var =IntVar()
var.set(16)
app_info = Label(frame_main, text="Tamanho da Senha", height=1, padx=0, relief="flat", anchor="nw", font=('Ivy 10 bold'), bg=fundo, fg=color_0)
app_info.place(x=15, y=60)
spin = Spinbox(frame_main, from_=8, to=20, width=5, textvariable=var)
spin.place(x=20, y=90)

app_senha = Label(frame_box , text="- - -", width=20, height=2, padx=0, relief="solid", anchor="center", font=('Ivy 10 bold'), bg=fundo, fg=color_0)
app_senha.grid(row=0, column=0, columnspan=2, sticky=NSEW, pady=10, padx=2)

# ----- Letras maiúsculas ----- #
app_info = Label(frame_box, text="Letras Maiúsculas", height=1, padx=0, relief="flat", anchor="nw",justify='center', font=('Ivy 10 bold'), bg=color_1, fg=color_0)
app_info.grid(row=1, column=1, sticky=NSEW, pady=5, padx=2)

variable_1 = StringVar()
variable_1.set(False)
chek_1 = Checkbutton(frame_box, width=1, var=variable_1,onvalue=uppercase, offvalue='off', bg=fundo)
chek_1.grid(row=1, column=0, sticky=NSEW, pady=5, padx=2)

# ----- Letras minúsculas ----- #
app_info = Label(frame_box, text="Letras Minúsculas", height=1, padx=0, relief="flat", anchor="nw",justify='center', font=('Ivy 10 bold'), bg=color_1, fg=color_0)
app_info.grid(row=2, column=1, sticky=NSEW, pady=5, padx=2)

variable_2 = StringVar()
variable_2.set(True)
chek_2 = Checkbutton(frame_box,width=1, var=variable_2,onvalue=lowercase, offvalue='off',bg=fundo)
chek_2.grid(row=2, column=0, sticky=NSEW, pady=5, padx=2)

# ----- Numbers ----- #
app_info = Label(frame_box, text="Números",height=1, padx=0, relief="flat", anchor="nw",justify='center', font=('Ivy 10 bold'), bg=color_1, fg=color_0)
app_info.grid(row=3, column=1, sticky=NSEW, pady=5, padx=2)

variable_3 = StringVar()
variable_3.set(True)
chek_3 = Checkbutton(frame_box,width=1, var=variable_3,onvalue=numbers, offvalue='off',bg=fundo)
chek_3.grid(row=3, column=0, sticky=NSEW, pady=5, padx=2)

# ----- Symbols ----- #
app_info = Label(frame_box, text="Símbolos", height=1, padx=0, relief="flat", anchor="nw",justify='center', font=('Ivy 10 bold'), bg=color_1, fg=color_0)
app_info.grid(row=4, column=1, sticky=NSEW, pady=1, padx=2)

variable_4 = StringVar()
variable_4.set(True)
chek_4 = Checkbutton(frame_box,width=1, var=variable_4, onvalue=symbols, offvalue='off',bg=fundo)
chek_4.grid(row=4, column=0, sticky=NSEW, pady=1, padx=2)

# ----- Botão de Gerar Senha ----- #
buttom_generator = Button(frame_box, command=criar_senha, text="Gerar senha",width=32, height=1, overrelief=SOLID, bg=color_3, fg="white", font=('Ivy 10 bold'), anchor="center", relief=FLAT )
buttom_generator.grid(row=5, column=0, sticky=NSEW, pady=20, padx=0, columnspan=5)

root.mainloop()