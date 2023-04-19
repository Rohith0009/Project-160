from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import os

root = Tk()
root.title("File editor")
root.minsize(650,650)
root.maxsize(650,650)
root.configure(bg="gray78")



ExitImage = ImageTk.PhotoImage(Image.open("exit.jpg"))
OpenImage = ImageTk.PhotoImage(Image.open("open.png"))
SaveImage = ImageTk.PhotoImage(Image.open("save.png"))

File_label = Label(root, text="File Name", font=("Arial", 10))
File_Entry = Entry(root)
My_text = Text(root, height=35, width=80)

from tkinter import filedialog

name = ""

def open_file():
    global name
    File_Entry.delete(0, END)
    My_text.delete(1.0,END)
    text_file = filedialog.askopenfilename(title="Open Text File", filetypes=(("HTML Files", "*.html"),))
    name = os.path.basename(text_file)
    formatted_name = name.split('.')[0]
    File_Entry.insert(END, formatted_name)
    root.title(formatted_name)
    text_file = open(name, 'r')
    print(text_file)
    paragraph = text_file.read()
    My_text.insert(END, paragraph)
    text_file.close()

exitBtn = Button(root, image=ExitImage, text="Exit File")
openBtn = Button(root, image=OpenImage, text="Open File", command=open_file)
saveBtn = Button(root, image=SaveImage, text="Save File")

File_label.place(anchor=CENTER, relx=0.35, rely=0.05)
File_Entry.place(anchor=CENTER, relx=0.51, rely=0.05)
My_text.place(anchor=CENTER, relx=0.5, rely=0.55)
openBtn.place(anchor=CENTER, relx=0.04, rely=0.05)
exitBtn.place(anchor=CENTER, relx=0.11, rely=0.05)
saveBtn.place(anchor=CENTER, relx=0.18, rely=0.05)



root.mainloop()