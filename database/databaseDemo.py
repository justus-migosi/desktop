from tkinter.constants import MOVETO
import mysql.connector  as mysql
import tkinter as tk

from tkinter import messagebox as msg  
window=tk.Tk()
user_name=tk.Entry(window,width=50)
user_name.insert(0,"enter username")
user_name.grid(row=0,column=0)
password=tk.Entry(window,width=50)
password.insert(0,"enter password")
password.grid(row=1,column=0)
host=tk.Entry(window,width=50)
host.insert(0,"enter host")
host.grid(row=2,column=0)
auth_plugin="mysql_native_password"
# Create TabControl.

def login():
       try:
            mysql.connect(user=user_name.get(),password=password.get(),host=host.get())
            msg.showinfo("Authentification","Log in successfull")
          
       except mysql.Error as error:
            msg.showinfo("Authentification","Authentification failed "+str(error))
Login=tk.Button(window,text="LogIn",bg="yellow",width=30,height=10,command=login)
Login.grid(row=3,column=0)






window.mainloop()
