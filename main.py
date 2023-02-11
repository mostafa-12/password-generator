import tkinter
import string
from pyautogui import size
import random
from tkinter import messagebox
import clipboard
from PIL import Image,ImageTk





# screen size 
screen_width=size()[0]
screen_hieght=size()[1]

# configure the main window
root=tkinter.Tk()
root.geometry(f"450x620+{int(screen_width/3)}+{int(screen_hieght/10)}")
root.title("Pasword Generator")
root.configure(bg="white")
root.iconbitmap("icons_logos/lock.ico")
root.resizable(0,0)

#functions
def clear_output(n):
    if output_var.get() == "new password here":
        output_var.set("")
    else:
        pass    
def set_output(n):
    if output_var.get()=="":
        output_var.set("new password here")
    else:
        pass
#variabels
output_var=tkinter.StringVar()
output_var.set("new password here")
password_len_var=tkinter.StringVar()
Upper_var=tkinter.IntVar()
Lower_var=tkinter.IntVar()
Numbers_var=tkinter.IntVar()
Symbols_var=tkinter.IntVar()

Upper_var.set(1)
Lower_var.set(1)
Numbers_var.set(1)
Symbols_var.set(1)


def generat(number):
    pass

def copy_to_clipboard(text):
    clipboard.copy(f"{text}")
    messagebox.showinfo("text copied",f"your password copied to clip board")
    
#LABELS

#Image label

photo=ImageTk.PhotoImage(Image.open("icons_logos/logo.png"))


image_lbl=tkinter.Label(root,image=photo,border=0,relief="flat")
image_lbl.place(relx=.05,rely=.05)

#normal labels

main_text=tkinter.Label(root,text="Customize your password",font=("Bahnschrift SemiBold",16,"bold"),fg="black",bg="white",border=0,relief="flat",foreground="#0066ff")
main_text.place(relx=.22,rely=.46)

password_len_lbl=tkinter.Label(root,text="Lenth of password : ",bg="white",bd=0,relief="flat",textvariable=password_len_var)

password_len_lbl.place(relx=.03,rely=.55)


# check boxes
Upper_case=tkinter.Checkbutton(root,text="Uppercase",bd=0,relief="flat",bg="white",fg="#FF1919",variable=Upper_var)

Upper_case.place(rely=.65,relx=.1)

Lower_case=tkinter.Checkbutton(root,text="Lowercase",bd=0,relief="flat",bg="white",fg="#FF1919",variable=Lower_var)

Lower_case.place(rely=.65,relx=.3)

Numbers=tkinter.Checkbutton(root,text="Numbers",bd=0,relief="flat",bg="white",fg="#FF1919",variable=Numbers_var)

Numbers.place(rely=.65,relx=.5)

Symbols=tkinter.Checkbutton(root,text="Symbols",bd=0,relief="flat",bg="white",fg="#FF1919",variable=Symbols_var)

Symbols.place(rely=.65,relx=.7)

#Entries
password_len=tkinter.Spinbox(root,from_=8,to=32,width=15,font=("Bahnschrift SemiBold",12,"bold"))

password_len.place(relx=.29,rely=.54)

out_put=tkinter.Entry(root,width=32,font=("Bahnschrift SemiBold",12,"bold"),justify="center",border=0,relief="flat",textvariable=output_var)
out_put.place(relx=.18,rely=.85)

#binding out_put entry
out_put.bind("<Enter>",clear_output)
out_put.bind("<Leave>",set_output)

#Buttons

submite=tkinter.Button(root,text="generate a password",font=("Bahnschrift SemiBold",10,"bold")
                       ,bg="white",fg="#FF1919",padx=2,pady=10,command=lambda:generat(output_var.get()))
submite.place(rely=.73,relx=.35)


copy_password=tkinter.Button(root,text="copy password",font=("Bahnschrift SemiBold",10,"bold")
                       ,bg="white",fg="#FF1919",command=lambda:copy_to_clipboard(output_var.get()))

copy_password.place(relx=.4,rely=.93)

#frames
tkinter.Frame(root,width=200,bg="#0066ff").place(relx=.27,rely=.52) #make underline
tkinter.Frame(root,width=290,bg="#0066ff").place(relx=.18,rely=.89) #make underline



root.mainloop()