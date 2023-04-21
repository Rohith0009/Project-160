from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import filedialog
import os

root = Tk()
root.title("File editor")
root.minsize(650,650)
root.maxsize(650,650)
root.configure(bg="pale green")

ExitImage = ImageTk.PhotoImage(Image.open("exit.png"))
OpenImage = ImageTk.PhotoImage(Image.open("open.png"))
SaveImage = ImageTk.PhotoImage(Image.open("save.png"))
CreateImage = ImageTk.PhotoImage(Image.open("create.png"))

File_label = Label(root, text="File Name", font=("Arial", 10))
File_Entry = Entry(root)
My_text = Text(root, height=35, width=80, bg="pale turquoise")


name = ""
FileFormat = ""

def open_file():
    global name, FileFormat
    File_Entry.delete(0, END)
    My_text.delete(1.0,END)
    text_file = filedialog.askopenfilename(title="Open Text File", filetypes=(("HTML Files", "*.html"),("Text Files", "*.txt"),("CSS Files", "*.css"),("Java Script Files", "*.js"),("Python Files", "*.py"),))
    name = os.path.basename(text_file)
    formatted_name = name.split('.')[0]
    FileFormat = name.split('.')[1]
    File_Entry.insert(END, formatted_name)
    root.title(formatted_name)
    text_file = open(name, 'r')
    paragraph = text_file.read()
    My_text.insert(END, paragraph)
    text_file.close()

def save():
    file_name = File_Entry.get()
    file = open(file_name+f".{FileFormat}", "w")
    the_text = My_text.get(1.0, END)
    print(the_text)
    file.write(the_text)
    messagebox.showinfo("Information", "Success")

def close():
    root.destroy()

def create():
    global FileFormat
    name = File_Entry.get()
    file = open(name, "x")
    File_Entry.delete(0, END)
    formatted_name = name.split('.')[0]
    FileFormat = name.split('.')[1]
    File_Entry.insert(END, formatted_name)
    root.title(formatted_name)
    text_file = open(name, 'r')
    paragraph = text_file.read()
    My_text.insert(END, paragraph)
    text_file.close()

createBtn = Button(root, image=CreateImage, text="Create File", command=create)
openBtn = Button(root, image=OpenImage, text="Open File", command=open_file)
saveBtn = Button(root, image=SaveImage, text="Save File", command=save)
exitBtn = Button(root, image=ExitImage, text="Exit File", command=close)

File_label.place(anchor=CENTER, relx=0.35, rely=0.05)
File_Entry.place(anchor=CENTER, relx=0.51, rely=0.05)
My_text.place(anchor=CENTER, relx=0.5, rely=0.55)

createBtn.place(anchor=CENTER, relx=0.04, rely=0.05)
openBtn.place(anchor=CENTER, relx=0.11, rely=0.05)
saveBtn.place(anchor=CENTER, relx=0.18, rely=0.05)
exitBtn.place(anchor=CENTER, relx=0.25, rely=0.05)


root.mainloop()