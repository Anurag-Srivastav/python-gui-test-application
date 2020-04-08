from tkinter import *
import sqlite3
from tkinter import messagebox


conn=sqlite3.connect("db/questions.db")
c=conn.cursor()

##################VARIABLES########################

i=1
m=0
r=0
un=0
f=0

################################FUNCTIONS#####################################

def new():
    box=0
    q2=["Integer","String","Float","Double"] #2
    q3=["z=z++","z=z+-","z=z+1","z=z**"] #1
    q4=["[1j,4,5]","[5,4,1j]","Type Error","[4,5,1j]"] #3
    q5=["Function","Cursor","Module","Class"] #4
    q6=["insert","append","Only 1","Both 1 and 2"] #1
    q7=["List","Tuple","Dictionary","Set"] #2
    q8=["12","16","64","18"] #2
    q9=["Canvas","Turtle","Tkinter","Graphics"] #2
    q10=["1","-2","2","-1"] #4
    global i
    i=i+1
    l.configure(text="Question Number "+str(i))
    b=c.execute("select quest from easyques where qid=" + str(i)).fetchall()
    p=str(b)
    ques.configure(text=p[2:(len(p) - 2):1])
    if(i==2):
        displayoptions(q2)
    if(i==3):
        displayoptions(q3)
    if(i==4):
        displayoptions(q4)
    if(i==5):
        displayoptions(q5)
    if(i==6):
        displayoptions(q6)
    if(i==7):
        displayoptions(q7)
    if(i==8):
        displayoptions(q8)
    if(i==9):
        displayoptions(q9)
    if(i==10):
        displayoptions(q10)
    if(i==11):
        w.destroy()
        import endpage
    for box in range(0,15):
        ent=Label(ef, text="YOUR RESPONSE :",font=("Times New Roman",22,'bold'),bg="grey")
        ent.place(relx=0.05, rely=0.8)
        res=Entry(ef,bg="skyblue",font=("Times New Roman",20,'bold'),width=4,bd=5)
        res.place(relx=0.32, rely=0.8)
        u=res.get()
    check(u)

def check(u):
    global i
    global m
    global r
    global un
    global f
    if(i==1 and u=='2'):
        m=m+1
        r=r+1
    elif i not in ['1','2','3','4']:
        un=un+1
    else:
        m=c-0.25
        f=f+1
    print(m,r,un,f)

def endpage():
    w.destroy()
    import endpage


def displayoptions(option):
    pp=0.35
    for k in range(0,len(option)):
        B=Label(text=option[k], bg="black",fg="white",font=("Times New Roman",22,'bold'),bd=5,width=12)
        B.place(relx=0.3,rely=pp)
        pp=pp+0.07
    b=Button(ef,text="Next",bg="black",fg="white",font=("Times New Roman",20,"bold"),width=10,bd=3,
               activebackground="grey",activeforeground="black",highlightcolor="grey",command=new)
    b.place(relx=0.75, rely=0.8)
    B.forget()

def calc(n):
    global i
    if(i==2 and n==2):
        c=c+1;
        print(c)





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

#response

#o=res.get()

#submit
ent=Label(ef, text="YOUR RESPONSE :",font=("Times New Roman", 22, 'bold'),bg="grey")
ent.place(relx=0.05, rely=0.8)
res=Entry(ef, bg="skyblue", font=("Times New Roman", 20, 'bold'), width=4, bd=5)
res.place(relx=0.32, rely=0.8)
u=res.get()
print(u)
S=Button(ef, text="SUBMIT", bg="black", fg="white", font=("Times New Roman", 20, "bold"), width=10, bd=3,activebackground="grey", activeforeground="black", highlightcolor="grey",command=new)
S.place(relx=0.56,rely=0.8)

w.mainloop()