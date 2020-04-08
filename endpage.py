from tkinter import *

def last():
    w.destroy()
    import landpagecopy

def last2():
    w.destroy()
    import new1

w=Tk()
w.attributes("-fullscreen",True)
w.configure(bg="black")

#mainframe
mf=Frame(bg="grey",width=w.winfo_screenwidth()/1.2,height=w.winfo_screenheight()/1.5)
mf.place(relx=0.1,rely=0.22)
l=Label(w,text="THANK YOU FOR USING THE PYTHON QUIZ",font=("Times New Roman",30,'bold'),bg="black",fg="white")
l.place(relx=0.1,rely=0.1)
r=Label(mf,text="THIS IS YOUR RESULT :",bg="grey",fg="black",font=("Times New Roman",30,'bold'))
r.place(relx=0.1,rely=0.1)
c=Label(mf,text="Number of Right Answers :",bg="grey",fg="black",font=("Times New Roman",20,))
c.place(relx=0.1,rely=0.3)
c=Label(mf,text="Number of Wrong Answers :",bg="grey",fg="black",font=("Times New Roman",20,))
c.place(relx=0.1,rely=0.4)
c=Label(mf,text="Number of Unattempted Answers :",bg="grey",fg="black",font=("Times New Roman",20,))
c.place(relx=0.1,rely=0.5)
sc=Label(mf,text="YOUR TOTAL SCORE IS :",bg="grey",fg="black",font=("Times New Roman",30,'bold'))
sc.place(relx=0.1,rely=0.6)
cm=Label(mf,text="Remarks :",bg="grey",fg="black",font=("Times New Roman",20))
cm.place(relx=0.1,rely=0.7)
re=Button(mf,text="RE-TEST",bd=5,font=("Times New Roman",20,'bold'),bg="black",foreground="white",activeforeground="white",activebackground="grey",command=last)
re.place(relx=0.7,rely=0.8)
lt=Button(mf,text="LOG OUT",bd=5,font=("Times New Roman",20,'bold'),bg="black",foreground="white",activeforeground="white",activebackground="grey",command=last2)
lt.place(relx=0.85,rely=0.8)
w.mainloop()