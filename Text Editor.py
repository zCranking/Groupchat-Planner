from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import os
from tkinter import filedialog
root = Tk()
root.minsize(650, 650)
root.maxsize(750, 750)
exitImg = ImageTk.PhotoImage(Image.open("exit.jpg"))
openImg = ImageTk.PhotoImage(Image.open("open.png"))
saveImg = ImageTk.PhotoImage(Image.open("save.png"))

label_file_name = Label(root, text="File Name" , foreground="#FFC43D", font=("Comic Sans MS", "10", "bold"))
label_file_name.place(relx=0.28, rely=0.03, anchor=CENTER)

input_file_name = Entry(root, foreground="#FFC43D", font=("Comic Sans MS", "10", "bold"))
input_file_name.place(relx = 0.46, rely=0.03, anchor=CENTER)

my_text = Text(root, height=32, width = 80, foreground="#FFC43D", font=("Comic Sans MS", "10", "bold"))
my_text.place(relx=0.5, rely=0.55, anchor=CENTER)

name = ""

def openfile():
    global name
    my_text.delete(1.0, END)
    input_file_name.delete(0, END)
    text_file = filedialog.askopenfilename(title = "Hacking your computer",
                                           filetypes =(("Text Files", "*.txt"),))
    
    print(text_file)
    name = os.path.basename(text_file)
    formatted_name = name.split('.')[0]
    input_file_name.insert(END, formatted_name)
    root.title(formatted_name)
    text_file = open(name, 'r')
    paragraph = text_file.read()
    my_text.insert(END, paragraph)
    text_file.close

def save():
    file_name = input_file_name.get()
    text_file = open(file_name+".txt", 'w')
    data = my_text.get(1.0, END)
    print(data)
    text_file.write(data)
    messagebox.showinfo("Update", "Your work was saved succesfully!")

def close():
    savework = messagebox.askquestion("Save", "Did you save your work?")
    print(savework)
    if savework == "yes":
        root.destroy()
    else:
        savethework = messagebox.askquestion("Save", "Do you want to save your work?")
    if savethework == "yes":
        save()
        root.destroy()
    else:
        root.destroy()
open_button = Button(root, image=openImg, command=openfile)
open_button.place(relx=0.05, rely=0.03, anchor=CENTER)
exit_button = Button(root, image=exitImg, command=close)
exit_button.place(relx=0.15, rely=0.03, anchor=CENTER)
save_button = Button(root, image=saveImg, command=save)
save_button.place(relx=0.10, rely=0.03, anchor=CENTER)

root.mainloop()