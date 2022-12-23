from tkinter import *
from tkinter import messagebox
from tkinter import filedialog as fd

def ClearText():
    '''This function clears text for app work.'''
    text.config(state = "normal")
    text.delete('1.0', END)
    text.config(state = "disabled")

def insertText():
    '''This function choose txt file for app work. After done work, this file will be close.'''
    text.config(state = "normal")
    file_name = fd.askopenfilename()
    f = open(file_name)
    s = f.read()
    text.insert(1.0, s)
    f.close()
    text.config(state = "disabled")

def extractText():
    '''This function save txt files in pc before/after work. User can choose place, where he will save txt file.'''
    #Before
    text.config(state = "normal")
    file_name = fd.asksaveasfilename(filetypes=(("TXT files", "*.txt"),
                                        ("HTML files", "*.html;*.htm"),
                                                ("All files", "*.*") ))
    f = open(file_name, 'wb')
    #text.config(state = ACTIVE)
    s = text.get(0.0, END)
    s = s.encode('utf-8')
    f.write(s)
    f.close()
    text.config(state = "disabled")
    #After

def getvalue():
    '''This function generate Unicod from get key word.'''
    s = cipher.get()
    x = 0
    for i in range(0,len(s)):
        x = x+((ord(s[i])*i*i))
    #print(x)
    return(x%65535)


def encryption():
    '''This function creates ciphertext'''
    text.config(state = "normal")
    x = text.get(0.0, END) 
    y=""
    k=getvalue()
    for i in range(0,len(x)-1):
        y = y+(chr(ord(x[i])+k))
    text.delete('1.0', END)
    text.insert(1.0, y)
    encryption_button.config(state = ACTIVE)
    decryption_button.config(state = ACTIVE)
    text.config(state = "disabled")


def decryption():
    '''This fucntionreturns the encrypted text to the original, if user use correct password.'''
    text.config(state = "normal")
    y = text.get(0.0, END) 
    x=""
    k=getvalue()
    for i in range(0,len(y)-1):
        x = x+(chr(ord(y[i])-k))
    text.delete('1.0', END)
    text.insert(1.0, x)
    decryption_button.config(state = DISABLED)
    encryption_button.config(state = ACTIVE)
    text.config(state = "disabled")

#Before   
#title_app
    
root = Tk()
root.title("Шифратор")
root.minsize(600,400)
root.maxsize(600,400)
root.geometry("600x400+300+250")
main_menu = Menu()
file_menu = Menu(font=("Verdana", 9, "bold"), tearoff=0)


#file_function

file_menu.add_command(
    label="Открыть",command=insertText
    )
file_menu.add_command(
    label="Сохранить",command=extractText
    )
file_menu.add_separator()
file_menu.add_command(label="Выход",command=exit)

main_menu.add_cascade(label="Файл", menu=file_menu)

root.config(menu=main_menu)

text = Text(
    width=43, height=50
    )
text.pack(side=LEFT)
#text.config(state = "disabled")


#Scrollbart

scroll = Scrollbar(command=text.yview)
scroll.pack(side=LEFT, fill=Y)

text.config(yscrollcommand=scroll.set)

top_frame = Frame(root)
bottom_frame = Frame(root)

top_frame.pack()
bottom_frame.pack()


#clear_button

clear_button = Button(
    text="Очистить", background="#555", foreground="#ccc", padx="14", pady="7", font="13",bg='blue', fg='white',command=ClearText
    )
clear_button.config(height = 1, width = 10)
clear_button.place(x=400, y=130)


#encryption_button

encryption_button = Button(
    text="Шифровка", background="#555", foreground="#ccc", padx="14", pady="7", font="13",bg='blue', fg='white',command=encryption
    )
encryption_button.config(height = 1, width = 10)
encryption_button.place(x=400, y=175)


#decryption_button

decryption_button = Button(
    text="Дешифровка", background="#555", foreground="#ccc", padx="14", pady="7", font="13",bg='blue', fg='white',command=decryption
    )
decryption_button.config(height = 1, width = 10)
decryption_button.place(x=400, y=220)
#After


#key_word

cipher = StringVar()
cipher_label = Label(text="Кодовое слово:")
cipher_label.place(x=420, y=50)


#entry_button

cipher_Entry = Entry(textvariable=cipher)
cipher_Entry.place(x=410, y=80)








