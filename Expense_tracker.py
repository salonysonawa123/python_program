from tkinter import *
from tkinter import ttk
import sqlite3  as db

from tkcalendar import DateEntry
root = Tk()
root.title("My Notes")
root.geometry("820x800")

def init():
    connectionObjn = db.connect("messageTracker.db")
    curr = connectionObjn.cursor()
    query = '''
    create table if not exists messages (
        date string,
        name string,
        title string,
        message string
        )
    '''
    curr.execute(query)
    connectionObjn.commit()


def submitmessage():
    values = [dateEntry.get(), Name.get(), Title.get(), Message.get()]
    print(values)
    Etable.insert('', 'end', values=values)

    connectionObjn = db.connect("messageTracker.db")
    curr = connectionObjn.cursor()
    query = '''
    INSERT INTO messages VALUES 
    (?, ?, ?, ?)
    '''
    curr.execute(query, (dateEntry.get(), Name.get(), Title.get(), Message.get()))
    connectionObjn.commit()


def viewmessage():
    connectionObjn = db.connect("messageTracker.db")
    curr = connectionObjn.cursor()
    query = '''
     select * from messages
    '''
    total = '''
    select sum(message) from messages
    '''
    curr.execute(query)
    rows = curr.fetchall()
    curr.execute(total)
    amount = curr.fetchall()[0]
    print(rows)
    print(amount)

    l = Label(root, text="Date\t  Name\t  Title\t  Message", font=('arial', 15, 'bold'), bg="DodgerBlue2", fg="white")
    l.grid(row=6, column=0, padx=7, pady=7)

    st = ""
    for i in rows:
        for j in i:
            st += str(j) + '\t'
        st += '\n'
    print(st)
    l = Label(root, text=st, font=('arial', 12))
    l.grid(row=7, column=0, padx=7, pady=7)


init()



dateLabel = Label(root, text="Date", font=('arial', 15, 'bold'), bg="DodgerBlue2", fg="white", width=12)
dateLabel.grid(row=0, column=0, padx=7, pady=7)

dateEntry = DateEntry(root, width=12, font=('arial', 15, 'bold'))
dateEntry.grid(row=0, column=1, padx=7, pady=7)

Name = StringVar()
nameLabel = Label(root, text="Name", font=('arial', 15, 'bold'), bg="DodgerBlue2", fg="white", width=12)
nameLabel.grid(row=1, column=0, padx=7, pady=7)

NameEntry = Entry(root, textvariable=Name, font=('arial', 15, 'bold'))
NameEntry.grid(row=1, column=1, padx=7, pady=7)

Title = StringVar()
titleLabel = Label(root, text="Title", font=('arial', 15, 'bold'), bg="DodgerBlue2", fg="white", width=12)
titleLabel.grid(row=2, column=0, padx=7, pady=7)

titleEntry = Entry(root, textvariable=Title, font=('arial', 15, 'bold'))
titleEntry.grid(row=2, column=1, padx=7, pady=7)

Message = StringVar()
messageLabel = Label(root, text="Message", font=('arial', 15, 'bold'), bg="DodgerBlue2", fg="white", width=12)
messageLabel.grid(row=3, column=0, padx=7, pady=7)

messageEntry = Entry(root, textvariable=Message, font=('arial', 15, 'bold'))
messageEntry.grid(row=3, column=1, padx=7, pady=7)



submitbtn = Button(root, command=submitmessage, text="Submit", font=('arial', 15, 'bold'), bg="DodgerBlue2", fg="white", width=12)
submitbtn.grid(row=4, column=0, padx=13, pady=13)

viewtn = Button(root, command=viewmessage, text="View messages", font=('arial', 15, 'bold'), bg="DodgerBlue2", fg="white", width=12)
viewtn.grid(row=4, column=1, padx=13, pady=13)

# all saved messages--------------

Elist = ['Date', 'Name', 'Title', 'Message']
Etable = ttk.Treeview(root, column=Elist, show='headings', height=7)




for c in Elist:
    Etable.heading(c, text=c.title())

Etable.grid(row=5, column=0, padx=7, pady=7, columnspan=3)






root.mainloop()