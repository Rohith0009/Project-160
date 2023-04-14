from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

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
exitBtn = Button(root, image=ExitImage, text="Exit File")
openBtn = Button(root, image=OpenImage, text="Open File")
saveBtn = Button(root, image=SaveImage, text="Save File")

File_label.place(anchor=CENTER, relx=0.35, rely=0.05)
File_Entry.place(anchor=CENTER, relx=0.51, rely=0.05)
My_text.place(anchor=CENTER, relx=0.5, rely=0.55)
openBtn.place(anchor=CENTER, relx=0.04, rely=0.05)
exitBtn.place(anchor=CENTER, relx=0.11, rely=0.05)
saveBtn.place(anchor=CENTER, relx=0.18, rely=0.05)



root.mainloop()