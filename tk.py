from Tkinter import *
import tkFileDialog
import ttk
from PIL import Image,ImageTk

fileOnly=''

def getFileName():
    fileLocation=tkFileDialog.askopenfilename()
    global fileOnly
    fileOnly=''
    for i in range(len(fileLocation)-1,-1,-1):
        if fileLocation[i]=='/' or fileLocation[i]=='//':
            break
        fileOnly=fileLocation[i]+fileOnly
    location.config(text=fileOnly)

def seamCarve(*args):
    width=int(inputWidth.get())
    height=int(inputHeight.get())
    image=Image.open(fileOnly)
    print height,width
    image.show()
    choice=str(option.get())
    print choice

root=Tk()
root.title("Harley and Chris' Seam Carving")

content=ttk.Frame(root,padding="3 3 12 12",borderwidth=5,width=800,height=400)
content.grid(column=0, row=0, sticky=(N,W,E,S))
content.columnconfigure(0,weight=1)
content.rowconfigure(0,weight=1)

textlbl=ttk.Label(content,text="Please select your image:").grid(column=1,row=1, sticky=(W,E))
address=StringVar()
ttk.Button(content, text="Browse...",command=getFileName).grid(column=2, row=2, sticky=(W,E))
location=ttk.Label(content,text="No file selected",foreground='blue')
location.grid(column=1,row=2,sticky=(W,E))
textlbl2=ttk.Label(content,text="Please select an option and a width/height:").grid(column=1,row=3,sticky=(W,E))

option=StringVar()
inputWidth=StringVar()
inputHeight=StringVar()

shrink=ttk.Radiobutton(content,text='Shrink',variable=option,value='shrink').grid(column=1,row=4,sticky=(W))
expand=ttk.Radiobutton(content,text='Expand',variable=option,value='expand').grid(column=1,row=5,sticky=(W))
textlbl4=ttk.Label(content,text="Height:").grid(column=1,row=4,sticky=(E))
height_entry=ttk.Entry(content,width=6,textvariable=inputHeight)
height_entry.grid(column=2,row=4,sticky=(W))
textlbl3=ttk.Label(content,text="Width:").grid(column=1,row=5,sticky=(E))
width_entry=ttk.Entry(content,width=6,textvariable=inputWidth)
width_entry.grid(column=2,row=5,sticky=(W))
textlbl5=ttk.Label(content,text="This may take a while...").grid(column=1,row=7,sticky=(E))
ttk.Button(content,text="Seam Carve It!",command=seamCarve).grid(column=2,row=7,sticky=(E))


for child in content.winfo_children(): child.grid_configure(padx=4, pady=4)

width_entry.focus()
height_entry.focus()
root.bind('<Return>',seamCarve)
root.mainloop()
