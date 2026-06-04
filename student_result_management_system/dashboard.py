from tkinter import *
from PIL import Image,ImageTk #pip install pillow
from course import CourseClass
from student import studentClass
class RMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1270x630+0+0")  # Fixed the geometry specifier
        self.root.config(bg="white")
        #=======icon=======
        self.logo_dash=ImageTk.PhotoImage(file="Image/logo2.png")
        #=======title======
        title=Label(self.root,text="Student Result Managment System",padx=10,compound=LEFT,image=self.logo_dash,font=("goudy old sytle",20,"bold"),bg="#033054",fg="white",).place(x=0,y=0,relwidth=1,height=50)
        #======menu======
        M_Frame=LabelFrame(self.root,text="Menus",font=("times new roman",15),bg="white")
        M_Frame.place(x=10,y=70,width=1265,height=80)

        btn_course=Button(M_Frame,text="Course",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_course).place(x=20,y=5,width=180,height=40)
        btn_student=Button(M_Frame,text="Student",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_student).place(x=230,y=5,width=180,height=40)
        btn_result=Button(M_Frame,text="Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2").place(x=440,y=5,width=180,height=40)
        btn_view=Button(M_Frame,text="View Student Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2").place(x=650,y=5,width=180,height=40)
        btn_logout=Button(M_Frame,text="Logout",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2").place(x=860,y=5,width=180,height=40)
        btn_exit=Button(M_Frame,text="Exit",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2").place(x=1070,y=5,width=180,height=40)

        #=======content_Windo=====
        self.bg_img=Image.open('Image/content1.png')
        self.bg_img=self.bg_img.resize((920,350),Image.Resampling.LANCZOS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=400,y=180,width=855,height=300)

        #======update-details=======
        self.lbl_course=Label(self.root,text="Total Course\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#e43b06",fg="white")
        self.lbl_course.place(x=400,y=483,width=285,height=70)
        
        self.lbl_student=Label(self.root,text="Total Course\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#0676ad",fg="white")
        self.lbl_student.place(x=685,y=483,width=285,height=70)

        self.lbl_result=Label(self.root,text="Total course\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#038074",fg="white")
        self.lbl_result.place(x=970,y=483,width=285,height=70)


        #======footer=======
        footer = Label(self.root, text="SPK-Student Result Management System\nContact Us for any Technical Issue: 987xxxxx01",font=("goudy old style", 12), bg="#262626", fg="white").pack(side=BOTTOM,fill=X)

    def add_course(self):
        self.new_win = Toplevel(self.root)  # Instantiate a new Toplevel window
        self.new_obj = CourseClass(self.new_win)
    
    def  add_student(self):
        self.new_win = Toplevel(self.root)  # Instantiate a new Toplevel window
        self.new_obj = studentClass(self.new_win)

if __name__ == "__main__":
    root = Tk()
    obj = RMS(root)
    root.mainloop()  # Fixed typo here
