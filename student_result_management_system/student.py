from tkinter import *
from PIL import Image, ImageTk  # Ensure Pillow is installed (pip install pillow)
from tkinter import ttk,messagebox
import sqlite3

class studentClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x470+50+150")  # Fixed the geometry specifier
        self.root.config(bg="white")
        self.root.focus_force()  # Corrected method name
        #=======Variables======
        self.var_roll=StringVar()
        self.var_duration=StringVar()
        self.var_charges=StringVar()
        self.var_gender = StringVar()
        
        # ====== Title ======
        title = Label(self.root, text="Manage Course Detail's", font=("goudy old style", 20, "bold"), bg="#033054", fg="white")
        title.place(x=11, y=15, relwidth=0.98, height=35)
        

        # ====== Widget ======
        lbl_roll = Label(self.root,text="Roll No.",font=("goudy old style", 15, "bold"),bg="white").place(x=10, y=60)
        lbl_Name = Label(self.root,text="Name",font=("goudy old style", 15, "bold"),bg="white").place(x=10, y=100)
        lbl_Email = Label(self.root,text="Email",font=("goudy old style", 15, "bold"),bg="white").place(x=10, y=140)
        lbl_gender = Label(self.root,text="Gender",font=("goudy old style", 15, "bold"),bg="white").place(x=10, y=180)
        #======Entery Fildes======
        self.txt_roll = Entry(self.root,textvariable=self.var_roll,font=("goudy old style", 15, "bold"),bg="lightyellow")
        self.txt_roll.place(x=150, y=60,width=200)
        txt_name = Entry(self.root,textvariable=self.var_duration,font=("goudy old style", 15, "bold"),bg="lightyellow").place(x=150, y=100,width=200)
        txt_email = Entry(self.root,textvariable=self.var_charges,font=("goudy old style", 15, "bold"),bg="lightyellow").place(x=150, y=140,width=200)
        self.txt_gender = ttk.Combobox(self.root, textvariable=self.var_gender, values=("Select", "Male", "Female", "Other"), state='readonly', justify='center', font=("goudy old style", 15))
        self.txt_gender.place(x=150, y=180, width=200)
        self.txt_gender.current(0)  # Set default to "Select"

        
        
        self.txt_description = Text(self.root, font=("goudy old style", 15, "bold"), bg="lightyellow")
        self.txt_description.place(x=150, y=230, width=500, height=130)

     
        #======Buttons=======
        self.btn_add=Button(self.root,text='Save',font=("goudy old style",15,"bold"),bg="#2196f3",fg="white",cursor="hand2",command=self.add)
        self.btn_add.place(x=150,y=400,width=110,height=40)
        self.btn_update=Button(self.root,text='Update',font=("goudy old style",15,"bold"),bg="#4caf50",fg="white",cursor="hand2",command=self.update)
        self.btn_update.place(x=270,y=400,width=110,height=40)
        self.btn_delete=Button(self.root,text='Delete',font=("goudy old style",15,"bold"),bg="#f44336",fg="white",cursor="hand2",command=self.delete)
        self.btn_delete.place(x=390,y=400,width=110,height=40)
        self.btn_clear=Button(self.root,text='Clear',font=("goudy old style",15,"bold"),bg="#607d8b",fg="white",cursor="hand2",command=self.clear)
        self.btn_clear.place(x=510,y=400,width=110,height=40)
        #========Search Panel========
        self.var_search=StringVar()
        lbl_search_courseName = Label(self.root,text="Course Name",font=("goudy old style", 15, "bold"),bg="white").place(x=720, y=60)
        txt_search_courseName = Entry(self.root,textvariable=self.var_search,font=("goudy old style", 15, "bold"),bg="lightyellow").place(x=870, y=60,width=200)
        btn_search=Button(self.root,text='Search',font=("goudy old style",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2",command=self.search).place(x=1080,y=59,width=100,height=28)
        #========Content========
        self.C_Frame=Frame(self.root,bd=2,relief=RIDGE)
        self.C_Frame.place(x=720,y=100,width=470,height=340)


        self.C_Frame = Frame(self.root, bd=2, relief=RIDGE)
        self.C_Frame.place(x=720, y=100, width=470, height=340)

        # ====== Scrollbars ======
        # ====== Scrollbars ======
        scrolly = Scrollbar(self.C_Frame, orient=VERTICAL)
        scrollx = Scrollbar(self.C_Frame, orient=HORIZONTAL)

        self.CourseTable = ttk.Treeview(self.C_Frame, columns=("cid", "name", "duration", "charges", "description"),xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.config(command=self.CourseTable.yview)
        scrollx.config(command=self.CourseTable.xview)

        self.CourseTable.heading("cid", text="Course ID")
        self.CourseTable.heading("name", text="Name")
        self.CourseTable.heading("duration", text="Duration")
        self.CourseTable.heading("charges", text="Charges")
        self.CourseTable.heading("description", text="Description")
        self.CourseTable["show"] = 'headings'

        self.CourseTable.column("cid", width=60)
        self.CourseTable.column("name", width=100)
        self.CourseTable.column("duration", width=100)
        self.CourseTable.column("charges", width=100)
        self.CourseTable.column("description", width=150)
        self.CourseTable.pack(fill=BOTH, expand=1)
        self.CourseTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        #=====================================================
    
    
    def clear(self):
        self.show()
        self.var_roll.set("")
        self.var_duration.set("")
        self.var_charges.set("")
        self.var_search.set("")
        self.txt_description.delete('1.0',END)
        self.txt_roll.config(state=NORMAL)


    def delete(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror("Error", "Course Name is required", parent=self.root)
            else:
               cur.execute("SELECT * FROM course WHERE name=?", (self.var_roll.get(),))
               row = cur.fetchone()

               if row is None:  
                messagebox.showinfo("Info", "Please select a valid course from the list", parent=self.root)
               else:
                   op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                   if op:
                       cur.execute("DELETE FROM course WHERE name=?", (self.var_roll.get(),))
                       con.commit()
                       messagebox.showinfo("Success", "Course deleted successfully", parent=self.root)
                       self.clear()  # Clear form after deletion
                       self.show()  # Refresh course list

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)



    def get_data(self,ev):
        self.txt_roll.config(state='readonly')
        self.txt_roll
        r=self.CourseTable.focus()
        content=self.CourseTable.item(r)
        row=content["values"]
        #print(row)
        self.var_roll.set(row[1])
        self.var_duration.set(row[2])
        self.var_charges.set(row[3])
        #self.var_roll.set(row[1])
        self.txt_description.delete('1.0',END)
        self.txt_description.insert(END,row[4])


    def add(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror("Error", "Course Name is required", parent=self.root)
            else:
                cur.execute("SELECT * FROM course WHERE name=?", (self.var_roll.get(),))
                row = cur.fetchone()
            if row!=None:
                messagebox.showinfo("Info", "Course Name already present", parent=self.root)
            else:
                cur.execute( "INSERT INTO course (name, duration, charges, description) VALUES (?, ?, ?, ?)", (
                        self.var_roll.get(),
                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.txt_description.get("1.0", END)
                    ))
                con.commit()
                messagebox.showinfo("Success", "Course added successfully", parent=self.root)
                self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
           
    def update(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror("Error", "Course Name is required", parent=self.root)
            else:
                cur.execute("SELECT * FROM course WHERE name=?", (self.var_roll.get(),))
                row = cur.fetchone()
            if row==None:
                messagebox.showinfo("Error", "Select Course from listt", parent=self.root)
            else:
                cur.execute( "UPDATE course set duration =?, charges=?, description=? where name =?", (
                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.txt_description.get("1.0", END),
                        self.var_roll.get()
                    ))
                con.commit()
                messagebox.showinfo("Success", "Course Update successfully", parent=self.root)
                self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
           

    def show(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
              cur.execute("SELECT * FROM course")
              row = cur.fetchall()
              self.CourseTable.delete(*self.CourseTable.get_children())
              for row in row:
                   self.CourseTable.insert('',END,values=row)

            
        except Exception as ex:
                 messagebox.showerror("Error", f"Error due to {str(ex)}")


    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
              cur.execute(f"SELECT * FROM course WHERE name LIKE '%{self.var_search.get()}%'",)
              row = cur.fetchall()
              self.CourseTable.delete(*self.CourseTable.get_children())
              for row in row:
                   self.CourseTable.insert('',END,values=row)

            
        except Exception as ex:
                 messagebox.showerror("Error", f"Error due to {str(ex)}")





if __name__ == "__main__":
    root = Tk()
    obj = studentClass(root)
    root.mainloop()
