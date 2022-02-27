from tkinter import *
from PIL import Image , ImageTk
from tkinter import  ttk , messagebox
import pymysql


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title('Student Managements system || Register')
        self.root.geometry("1350x700+0+0")

        #bg image

        self.bg=ImageTk.PhotoImage(file='images/a.jpg')
        bg=Label(self.root,image=self.bg)
        bg.place(x=250,y=0, relwidth=1,relheight=1)

        self.left = ImageTk.PhotoImage(file='images/aa.JPG')
        left = Label(self.root, image=self.left)
        left.place(x=80, y=100, width=400,height=500)

        #register frame
        frame1= Frame(self.root,bg='white')
        frame1.place(x=480,y=100 ,width=700,height=500)

        title=Label(frame1, text="Register here", font=("times new roman",20 ,"bold") ,bg="white",fg="green")
        title.place(x=50,y=30)

# r1

        fname = Label(frame1, text="First Name", font=("times new roman", 15, "bold"), bg="white", fg="gray")
        fname.place(x=50, y=70)
        self.textfname=Entry(frame1,font=("times new roman", 15), bg="lightgray")
        self.textfname.place(x=50,y=110,width=250)

        lname = Label(frame1, text="Last Name", font=("times new roman", 15, "bold"), bg="white", fg="gray")
        lname.place(x=370, y=70)
        self.textlname = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.textlname.place(x=370, y=110, width=250)

# r2
        contact = Label(frame1, text="Contact Number", font=("times new roman", 15, "bold"), bg="white", fg="gray")
        contact.place(x=50, y=150)
        self.textcontact = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.textcontact.place(x=50, y=190, width=250)

        email = Label(frame1, text="Enter your email", font=("times new roman", 15, "bold"), bg="white", fg="gray")
        email.place(x=370, y=150)
        self.textemail = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.textemail.place(x=370, y=190, width=250)

#r3
        question = Label(frame1, text="Security question", font=("times new roman", 15, "bold"), bg="white", fg="gray")
        question.place(x=50, y=230)
        self.cmbques = ttk.Combobox(frame1, font=("times new roman", 13),state="readonly" , justify="center")

        self.cmbques['values']=("Select","Your first pet name", "Your first school name", "Your hometown")
        self.cmbques.place(x=50, y=270, width=250)
        self.cmbques.current(0)

        answer = Label(frame1, text="Answer", font=("times new roman", 15, "bold"), bg="white", fg="gray")
        answer.place(x=370, y=230)
        self. textanswer = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.textanswer.place(x=370, y=270, width=250)

        # r4
        password = Label(frame1, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="gray")
        password.place(x=50, y=310)
        self.textpassword = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.textpassword.place(x=50, y=350, width=250)

        confirmpassword = Label(frame1, text="Confirm password", font=("times new roman", 15, "bold"), bg="white", fg="gray")
        confirmpassword.place(x=370, y=310)
        self.textconfirmpassword = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.textconfirmpassword.place(x=370, y=350, width=250)

        #term
        self.var_chk= IntVar()
        chk= Checkbutton(frame1, variable= self.var_chk,text="I agree the term and condition", onvalue=1,offvalue=0, bg="white", font=("time new roman",12))
        chk.place(x=50, y= 390)

        btnl = Button(self.root, text="Login", command=self.login_window, font=("times new roman",15, ), cursor="hand2", bg="white", fg="gray", bd=5)
        btnl.place(x=350 ,y=520)
        btnr= Button(frame1, text= "Register", command=self.register_data, font=("times new roman",15, ),cursor="hand2",bg="green", fg="white", bd=5 )
        btnr.place(x=550, y= 420)


    def clear(self):
        self.textfname.delete(0,END),
        self.textlname.delete(0,END),
        self.textcontact.delete(0,END),
        self.textemail.delete(0,END),
        self.cmbques.delete(0,END),
        self.textanswer.delete(0,END),
        self.textpassword.delete(0,END),
        self.textconfirmpassword.delete(0,END),
        self.cmbques.current(0)
    def login_window(self):
        self.root.destroy()
        import login
    def register_data(self):
        if self.textfname.get() =="" or self.textcontact.get()=="" or self.textemail.get()=="" or self.textpassword.get()=="" or  self.textconfirmpassword.get()=="" or self.cmbques.get()=="" or  self.textanswer.get()=="" :
            messagebox.showerror("Error","All fields are required", parent=self.root)
        elif self.textpassword.get()!= self.textconfirmpassword.get():
            messagebox.showerror("Error", "Password does not match", parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error","Agree terms and condition", parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="employee")
                cur=con.cursor()
                cur.execute("select * from employee where email=%s",self.textemail.get())
                row=cur.fetchone()
                print(row)
                if row != None:
                    messagebox.showerror("Error", "User already exist", parent=self.root)
                else:
                    cur.execute(
                        "insert into employee (fname,lname,contact,email,question,answer,password) values(%s,%s,%s,%s,%s,%s,%s)",
                        (self.textfname.get(),
                         self.textlname.get(),
                         self.textcontact.get(),
                         self.textemail.get(),
                         self.cmbques.get(),
                         self.textanswer.get(),
                         self.textpassword.get())
                        )
                    con.commit()
                    con.close()
                    messagebox.showinfo("Sucess", "You registered sucessfully", parent=self.root)
                    self.clear()



            except Exception as es:
                messagebox.showerror("Error", f"Error due to : {str(es)}", parent=self.root)




root= Tk()
obj=Register(root)
root.mainloop()
