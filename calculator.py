from tkinter import Button, Entry, Label, Tk, StringVar



gui = Tk()

gui.title('My Simple Calculator')

gui.geometry('390x120')

gui.configure(bg='light green')

gui.resizable(width=False, height=False)



expression = ''





def clicked(num):

    global expression
    if num != 'del':
        expression += str(num)
        
        equation.set(expression)
    else:
        expression = expression[0:-1]
        
        equation.set(expression)

def evaluate():

    try:

        global expression

        expression = str(eval(expression))

        equation.set(expression)

    except:



        expression = ''

        equation.set(' Error ')





def clear():

    global expression

    expression = ''

    equation.set('')





equation = StringVar()

equation.set('Enter your equation here:')



screen = Entry(gui, textvariable=equation, fg='black')

screen.grid(columnspan=5, ipadx=100)

programmer = Label(gui, text='By: Marcus', bg='light green', fg='black')
programmer.grid(row=4,column=4)

clearbtn = Button(gui, text='Clear', command=clear,

                  width=7, height=1, fg='black')

clearbtn.grid(row=4, column=2)

btn1 = Button(gui, text='  1  ', command=lambda: clicked(1),

              width=7, height=1, fg='black')

btn1.grid(row=1, column=0)

btn2 = Button(gui, text='  2  ', command=lambda: clicked(2),

              width=7, height=1, fg='black')

btn2.grid(row=1, column=1)

btn3 = Button(gui, text='  3  ', command=lambda: clicked(3),

              width=7, height=1, fg='black')

btn3.grid(row=1, column=2)

btn4 = Button(gui, text='  4  ', command=lambda: clicked(4),

              width=7, height=1, fg='black')

btn4.grid(row=2, column=0)

btn5 = Button(gui, text='  5  ', command=lambda: clicked(5),

              width=7, height=1, fg='black')

btn5.grid(row=2, column=1)

btn6 = Button(gui, text='  6  ', command=lambda: clicked(6),

              width=7, height=1, fg='black')

btn6.grid(row=2, column=2)

btn7 = Button(gui, text='  7  ', command=lambda: clicked(7),

              width=7, height=1, fg='black')

btn7.grid(row=3, column=0)

btn8 = Button(gui, text='  8  ', command=lambda: clicked(8),

              width=7, height=1, fg='black')

btn8.grid(row=3, column=1)

btn9 = Button(gui, text='  9  ', command=lambda: clicked(9),

              width=7, height=1, fg='black')

btn9.grid(row=3, column=2)

btn0 = Button(gui, text='  0  ', command=lambda: clicked(0),

              width=7, height=1, fg='black')

btn0.grid(row=4, column=0)

equalsbtn = Button(gui, text='  =  ', command=evaluate,

                   width=7, height=1, fg='black')

equalsbtn.grid(row=4, column=1)

addbtn = Button(gui, text='  +  ', command=lambda: clicked('+'),

                width=7, height=1, fg='black')

addbtn.grid(row=1, column=3)

subtractbtn = Button(gui, text='  -  ', command=lambda: clicked('-'),

                     width=7, height=1, fg='black')

subtractbtn.grid(row=2, column=3)

multiplybtn = Button(gui, text='  *  ', command=lambda: clicked('*'),

                     width=7, height=1, fg='black')

multiplybtn.grid(row=3, column=3)

dividebtn = Button(gui, text='  /  ', command=lambda: clicked('/'),

                   width=7, height=1, fg='black')

dividebtn.grid(row=4, column=3)
# del button and a point (.) button and exponents

delbtn = Button(gui, text = ' Del ', command=lambda: clicked('del'),
                width=7, height=1, fg='black')
delbtn.grid(row=1, column=4)
decimalbtn = Button(gui, text =  ' . ', command=lambda: clicked('.'),
                    width=7, height=1, fg='black')
decimalbtn.grid(row=2, column=4)
expbtn = Button(gui, text = ' ** ', command=lambda: clicked('**'),
                width=7, height=1, fg='black' )
expbtn.grid(row=3, column=4)

gui.mainloop()
