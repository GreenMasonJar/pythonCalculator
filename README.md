# pythonCalculator

Welcome to my calculator! This is my first project using python and a gui. 

For the GUI I used Tkinter, and primarily used the button and Entry widgets.

To begin, the program starts with an empty string named "inputText"

Each button calls a function. Number and symbol buttons call the "addToCalculation" function, which adds that symbol to the inputText string, and updates the Entry display. 

Equals calls the evalCalc function. This evaluates the string, which basically does the math, and converts it to a string and displays the answer. It also converts inputText to the answer, unless it's an errorin which case it resets inputText to an empty string. For simplicity's sake I used try/excet to catch any errors (ex: when you divide by zero). If the evaluation fails, it displays "ERROR"

CA deletes the Entry text and convert inputText back into an empty string

C removes the last symbol/character in inputText and updates the Entry.

And that's it! Hope you enjoy this simple calculator, I had a lot of fun creating it. Cheers!
