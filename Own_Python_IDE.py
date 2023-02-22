#Libraries
from tkinter import *
from tkinter import messagebox,colorchooser,filedialog
import subprocess as sp

#Application Setup
root = Tk()
root.title("Own Python IDE")
root.resizable(False,False)
root.configure(bg='#323846')
root.geometry("1180x620+100+40")

#Functions
file_path = ''
def set_file_path(path):
    global file_path
    file_path = path

def color(event):
    cls = colorchooser.askcolor(title="Select Color to change")
    root.configure(bg=cls[1])

def open_file():
    path = filedialog.askopenfilename(filetypes=[('Python Files','*.py')])
    with open(path,'r') as file:
        code = file.read()
        code_input.delete('1.0',END)
        code_input.insert('1.0',code)
        set_file_path(path)

def save_file():
    if(file_path==''):
        path = filedialog.asksaveasfilename(filetypes=[('Python Files','*.py')])
    else:
        path = file_path
    with open(path,'w') as file:
        code = code_input.get('1.0',END)
        file.write(code)
        set_file_path(path)

def run_file():
    if(file_path==''):
        messagebox.showwarning("IDE Error","Save your code")
        return
    command = f'python {file_path}'
    process = sp.Popen(command,stdout=sp.PIPE , stderr=sp.PIPE,shell=True)
    output , error = process.communicate()
    code_output.insert('1.0',output)
    code_output.insert('1.0',error)

#Application Creation
logo = PhotoImage(file="E:\\pyImages\\python logo.png")
open_img = PhotoImage(file="E:\\pyImages\\open.png")
run_img = PhotoImage(file="E:\\pyImages\\run.png")
save_img = PhotoImage(file="E:\\pyImages\\save.png")
root.iconphoto(False,logo)

code_input = Text(root,font="consolas 18",bd=4,bg="light grey")
code_input.place(x=180,y=0,width=680,height=620)

code_output = Text(root,font="consolas 15",bg="#323846",fg="light green",bd=2)
code_output.place(x=860,y=0,width=420,height=620)

Open = Button(root,image=open_img,bd=0,bg="#323846",activebackground="#323846",command=open_file)
Open.place(x=30,y=30)
Save = Button(root,image=save_img,bd=0,bg="#323846",activebackground="#323846",command=save_file)
Save.place(x=30,y=145)
Run = Button(root,image=run_img,bd=0,bg="#323846",activebackground="#323846",command=run_file)
Run.place(x=30,y=260)
root.bind('<Control-g>',color)
root.mainloop()
