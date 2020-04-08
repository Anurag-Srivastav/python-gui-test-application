from tkinter import *
from tkinter import messagebox
import sqlite3
import random
conn=sqlite3.connect("db/questions.db")
c=conn.cursor()
i=1
e=0
g=[]
m=0
w=0
r=0
op=[[],["James Gouslin","Guido Rossum","Dennis Retchie","Bane Strostrup"],["Integer","String","Float","Double"],["z=z++","z=z+-","z=z+1","z=z**"],["[1j,4,5]","[5,4,1j]","Type Error","[4,5,1j]"],["Function","Cursor","Module","Class"],["insert","append","Only 1","Both 1 and 2"],["List","Tuple","Dictionary","Set"],["12","16","64","18"],["Canvas","Turtle","Tkinter","Graphics"],["1","-2","2","-1"],[]]
while(len(g)<10):
    x=random.randint(1,10)
    if(x not in g):
        g.append(x)
print(g)

def new():
    global op
    global i
    global e
    global g
    i=i+1
    if(e<9):
        e=e+1
    l.configure(text="Question Number "+str(i))
    b=c.execute("select quest from easyques where qid="+str(g[e])).fetchall()
    p=str(b)
    ques.configure(text=p[2:(len(p)-2):1])
    b1.configure(text=op[g[e]][0])
    b2.configure(text=op[g[e]][1])
    b3.configure(text=op[g[e]][2])
    b4.configure(text=op[g[e]][3])


def endpage():
    ef.destroy()
    sf.destroy()
    tf.destroy()
    tb1.destroy()
    z.destroy()

    #mainframe
    mf=Frame(bg="grey",width=w.winfo_screenwidth()/1.2,height=w.winfo_screenheight()/1.5)
    mf.place(relx=0.1,rely=0.22)
    l=Label(w,text="THANK YOU FOR USING THE PYTHON QUIZ",font=("Times New Roman",30,'bold'),bg="black",fg="white")
    l.place(relx=0.1,rely=0.1)
    r=Label(mf,text="THIS IS YOUR RESULT :",bg="grey",fg="black",font=("Times New Roman",30,'bold'))
    r.place(relx=0.1,rely=0.1)
    c=Label(mf,text="Number of Right Answers : +"+str(r),bg="grey",fg="black",font=("Times New Roman",20))
    c.place(relx=0.1,rely=0.3)
    c=Label(mf,text="Number of Wrong Answers : "+str(w),bg="grey",fg="black",font=("Times New Roman",20))
    c.place(relx=0.1,rely=0.4)
    c=Label(mf, text="Number of Unattempted Answers : 3", bg="grey",fg="black",font=("Times New Roman", 20))
    c.place(relx=0.1, rely=0.5)
    sc=Label(mf,text="YOUR TOTAL SCORE IS : "+str(m)+"/10",bg="grey",fg="black",font=("Times New Roman", 30, 'bold'))
    sc.place(relx=0.1, rely=0.6)
    cm=Label(mf,text="Remarks :",bg="grey",fg="black",font=("Times New Roman",20))
    cm.place(relx=0.1, rely=0.7)
    re=Button(mf,text="RE-TEST",bd=5,font=("Times New Roman",20,'bold'),bg="black",foreground="white",activeforeground="white",activebackground="grey")
    re.place(relx=0.7,rely=0.8)
    lt=Button(mf,text="LOG OUT",bd=5,font=("Times New Roman",20,'bold'),bg="black",foreground="white",activeforeground="white",activebackground="grey")
    lt.place(relx=0.85,rely=0.8)

def check(a):
    global m,r,w,i
    global g
    global e
    if(g[e]==1 and a==2):
        m+=1
        r+=1
    if(g[e]==2 and a==2):
        m=m+1
        r+=1
    if(g[e]==3 and a==1):
        m=m+1
        r+=1
    if(g[e]==4 and a==3):
        m=m+1
        r+=1
    if(g[e]==5 and a==4):
        m=m+1
        r+=1
    if(g[e]==6 and a==1):
        m=m+1
        r+=1
    if(g[e]==7 and a==2):
        m=m+1
        r+=1
    if(g[e]==8 and a==2):
        m=m+1
        r+=1
    if(g[e]==9 and a==2):
        m=m+1
        r+=1
    if(g[e]==10 and a==4):
        m=m+1
        r+=1
    if(e==9):
        w=10-r
        m=m-(w*0.25)
        print(m,r,w)
        endpage()
        exit
    new()


w=Tk()
w.attributes("-fullscreen",True)
w.configure(bg="black")

#examframe
ef=Frame(bg="grey",height=w.winfo_screenheight()/1.8,width=w.winfo_screenwidth()/1.5)
ef.place(relx=0.23,rely=0.2)
a=str(c.execute("select quest from easyques where qid="+str(g[e])).fetchall())
ques=Label(ef,text=a[2:(len(a)-2):1],bg="grey",font=("Times New Roman",25,"bold"))
ques.place(relx=0.09,rely=0.1)

#sideframe
sf=Frame(bg="grey",height=w.winfo_screenheight()/1.8,width=w.winfo_screenwidth()/5)
sf.place(relx=0.01,rely=0.2)

#topframe
tf=Frame(bg="grey",height=w.winfo_screenheight()/9,width=w.winfo_screenwidth()/2)
tf.place(relx=0.23,rely=0.04)
l=Label(text="Question Number 1",bg="grey",font=("Arial Black",40))
l.place(relx=0.27,rely=0.05)

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
S=Button(ef,text="SUBMIT",bg="black",fg="white",font=("Times New Roman",20,"bold"),width=10,bd=3,activebackground="grey",activeforeground="black",highlightcolor="grey",command=new)
S.place(relx=0.56,rely=0.8)

#button
b1=Button(ef,text=op[g[e]][0],bg="black",fg="white",font=("Times New Roman",20,"bold"),width=10,bd=6,activebackground="grey",activeforeground="black",highlightcolor="grey",command=lambda:check(1))
b1.place(relx=0.1,rely=0.3)
b2=Button(ef,text=op[g[e]][1],bg="black",fg="white",font=("Times New Roman",20,"bold"),width=10,bd=6,activebackground="grey",activeforeground="black",highlightcolor="grey",command=lambda:check(2))
b2.place(relx=0.1,rely=0.45)
b3=Button(ef,text=op[g[e]][2],bg="black",fg="white",font=("Times New Roman",20,"bold"),width=10,bd=6,activebackground="grey",activeforeground="black",highlightcolor="grey",command=lambda:check(3))
b3.place(relx=0.1,rely=0.6)
b4=Button(ef,text=op[g[e]][3],bg="black",fg="white",font=("Times New Roman",20,"bold"),width=10,bd=6,activebackground="grey",activeforeground="black",highlightcolor="grey",command=lambda:check(4))
b4.place(relx=0.1,rely=0.75)


w.mainloop()
