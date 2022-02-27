from tkinter import *
from PIL import Image, ImageTk, ImageDraw
from datetime import *
from math import *
from tkinter import messagebox
import pymysql
import time


class Login_window:
    def __init__(self, root):
        self.root = root
        self.root.title("GUI Analouge clock")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#021e2f")
        left_lbl = Label(self.root, bg="#08a3d2", bd=0)
        left_lbl.place(x=0, y=0, width=600, relheight=1)

        right_lbl = Label(self.root, bg="#031f3c", bd=0)
        right_lbl.place(x=600, y=0, relwidth=1, relheight=1)

        # frames
        login_frame = Frame(self.root, bg="white")
        login_frame.place(x=250, y=100, width=800, height=500)

        title = Label(login_frame, text='Login Here', font=("times new roman", 30, 'bold'), bg='white', fg='#08a3d2')
        title.place(x=250, y=50)

        email = Label(login_frame, text='Email address', font=("times new roman", 18, 'bold'), bg='white', fg='gray')
        email.place(x=250, y=150)

        self.txtemail = Entry(login_frame, font=("times new roman", 18), bg='lightgray', )
        self.txtemail.place(x=250, y=180, width=350, height=35)

        password = Label(login_frame, text='Enter pasword', font=("times new roman", 18, 'bold'), bg='white', fg='gray')
        password.place(x=250, y=250)

        self.txtpassword = Entry(login_frame, font=("times new roman", 18), bg='lightgray', )
        self.txtpassword.place(x=250, y=280, width=350, height=35)

        btn_reg = Button(login_frame, command=self.register_window, text="Register new account", font=("times new roman", 14,), bd=0, fg='#b00857',
                         bg='white', )
        btn_reg.place(x=250, y=320)

        btn_log = Button(login_frame, text="Login", command=self.login, font=("times new roman", 15, 'bold'),
                         fg='white',
                         bg='#b00857', )
        btn_log.place(x=250, y=360, width=180, height=40)

        # clock--- starts here
        # self.clock_image()
        self.lbl = Label(self.root, text='Yugesh Clock', font=("times new roman", 25, 'bold'), compound='bottom',
                         fg='white', bg="#081923", bd=0)
        self.lbl.place(x=90, y=120, width=350, height=450)
        self.working()
    def register_window(self):
        self.root.destroy()
        import register
    def login(self):
        if self.txtemail.get() == "" or self.txtpassword.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="employee")
                cur = con.cursor()
                cur.execute("select * from employee where email=%s and password =%s",
                            (self.txtemail.get(), self.txtpassword.get()))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid username and password", parent=self.root)
                    self.root.destroy()
                    import register
                else:
                    messagebox.showinfo("Sucess","Welcome you have sucessfully loged in",parent=self.root)
                    self.root.destroy()
                    import studentmanagement

                con.close()
            except Exception as e:
                messagebox.showerror("Error", f"Error due to :{str(e)}", parent=self.root)

    def clock_image(self, hr, min_, sec_):
        clock = Image.new("RGB", (400, 400), (8, 25, 35))
        draw = ImageDraw.Draw(clock)
        # clock image
        bg = Image.open("images/watch.png")
        bg = bg.resize((300, 300), Image.ANTIALIAS)
        clock.paste(bg, (50, 50))

        # formula to rotate clock
        origin = 200, 200
        # clock Hour line
        draw.line((origin, 200 + 50 * sin(radians(hr)), 200 - 50 * cos(radians(hr))), fill="#df005e", width=4)

        # clock Minute line
        draw.line((origin, 200 + 80 * sin(radians(min_)), 200 - 80 * cos(radians(min_))), fill="blue", width=3)

        # clock second line
        draw.line((origin, 200 + 100 * sin(radians(sec_)), 200 - 100 * cos(radians(sec_))), fill="red", width=2)
        # ellipse
        draw.ellipse((195, 195, 210, 210,), fill="#1ad5d5")

        clock.save("images/clock_new.png")

    def working(self):
        h = datetime.now().time().hour
        m = datetime.now().time().minute
        s = datetime.now().time().second

        hr = (h / 12) * 360
        min_ = (m / 60) * 360
        sec_ = (s / 60) * 360

        self.clock_image(hr, min_, sec_)
        self.img = ImageTk.PhotoImage(file="images/clock_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(200, self.working)


root = Tk()
obj = Login_window(root)
root.mainloop()
