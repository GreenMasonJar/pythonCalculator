from tkinter import *

##inputText is what goes into the calculator. As user inputs data this updates. 
inputText = ""

#Adds to inputText string
def addToCalculation(symbol):
    global inputText
    inputText += symbol
    
    e.delete(0, END)
    e.insert(0, inputText)

#converts string to calculation and does the math. Algebraic!
#shows error if math is not mathing
def evalCalc():
    try:
        global inputText 
        inputText = str(eval(inputText))
        
        e.delete(0,END)
        e.insert(0, inputText)

    except:
        e.delete(0, END)
        e.insert(0, "ERROR")

#When you hit the CA (Clear All) button it clears the calculator 
def clearField():
    global inputText
    inputText = ""
    e.delete(0, END)

#has a clear/delete button to delete one space
def deleteButton():
    global inputText
    inputText = inputText[: -1]

    e.delete(0,END)
    e.insert(0, inputText)





#GUI through Tkinter
root = Tk()
root.geometry("500x500")
root.title("Calculator")

e = Entry(root)
e.grid(row = 0, column = 0, columnspan = 3)

#Creating buttons
button1 = Button(root, text="1", command=lambda: addToCalculation("1"))
button2 = Button(root, text="2", command=lambda: addToCalculation("2"))
button3 = Button(root, text="3", command=lambda: addToCalculation("3"))
button4 = Button(root, text="4", command=lambda: addToCalculation("4"))
button5 = Button(root, text="5", command=lambda: addToCalculation("5"))
button6 = Button(root, text="6", command=lambda: addToCalculation("6"))
button7 = Button(root, text="7", command=lambda: addToCalculation("7"))
button8 = Button(root, text="8", command=lambda: addToCalculation("8"))
button9 = Button(root, text="9", command=lambda: addToCalculation("9"))
button0 = Button(root, text="0", command=lambda: addToCalculation("0"))
buttonStarPer = Button(root, text="(", command=lambda: addToCalculation("("))
buttonEndPer = Button(root, text=")", command=lambda: addToCalculation(")"))
buttonPlus = Button(root, text="+", command=lambda: addToCalculation("+"))
buttonMinus = Button(root, text="-", command=lambda: addToCalculation("-"))
buttonMult = Button(root, text="*", command=lambda: addToCalculation("*"))
buttonDiv = Button(root, text="/", command=lambda: addToCalculation("/"))

buttonCA = Button(root, text="CA", command=clearField)
buttonC = Button(root, text="C", command=deleteButton)
buttonEqual = Button(root, text="=", command=evalCalc)

#Organizing the buttons into a grid
button1.grid(row = 1, column = 0)
button2.grid(row = 1, column = 1)
button3.grid(row = 1, column = 2)
button4.grid(row = 2, column = 0)
button5.grid(row = 2, column = 1)
button6.grid(row = 2, column = 2)
button7.grid(row = 3, column = 0)
button8.grid(row = 3, column = 1)
button9.grid(row = 3, column = 2)
button0.grid(row = 4, column = 1)
buttonStarPer.grid(row = 4, column = 0)
buttonEndPer.grid(row = 4, column = 2)
buttonCA.grid(row = 5, column = 0)
buttonC.grid(row = 5, column = 1)
buttonEqual.grid(row = 5, column = 2) 
buttonPlus.grid(row = 1, column = 3)
buttonMinus.grid(row = 2, column = 3)
buttonMult.grid(row = 3, column = 3)
buttonDiv.grid(row = 4, column = 3)

root.mainloop()