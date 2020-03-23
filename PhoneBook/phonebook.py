from Tkinter import *
from tkMessageBox import *
import phone1
import sqlite3
con=sqlite3.Connection("phonebook_db")
cur=con.cursor()
cur.execute("create table if not exists phonebook(Fname varchar2(20),Mname varchar2(10),Lname varchar2(20),company varchar2(30),address varchar2(30),city varchar2(20),pin number(6),website varchar2(30),dob date,contact_type varchar2(10),contact_no number,email_type varchar2(10),email varchar2(50),id number primary key)")
root=Tk()
root.geometry("550x600")
root.title("Phone Book")
d={1:'Office',2:'Home',3:'Mobile',4:'Office',5:'Personal'}
def close():
    root.destroy()
def save():
    if(e1.get()=='' and e2.get()=='' and e3.get()=='' and e4.get()=='' and e5.get()=='' and e6.get()=='' and e7.get()=='' and e8.get()=='' and e9.get()=='' and e11.get()=='' and e13.get()==''):
        showinfo("Save","No data entered!")
    else:
        cur.execute("select max(id) from phonebook")
        id1=cur.fetchall()
        if id1[0][0]==None:
            id0=1
        else:
            id0=id1[0][0]
            id0=id0+1
        p=(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get(),d.get(v1.get()),e11.get(),d.get(v2.get()),e13.get(),id0)
        cur.execute("insert into phonebook values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)",p)
        con.commit()
        showinfo("Save","contact saved!")
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e6.delete(0,END)
        e7.delete(0,END)
        e8.delete(0,END)
        e9.delete(0,END)
        e11.delete(0,END)
        e13.delete(0,END)
def search():
    root_se=Tk()
    root_se.title("Search..")
    def close_s():
        root_se.destroy()
    Label(root_se,text='Searching Phone Book',fg='Black',font='bold 25',bg='sky blue').grid(row=0,column=1)
    Label(root_se,text='Enter Name').grid(row=1,column=0)
    e_s=Entry(root_se)
    e_s.grid(row=1,column=1)
    lb=Listbox(root_se,height=15,width=30,font='20',fg='Blue')
    lb.grid(row=2,column=1)
    def show(sh=1):
        m=lb.curselection()
        for i in m:
            fn=lb.get(i)
        l=fn.split(" ")
        l1=l[0]
        l2=l[1]
        l3=l[2]
        lb.destroy()
        lb1=Listbox(root_se,height=15,width=30,font='20',fg='Black')
        lb1.grid(row=2,column=1)
        cur.execute("select * from phonebook where Fname=? and Mname=? and Lname=?",(l1,l2,l3))
        al=cur.fetchall()
        al1=[]
        al1.append('First Name : '+al[0][0])
        al1.append('Middle Name : '+al[0][1])
        al1.append('Last Name : '+al[0][2])
        al1.append('Company : '+al[0][3])
        al1.append('Address : '+al[0][4])
        al1.append('City : '+al[0][5])
        al1.append('Pin Code : '+str(al[0][6]))
        al1.append('Website URL : '+al[0][7])
        al1.append('Date of Birth : '+al[0][8])
        al1.append('Phone Details...')
        al1.append(str(al[0][9])+' : '+str(al[0][10]))
        al1.append('Email Addresses...')    
        al1.append(str(al[0][11])+' : '+(al[0][12]))
        def delete(e=1):
            d=al[0][13]
            cur.execute("delete from phonebook where id=?",(d,))
            con.commit()
            root_se.destroy()
        Button(root_se,text='Delete',command=delete).grid(row=3,column=2)
        for i in range(len(al1)):
            lb1.insert(END,al1[i])
    cur.execute("select Fname,Mname,Lname from phonebook")
    pall=cur.fetchall()
    for i in range(len(pall)):
                   k1=pall[i][0]
                   k2=pall[i][1]
                   k3=pall[i][2]
                   k=k1+' '+k2+' '+k3+' '
                   lb.insert(END,k)
                   lb.itemconfig(i, {'fg':'blue'})              #self
    lb.bind("<<ListboxSelect>>",show)
    def sname(e=1):
        es=str('%'+e_s.get()+'%')
        lb.delete(0,END)
        cur.execute("select Fname,Mname,Lname from phonebook where Fname like ? or Mname like ? or Lname like ?",(es,es,es))
        pall1=cur.fetchall()
        for i in range(len(pall1)):
                   k1=pall1[i][0]
                   k2=pall1[i][1]
                   k3=pall1[i][2]
                   k=k1+' '+k2+' '+k3
                   lb.insert(END,k)
                   lb.itemconfig(i, {'fg':'blue'})
    
    e_s.bind("<KeyRelease>",sname)
    Button(root_se,text='Close',command=close_s).grid(row=3,column=1)
def edit_search():
    root_se=Tk()
    root_se.title("Edit..")
    def close_s(e=1):
        root_se.destroy()
    def edit_show(E=1):
        def close_e():
            root_edit.destroy()
        def edit_save():
            if(e1.get()=='' and e2.get()=='' and e3.get()=='' and e4.get()=='' and e5.get()=='' and e6.get()=='' and e7.get()=='' and e8.get()=='' and e9.get()=='' and e11.get()=='' and e13.get()==''):
                showinfo("Save","No data entered!")
            else:
                c=al[0][13]
                cur.execute("delete from phonebook where id=?",(c,))
                con.commit()
                cur.execute("select max(id) from phonebook")
                id1=cur.fetchall()
                if id1[0][0]==None:
                    id0=1
                else:
                    id0=id1[0][0]
                    id0=id0+1
                p=(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get(),d.get(v1.get()),e11.get(),d.get(v2.get()),e13.get(),id0)
                cur.execute("insert into phonebook values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)",p)
                con.commit()
                showinfo("Save","contact saved!")
                e1.delete(0,END)
                e2.delete(0,END)
                e3.delete(0,END)
                e4.delete(0,END)
                e5.delete(0,END)
                e6.delete(0,END)
                e7.delete(0,END)
                e8.delete(0,END)
                e9.delete(0,END)
                e11.delete(0,END)
                e13.delete(0,END)
        m=lb.curselection()
        for i in m:
            fn=lb.get(i)
        l=fn.split(" ")
        l1=l[0]
        l2=l[1]
        l3=l[2]
        cur.execute("select * from phonebook where Fname=? and Mname=? and Lname=?",(l1,l2,l3))
        al=cur.fetchall()
        root_se.destroy()
        root_edit=Tk()
        root_edit.title("Edit")
        Label(root_edit,text='First Name').grid(row=1,column=0)
        Label(root_edit,text='Middle Name').grid(row=2,column=0)
        Label(root_edit,text='Last Name').grid(row=3,column=0)
        Label(root_edit,text='Company Name').grid(row=4,column=0)
        Label(root_edit,text='Address').grid(row=5,column=0)
        Label(root_edit,text='City').grid(row=6,column=0)
        Label(root_edit,text='Pin Code').grid(row=7,column=0)
        Label(root_edit,text='Website URL').grid(row=8,column=0)
        Label(root_edit,text='Date of Birth').grid(row=9,column=0)
        Label(root_edit,text='Select Phone Type:',fg='Blue').grid(row=10,column=0)
        Label(root_edit,text='Phone Number').grid(row=11,column=0)
        Label(root_edit,text='Select Email Type:',fg='Blue').grid(row=12,column=0)
        Label(root_edit,text='Email id').grid(row=13,column=0)
        Button(root_edit,text='Save',command=edit_save).grid(row=14,column=0)
        Button(root_edit,text='Close',command=close_e).grid(row=14,column=2)
        e1=Entry(root_edit)
        e1.grid(row=1,column=1)
        e2=Entry(root_edit)
        e2.grid(row=2,column=1)
        e3=Entry(root_edit)
        e3.grid(row=3,column=1)
        e4=Entry(root_edit)
        e4.grid(row=4,column=1)
        e5=Entry(root_edit)
        e5.grid(row=5,column=1)
        e6=Entry(root_edit)
        e6.grid(row=6,column=1)
        e7=Entry(root_edit)
        e7.grid(row=7,column=1)
        e8=Entry(root_edit)
        e8.grid(row=8,column=1)
        e9=Entry(root_edit)
        e9.grid(row=9,column=1)
        e11=Entry(root_edit)
        e11.grid(row=11,column=1)
        e13=Entry(root_edit)
        e13.grid(row=13,column=1)
        v1=IntVar()
        r1=Radiobutton(root_edit,text='Office',variable=v1,value=1)
        r1.grid(row=10,column=1)
        r2=Radiobutton(root_edit,text='Home',variable=v1,value=2)
        r2.grid(row=10,column=2)
        r3=Radiobutton(root_edit,text='Mobile',variable=v1,value=3)
        r3.grid(row=10,column=3)
        v2=IntVar()
        r4=Radiobutton(root_edit,text='Office',variable=v2,value=4)
        r4.grid(row=12,column=1)
        r5=Radiobutton(root_edit,text='Personal',variable=v2,value=5)
        r5.grid(row=12,column=2)
        e1.insert(0,al[0][0])
        e2.insert(0,al[0][1])
        e3.insert(0,al[0][2])
        e4.insert(0,al[0][3])
        e5.insert(0,al[0][4])
        e6.insert(0,al[0][5])
        e7.insert(0,al[0][6])
        e8.insert(0,al[0][7])
        e9.insert(0,al[0][8])
        e11.insert(0,al[0][10])
        e13.insert(0,al[0][12])
    def edit_sname(e=1):
        es=str('%'+e_s.get()+'%')
        lb.delete(0,END)
        cur.execute("select Fname,Mname,Lname from phonebook where Fname like ? or Mname like ? or Lname like ?",(es,es,es))
        pall1=cur.fetchall()
        for i in range(len(pall1)):
                   k1=pall1[i][0]
                   k2=pall1[i][1]
                   k3=pall1[i][2]
                   k=k1+' '+k2+' '+k3
                   lb.insert(END,k)
                   lb.itemconfig(i, {'fg':'blue'})
    Label(root_se,text='Enter Name').grid(row=1,column=0)
    e_s=Entry(root_se)
    e_s.grid(row=1,column=1)
    lb=Listbox(root_se,height=15,width=30,font='20',fg='Blue')
    lb.grid(row=2,column=1)
    cur.execute("select Fname,Mname,Lname from phonebook")
    pall=cur.fetchall()
    for i in range(len(pall)):
                   k1=pall[i][0]
                   k2=pall[i][1]
                   k3=pall[i][2]
                   k=k1+' '+k2+' '+k3+' '
                   lb.insert(END,k)
                   lb.itemconfig(i, {'fg':'blue'})              #self
    lb.bind("<<ListboxSelect>>",edit_show)
    e_s.bind("<KeyRelease>",edit_sname)
    Button(root_se,text='Close',command=close_s).grid(row=3,column=1)
pbimg=PhotoImage(file='phone_image1.gif')
Label(root,image=pbimg).grid(row=0,column=1)
Label(root,text='First Name').grid(row=1,column=0)
Label(root,text='Middle Name').grid(row=2,column=0)
Label(root,text='Last Name').grid(row=3,column=0)
Label(root,text='Company Name').grid(row=4,column=0)
Label(root,text='Address').grid(row=5,column=0)
Label(root,text='City').grid(row=6,column=0)
Label(root,text='Pin Code').grid(row=7,column=0)
Label(root,text='Website URL').grid(row=8,column=0)
Label(root,text='Date of Birth').grid(row=9,column=0)
Label(root,text='Select Phone Type:',fg='Blue').grid(row=10,column=0)
Label(root,text='Phone Number').grid(row=11,column=0)
Label(root,text='Select Email Type:',fg='Blue').grid(row=12,column=0)
Label(root,text='Email id').grid(row=13,column=0)
Button(root,text='Save',command=save).grid(row=14,column=0)
Button(root,text='Search',command=search).grid(row=14,column=1)
Button(root,text='Close',command=close).grid(row=14,column=2)
Button(root,text='Edit',command=edit_search).grid(row=14,column=3)
e1=Entry(root)
e1.grid(row=1,column=1)
e2=Entry(root)
e2.grid(row=2,column=1)
e3=Entry(root)
e3.grid(row=3,column=1)
e4=Entry(root)
e4.grid(row=4,column=1)
e5=Entry(root)
e5.grid(row=5,column=1)
e6=Entry(root)
e6.grid(row=6,column=1)
e7=Entry(root)
e7.grid(row=7,column=1)
e8=Entry(root)
e8.grid(row=8,column=1)
e9=Entry(root)
e9.grid(row=9,column=1)
e11=Entry(root)
e11.grid(row=11,column=1)
e13=Entry(root)
e13.grid(row=13,column=1)
v1=IntVar()
r1=Radiobutton(root,text='Office',variable=v1,value=1)
r1.grid(row=10,column=1)
r2=Radiobutton(root,text='Home',variable=v1,value=2)
r2.grid(row=10,column=2)
r3=Radiobutton(root,text='Mobile',variable=v1,value=3)
r3.grid(row=10,column=3)
v2=IntVar()
r4=Radiobutton(root,text='Office',variable=v2,value=4)
r4.grid(row=12,column=1)
r5=Radiobutton(root,text='Personal',variable=v2,value=5)
r5.grid(row=12,column=2)
mainloop()
