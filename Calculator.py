from tkinter import *
from tkinter import messagebox

root = Tk()                
root.geometry("312x329")  
root.resizable(0, 0)      
root.title("calculator")

#functions
def click(item):                                   
    global expression
    inputs.set(inputs.get()+(str(item)))

def backspace():                                 
    global expression
    if inputs.get()=="_ERROR_":
        clear()
    inputs.set(inputs.get()[0:-1])

def clear():                                          
    inputs.set("")

def equal():
    result = ""
    try:
        result = eval(inputs.get())                            
        inputs.set(result)
    except:
        result = "_ERROR_"
        inputs.set(result)

inputs = StringVar()                     

#Input Frame
inputFrame = Frame(root, width=280, height=100, bd=0, highlightbackground="grey50", highlightthickness=2)
inputFrame.pack(side=TOP)
inputField = Entry(inputFrame,  textvariable=inputs, width=100,fg="white", bg="black", borderwidth=2, relief="solid", bd=0, justify=RIGHT)
inputField.grid(row=0, column=0)
inputField.pack(ipady=19)

#Button Frame
button_frame = Frame(root, width=300, height=272.5, bg="black")
button_frame.pack()

#Buttons
clear_all = Button(button_frame, text = "C", fg = "white", width = 10, height = 3, bd = 0, bg = "grey50", cursor = "hand2", command = lambda: clear()).grid(row = 1, column = 0, padx = 1, pady = 1)
left_bracket= Button(button_frame, text = "(", fg = "white", width = 10, height = 3, bd = 0, bg = "grey50", cursor = "hand2", command = lambda: click("(")).grid(row = 1, column = 1, padx = 1, pady = 1)
right_bracket = Button(button_frame, text = ")", fg = "white", width = 10, height = 3, bd = 0, bg = "grey50", cursor = "hand2", command = lambda: click(")")).grid(row = 1, column = 2, padx = 1, pady = 1)
back = Button(button_frame, text = "Del", fg = "white", width = 10, height = 3, bd = 0, bg = "grey50", cursor = "hand2", command = lambda: backspace()).grid(row = 1, column = 3, padx = 1, pady = 1)

seven = Button(button_frame, text = "7", fg = "white", width = 10, height = 3, bd = 0, bg = "grey25", cursor = "hand2", command = lambda: click(7)).grid(row = 2, column = 0, padx = 1, pady = 1)
eight = Button(button_frame, text = "8", fg = "white", width = 10, height = 3, bd = 0, bg = "grey25", cursor = "hand2", command = lambda: click(8)).grid(row = 2, column = 1, padx = 1, pady = 1)
nine = Button(button_frame, text = "9", fg = "white", width = 10, height = 3, bd = 0, bg = "grey25", cursor = "hand2", command = lambda: click(9)).grid(row = 2, column = 2, padx = 1, pady = 1)
divide = Button(button_frame, text = "/",  fg = "white", width = 10, height = 3, bd = 0, bg = "grey50", cursor = "hand2", command = lambda: click("/")).grid(row = 2, column = 3, padx = 1, pady = 1)

four = Button(button_frame, text = "4",  fg = "white", width = 10, height = 3, bd = 0, bg = "grey25", cursor = "hand2", command = lambda: click(4)).grid(row = 3, column = 0, padx = 1, pady = 1)
five = Button(button_frame, text = "5",  fg = "white", width = 10, height = 3, bd = 0, bg = "grey25", cursor = "hand2", command = lambda: click(5)).grid(row = 3, column = 1, padx = 1, pady = 1)
six = Button(button_frame, text = "6",  fg = "white", width = 10, height = 3, bd = 0, bg = "grey25", cursor = "hand2", command = lambda: click(6)).grid(row = 3, column = 2, padx = 1, pady = 1)
multiply = Button(button_frame, text = "*", fg = "white", width = 10, height = 3, bd = 0, bg = "grey50", cursor = "hand2", command = lambda: click("*")).grid(row = 3, column = 3, padx = 1, pady = 1)

one = Button(button_frame, text = "1", fg = "white", width = 10, height = 3, bd = 0, bg = "grey25", cursor = "hand2", command = lambda: click(1)).grid(row = 4, column = 0, padx = 1, pady = 1)
two = Button(button_frame, text = "2", fg = "white", width = 10, height = 3, bd = 0, bg = "grey25", cursor = "hand2", command = lambda: click(2)).grid(row = 4, column = 1, padx = 1, pady = 1)
three = Button(button_frame, text = "3", fg = "white", width = 10, height = 3, bd = 0, bg = "grey25", cursor = "hand2", command = lambda: click(3)).grid(row = 4, column = 2, padx = 1, pady = 1)
minus = Button(button_frame, text = "-", fg = "white", width = 10, height = 3, bd = 0, bg = "grey50", cursor = "hand2", command = lambda: click("-")).grid(row = 4, column = 3, padx = 1, pady = 1)

zero = Button(button_frame, text = "0", fg = "white", width = 10, height = 3, bd = 0, bg = "grey25", cursor = "hand2", command = lambda: click(0)).grid(row = 5, column = 0, padx = 1, pady = 1)
point = Button(button_frame, text = ".", fg = "white", width = 10, height = 3, bd = 0, bg = "grey25", cursor = "hand2", command = lambda: click(".")).grid(row = 5, column = 1, padx = 1, pady = 1)
equals = Button(button_frame, text = "=",  fg = "black", width = 10, height = 3, bd = 0, bg = "steelblue1", cursor = "hand2", command = lambda: equal()).grid(row = 5, column = 2, padx = 1, pady = 1)
plus = Button(button_frame, text = "+",  fg = "white", width = 10, height = 3, bd = 0, bg = "grey50", cursor = "hand2", command = lambda: click("+")).grid(row = 5, column = 3, padx = 1, pady = 1)

root.bind("<Return>", lambda e: equal())
root.mainloop()               
