from tkinter import*
from PIL import ImageTk #pip install pilo 
from tkinter import ttk,messagebox


class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Home Page")
        self.root.geometry("1350x700+100+50")
        self.root.resizable(False,False)
        
        
        self.bg=ImageTk.PhotoImage(file="wall.jpg")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        
        #===Login Frame====
        title=Label(self.root,text="ELECTRICITY THEFT DETECTION SYSTEM",font=("Impact",35,"bold"),fg="#d77337",bg="white").place(x=280,y=250)
        Register_btn=Button(self.root,text="Register",command=self.register_window,bg="#d77337",fg="white",font=("time new Roman",20)).place(x=680,y=470,width=180,height=40)
        login_btn=Button(self.root,text="Login",command=self.login_window,bg="#d77337",fg="white",font=("time new Roman",20)).place(x=490,y=470,width=180,height=40)
        
    
    def register_window(self):
        self.root.destroy()
        import register

    def login_window(self):
        self.root.destroy()
        import login    
        

        
root=Tk()      
obj=Login(root)
root.mainloop()