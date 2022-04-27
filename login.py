

from tkinter import *
root=Tk() #creating the main window and storing the window object in 'win'
root.title("Login")
def font_style():
   label.config(font=('Helvetica bold', 26))

def close():
    quit()

def closew():
    root.destroy()

def elements():

        root=Tk() #creating the main window and storing the window object in 'win'
        root.title("Future")
        def font_style():
           label.config(font=('Helvetica bold', 26))

        label = Label(root, text="Menu", font=('Times', 24))
        label.place(bordermode=OUTSIDE,x=960,y=100)

        button= Button(root, text="Graphing", padx=960 , pady=200, command=graphing)
        button.place(bordermode=OUTSIDE, height=100, width=300,x=860,y=150)

        button2= Button(root, text="Stock Market Prediction", padx=960 , pady=400, command=smp)
        button2.place(bordermode=OUTSIDE, height=100, width=300,x=860,y=300)

        button3= Button(root, text="Graph Prediciton", padx=960 , pady=600,command=lobf)
        button3.place(bordermode=OUTSIDE, height=100, width=300,x=860,y=450)

        button4= Button(root, text="Settings", padx=960 , pady=400)
        button4.place(bordermode=OUTSIDE, height=100, width=300,x=860,y=600)

        button5= Button(root, text="quit", padx=960 , pady=600, command=close)
        button5.place(bordermode=OUTSIDE, height=100, width=300,x=860,y=750)

        root.configure(bg='grey')
        root.geometry('1920x1080') #setting the size of the window
        root.mainloop() #running the loop that works as a trigge
def smp():
    closew()
    root=Tk() #creating the main window and storing the window object in 'win'
    root.title("Graphing")
    def font_style():
       label.config(font=('Helvetica bold', 26))

    label = Label(root, text="stock market prediction", font=('Times', 24))
    label.place(bordermode=OUTSIDE,x=910,y=100)


    def inputx():
        inputx = Label(root, text=x.get())
        input.place()

    x= Entry(root, width=50)
    x.place(bordermode=OUTSIDE,  width=300,x=860,y=250)

    button= Button(root, text="What stock", padx=960 , pady=200,command=inputx)
    button.place(bordermode=OUTSIDE, height=100, width=300,x=860,y=300)





    def inputy():
        inputx = Label(root, text=y.get())
        input.place()

    y= Entry(root, width=50)
    y.place(bordermode=OUTSIDE,  width=300,x=860,y=450)

    button= Button(root, text="what time lenth?", padx=960 , pady=200,command=inputx)
    button.place(bordermode=OUTSIDE, height=100, width=300,x=860,y=500)


    root.configure(bg='grey')
    root.geometry('1920x1080') #setting the size of the window
    root.mainloop() #running the loop that works as a trigge


def graphing():
    closew()
    root=Tk() #creating the main window and storing the window object in 'win'
    root.title("Graphing")
    def font_style():
       label.config(font=('Helvetica bold', 26))

    label = Label(root, text="Line of best fit", font=('Times', 24))
    label.place(bordermode=OUTSIDE,x=910,y=100)


    def inputx():
        inputx = Label(root, text=x.get())
        input.place()

    x= Entry(root, width=50)
    x.place(bordermode=OUTSIDE,  width=300,x=860,y=250)

    button= Button(root, text="input X values", padx=960 , pady=200,command=inputx)
    button.place(bordermode=OUTSIDE, height=100, width=300,x=860,y=300)





    def inputy():
        inputx = Label(root, text=y.get())
        input.place()

    y= Entry(root, width=50)
    y.place(bordermode=OUTSIDE,  width=300,x=860,y=450)

    button= Button(root, text="input y values", padx=960 , pady=200,command=inputx)
    button.place(bordermode=OUTSIDE, height=100, width=300,x=860,y=500)


    root.configure(bg='grey')
    root.geometry('1920x1080') #setting the size of the window
    root.mainloop() #running the loop that works as a trigge


    def inputx():
        inputx = Label(root, text=x.get())
        input.place()

    x= Entry(root, width=50)
    x.place(bordermode=OUTSIDE,  width=300,x=860,y=250)

    button= Button(root, text="input X values", padx=960 , pady=200,command=inputx)
    button.place(bordermode=OUTSIDE, height=100, width=300,x=860,y=300)

    root.configure(bg='grey')
    root.geometry('1920x1080') #setting the size of the window
    root.mainloop() #running the loop that works as a trigge



    def inputy():
        inputx = Label(root, text=y.get())
        input.place()

    y= Entry(root, width=50)
    y.place(bordermode=OUTSIDE,  width=300,x=860,y=450)

    button= Button(root, text="input y values", padx=960 , pady=200,command=inputx)
    button.place(bordermode=OUTSIDE, height=100, width=300,x=860,y=500)


    root.configure(bg='grey')
    root.geometry('1920x1080') #setting the size of the window
    root.mainloop() #running the loop that works as a trigge


def lobf(): #line of best fit
    closew()
    root=Tk() #creating the main window and storing the window object in 'win'
    root.title("Line of best fit")
    def font_style():
       label.config(font=('Helvetica bold', 26))

    label = Label(root, text="Line of best fit", font=('Times', 24))
    label.place(bordermode=OUTSIDE,x=910,y=100)


    def inputx():
        inputx = Label(root, text=x.get())
        input.place()

    x= Entry(root, width=50)
    x.place(bordermode=OUTSIDE,  width=300,x=860,y=250)

    button= Button(root, text="input X values", padx=960 , pady=200,command=inputx)
    button.place(bordermode=OUTSIDE, height=100, width=300,x=860,y=300)





    def inputy():
        inputx = Label(root, text=y.get())
        input.place()

    y= Entry(root, width=50)
    y.place(bordermode=OUTSIDE,  width=300,x=860,y=450)

    button= Button(root, text="input y values", padx=960 , pady=200,command=inputx)
    button.place(bordermode=OUTSIDE, height=100, width=300,x=860,y=500)


    root.configure(bg='grey')
    root.geometry('1920x1080') #setting the size of the window
    root.mainloop() #running the loop that works as a trigge


def openn(): # open gui.py
    closew()
    root=Tk() #creating the main window and storing the window object in 'win'
    root.title("Menu")
    def font_style():
       label.config(font=('Helvetica bold', 26))

    label = Label(root, text="Menu", font=('Times', 24))
    label.place(bordermode=OUTSIDE,x=960,y=100)
    button= Button(root, text="Load Program", padx=960 , pady=200,command=elements)
    button.place(bordermode=OUTSIDE, height=100, width=300,x=860,y=210)

    button2= Button(root, text="Settings", padx=960 , pady=400)
    button2.place(bordermode=OUTSIDE, height=100, width=300,x=860,y=420)

    button3= Button(root, text="quit", padx=960 , pady=600,command=close)
    button3.place(bordermode=OUTSIDE, height=100, width=300,x=860,y=660)

    root.configure(bg='grey')
    root.geometry('1920x1080') #setting the size of the window
    root.mainloop() #running the loop that works as a trigge




label = Label(root, text="Menu", font=('Times', 24))
label.place(bordermode=OUTSIDE,x=960,y=100)
button= Button(root, text="Login", padx=960 , pady=200, command=openn)
button.place(bordermode=OUTSIDE, height=100, width=300,x=860,y=210,)

button2= Button(root, text="quit", padx=960 , pady=400, command=close)#close program after pressing
button2.place(bordermode=OUTSIDE, height=100, width=300,x=860,y=420)


root.configure(bg='grey')
root.geometry('1920x1080') #setting the size of the window
root.mainloop() #running the loop that works as a trigge
