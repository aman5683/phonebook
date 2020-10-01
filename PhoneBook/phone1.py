from Tkinter import *
root1=Tk()
root1.geometry("701x501")
def phone(a=1):
    root1.destroy()
Label(root1,text='Project Title : PhoneBook',fg='Black',font='bold 16').grid(row=0,column=0)
Label(root1,text='Project of Python and database',fg='Black',font='bold 16').grid(row=1,column=0)
Label(root1,text='Developed By: Aman Ghatiya[181B027]',fg='Blue',font='bold 16').grid(row=2,column=0)
Label(root1,text='Hover the mouseover the screen.',fg='Red',font='bold 16').grid(row=3,column=0)
root1.bind("<Motion>",phone)  #Motion
mainloop()
