#sp.plot






#Import PySimpleGUI
import PySimpleGUI as sg
import tkinter as tk
from tkinter import *
import sympy as sp
from sympy import *
#Draw the button
# layout = [[sg.Button('Hello, New Stack', size=(30,4))]]
 
# #Draw the window
# window = sg.Window('GUI SAMPLE', layout, size=(200,100))
 
# #Define what happens when the button is clicked
# event, values = window.read()



# Import tkinter and simpledialog
from tkinter import simpledialog
dvalue = 1
# Syntax form
window = tk.Toplevel()
# to rename the title of the window
window.title("GUI")
# pack is used to show the object in the window
label = tk.Label(window, text = " Use ** for exponents.  ").pack()
label = tk.Label(window, text = "  Use 'pi' to access the constant π. ").pack()
label = tk.Label(window, text = "Use 'E' (case sensitive) to access the natural number e. ").pack()
label = tk.Label(window, text = "  Use 'oo' to indicate infinity. ").pack()
label = tk.Label(window, text = "  Square root function ---> sqrt(x) ").pack()
label = tk.Label(window, text = " Nth root function ---> root(x,n)").pack()
label = tk.Label(window, text = "Welcome to the calculus calculator!\n", font= 100).pack()
label = tk.Label(window, text = "Please adhere to this syntax when entering functions: ", font= 150).pack()
label = tk.Label(window, text = "sin(x) ---> sin(x)").pack()
label = tk.Label(window, text = "cos(x) ---> cos(x)").pack()
label = tk.Label(window, text = "tan(x) ---> tan(x)").pack()
label = tk.Label(window, text = "sinh(x) ---> sinh(x)").pack()
label = tk.Label(window, text = "cosh(x) ---> cosh(x)").pack()
label = tk.Label(window, text = "tanh(x) ---> tanh(x)").pack()
label = tk.Label(window, text = "arcsinh(x) ---> arcsinh(x)").pack()
label = tk.Label(window, text = "arccosh(x) ---> arccosh(x)").pack()
label = tk.Label(window, text = "arctanh(x) ---> arctanh(x)").pack()
label = tk.Label(window, text = "ln(x) ---> log(x)").pack()
label = tk.Label(window, text = "log(x) (base 10) ---> log10(x)").pack()
label = tk.Label(window, text = "e^x --> exp(x)").pack()
label = tk.Label(window, text = "|x| ---> abs(x)").pack()
label = tk.Label(window, text = " csc(x) ---> csc(x)  ").pack()
label = tk.Label(window, text = " sec(x) ---> sec(x)  ").pack()
label = tk.Label(window, text = " cot(x) ---> cot(x)  ").pack()
label = tk.Label(window, text = "  sin inverse ---> asin(x) ").pack()
label = tk.Label(window, text = "  cos inverse ---> acos(x) ").pack()
label = tk.Label(window, text = "  tan inverse ---> atan(x) ").pack()
label = tk.Label(window, text = " csc inverse ---> acsc(x)  ").pack()
label = tk.Label(window, text = " sec inverse ---> asec(x)  ").pack()
label = tk.Label(window, text = " cotan inverse ---> acot(x)  ").pack()
label = tk.Label(window, text = " csch(x) ---> csch(x)  ").pack()
label = tk.Label(window, text = "  sech(x) ---> sech(x) ").pack()
label = tk.Label(window, text = " coth inverse ---> acoth(x)  ").pack()
label = tk.Label(window, text = "  log(x) ---> log(x, base) ").pack()




#Asking for either antiderivative, derivative, or just graph of the function
# Create an instance of tkinter frame or window
win = tk.Toplevel()

# Set the size of the window
win.geometry("700x350")

# Define a function to get the output for selected option
def selection():
   selected = "You selected the option " + str(radio.get())
   label.config(text=selected)



radio = IntVar()
Label(text="Do you want to work with the derivative, antiderivative, or normal function:", font=('Aerial 11')).pack()
# Define radiobutton for each options
r1 = Radiobutton(win, text="Derivative", variable=radio, value=1, command=selection)

r1.pack(anchor=tk.N)
r2 = Radiobutton(win, text="AntiDerivative", variable=radio, value=2, command=selection)

r2.pack(anchor=tk.N)
r3 = Radiobutton(win, text="Normal", variable=radio, value=3, command=selection)

r3.pack(anchor=tk.N)


# Define a label widget
label = Label(win)
label.pack()

win.mainloop()

#Same thing but for definte/graph


# Create an instance of tkinter frame or window
win2 = tk.Toplevel()

# Set the size of the window
win2.geometry("700x350")

# Define a function to get the output for selected option
def selection2():
   selected = "You selected the option " + str(radio2.get())
   label2.config(text=selected)



radio2 = IntVar()

# Define radiobutton for each options
r4 = Radiobutton(win2, text="Graph", variable=radio2, value=4, command=selection2)

r4.pack(anchor=tk.N)
r5 = Radiobutton(win2, text="Definite", variable=radio2, value=5, command=selection2)

r5.pack(anchor=tk.N)

# Define a label widget
label2 = Label(win2)
label2.pack()

win2.mainloop()




# Define the root window
windows = tk.Tk()
windows.title("GUI")
# Define input dialog
 
#Option 2
selectedOption = radio.get()
selectedOption2 = radio2.get()

# Define the input dialog
USER_INP = simpledialog.askstring(title="Input Test",
                                  prompt="Type your funtion:")

if (selectedOption2 == 5 and selectedOption ==1):
# For Definite Derivative
    USER_INPDER = simpledialog.askstring(title="Input Test",
                                    prompt="Input Derivative X value:")
    processed_inputDER = sp.sympify(USER_INPDER)
if (selectedOption2 == 5 and selectedOption ==2):
# For Definite Integral
    USER_INPLOW = simpledialog.askstring(title="Input Test",
                                    prompt="Input lower bound:")
    processed_inputLOW = sp.sympify(USER_INPLOW)
    USER_INPHIGH = simpledialog.askstring(title="Input Test",
                                    prompt="Input upper bound:")
    processed_inputHIGH = sp.sympify(USER_INPHIGH)
if (selectedOption2 == 5 and selectedOption ==3):                                    
# For Definite Normal
    USER_INPNORM = simpledialog.askstring(title="Input Test",
                                    prompt="Input X value:")
    processed_inputNORM = sp.sympify(USER_INPNORM)



processed_input = sp.sympify(USER_INP)




# Print the user input
print("Your Function is: ", USER_INP)


x = sp.symbols('x')
y = x
    #Derivative Graph


if (selectedOption == 1 and selectedOption2 == 4):
    derivative = sp.diff(processed_input,x)
    gra = sp.plot(derivative, (x,-4,4),title = 'derivative', show = True)
elif (selectedOption == 1 and selectedOption2 == 5):
    #Definite derivative
    derivative = sp.diff(processed_input,x)
    dValue = derivative.subs({'x':processed_inputDER}).evalf()


elif (selectedOption == 2 and selectedOption2 == 4):
    #AntiDerivatve Graph
    indefinite_integral = sp.integrate(processed_input, x)
    gra = sp.plot(indefinite_integral, (x,-4,4),title = 'antiderivative', show = True)
elif (selectedOption == 2 and selectedOption2 == 5):
    #Definite integral
    dValue = sp.integrate(processed_input,(x,processed_inputLOW,processed_inputHIGH))

elif (selectedOption == 3 and selectedOption2 == 4):
    #Normal Graph
    gra = sp.plot(processed_input, (x,-4,4),title = 'constant function', show = True)
elif (selectedOption == 3 and selectedOption2 == 5):
    #Definite normal value
    dValue = processed_input.subs({'x':processed_inputNORM}).evalf()


# Making a graph based on the given input (so far makes a graph with the given bounds)

 


def graph():
     gra

if (selectedOption2 == 4):
    tk.Button(windows, text='Training 1', command=graph, fg='red')
elif (selectedOption2 ==5):
    windows.update()
    label6 = tk.Label(windows, text = str(dValue)).pack()
    print(str(dValue))
windows.mainloop()
