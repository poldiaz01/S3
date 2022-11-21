import os
import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

# Create a tkinter window
root = tk.Tk()
root.title('Codecs converter')
root.geometry('600x280')
root.configure(bg='#49A')
root.resizable(False, False)

# We create a function to read the file
def select_file(root):
    filetypes = (
        ('video files', '*.mp4'),
        ('All files', '*.*')
    )
    root.filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    showinfo(
        title='Selected File',
        message=root.filename
    )

# We create the open button
open_button = tk.Button(root, text='Open a File', bd='5', bg='white', command=lambda: select_file(root))
open_button.pack(expand=True)


# Create a label
label = Label(root,text='Select the file you want to convert: ', bg='#49A', fg='black', font=('Calibri', 10))
label.place(x=100, y=10)


# Create a second label
label2 = Label(root,text='Click the button for obtaining the conversion', bg='#49A', fg='black', font=('Calibri', 10))
label2.place(x=170, y=60)

# Function to convert the input video into VP8
def toVP8(filename):
    os.system("ffmpeg -i " + str(filename) + " -c:v libvpx -crf 30 -b:v 0 -b:a 128k -c:a libopus ex2_vp8.webm")

# Create a Button to convert VP8
btn = Button(root, text='Codec VP8', bd='5', bg='white', fg='#49A',
             command=lambda: toVP8(root.filename))

# Function to convert the input video into VP9
def toVP9(filename):
    os.system("ffmpeg -i " + str(filename) + " -c:v libvpx-vp9 -crf 30 -b:v 0 -b:a 128k -c:a libopus ex2_vp9.webm")

# Create a Button to convert VP9
btn2 = Button(root, text='Codec VP9', bd='5',bg='white', fg='#49A',
             command=lambda: toVP9(root.filename))

# Function to convert the input video into h265
def toh265(filename):
    os.system("ffmpeg -i " + str(filename) + " -c:v libx265 -c:a copy ex2_h265.mp4")

# Create a Button to convert h265
btn3 = Button(root, text='Codec h265', bd='5', bg='white', fg='#49A',
             command=lambda: toh265(root.filename))

# Function to convert the input video into AV1
def toAV1(filename):
    os.system("ffmpeg -i " + str(filename) + " -c:v libaom-av1 -crf 30 ex_1.av1.mkv")

# Create a Button to convert AV1
btn4 = Button(root, text='Codec AV1', bd='5', bg='white', fg='#49A',
             command=lambda: toAV1(root.filename))

# Set the position of the buttons in the window
open_button.place(x=350, y=10)
btn.place(x=250,y=90)
btn2.place(x=150,y=140)
btn3.place(x=350, y=140)
btn4.place(x=250, y=190)

# Quit the application
QUIT = tk.Button(root, text='QUIT', command=root.destroy)
QUIT.place(x=500,y=220)


# start the app
root.mainloop()