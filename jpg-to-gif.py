from tkinter import *
from tkinter import filedialog as fd
import os
from PIL import Image
from tkinter import messagebox

root = Tk()
root.title("Image_Conversion")


def jpg_to_gif():
    global im1
    import_filename = fd.askopenfilename()

    if import_filename.endswith(".jpg"):
        im1 = Image.open(import_filename)
        export_filename = fd.asksaveasfilename(defaultextension=".gif")
        im1.save(export_filename)
        messagebox.showinfo(
            "success ", "your image converted to GIF format...")

    else:
        Label_2 = Label(root, text="Error!", width=20,
                        fg="red", font=("bold", 15))
        Label_2.place(x=80, y=280)
        messagebox.showerror("Fail!", "Something Went Wrong...")


def gif_to_jpg():
    global im1
    import_filename = fd.askopenfilename()

    if import_filename.endswith(".gif"):
        im1 = Image.open(import_filename).convert("RGB")
        export_filename = fd.asksaveasfilename(defaultextension=".jpg")
        im1.save(export_filename)
        messagebox.showinfo(
            "success ", "your image converted to JPG format...")

    else:
        messagebox.showerror("Fail!", "Error Interrupted!! Check Again...")


button1 = Button(root, text="JPG TO GIF", width=20, height=2, bg="green",
                 fg="white", font=("helvetica", 12, "bold"), command=jpg_to_gif)
button1.place(x=120, y=120)

button2 = Button(root, text="GIF TO JPG", width=20, height=2, bg="green",
                 fg="white", font=("helvetica", 12, "bold"), command=gif_to_jpg)
button2.place(x=120, y=220)

root.geometry("500x500+400+200")
root.mainloop()
