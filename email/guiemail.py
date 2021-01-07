from tkinter import *
from tkinter import messagebox
import tkinter.font as Font
import tkinter.messagebox

# ****** Global Variables ******

objects = []
window = Tk()
window.withdraw()
window.title("User Information")


class popupWindow(object):

    loop = False
    attempts = 0

    def __init__(self, master):
        top = self.top = Toplevel(master)
        top.title('Input Password')
        top.geometry('{}x{}'.format(250, 100))
        top.resizable(width = False, height = False)
        self.lbl = Label(top, text = 'Password: ', font = ('Courier', 14), justify = CENTER)
        self.lbl.pack()
        self.entry = Entry(top, show = '*', width = 30)
        self.entry.pack()
        self.btn = Button(top, text = 'Submit', command = self.cleanup, font = ('Courier', 14))
        self.btn.pack()

    def cleanup(self):
        self.value = self.entry.get()
        access = 'Marcus'

        if self.value == access:
            self.loop = True
            self.top.destroy()
            window.deiconify()
        else:
            self.attempts += 1
            if self.attempts == 5:
                window.quit()
                exit()
            self.entry.delete(0, 'end')
            messagebox.showerror('Incorrect Password', 'Incorrect password, attempts remaining: ' + str(5 - self.attempts))

class entity_add:

    def __init__(self, master, n, p, e):
        self.password = p
        self.name = n
        self.email = e
        self.window = master
        
    def write(self):
        f = open('emails.txt', 'a')
        n = self.name
        e = self.email
        p = self.password

        encryptedN = ""
        encryptedE = ""
        encryptedP = ""
        for letter in n:
            if letter == ' ':
                encryptedN += ' '
            else:
                encryptedN += chr(ord(letter) + 5)

        for letter in e:
            if letter == ' ':
                encryptedE += ' '
            else:
                encryptedE += chr(ord(letter) + 5)

        for letter in p:
            if letter == ' ':
                encryptedP += ' '
            else:
                encryptedP += chr(ord(letter) + 5)

        f.write(encryptedN + ',' + encryptedE + ',' + encryptedP + ', \n')
        f.close()

class entity_display:
    def __init__(self, master, n, e , p, i):
        self.password = p
        self.name = n
        self.email = e
        self.window = master
        self.i = i

        decryptedN = ''
        decryptedE = ''
        decryptedP = ''
        for letter in self.name:
            if letter == ' ':
                decryptedN += ' '
            else:
                decryptedN += chr(ord(letter) - 5)
                
        for letter in self.email:
            if letter == ' ':
                decryptedE += ' '
            else:
                decryptedE += chr(ord(letter) - 5)

        for letter in self.password:
            if letter == ' ':
                decryptedP += ' '
            else:
                decryptedP += chr(ord(letter) - 5)

        self.lbl_name = Label(self.window, text = decryptedN, font = ('Courier', 14))
        self.lbl_email = Label(self.window, text = decryptedE, font = ('Courier', 14))
        self.lbl_password = Label(self.window, text = decryptedP, font = ('Courier', 14))
        self.delbtn = Button(self.window, text = 'X', fg = 'red', command = self.delete)

    def display(self):
        self.lbl_name.grid(row = 6 + self.i, sticky = W)
        self.lbl_email.grid(row = 6 + self.i, column = 1)
        self.lbl_password.grid(row = 6 + self.i, column = 2, sticky = E)
        self.delbtn.grid(row = 6 + self.i, column = 3, sticky = E)

    def delete(self):
        answer = tkinter.messagebox.askquestion('Delete', 'Are you sure you want to delete this entry?')

        if answer == 'yes':
            for i in objects:
                i.destroy()

            f = open('emails.txt', 'r')
            lines = f.readlines()
            f.close()

            f = open('emails.txt', 'w')
            count = 0

            for line in lines:
                if count != self.i:
                    f.write(line)
                    count += 1

            f.close()
            readfile()

    def destroy(self):
        self.lbl_name.destroy()
        self.lbl_email.destroy()
        self.lbl_password.destroy()
        self.delbtn.destroy()

# ****** Functions ******

def onsubmit():
    m = email.get()
    p = password.get()
    n = name.get()
    e = entity_add(window, n, p, m)
    e.write()
    name.delete(0, 'end')
    email.delete(0, 'end')
    password.delete(0, 'end')
    messagebox.showinfo('Added Entity', 'Successfully Added, \n' + 'Name: ' + n + '\nEmail: '+ m + '\nPassword: ' + p)
    readfile()

def clearfile():
    f = open('emails.txt', 'w')
    f.close()

def readfile():
    f = open('emails.txt', 'r')
    count = 0

    for line in f:
        entityList = line.split(',')
        e = entity_display(window, entityList[0], entityList[1], entityList[2], count)
        objects.append(e)
        e.display()
        count += 1
        
# ****** Graphics ******

m = popupWindow(window)

entity_lbl = Label(window, text = 'Add Entity', font = ('Courier', 18))
name_lbl = Label(window, text = 'Name: ', font = ('Courier', 14))
email_lbl = Label(window, text = 'Email: ', font = ('Courier', 14))
password_lbl = Label(window, text = 'Password: ', font = ('Courier', 14))
name = Entry(window, font = ('Courier', 14))
email = Entry(window, font = ('Courier', 14))
password = Entry(window, show = '*', font = ('Courier', 14))
submit = Button(window, text = 'Add Email', command = onsubmit, font = ('Courier', 14))

entity_lbl.grid(columnspan = 3, row = 0)
name_lbl.grid(row = 1, sticky = E, padx = 3)
email_lbl.grid(row = 2, sticky = E, padx = 3)
password_lbl.grid(row = 3, sticky = E, padx = 3)

name.grid(columnspan = 3, row = 1, column = 1, padx = 2, pady = 2, sticky = W)
email.grid(columnspan = 3, row = 2, column = 1, padx = 2, pady = 2, sticky = W)
password.grid(columnspan = 3, row = 3, column = 1, padx = 2, pady = 2, sticky = W)

submit.grid(columnspan = 3, pady = 4)

name_lbl2 = Label(window, text = 'Name: ', font = ('Courier', 14))
email_lbl2 = Label(window, text = 'Email: ', font = ('Courier', 14))
password_lbl2 = Label(window, text = 'Password: ', font = ('Courier', 14))

name_lbl2.grid(row = 5)
email_lbl2.grid(row = 5, column = 1)
password_lbl2.grid(row = 5, column = 2)

readfile()

window.mainloop()
