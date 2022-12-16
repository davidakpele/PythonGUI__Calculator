from tkinter import *
from PIL import *

expression = " "

def textInput(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equalPress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)

        expression = " "
    except:
        equation.set("Error: " + expression)
        expression = " "

def clear():
    global expression
    expression = " "
    equation.set(" ")

if __name__ == "__main__":

    window = Tk()
    window.title = ("Calculator Application")
    window.geometry = ("900x670")
    window.resizable(0, 0)
    '''photo = PhotoImage(file = "icon1.png")
    window.iconphoto(False, photo)'''

    equation = StringVar()
    label = Label(text="Calculate anything!", pady=5, fg="black", height=1).grid(row=0, columnspan=3, sticky="NSEW")

numbersTxt = Entry(window, textvariable=equation, bg="lightgray").grid(row=1, column=0, columnspan=4, sticky="NSEW")
oneBtn = Button(window, text="7", command=lambda: textInput(7), width=10, pady=5, height=1).grid(row=2, column=0, sticky="NSEW")
twoBtn = Button(window, text="8", command=lambda: textInput(8), width=10, height=1).grid(row=2, column=1, sticky="NSEW")
threeBtn = Button(window, text="9", command=lambda: textInput(9), width=10, height=1).grid(row=2, column=2, sticky="NSEW")
threBtn = Button(window, text="x", command=lambda: textInput("*"), width=10, height=1).grid(row=2, column=3, sticky="NSEW")

fourBtn = Button(window, text="4", command=lambda: textInput(4), pady=5, width=10, height=1).grid(row=3, column=0, sticky="NSEW")
fiveBtn = Button(window, text="5", command=lambda: textInput(5), width=10, height=1).grid(row=3, column=1, sticky="NSEW")
sixBtn = Button(window, text="6", command=lambda: textInput(6), width=10, height=1).grid(row=3, column=2, sticky="NSEW")
minusBtn = Button(window, text="-", command=lambda: textInput("-"), width=10, height=1).grid(row=3, column=3, sticky="NSEW")

senBtn = Button(window, text="1", command=lambda: textInput(1), width=10, pady=5, height=1).grid(row=4, column=0, sticky="NSEW")
eightBtn = Button(window, text="2", command=lambda: textInput(2), width=10, height=1).grid(row=4, column=1, sticky="NSEW")
nineBtn = Button(window, text="3", command=lambda: textInput(3), width=10, height=1).grid(row=4, column=2, sticky="NSEW")
divideBtn = Button(window, text="/", command=lambda: textInput("/"), width=10, height=1).grid(row=4, column=3, sticky="NSEW")

rBracketBtn = Button(window, text="(", command=lambda: textInput("("), width=10, pady=5, height=1).grid(row=5, column=0, sticky="NSEW")
zeroBtn = Button(window, text="0", command=lambda: textInput(0), width=10, height=1).grid(row=5, column=1, sticky="NSEW")
lBracketBtn = Button(window, text=")", command=lambda: textInput(")"), width=10, height=1).grid(row=5, column=2, sticky="NSEW")
addBtn = Button(window, text="+", command=lambda: textInput("+"), width=10, height=1).grid(row=5, column=3, sticky="NSEW")

clearBtn = Button(window, text="C", command=lambda: clear(), bg="grey", width=10, height=1).grid(row=6, column=0, columnspan=2, sticky="NSEW")
equalBtn = Button(window, text="=", command=lambda: equalPress(), bg="lightblue", width=10, height=1).grid(row=6, column=2, columnspan=3, sticky="NSEW")

window.mainloop()