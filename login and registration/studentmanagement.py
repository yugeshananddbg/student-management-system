from tkinter import *
from tkinter import ttk
import pymysql


class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management system")
        self.root.geometry("1350x750+0+0")

        self.searchby=StringVar()
        self.searchtxt=StringVar()



        title = Label(self.root, text='Student management system', bd=10, relief=GROOVE,
                      font=("times new roman", 40, 'bold'), bg='yellow', fg='red')
        title.pack(side=TOP, fill=X)
        # main frame
        manage_frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        manage_frame.place(x=20, y=100, width=450, height=600)

        detail_frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        detail_frame.place(x=500, y=100, width=800, height=600)
        # manage frame
        m_title = Label(manage_frame, text='Manage Students', font=("times new roman", 30, 'bold'), bg="crimson",
                        fg='white')
        m_title.grid(row=0, columnspan=2, pady=20)

        lbl_roll = Label(manage_frame, text='Roll Number', font=("times new roman", 20,), bg="crimson", fg='white')
        lbl_roll.grid(row=1, column=0, pady=5, padx=20, sticky="w")

        self.txt_roll = Entry(manage_frame, font=("times new roman", 15,), bd=5, relief=GROOVE)
        self.txt_roll.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        lbl_name = Label(manage_frame, text='Name', font=("times new roman", 20,), bg="crimson", fg='white')
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        self.txt_name = Entry(manage_frame, font=("times new roman", 15,), bd=5, relief=GROOVE)
        self.txt_name.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        lbl_email = Label(manage_frame, text='Email address', font=("times new roman", 20,), bg="crimson", fg='white')
        lbl_email.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        self.txt_email = Entry(manage_frame, font=("times new roman", 15,), bd=5, relief=GROOVE)
        self.txt_email.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        lbl_gender = Label(manage_frame, text='Gender', font=("times new roman", 20,), bg="crimson", fg='white')
        lbl_gender.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        self.txt_gender = ttk.Combobox(manage_frame, font=("times new roman", 13,), state="readonly")
        self.txt_gender['values'] = ("male", "female", "other")
        self.txt_gender.grid(row=4, column=1, pady=10, padx=20, sticky="w")

        lbl_contact = Label(manage_frame, text='Contact No', font=("times new roman", 20,), bg="crimson", fg='white')
        lbl_contact.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        self.txt_contact = Entry(manage_frame, font=("times new roman", 15,), bd=5, relief=GROOVE)
        self.txt_contact.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        lbl_dateofbirth = Label(manage_frame, text='Date of Birth', font=("times new roman", 20,), bg="crimson",
                                fg='white')
        lbl_dateofbirth.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        self.txt_dateofbirth = Entry(manage_frame, font=("times new roman", 15,), bd=5, relief=GROOVE)
        self.txt_dateofbirth.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        lbl_address = Label(manage_frame, text='Address', font=("times new roman", 20,), bg="crimson", fg='white')
        lbl_address.grid(row=7, column=0, pady=10, padx=20, sticky="w")

        self.txt_address = Text(manage_frame, width=20, height=3, font=("times new roman", 15,), bd=5, relief=GROOVE)
        self.txt_address.grid(row=7, column=1, pady=10, padx=20, sticky="w")

        # btn frame
        btn_frame = Frame(manage_frame, bd=4, relief=RIDGE, bg="crimson")
        btn_frame.place(x=10, y=530, width=430, )

        addbtn = Button(btn_frame, text="Add", command=self.add_students, width=10)
        addbtn.grid(row=0, column=0, padx=10, pady=10)

        updatebtn = Button(btn_frame, text="Update",command=self.update_student, width=10)
        updatebtn.grid(row=0, column=1, padx=10, pady=10)

        deletebtn = Button(btn_frame, text="Delete", command=self.delete_data, width=10)
        deletebtn.grid(row=0, column=2, padx=10, pady=10)

        clearbtn = Button(btn_frame, text="Clear", command=self.clear,width=10)
        clearbtn.grid(row=0, column=3, padx=10, pady=10)

        # Detail frame
        lbl_search = Label(detail_frame, text='Search By', font=("times new roman", 20,), bg="crimson", fg='white')
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        combo_serch = ttk.Combobox(detail_frame, width=10, textvariable=self.searchby,font=("times new roman", 13,), state="readonly")
        combo_serch['values'] = ("Roll", "Name", "Contact")
        combo_serch.grid(row=0, column=1, pady=10, padx=20, sticky="w")

        txt_search = Entry(detail_frame, width=15, textvariable=self.searchtxt,font=("times new roman", 12,), bd=5, relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        search_btn = Button(detail_frame, text="Search",command=self.search_data, width=10, pady=5)
        search_btn.grid(row=0, column=3, padx=10, pady=10)

        showall_btn = Button(detail_frame, text="Show All", command=self.fetch_data,width=10, pady=5)
        showall_btn.grid(row=0, column=4, padx=10, pady=10)

        # table frame

        table_frame = Frame(detail_frame, bd=4, relief=RIDGE, bg="crimson")
        table_frame.place(x=10, y=70, width=760, height=500)
        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)
        self.Student_table = ttk.Treeview(table_frame, xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set,
                                          columns=("roll", "name", "email", "gender", "contact", "dob", "address"))
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)

        self.Student_table.heading("roll", text="Roll Number")
        self.Student_table.heading("name", text="Name")
        self.Student_table.heading("email", text="Email")
        self.Student_table.heading("gender", text="Gender")
        self.Student_table.heading("contact", text="Contact")
        self.Student_table.heading("dob", text="Date of birth")
        self.Student_table.heading("address", text="Address")
        self.Student_table['show'] = 'headings'
        self.Student_table.column("roll", width=100)
        self.Student_table.column("name", width=150)
        self.Student_table.column("email", width=150)
        self.Student_table.column("gender", width=100)
        self.Student_table.column("contact", width=100)
        self.Student_table.column("dob", width=100)
        self.Student_table.column("address", width=200)

        self.Student_table.pack(fill=BOTH, expand=1)
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


    def get_cursor(self,ev):
        cursor_row=self.Student_table.focus()
        content=self.Student_table.item(cursor_row)
        row=content['values']
        print(row)
        self.txt_roll.delete("0", END)
        self.txt_roll.insert( END,row[0])
        self.txt_name.delete("0", END)
        self.txt_name.insert( END,row[1])
        self.txt_email.delete("0", END)
        self.txt_email.insert( END,row[2])
        self.txt_gender.set("")
        self.txt_gender.insert( END,row[3])
        self.txt_contact.delete("0", END)
        self.txt_contact.insert( END,row[4])
        self.txt_dateofbirth.delete("0", END)
        self.txt_dateofbirth.insert( END,row[5])
        self.txt_address.delete("1.0", END)
        self.txt_address.insert( END,row[6])









    def add_students(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="student")
        cur = con.cursor()
        cur.execute("insert into students values (%s,%s,%s,%s,%s,%s,%s)", (
            self.txt_roll.get(),
            self.txt_name.get(),
            self.txt_email.get(),
            self.txt_gender.get(),
            self.txt_contact.get(),
            self.txt_dateofbirth.get(),

            self.txt_address.get('1.0', END)
        ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def update_student(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="student")
        cur = con.cursor()


        cur.execute("update  students set name=%s, email=%s,  contact=%s,dob=%s, address=%s where roll=%s", (
            self.txt_name.get(),
            self.txt_email.get(),
            self.txt_contact.get(),
            self.txt_dateofbirth.get(),
            self.txt_address.get('1.0', END),
            self.txt_roll.get(),
        ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def clear(self):
        self.txt_roll.delete("0", END)
        self.txt_name.delete("0", END)
        self.txt_email.delete("0", END)
        self.txt_gender.set("")
        self.txt_contact.delete("0", END)
        self.txt_dateofbirth.delete("0", END)
        self.txt_address.delete("1.0", END)

    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="student")
        cur = con.cursor()
        cur.execute("select * from students")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('', END, values=row)
            con.commit()
            con.close()

    def delete_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="student")
        cur = con.cursor()
        cur.execute("delete from students where roll=%s",self.txt_roll.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()

    def search_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="student")
        cur = con.cursor()
        cur.execute("select * from students where "+str(self.searchby.get())+" = '"+str(self.searchtxt.get())+"'")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('', END, values=row)
            con.commit()
            con.close()

root = Tk()
obj = Student(root)
root.mainloop()
