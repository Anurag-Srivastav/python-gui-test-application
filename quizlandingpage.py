from tkinter import *
from tkinter import messagebox
#from PIL import ImageTk,Image

def hello():
    con.config(state="normal")

def custom():
    w.destroy()
    import exam3


b="#6495ED"
#window
w=Tk()
w.attributes("-fullscreen",True)
w.configure(bg="black")
tl=Label(w,text="THE PYTHON QUIZ",font=("Times New Roman",50,'bold'),fg="white",bg="black")
tl.place(relx=0.15,rely=0.1)


#mainframe
mf=Frame(w,bg="grey",height=w.winfo_screenheight()/2,width=w.winfo_screenwidth()/1.5)
mf.place(relx=0.15,rely=0.25)
t1=Label(mf,text="Please read the following instructions very carefully : ",font=("Times New Roman",20,'bold'),bg="grey")
t1.place(relx=0.05,rely=0.06)
t2=Label(mf,text="1) Check Your Browser Options before the Test to ensure that it is not set to disconnect \n after several minutes of inactivity",
         bg="grey",font=("Bradley Hand ITC",18,'bold'))
t2.place(relx=0.05,rely=0.2)
t3=Label(mf,text="2) Do not press the end botton at any part before completion of the test \n It will commence the test",bg="grey",font=("Bradley Hand ITC",18,'bold'))
t3.place(relx=0.05,rely=0.34)
t4=Label(mf,text="3) Review All of Your Answers Before Submitting the Quiz. Make sure you have not \n accidentally changed your response to a question or made a typographic mistake.",
        bg="grey",font=("Bradley Hand ITC", 18,'bold'))
t4.place(relx=0.05,rely=0.50)
t5=Label(text="4) After you submit the test answers, you will receive a score unless\n you have exceeded the time limit for the quiz."
         ,bg="grey",font=("Bradley Hand ITC", 18,'bold'))
t5.place(relx=0.185,rely=0.60)

#bottomframe
bf=Frame(w,bg="grey",height=w.winfo_screenheight()/7,width=w.winfo_screenwidth())
bf.place(relx=0,rely=0.8)
ia=Frame(bf,height=w.winfo_screenheight()/18,width=w.winfo_screenwidth(),bg="black")
ia.place(relx=0.1,rely=0.1)
c=IntVar()
agree=Checkbutton(bf,font=(22),bg="black",activebackground="black",command=hello)
agree.place(relx=0.18,rely=0.15)
tg=Label(bf,text="I have read all the instructions and agree to the terms and policy.",activebackground="white",font=("Eras Bold ITC",18),bg="black",fg="white")
tg.place(relx=0.2,rely=0.15)

#taskbar
tb=Frame(w,bg="black",height=w.winfo_screenheight()/15,width=w.winfo_screenwidth())
tb.place(relx=0,rely=0.88)
bt1=Button(tb,bd=5,text="Developed by:- Anurag Srivastava",bg="black",activeforeground="white",activebackground="black",font=("Eras Bold ITC",18),fg="white")
bt1.place(relx=0,rely=0.1)

#continue
con=Button(tb,bd=5,text="Continue",bg="black",font=("Eras Bold ITC",20),activebackground="black",fg="white",activeforeground="white",state="disable",command=custom)
con.place(relx=0.8,rely=0.02)

''''#image
ca=Canvas(w,width=200,height=200,)
ca.place(relx=0.001,rely=0.001)'''

w.mainloop()
