from customtkinter import *
from tkinter import *
from tkinter import messagebox


app=CTk()
app.title("TO-DO LIST")
app.geometry("350x450")
app.config(bg="white")


font1=('Arial',30,'bold')
font2=('Arial',18,'bold')
font3=('Arial',10,'bold')


def addTask():
    s=entry.get()
    if s:
        box.insert(0,s)
        entry.delete(0,END)
        saveTask()
    else:
        messagebox.showerror('ERROR','Choose a task to delete')
def RemoveTask():
    s=box.curselection()
    if s:
        box.delete(s)
        saveTask()
    else:
        messagebox.showerror('ERROR','Choose a Task to delete')
def saveTask():
    f=open("tasks.txt","w")
    tasks=box.get(0,END)
    for task in tasks:
        f.write(task + "\n")
def loadTasks():
    try:
        f=open("tasks.txt","r")
        tasks=f.readlines()
        for task in tasks:
            box.insert(0,task.strip())
    except FileNotFoundError:
        messagebox.showerror('ERROR','Cannot load Tasks')




title=CTkLabel(app,font=font1,text='TO-DO LIST',text_color="black",bg_color="white")
title.place(x=90,y=20)

add=CTkButton(app,font=font2,text="Add Task",text_color="white",bg_color="red",cursor="hand2",corner_radius=5,hover_color="green",width=120,command=addTask)

add.place(x=40,y=80)

remove=CTkButton(app,font=font2,text="Remove Task",text_color="white",bg_color="red",cursor="hand2",corner_radius=5,hover_color="green",width=120,command=RemoveTask)
remove.place(x=180,y=80)

entry=CTkEntry(app,font=font2,text_color="black",fg_color="white",bg_color="white",border_color="black",width=280,border_width=2)
entry.place(x=40,y=120)

box=Listbox(app,width=39,height=15,font=font3)
box.place(x=80,y=200)


    


loadTasks()
app.mainloop()