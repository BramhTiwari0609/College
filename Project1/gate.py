from tkinter import*
import mysql.connector
from tkinter import font
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image



#===================================List Of Student ===============================

def list1():
    Li = Toplevel(tk)
    Li.geometry('800x600')
    Li.configure(bg='#12a4d9')
    headingFrame1 = Frame(Li,bg='#FFBB00',bd=5) 
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

    hlabl = Label(headingFrame1,text="View the List of \n Student Gate Pass System",font=('Courier',15,'bold','italic'),bg='black',fg='white')
    hlabl.place(relx=0,rely=0,relwidth=1,relheight=1)
    
    labelFrame = Frame(Li,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)


    Label(labelFrame,text="%-30s%-20s%-20s%-20s%-20s%-50s"%('Student_Name','Student_id','Course','Branch','Contact_no','Reason'),bg='black',fg='white').place(relx=0.07,rely=0.1)
    Label(labelFrame,text="===========================================================================================================",bg='black',fg='white').place(relx=0.07,rely=0.15)
    y=0.25
    try:
        con = mysql.connector.connect(host='localhost',user='gate',password='gatepass',database='gate_pass')
        cur=con.cursor()
        
        cur.execute('select * from student')
        row = cur.fetchall()
        con.commit()
        for i in row:
            Label(labelFrame,text="%-30s%-20s%-20s%-20s%-20s%-50s"%(i[0],i[1],i[2],i[3],i[4],i[5]),bg='black',fg='white').place(relx=0.07,rely=y)
            y += 0.1
    except Exception as es:
               messagebox.showerror("Error",f"Error Due to : {str(es)}")
     


#=====================================================List Of Visitor====================================


def list2():

    Li = Toplevel(tk)
    Li.geometry('800x600')

    Li.configure(bg='#12a4d9')

    
    headingFrame1 = Frame(Li,bg='#FFBB00',bd=5) 
    headingFrame1.place(relx=0.1,rely=0.1,relwidth=0.6,relheight=0.16)

    hlabl = Label(headingFrame1,text="View the List of \n Visitor Gate Pass System",font=('Courier',15,'bold','italic'),bg='black',fg='white')
    hlabl.place(relx=0,rely=0,relwidth=1,relheight=1)
    
    labelFrame = Frame(Li,bg='black')
    labelFrame.place(relx=0.05,rely=0.3,relwidth=0.9,relheight=0.6)


    Label(labelFrame,text="%-20s%-30s%-40s%-40s%-30s%-30s"%('Name','Email','Address','Contact_no','Reason','Time'),bg='black',fg='white').place(relx=0.07,rely=0.1)
    Label(labelFrame,text="===========================================================================================================",bg='black',fg='white').place(relx=0.07,rely=0.15)
    y=0.25
    
    try:
        con = mysql.connector.connect(host='localhost',user='gate',password='gatepass',database='gate_pass')
        cur=con.cursor()
        
        cur.execute('select * from visitor')
        row = cur.fetchall()
        con.commit()
        for i in row:
            Label(labelFrame,text="%-20s%-20s%-40s%-20s%-20s%-20s"%(i[0],i[1],i[2],i[3],i[4],i[5]),bg='black',fg='white').place(relx=0.07,rely=y)
            y += 0.1
       
         
    except Exception as es:
               messagebox.showerror("Error",f"Error Due to : {str(es)}")
     




#==================================================================Visitor===================================================================
def outsider():
    In = Toplevel(tk)
    In.geometry('800x600')
    In.config(bg='#006B38')
    headingFrame1 = Frame(In,bg='yellow',bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

    hlabl = Label(headingFrame1,text="Welcom To Visitor\n Gate Pass System",font=('Courier',15,'bold','italic'),bg='black',fg='white')
    hlabl.place(relx=0,rely=0,relwidth=1,relheight=1)

    labelFrame = Frame(In,bg='black')
    labelFrame.place(relx=0.15,rely=0.35,relwidth=0.7,relheight=0.5)

    lb1 = Label(labelFrame,text='Name : ', bg='black',fg='white',font=('Courier',15))
    lb1.place(relx=0.03,rely=0.12,relheight=0.08)

    vn = ttk.Entry(labelFrame)
    vn.place(relx=0.3,rely=0.12,relwidth=0.62,relheight=0.08)
    
    lb2 = Label(labelFrame,text='Email : ', bg='black',fg='white',font=('Courier',15))
    lb2.place(relx=0.03,rely=0.27,relheight=0.08)

    ve = ttk.Entry(labelFrame)
    ve.place(relx=0.3,rely=0.27,relwidth=0.62,relheight=0.08)
    
    lb3 = Label(labelFrame,text='Address : ', bg='black',fg='white',font=('Courier',15))
    lb3.place(relx=0.03,rely=0.42,relheight=0.08)

    va = ttk.Entry(labelFrame)
    va.place(relx=0.3,rely=0.42,relwidth=0.62,relheight=0.08)

    lb4 = Label(labelFrame,text='Contact No. : ', bg='black',fg='white',font=('Courier',15))
    lb4.place(relx=0.03,rely=0.57,relheight=0.08)

    vc = ttk.Entry(labelFrame)
    vc.place(relx=0.3,rely=0.57,relwidth=0.62,relheight=0.08)


    lb5 = Label(labelFrame,text='REASON : ', bg='black',fg='white',font=('Courier',15))
    lb5.place(relx=0.03,rely=0.72,relheight=0.08)

    vr = ttk.Entry(labelFrame)
    vr.place(relx=0.3,rely=0.72,relwidth=0.62,relheight=0.08)

    lb6 = Label(labelFrame,text='Time : ', bg='black',fg='white',font=('Courier',15))
    lb6.place(relx=0.03,rely=0.87,relheight=0.08)

    vt = ttk.Entry(labelFrame)
    vt.place(relx=0.3,rely=0.87,relwidth=0.62,relheight=0.08)



    def visitor():
        name = vn.get()
        email = ve.get()
        address = va.get()
        contact = vc.get()
        reason = vr.get()
        time = vt.get()
        
        if vn.get()=="" or ve.get()=="" or va.get()==""or vc.get()=="" or vr.get()=="" or vt.get()=="" :
           messagebox.showerror("Error","All fields are required")
        else:
            try:
                con = mysql.connector.connect(host='localhost',user='gate',password='gatepass',database='gate_pass')
                cur=con.cursor()
                sql = "insert into visitor (name,email,address,contact,reason,time)values(%s,%s,%s,%s,%s,%s)"
                v = (name,email,address,contact,reason,time)
                cur.execute(sql,v)
                con.commit()
                messagebox.showinfo("Success","Pass Generated")
                p = Toplevel(In)
                p.geometry('600x500')
                p.configure(bg='darkcyan')
                heading = Label(p,text="SucessFully Generated Pass")
                heading.pack()
                
            except Exception as es:
               messagebox.showerror("Error",f"Error Due to : {str(es)}")


    
    Genbtn = Button(In,text='Generate',bg='#1dccc0',fg='black',command=visitor)
    Genbtn.place(relx=0.28,rely=0.9,relwidth=0.18,relheight=0.08)

    quitbtn = Button(In,text='Quit',bg='#f7f1e3',fg='black',command=In.destroy)
    quitbtn.place(relx=0.53,rely=0.9,relwidth=0.18,relheight=0.08)
     
#===================================================================Enquiry Portion===================================================================

def enquiry1():
    en = Toplevel(tk)
    en.geometry('800x600')
    en.config(bg='#ff6e40')
    headingFrame1 = Frame(en,bg='yellow',bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

    hlabl = Label(headingFrame1,text="Search Gate Pass",font=('Courier',15,'bold','italic'),bg='black',fg='white')
    hlabl.place(relx=0,rely=0,relwidth=1,relheight=1)

    labelFrame = Frame(en,bg='black')
    labelFrame.place(relx=0.15,rely=0.35,relwidth=0.7,relheight=0.5)

    lb1 = Label(labelFrame,text='Student Id : ', bg='black',fg='white',font=('Courier',15))
    lb1.place(relx=0.03,rely=0.12,relheight=0.08)

    stdi = ttk.Entry(labelFrame,font=("times new roman",15,'bold'))
    stdi.place(relx=0.3,rely=0.12,relwidth=0.62,relheight=0.08)
    
    lb2 = Label(labelFrame,text='Course : ', bg='black',fg='white',font=('Courier',15))
    lb2.place(relx=0.03,rely=0.27,relheight=0.08)

    stdc = ttk.Entry(labelFrame,font=("times new roman",15,'bold'))
    stdc.place(relx=0.3,rely=0.27,relwidth=0.62,relheight=0.08)
    def search():

        if stdi.get()=="" or stdc.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            try:
              con = mysql.connector.connect(host='localhost',user='gate',password='gatepass',database='gate_pass')
              cur = con.cursor()
              cur.execute("select * from student where student_id=%s and course=%s",(stdi.get(),stdc.get()))
              row = cur.fetchone()
              if row==None:
                messagebox.showerror("Error","Pass is Not aviable")
              else:
                messagebox.showinfo("Successfully ","Pass Is Exist")
                con.close()
            except Exception as es:
                messagebox.showerror("Error",f"Error Due to : {str(es)}")

    btn = Button(en,text='Search',bg='#1dccc0',fg='black',command=search)
    btn.place(relx=0.28,rely=0.9,relwidth=0.18,relheight=0.08)

    quitbtn = Button(en,text='Quit',bg='#f7f1e3',fg='black',command=en.destroy)
    quitbtn.place(relx=0.53,rely=0.9,relwidth=0.18,relheight=0.08)
#===================================================================================================    


def enquiry2():
    en = Toplevel(tk)
    en.geometry('800x600')
    en.config(bg='#ff6e40')
    headingFrame1 = Frame(en,bg='yellow',bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

    hlabl = Label(headingFrame1,text="Search Gate Pass",font=('Courier',15,'bold','italic'),bg='black',fg='white')
    hlabl.place(relx=0,rely=0,relwidth=1,relheight=1)

    labelFrame = Frame(en,bg='black')
    labelFrame.place(relx=0.15,rely=0.35,relwidth=0.7,relheight=0.5)

    lb1 = Label(labelFrame,text='Email : ', bg='black',fg='white',font=('Courier',15))
    lb1.place(relx=0.03,rely=0.12,relheight=0.08)

    stde = ttk.Entry(labelFrame,font=("times new roman",15,'bold'))
    stde.place(relx=0.3,rely=0.12,relwidth=0.62,relheight=0.08)
    
    lb2 = Label(labelFrame,text='Contact : ', bg='black',fg='white',font=('Courier',15))
    lb2.place(relx=0.03,rely=0.27,relheight=0.08)

    stdc = ttk.Entry(labelFrame,font=("times new roman",15,'bold'))
    stdc.place(relx=0.3,rely=0.27,relwidth=0.62,relheight=0.08)
    
    def search():

        if stde.get()=="" or stdc.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            try:
              con = mysql.connector.connect(host='localhost',user='gate',password='gatepass',database='gate_pass')
              cur = con.cursor()
              cur.execute("select * from visitor where email=%s and contact=%s",(stde.get(),stdc.get()))
              row = cur.fetchone()
              if row==None:
                messagebox.showerror("Error","Pass is Not aviable")
              else:
                messagebox.showinfo("Successfully ","Pass Is Exist")
                con.close()
            except Exception as es:
                messagebox.showerror("Error",f"Error Due to : {str(es)}")




    btn = Button(en,text='Search',bg='#1dccc0',fg='black',command=search)
    btn.place(relx=0.28,rely=0.9,relwidth=0.18,relheight=0.08)

    quitbtn = Button(en,text='Quit',bg='#f7f1e3',fg='black',command=en.destroy)
    quitbtn.place(relx=0.53,rely=0.9,relwidth=0.18,relheight=0.08)




#================================================Student=====================================================================



def insider():
    #global stdn,stdi,stdc,stdC,stdb,stdr,In,con,cur
    In = Toplevel(tk)
    In.geometry('800x600')
    In.config(bg='#ff6e40')

    


    headingFrame1 = Frame(In,bg='yellow',bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

    hlabl = Label(headingFrame1,text="Welcom To Student\n Gate Pass System",font=('Courier',15,'bold','italic'),bg='black',fg='white')
    hlabl.place(relx=0,rely=0,relwidth=1,relheight=1)

    labelFrame = Frame(In,bg='black')
    labelFrame.place(relx=0.15,rely=0.35,relwidth=0.7,relheight=0.5)

    lb1 = Label(labelFrame,text='Student Name : ', bg='black',fg='white',font=('Courier',15))
    lb1.place(relx=0.03,rely=0.12,relheight=0.08)

    stdn = ttk.Entry(labelFrame,font=("times new roman",15,'bold'))
    stdn.place(relx=0.3,rely=0.12,relwidth=0.62,relheight=0.08)
    
    lb2 = Label(labelFrame,text='Student Id : ', bg='black',fg='white',font=('Courier',15))
    lb2.place(relx=0.03,rely=0.27,relheight=0.08)

    stdi = ttk.Entry(labelFrame,font=("times new roman",15,'bold'))
    stdi.place(relx=0.3,rely=0.27,relwidth=0.62,relheight=0.08)
    
    lb3 = Label(labelFrame,text='Course : ', bg='black',fg='white',font=('Courier',15))
    lb3.place(relx=0.03,rely=0.42,relheight=0.08)

    stdc = ttk.Entry(labelFrame,font=("times new roman",15,'bold'))
    stdc.place(relx=0.3,rely=0.42,relwidth=0.62,relheight=0.08)

    lb4 = Label(labelFrame,text='Branch : ', bg='black',fg='white',font=('Courier',15))
    lb4.place(relx=0.03,rely=0.57,relheight=0.08)

    stdb = ttk.Entry(labelFrame,font=("times new roman",15,'bold'))
    stdb.place(relx=0.3,rely=0.57,relwidth=0.62,relheight=0.08)


    lb5 = Label(labelFrame,text='Contact No. : ', bg='black',fg='white',font=('Courier',15))
    lb5.place(relx=0.03,rely=0.72,relheight=0.08)

    stdC = ttk.Entry(labelFrame,font=("times new roman",15,'bold'))
    stdC.place(relx=0.3,rely=0.72,relwidth=0.62,relheight=0.08)


    lb6 = Label(labelFrame,text='Reason : ', bg='black',fg='white',font=('Courier',15))
    lb6.place(relx=0.03,rely=0.87,relheight=0.08)

    stdr = ttk.Entry(labelFrame,font=("times new roman",15,'bold'))
    stdr.place(relx=0.3,rely=0.87,relwidth=0.62,relheight=0.08)
    def add():
        name = stdn.get()
        id = stdi.get()
        course = stdc.get()
        branch = stdb.get()
        contact = stdC.get()
        reason = stdr.get()
        
        if stdn.get()=="" or stdi.get()=="" or stdc.get()==""or stdb.get()=="" or stdC.get()=="" or stdr.get()=="" :
           messagebox.showerror("Error","All fields are required")
        else:
            try:
                con = mysql.connector.connect(host='localhost',user='gate',password='gatepass',database='gate_pass')
                cur=con.cursor()
                sql = "insert into student (student_name,student_id,course,branch,contact_no,reason)values(%s,%s,%s,%s,%s,%s)"
                v = (name,id,course,branch,contact,reason)
                cur.execute(sql,v)
                con.commit()
                messagebox.showinfo("Success","Pass Generated")
                p = Toplevel(In)
                p.geometry('600x500')
                p.configure(bg='darkcyan')

         
            except Exception as es:
               messagebox.showerror("Error",f"Error Due to : {str(es)}")


    
    Genbtn = Button(In,text='Generate',bg='#1dccc0',fg='black',command=add)
    Genbtn.place(relx=0.28,rely=0.9,relwidth=0.18,relheight=0.08)

    quitbtn = Button(In,text='Quit',bg='#f7f1e3',fg='black',command=In.destroy)
    quitbtn.place(relx=0.53,rely=0.9,relwidth=0.18,relheight=0.08)
     


#====================================================================
def generate():
    gen = Toplevel(tk)
    gen.geometry('1000x800')
    headingFrame1 = Frame(gen,bg='#FFBB00',bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

    hlabl = Label(headingFrame1,text="Generate Pass",font=('Courier',25,'bold','italic'),bg='black',fg='white')
    hlabl.place(relx=0,rely=0,relwidth=1,relheight=1) 

    Ganrate1 = Button(gen,text='Generate Student Gate Pass',font=('Courier',15,'bold'),bg='black',fg='white',command=insider)
    Ganrate1.place(relx=0.28,rely=0.4,relwidth=0.45,relheight=0.1) 
    Ganrate2 = Button(gen,text='Generate Visitor Gate Pass ',font=('Courier',15,'bold'),bg='black',fg='white',command=outsider)
    Ganrate2.place(relx=0.28,rely=0.5,relwidth=0.45,relheight=0.1) 
    Ganrate2 = Button(gen,text=' Enquiry for student gate pass ',font=('Courier',15,'bold'),bg='black',fg='white',command=enquiry1)
    Ganrate2.place(relx=0.28,rely=0.6,relwidth=0.45,relheight=0.1) 
    Ganrate2 = Button(gen,text='Enquiry for Visitor gate pass ',font=('Courier',15,'bold'),bg='black',fg='white',command=enquiry2)
    Ganrate2.place(relx=0.28,rely=0.7,relwidth=0.45,relheight=0.1) 
#==================================================================
def login():
    if username.get()=="" or password.get()=="":
        messagebox.showerror("Error","All fields are required")
    else:
        try:
            con = mysql.connector.connect(host='localhost',user='gate',password='gatepass',database='gate_pass')
            cur = con.cursor()
            cur.execute("select * from login where email=%s and password=%s",(username.get(),password.get()))
            row = cur.fetchone()
            if row==None:
                messagebox.showerror("Error","Invailid Username and Password")
            else:
                #messagebox.showinfo("Success","Welcome")
                new = Toplevel(tk)
                new.geometry('1000x800')
                new.configure(bg='black')

                headingFrame1 = Frame(new,bg='#FFBB00',bd=5)
                headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

                labl = Label(headingFrame1,text="Gate Pass",font=('Courier',25,'bold','italic'),bg='black',fg='white')
                labl.place(relx=0,rely=0,relwidth=1,relheight=1)
                Ganrate = Button(new,text='Generate Gate Pass',font=('Courier',15,'bold'),bg='black',fg='white',command=generate)
                Ganrate.place(relx=0.28,rely=0.4,relwidth=0.45,relheight=0.1) 
                Total = Button(new,text='student Generated Pass',font=('Courier',15,'bold'),bg='black',fg='white',command=list1)
                Total.place(relx=0.28,rely=0.5,relwidth=0.45,relheight=0.1) 
                Add = Button(new,text='Visitor Generated Pass',font=('Courier',15,'bold'),bg='black',fg='white',command=list2)
                Add.place(relx=0.28,rely=0.6,relwidth=0.45,relheight=0.1)
            con.close()
        except Exception as es:
            messagebox.showerror("Error",f"Error Due to : {str(es)}")


#=================================================Forget Password======================================================

def forgets():
    fo = Toplevel(tk)
    fo.geometry('600x500')
    fo.configure(bg='orange')
    flabel = Label(fo,text="Forget Password",font=('Courier',20,'bold'),bg='orange')
    flabel.pack(pady=10)
    lb2 = Label(fo,text='Email : ',fg='black',font=('Courier',15,'bold'),bg='orange')
    lb2.place(relx=0.010,rely=0.27,relheight=0.08)

    Email = ttk.Entry(fo,font=('Courier',15))
    Email.place(relx=0.45,rely=0.27,relwidth=0.5,relheight=0.08)

    lb3 = Label(fo,text='Enter New Password:',fg='black',font=('Courier',15,'bold'),bg='orange')
    lb3.place(relx=0.010,rely=0.42,relheight=0.08)

    password = ttk.Entry(fo,font=('Courier',15))
    password.place(relx=0.45,rely=0.42,relwidth=0.5,relheight=0.08)
    def reset():
         if Email.get()=="" or password.get()=="":
          messagebox.showerror("Error","All fields are required")
         else:
            try:
                con = mysql.connector.connect(host='localhost',user='gate',password='gatepass',database='gate_pass')
                cur = con.cursor()
                cur.execute("select * from login where email=%s",(Email.get()))
                row = cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please Enter Vaild Email")
                else:
                    cur.execute("update login set password=%s where email=%s",(password.get(),Email.get())) 
                    con.commit() 
                    con.close()                      
                    messagebox.showinfo("Successful update")
                    
            except Exception as es:
                 messagebox.showerror("Error",f"Error Due to : {str(es)}")

    
    ok = Button(fo,text='Click',font=('Courier',15,'bold'),borderwidth=0,fg='white',bg='green',command=reset)
    ok.place(x=200,y=300,width=100)



#=====================================First Window====================================================================
def first():
    global tk
    global username
    global password

    tk = Tk()
    tk.title('Gate Pass')
    tk.geometry("1000x800")
    bg = ImageTk.PhotoImage(file="bg1.jpg")
    label = Label(tk, image=bg)
    label.place(relx=0, rely=0, relwidth=1, relheight=1)

 #===============================heading label===============================================================================
 
    my_text = Label(tk,text='Welcome To Gate Pass System', font=("Courier",40,'bold','italic'),fg='red',bg='white')
    my_text.pack(pady=10)
    #==================== login form===========================
    bg1 = ImageTk.PhotoImage(file="images.jpg")
    label1 = Label(tk, image=bg1)
    label1.place(x=150, y=150, width=400, height=500)

    frame = Frame(tk,bg='white')
    frame.place(x=450,y=150, width=400, height=500)

    img = Image.open("login.png")
    img=img.resize((100,70),Image.ANTIALIAS)
    photoimage1 = ImageTk.PhotoImage(img)
    btn2 = Label(frame,image=photoimage1,borderwidth=0,bg='white')
    btn2.place(x=100,y=10,width=100)

    log_label = Label(frame,text='Login',font=("times new roman",25,'bold'),fg='darkgreen',bg='white')
    log_label.place(x=100,y=70)


    usernamelabel = Label(frame,text="User Name",font=("times new roman",15,'bold'),fg='red',bg='white')
    usernamelabel.place(x=40,y=120)

    username=ttk.Entry(frame,font=("times new roman",15,'bold'))
    username.place(x=20,y=160,width=250)


    passwordlabel = Label(frame,text="Password",font=("times new roman",15,'bold'),fg='red',bg='white')
    passwordlabel.place(x=40,y=220)

    password=ttk.Entry(frame,font=("times new roman",15,'bold'))
    password.place(x=20,y=260,width=250)

    #============= login button=========================================
    img = Image.open("btn.png")
    img=img.resize((100,50),Image.ANTIALIAS)
    photoimage = ImageTk.PhotoImage(img)
    btn1 = Button(frame,image=photoimage,borderwidth=0,cursor='hand2',bg='white',command=login)
    btn1.place(x=100,y=300,width=100)

    #============================forgetbutton=======================

    forget = Button(frame,text='Forget Password',font=('Courier',15,'bold'),borderwidth=0,fg='darkcyan',bg='white',command=forgets)
    forget.place(x=20,y=350,width=200)



    #====================icon======================================
    img = Image.open("user.png")
    img=img.resize((25,25),Image.ANTIALIAS)
    photoimage2 = ImageTk.PhotoImage(img)
    btn3 = Label(frame,image=photoimage2,borderwidth=0,bg='white')
    btn3.place(x=10,y=120,width=25)


    img = Image.open("pass.png")
    img=img.resize((25,25),Image.ANTIALIAS)
    photoimage3 = ImageTk.PhotoImage(img)
    btn4 = Label(frame,image=photoimage3,borderwidth=0,bg='white')
    btn4.place(x=10,y=220,width=25)
    tk.mainloop()
first()
 
#========================================================================================================================


