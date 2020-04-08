from tkinter import *
from tkinter import messagebox
import sqlite3

conn=sqlite3.connect("db/registrations.db")
c=conn.cursor()

def login():
    a=eid.get()
    b=eid2.get()
    print(a,b)
    t=c.execute("select Password from student where Name='"+str(a)+"'").fetchall()
    t=str(t)
    t=t[3:len(t)-4:1]
    print(t)
    if(b==t and b!=" " and a!=" "):
        w.destroy()
        import landpagecopy
    else:
        messagebox.showinfo("WARNING","\nInvaid username or password")

def register():
    w.destroy()
    import registration

hfont="MathJax_Typewriter"
#window
w=Tk()
w.attributes("-fullscreen",True)
w.configure(bg="black")
w.title("PYTHON QUIZ")
t1=Label(w,text=" WELCOME TO PYTHON QUIZ",font=("Times New Roman",44),bg="black",fg="white")
t1.place(relx=0.24,rely=0.18)
t2=Label(w,text="A NEW WAY TO LEARN",font=("Britannic Bold",33),bg="black",fg="grey")
t2.place(relx=0.33,rely=0.28)

#frame
loginf=Frame(w,bg="grey",height=w.winfo_screenheight()/3,width=w.winfo_screenwidth()/2)
loginf.place(relx=0.23,rely=0.4)
label=Label(loginf,text="LOGIN TO ATTEMPT TEST",font=("Gill Sans Ultra Bold",30),fg="black",bg="grey")
label.place(relx=0.16,rely=0.1)
label1=Label(loginf,text="USERNAME  :",bg="grey",font=("Century",18))
label1.place(relx=0.15,rely=0.38)
label2=Label(loginf,text="PASSWORD  :",bg="grey",font=("Century",18),highlightbackground="red")
label2.place(relx=0.15,rely=0.52)
eid=Entry(loginf,bg="sky blue",bd=2,font=(hfont,18))
eid.insert(0," ")
eid.place(relx=0.39,rely=0.38)
eid2=Entry(loginf,bg="sky blue",bd=2,font=(hfont,18),show='*')
eid2.insert(0," ")
eid2.place(relx=0.39,rely=0.52)
b1=Button(loginf,bd=11,text="LOGIN",bg="black",font=("Eras Bold ITC",20),activeforeground="black",highlightcolor="red",activebackground="grey",command=login,fg="white")
b1.place(relx=0.56,rely=0.65)

#taskbar
tb=Frame(w,bg="grey",height=w.winfo_screenheight()/12,width=w.winfo_screenwidth())
tb.place(relx=0,rely=0.85)
lbt=Button(tb,bd=1,bg="black",text="DEVELOPED BY : Anurag Srivastava",fg="white",font=("Times New Roman",16),activebackground="black",activeforeground="white")
lbt.place(relx=0,rely=0.3)
mb=Label(tb,text="LOGIN TO ATTEMPT TEST",bg="grey",font=(hfont,18,'bold','italic'),fg="black")
mb.place(relx=0.4,rely=0.4)

#canvas
c1=Canvas(w,height=w.winfo_screenheight()/3.6,width=w.winfo_screenwidth()/6.6)
c1.place(relx=0.009,rely=0.05)
img=PhotoImage(file="new.gif")
c1.create_image(2,0, anchor=NW, image=img)

#button
t=Button(w,text="SIGN UP",bd=11,bg="black",font=("Eras Bold ITC",20),foreground="white",activeforeground="white",highlightcolor="red",activebackground="grey",command=register)
t.place(relx=0.8,rely=0.85)
w.mainloop()