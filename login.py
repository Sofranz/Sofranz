import webbrowser
import plotly.express as px
from tkinter import *
root=Tk() #creating the main window and storing the window object in 'win'
root.title("Login")
def font_style():
   label.config(font=('Helvetica bold', 26))

def close():
    quit()

def closew():
    root.destroy()

def lobf(): #line of best fit
    root=Tk() #creating the main window and storing the window object in 'win'
    root.title("Graphing")
    def font_style():
       label.config(font=('Helvetica bold', 26))

    label = Label(root, text="Graph Prediction", font=('Times', 24),bg='grey' )
    label.place(bordermode=OUTSIDE,x=910,y=100)




    label = Label(root, text="Y Values",bg='grey' )
    label.place(bordermode=OUTSIDE, height=20, width=300,x=860,y=500)

    label = Label(root, text="X Values",bg='grey' )
    label.place(bordermode=OUTSIDE, height=20, width=300,x=860,y=300)

    x = Entry(root, width=50)
    x.place(bordermode=OUTSIDE, height=20, width=300,x=860,y=320)

    y = Entry(root, width=50)
    y.place(bordermode=OUTSIDE, height=20, width=300,x=860,y=520)

    def inputy():
        inputyy = Label(root, text=x.get())
        inputyy.place()
        yval=y.get()

        inputxx = Label(root, text=x.get())
        inputxx.place()
        xval=x.get()

        myArray = xval.split(",")


        myArrayy = yval.split(",")

        fig = px.scatter(x=myArray, y=myArrayy)
        fig.show()

    Button1 = Button( root,text="Input",command=inputy,bg="grey")
    Button1.place(bordermode=OUTSIDE, height=100, width=300,x=860,y=620)

    button5= Button(root, text="quit", padx=960 , pady=600, command=close, bg='grey')
    button5.place(bordermode=OUTSIDE, height=100, width=300,x=860,y=750)


    root.configure(bg='grey')
    root.geometry('1920x1080') #setting the size of the window
    root.mainloop() #running the loop that works as a trigge






def smp():

    root=Tk() #creating the main window and storing the window object in 'win'
    root.title("Graphing")
    def font_style():
       label.config(font=('Helvetica bold', 26))

    label = Label(root, text="Stock Prediction", font=('Times', 24),bg='grey' )
    label.place(bordermode=OUTSIDE,x=910,y=100)





    label = Label(root, text="Which Stock",bg='grey' )
    label.place(bordermode=OUTSIDE, height=20, width=300,x=860,y=300)

    x = Entry(root, width=50)
    x.place(bordermode=OUTSIDE, height=20, width=300,x=860,y=320)


    def inputy():

        inputxx = Label(root, text=x.get())
        inputxx.place()
        xval=x.get()
        webbrowser.open("https://www.tipranks.com/stocks/"+xval+"/forecast", new=1, autoraise=True)

    Button1 = Button( root,text="Input",command=inputy,bg="grey")
    Button1.place(bordermode=OUTSIDE, height=100, width=300,x=860,y=620)



    button5= Button(root, text="quit", padx=960 , pady=600, command=close, bg='grey')
    button5.place(bordermode=OUTSIDE, height=100, width=300,x=860,y=750)
    root.configure(bg='grey')
    root.geometry('1920x1080') #setting the size of the window
    root.mainloop() #running the loop that works as a trigge




def graphing():
    root=Tk() #creating the main window and storing the window object in 'win'
    root.title("Graphing")
    def font_style():
       label.config(font=('Helvetica bold', 26))

    label = Label(root, text="Graphing", font=('Times', 24),bg='grey' )
    label.place(bordermode=OUTSIDE,x=910,y=100)

    label = Label(root, text="Y Values",bg='grey' )
    label.place(bordermode=OUTSIDE, height=20, width=300,x=860,y=500)

    label = Label(root, text="X Values",bg='grey' )
    label.place(bordermode=OUTSIDE, height=20, width=300,x=860,y=300)

    x = Entry(root, width=50)
    x.place(bordermode=OUTSIDE, height=20, width=300,x=860,y=320)

    y = Entry(root, width=50)
    y.place(bordermode=OUTSIDE, height=20, width=300,x=860,y=520)

    def inputy():
        inputyy = Label(root, text=x.get())
        inputyy.place()
        yval=y.get()

        inputxx = Label(root, text=x.get())
        inputxx.place()
        xval=x.get()

        myArray = xval.split(",")


        myArrayy = yval.split(",")

        fig = px.scatter(x=myArray, y=myArrayy)
        fig.show()

    Button1 = Button( root,text="Input",command=inputy,bg="grey")
    Button1.place(bordermode=OUTSIDE, height=100, width=300,x=860,y=620)



    button5= Button(root, text="quit", padx=960 , pady=600, command=close, bg='grey')
    button5.place(bordermode=OUTSIDE, height=100, width=300,x=860,y=750)

    button6= Button(root, text="Go Back", padx=960 , pady=600,command=elements,bg='grey')
    button6.place(bordermode=OUTSIDE, height=100, width=300,x=0,y=900)


    root.configure(bg='grey')
    root.geometry('1920x1080') #setting the size of the window
    root.mainloop() #running the loop that works as a trigge


def openn(): # open gui.py
    root=Tk() #creating the main window and storing the window object in 'win'
    root.title("Menu")
    def font_style():
       label.config(font=('Helvetica bold', 26))

    label = Label(root, text="Menu", font=('Times', 24),bg='grey')
    label.place(bordermode=OUTSIDE,x=960,y=100)
    button= Button(root, text="Load Program", padx=960 , pady=200,command=elements,bg='grey')
    button.place(bordermode=OUTSIDE, height=100, width=300,x=860,y=210)

    button2= Button(root, text="Settings", padx=960 , pady=400,bg='grey')
    button2.place()

    button3= Button(root, text="quit", padx=960 , pady=600,command=close,bg='grey')
    button3.place(bordermode=OUTSIDE, height=100, width=300,x=860,y=660)

    root.configure(bg='grey')
    root.geometry('1920x1080') #setting the size of the window
    root.mainloop() #running the loop that works as a trigge


def login():
        root=Tk() #creating the main window and storing the window object in 'win'
        root.title("Graphing")
        def font_style():
           label.config(font=('Helvetica bold', 26))

        label = Label(root, text="Login", font=('Times', 24),bg='grey' )
        label.place(bordermode=OUTSIDE,x=910,y=100)

        def inputx():
            inputx = Label(root, text=x.get())
            input.place()

        x= Entry(root, width=50)
        x.place(bordermode=OUTSIDE,  width=300,x=860,y=250)

        button= Button(root, text="Username", padx=960 , pady=200,command=inputx , bg='grey')
        button.place(bordermode=OUTSIDE, height=100, width=300,x=860,y=300)

        def inputy():
            inputx = Label(root, text=y.get())
            input.place()

        y= Entry(root, width=50)
        y.place(bordermode=OUTSIDE,  width=300,x=860,y=450)

        button= Button(root, text="Password", padx=960 , pady=200,command=inputx , bg='grey')
        button.place(bordermode=OUTSIDE, height=100, width=300,x=860,y=500 , )

        button5= Button(root, text="quit", padx=960 , pady=600, command=close, bg='grey')
        button5.place(bordermode=OUTSIDE, height=100, width=300,x=860,y=750)

        root.configure(bg='grey')
        root.geometry('1920x1080') #setting the size of the window
        root.mainloop() #running the loop that works as a trigge


label = Label(root, text="Menu", font=('Times', 24),bg='grey')
label.place(bordermode=OUTSIDE,x=960,y=100)
button= Button(root, text="Login", padx=960 , pady=200, command=openn,bg='grey')
button.place(bordermode=OUTSIDE, height=100, width=300,x=860,y=210,)

button2= Button(root, text="quit", padx=960 , pady=400, command=close,bg='grey')#close program after pressing
button2.place(bordermode=OUTSIDE, height=100, width=300,x=860,y=420)

def elements():

        root=Tk() #creating the main window and storing the window object in 'win'
        root.title("Future")
        def font_style():
           label.config(font=('Helvetica bold', 26))

        label = Label(root, text="Menu", font=('Times', 24),bg='grey')
        label.place(bordermode=OUTSIDE,x=960,y=100)

        button= Button(root, text="Graphing", padx=960 , pady=200, command=graphing,bg='grey')
        button.place(bordermode=OUTSIDE, height=100, width=300,x=860,y=150)

        button2= Button(root, text="Stock Market Prediction", padx=960 , pady=400, command=smp,bg='grey')
        button2.place(bordermode=OUTSIDE, height=100, width=300,x=860,y=300)

        button3= Button(root, text="Graph Prediciton", padx=960 , pady=600,command=lobf,bg='grey')
        button3.place(bordermode=OUTSIDE, height=100, width=300,x=860,y=450)

        button4= Button(root, text="Settings", padx=960 , pady=400,bg='grey')
        button4.place(bordermode=OUTSIDE, height=100, width=300,x=860,y=600)

        button5= Button(root, text="quit", padx=960 , pady=600, command=close,bg='grey')
        button5.place(bordermode=OUTSIDE, height=100, width=300,x=860,y=750)

        root.configure(bg='grey')
        root.geometry('1920x1080') #setting the size of the window
        root.mainloop() #running the loop that works as a trigge

root.configure(bg='grey')
root.geometry('1920x1080') #setting the size of the window
root.mainloop() #running the loop that works as a trigge
