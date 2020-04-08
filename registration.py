from tkinter import *
import sqlite3
from tkinter import messagebox
conn=sqlite3.connect("db/registrations.db")
c=conn.cursor()

#c.execute("create table student(Name char(20),Password char(20) primary key)")
def insert_val(name,pwd):
    c.execute("insert into student values(:name,:pwd)",{'name':name,'pwd':pwd})
    conn.commit()

def direct():
    global a,b1
    b1=fn.get()
    a=pe.get()
    print(b1,a)
    final=[pi.get(),ci.get(),ss.get(),bi.get(),ci.get(),ce.get(),pe.get(),em.get(),ni.get(),fn.get()]
    for v in final:
        if(v==" "):
            messagebox.showinfo("WARNING","REQUIRED FIELD IS EMPTY")
            break
        else:
            insert_val(b1,a)
            w.destroy()
            import new1
            break

w=Tk()
w.attributes("-fullscreen",True)
l=Label(text="WELCOME TO PYTHON QUIZ",font=("Times New Roman",44),bg="black",fg="white")
l.place(relx=0.26,rely=0.1)
w.configure(bg="black")

#variables


#mainframe
mf=Frame(bg="grey",height=w.winfo_screenheight()/1.4,width=w.winfo_screenwidth()/1.2)
mf.place(relx=0.1,rely=0.22)
fn=Entry(mf,bg="skyblue",font=(15),bd=2,width=23)
fn.insert(0," ")
n=Label(mf,text="NAME :",bg="grey",font=("Times New Roman",15,'bold'))
fn.place(relx=0.2,rely=0.2)
n.place(relx=0.12,rely=0.2)
na=Label(mf,text="NATIONALITY :",bg="grey",font=("Times New Roman",15,'bold'))
na.place(relx=0.5,rely=0.2)
ni=Entry(mf,bg="skyblue",font=(15),bd=2,width=18)
ni.insert(0," ")
ni.place(relx=0.63,rely=0.2)
em=Entry(mf,bg="skyblue",font=(15),bd=2,width=25)
em.insert(0," ")
e=Label(mf,text="E-MAIL ID :",bg="grey",font=("Times New Roman",15,'bold'))
em.place(relx=0.22,rely=0.3)
e.place(relx=0.12,rely=0.3)
pw=Label(mf,text="PASSWORD :",bg="grey",font=("Times New Roman",15,'bold'))
pe=Entry(mf,bg="skyblue",font=(15),bd=2,show="*")
pe.insert(0," ")
pe.place(relx=0.63,rely=0.3)
pw.place(relx=0.52,rely=0.3)
nc=Label(mf,text="NAME OF THE COLLEGE/UNIVERSITY :",bg="grey",font=("Times New Roman",15,'bold'))
ce=Entry(mf,bg="skyblue",font=(15),bd=2,width=40)
ce.insert(0," ")
nc.place(relx=0.12,rely=0.4)
ce.place(relx=0.43,rely=0.4)
cd=Label(mf,text="NAME OF THE COURSE ENROLLED :",bg="grey",font=("Times New Roman",15,'bold'))
cd.place(relx=0.12,rely=0.5)
ci=Entry(mf,bg="skyblue",font=(15),bd=2,width=30)
ci.insert(0," ")
ci.place(relx=0.4,rely=0.5)
b=Label(mf,text="BRANCH :",bg="grey",font=("Times New Roman",15,'bold'))
b.place(relx=0.12,rely=0.6)
bi=Entry(mf,bg="skyblue",font=(15),bd=2,width=30)
bi.insert(0," ")
bi.place(relx=0.21,rely=0.6)
si=Label(mf,text="SPECIFIC INFORMATION(IF ANY) :",bg="grey",font=("Times New Roman",15,'bold'))
si.place(relx=0.49,rely=0.6)
ss=Entry(mf,bg="skyblue",font=(15),bd=2,width=20)
ss.insert(0," ")
ss.place(relx=0.75,rely=0.6)
ad=Label(mf,text="CONTACT NUMBER :",bg="grey",font=("Times New Roman",15,'bold'))
ci=Entry(mf,bg="skyblue",font=(15),bd=2,width=20)
ci.insert(0," ")
ad.place(relx=0.12,rely=0.7)
ci.place(relx=0.29,rely=0.7)
pa=Label(mf,text="ADDRESS :",bg="grey",font=("Times New Roman",15,'bold'))
pi=Entry(mf,bg="skyblue",font=(15),bd=2,width=50)
pi.insert(0," ")
pa.place(relx=0.12,rely=0.8)
pi.place(relx=0.22,rely=0.8)

#submit
b=Button(mf,text="SUBMIT",bd=5,font=("Times New Roman",20),bg="black",activebackground="black",foreground="white",activeforeground="white",command=direct)
b.place(relx=0.8,rely=0.85)

conn.commit()



w.mainloop()

