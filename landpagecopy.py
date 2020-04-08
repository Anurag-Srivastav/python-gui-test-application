from tkinter import*

def butt():
    w.destroy()
    import quizlandingpage

def buttonclick(n):
    if(n==1):
        cont.config(state="normal")
    if(n==2):
        cont.config(state="normal")
    if(n==3):
        cont.config(state="normal")

b="#6495ED"
c="#00ffd4"
hfont="MathJax_Typewriter"
w=Tk()
w.attributes("-fullscreen",True)
w.configure(bg="black")
tl=Label(w,text="THE PYTHON QUIZ",font=("Times New Roman",45,'bold'),fg="white",bg="black")
tl.place(relx=0.25,rely=0.08)

#mainframe
mf=Frame(w,bg="grey",height=w.winfo_screenheight()/1.5,width=w.winfo_screenwidth()/1.5)
mf.place(relx=0.13,rely=0.2)
wel=Label(mf,text="Hello Student",font=("Arial Rounded MT Bold",30),fg="black",bg="grey")
wel.place(relx=0.1,rely=0.09)
levb=Button(mf,bd=10,text="YOUR LEVEL : 1",bg="black",activeforeground="white",activebackground="black",font=("Eras Bold ITC",18),fg="white")
levb.place(relx=0.1,rely=0.25)
choice=Label(mf,text="What do you feel like today.???",bg="grey",fg="black",font=("Arial Black",25))
choice.place(relx=0.1,rely=0.4)
c=Canvas(mf,bg="grey",height=w.winfo_screenheight()/5,width=w.winfo_screenheight()/5)
img=PhotoImage(file="dp.gif")
c.create_image(2,1 ,anchor=NW,image=img)
c.place(relx=0.4,rely=0.06)

#radiobutton
var=IntVar()
easy=Radiobutton(text="EASY (Your basic knowledge will be tested)",bg="grey",font=("Eras Bold ITC",18),activebackground="grey",variable="var",value=1,command=lambda:buttonclick(1))
easy.place(relx=0.25,rely=0.55)
normal=Radiobutton(text="NORMAL (Your skills will be challenged)",bg="grey",activebackground="grey",font=("Eras Bold ITC",18),variable="var",value=2,command=lambda:buttonclick(2))
normal.place(relx=0.25,rely=0.6)
hard=Radiobutton(text="HARD (You need to be a master)",bg="grey",activebackground="grey",font=("Eras Bold ITC",18),variable="var",value=3,command=lambda:buttonclick(3))
hard.place(relx=0.25,rely=0.65)


#previousresult
sf=Frame(w,bg="grey",height=w.winfo_screenheight()/5,width=w.winfo_screenheight()/3.5)
sf.place(relx=0.84,rely=0.05)
pb=Button(sf,bd=5,text="PREVIOUS RESULTS",bg="black",activeforeground="white",activebackground="black",font=("Eras Bold ITC",13),fg="white")
pb.place(relx=0.12,rely=0.12)
tsf=Label(sf,text="LET'S SEE SOME OF YOUR \n ACHIEVEMENTS AND FAILURES",font=("Arial Rounded MT Bold",11),bg="grey")
tsf.place(relx=0.06,rely=0.39)
tsf2=Label(sf,text="It's ok to look back,just don't stare",font=("Lucida Calligraphy",10),bg="grey")
tsf2.place(relx=0.01,rely=0.69)

#sideframe1
sf1=Frame(w,bg="grey",height=w.winfo_screenheight()/0.25,width=w.winfo_screenheight())
sf1.place(relx=0.84,rely=0.3)
py1=Label(sf1,text="HISTORY OF \nPYTHON ",bg="grey",font=("Eras Bold ITC",18))
py1.place(relx=0.05,rely=0.002)
py2=Label(sf1,text="python eas developed ny kjfghihrg in 098",bg="grey",font=(hfont,18))
py2.place(relx=0.2,rely=0.2)


#taskbar
tb=Frame(w,bd=5,bg="grey",height=w.winfo_screenheight()/15,width=w.winfo_screenwidth())
tb.place(relx=0,rely=0.89)
bt1=Button(tb,bd=5,text="DEVELOPED BY :- Anurag Srivastava",bg="black",activebackground="black",activeforeground="white",font=("Eras Bold ITC",15),fg="white")
bt1.place(relx=0,rely=0.12)

#continue
cont=Button(mf,bd=10,text="Continue",bg="black",activebackground="black",activeforeground="white",font=("Eras Bold ITC",22),fg="white",state="disable",command=butt)
cont.place(relx=0.8,rely=0.8)

#canvas
z=Canvas(w,height=w.winfo_screenheight()/6,width=w.winfo_screenwidth()/10)
z.place(relx=0.09,rely=0.01)
img=PhotoImage(file="new11.gif")
z.create_image(2,2 ,anchor=NW , image=img)

w.mainloop()
