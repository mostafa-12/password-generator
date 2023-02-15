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
root.geometry(f"450x620+{int(screen_width/3)}+{int(screen_hieght/10)}") # make it in middekl of any screen
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


def generat(Number):
    number=int(Number)
    String=[]
    if int(Upper_var.get()) == 1 and int(Lower_var.get()) == 1 and int(Numbers_var.get()) == 1 and int(Symbols_var.get()) == 1 :
        Upper_len=int(round(number*(20/100)))
        digits_len=int(round(number*(20/100)))
        punc_len=int(round(number*(20/100)))
        Lower_len=number-(Upper_len*3)
        Upper_case=random.choices(list(string.ascii_uppercase),k=Upper_len)
        Lower_case=random.choices(list(string.ascii_lowercase),k=Lower_len)
        digits=random.choices(list(string.digits),k=digits_len)
        punc=random.choices(list(string.punctuation),k=punc_len)
        String.clear()
        String=[Upper_case,Lower_case,punc,digits]
    elif int(Upper_var.get() == 1) and int(Lower_var.get()) == 1 and int(Numbers_var.get()) != 1 and int(Symbols_var.get()) != 1:
        string_len=round(number*(50/100))
        Upper_case=random.choices(list(string.ascii_uppercase),k=string_len)
        Lower_case=random.choices(list(string.ascii_uppercase),k=(number-string_len))
        String.clear()
        String=[Upper_case,Lower_case]
    elif int(Upper_var.get()) == 1 and int(Lower_var.get()) == 1 and int(Numbers_var.get()) == 1 and int(Symbols_var.get()) != 1 :
        Upper_len=int(round(number*(20/100)))
        digits_len=int(round(number*(30/100)))
        Lower_len=number-(Upper_len+digits_len)

        Upper_case=random.choices(list(string.ascii_uppercase),k=Upper_len)
        Lower_case=random.choices(list(string.ascii_lowercase),k=Lower_len)
        digits=random.choices(list(string.digits),k=digits_len)
        String.clear()
        String=[Upper_case,Lower_case,digits]
    elif int(Upper_var.get()) == 1 and int(Lower_var.get()) == 1 and int(Numbers_var.get()) != 1 and int(Symbols_var.get()) == 1:
        Upper_len=int(round(number*(20/100)))
        punc_len=int(round(number*(30/100)))
        Lower_len=number-(Upper_len*+punc_len)

        Upper_case=random.choices(list(string.ascii_uppercase),k=Upper_len)
        Lower_case=random.choices(list(string.ascii_lowercase),k=Lower_len)
        punc=random.choices(list(string.punctuation),k=punc_len)
        String.clear()
        String=[Upper_case,Lower_case,punc]
    else:
        messagebox.showerror("note","password must include Uppercase and Lowercase")
        return
    password_chars_list=[]
    for chars in String:
        for char in chars:
            password_chars_list.append(char)
            
    for i in range(number):
        random.shuffle(password_chars_list)
        
    password=""
    
    for char in password_chars_list:
        password=password+char
        
    output_var.set(f"{password}")
            
        
        
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

password_len_lbl=tkinter.Label(root,text="Lenth of password : ",bg="white",bd=0,relief="flat",font=("Bahnschrift SemiBold",10,"bold"),fg="black")

password_len_lbl.place(relx=.03,rely=.547)


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
password_len=tkinter.Spinbox(root,from_=8,to=32,width=15,font=("Bahnschrift SemiBold",12,"bold"),textvariable=password_len_var)

password_len.place(relx=.29,rely=.54)

out_put=tkinter.Entry(root,width=32,font=("Bahnschrift SemiBold",12,"bold"),justify="center",border=0,relief="flat",textvariable=output_var)
out_put.place(relx=.18,rely=.85)

#binding out_put entry
out_put.bind("<Enter>",clear_output)
out_put.bind("<Leave>",set_output)

#Buttons

submite=tkinter.Button(root,text="generate a password",font=("Bahnschrift SemiBold",10,"bold")
                       ,bg="white",fg="#FF1919",padx=2,pady=10,command=lambda:generat(password_len_var.get()))
submite.place(rely=.73,relx=.35)


copy_password=tkinter.Button(root,text="copy password",font=("Bahnschrift SemiBold",10,"bold")
                       ,bg="white",fg="#FF1919",command=lambda:copy_to_clipboard(output_var.get()))

copy_password.place(relx=.4,rely=.93)

#frames
tkinter.Frame(root,width=200,bg="#0066ff").place(relx=.27,rely=.52) #make underline
tkinter.Frame(root,width=290,bg="#0066ff").place(relx=.18,rely=.89) #make underline



root.mainloop()