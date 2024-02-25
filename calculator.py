from tkinter import *

##inputText is what goes into the calculator. As user inputs data this updates. 
inputText = ""

#Adds to inputText string
def addToCalculation(symbol):
    pass

#converts string to calculation and does the math. Algebraic!
#shows error if math is not mathing
def evalCalc(inputText):
    pass

#When you hit the CA (Clear All) button it clears the calculator 
def clearField():
    pass

#has a clear/delete button to delete one space
def deleteButton():
    pass



#GUI through Tkinter
root = Tk()
root.geometry("1000x1000")
root.title("Calculator")

#Creating grid of number buttons (sans 0)
rowIndex = 0
columnIndex = 0
for i in range(1, 10):
    if columnIndex > 2:
        columnIndex = 0
        rowIndex += 1
    button = Button(root, text=i)
    button.grid(row=rowIndex, column=columnIndex)
    columnIndex+=1

#creating special buttons AND 0 number
special = ["(", "0", ")", "C", "CA", "="]
for i in special:
    if columnIndex > 2:
        columnIndex = 0
        rowIndex += 1

    specialButton = Button(root, text=i)
    specialButton.grid(row = rowIndex, column=columnIndex)
    columnIndex+=1

root.mainloop()