from tkinter import *
import sqlite3
import random
from tkinter import messagebox


conn=sqlite3.connect("db/questions.db")
c=conn.cursor()

##################VARIABLES########################

i=0
e=0
m=0
r=0
un=0
f=0
g=[]
while(len(g)<11):
    x=random.randint(1,10)
    if x not in g:
        g.append(x)
print(g)

################################FUNCTIONS#####################################

def new():
    global i
    global e
    global g
    i=i+1
    e=e+1
    l.configure(text="Question Number "+str(i))
    b=c.execute("select quest from easyques where qid="+str(g[e])).fetchall()
    p=str(b)
    ques.configure(text=p[2:(len(p)-2):1])

    


def last():
    w.destroy()
    import landpagecopy

def last2():
    w.destroy()
    import new1


def endpage():
    ef.destroy()
    sf.destroy()
    tf.destroy()
    tb1.destroy()
    z.destroy()

    # mainframe
    mf = Frame(bg="grey", width=w.winfo_screenwidth() / 1.2, height=w.winfo_screenheight() / 1.5)
    mf.place(relx=0.1, rely=0.22)
    l = Label(w, text="THANK YOU FOR USING THE PYTHON QUIZ", font=("Times New Roman", 30, 'bold'), bg="black",
              fg="white")
    l.place(relx=0.1, rely=0.1)
    r = Label(mf, text="THIS IS YOUR RESULT :", bg="grey", fg="black", font=("Times New Roman", 30, 'bold'))
    r.place(relx=0.1, rely=0.1)
    c = Label(mf, text="Number of Right Answers : 5", bg="grey", fg="black", font=("Times New Roman", 20,))
    c.place(relx=0.1, rely=0.3)
    c = Label(mf, text="Number of Wrong Answers : 2", bg="grey", fg="black", font=("Times New Roman", 20,))
    c.place(relx=0.1, rely=0.4)
    c = Label(mf, text="Number of Unattempted Answers : 3", bg="grey", fg="black", font=("Times New Roman", 20,))
    c.place(relx=0.1, rely=0.5)
    sc = Label(mf, text="YOUR TOTAL SCORE IS : 4.5/10", bg="grey", fg="black", font=("Times New Roman", 30, 'bold'))
    sc.place(relx=0.1, rely=0.6)
    cm = Label(mf, text="Remarks :", bg="grey", fg="black", font=("Times New Roman", 20))
    cm.place(relx=0.1, rely=0.7)
    re = Button(mf, text="RE-TEST", bd=5, font=("Times New Roman", 20, 'bold'), bg="black", foreground="white",
                activeforeground="white", activebackground="grey", command=last)
    re.place(relx=0.7, rely=0.8)
    lt = Button(mf, text="LOG OUT", bd=5, font=("Times New Roman", 20, 'bold'), bg="black", foreground="white",
                activeforeground="white", activebackground="grey", command=last2)
    lt.place(relx=0.85, rely=0.8)



def displayoptions(option):
    pp=0.35
    for k in range(0,len(option)):
        B=Label(text=option[k], bg="black",fg="white",font=("Times New Roman",22,'bold'),bd=5,width=12)
        B.place(relx=0.3,rely=pp)
        pp=pp+0.07
    b=Button(ef,text="NEXT",bg="black",fg="white",font=("Times New Roman",20,"bold"),width=8,bd=3,
               activebackground="grey",activeforeground="black",highlightcolor="grey",command=new)
    b.place(relx=0.8, rely=0.8)
    B.forget()

##################################window#################################################

w=Tk()
w.attributes("-fullscreen",True)
w.configure(bg="black")

#examframe
ef=Frame(bg="grey",height=w.winfo_screenheight()/1.8,width=w.winfo_screenwidth()/1.5)
ef.place(relx=0.23,rely=0.2)
a=str(c.execute("select quest from easyques where qid=1").fetchall())
ques=Label(ef,text=a[2:(len(a)-2):1],bg="grey",font=("Times New Roman",25,"bold"))
ques.place(relx=0.09,rely=0.1)

#numbering
bp=0.269
for y in range(1,5):
    hi=Label(ef,text=(str(y)+")"),bg="black",fg="white",font=("Times New Roman",22,'bold'),bd=5,width=4)
    hi.place(relx=0.05,rely=bp)
    bp=bp+0.126

#options
q1=["James Gouslin","Guido Rossum","Dennis Retchie","Bane Strostrup"]
displayoptions(q1)

#sideframe
sf=Frame(bg="grey",height=w.winfo_screenheight()/1.8,width=w.winfo_screenwidth()/5)
sf.place(relx=0.01,rely=0.2)

#topframe
tf=Frame(bg="grey",height=w.winfo_screenheight()/9,width=w.winfo_screenwidth()/2)
tf.place(relx=0.23,rely=0.04)
l=Label(tf,text="Question Number 1",bg="grey",font=("Arial Black",40))
l.place(relx=0.17,rely=0.05)

#canvas
z=Canvas(w,height=w.winfo_screenheight()/6,width=w.winfo_screenwidth()/10)
z.place(relx=0.0999,rely=0.01)
img=PhotoImage(file="new11.gif")
z.create_image(2,2 ,anchor=NW , image=img)

#taskbar
tb1=Frame(bg="grey",height=w.winfo_screenheight()/12,width=w.winfo_screenwidth()/1)
tb1.place(relx=0.0,rely=0.85)
end=Button(tb1,text="END",background="black",foreground="white",activebackground="black",font=("Times New Roman",20,'bold'),width=10,command=endpage)
end.place(relx=0.8,rely=0.1)


#response

#o=res.get()

#submit
ent=Label(ef, text="YOUR RESPONSE :",font=("Times New Roman", 22, 'bold'),bg="grey")
ent.place(relx=0.05, rely=0.8)
res=Entry(ef, bg="skyblue", font=("Times New Roman", 20, 'bold'), width=4, bd=5)
res.place(relx=0.32, rely=0.8)
S=Button(ef, text="SUBMIT", bg="black", fg="white", font=("Times New Roman", 20, "bold"), width=10, bd=3,activebackground="grey", activeforeground="black", highlightcolor="grey",command=new)
S.place(relx=0.62,rely=0.8)

w.mainloop()
