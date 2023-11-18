import tkinter as tk
import math

win = tk.Tk()
win.geometry("388x359")
win.resizable(1, 0)
win.title("Calculadora")
win.configure(bg = "#303030")

list_of_operators = ["/", "*", "+", "-"]

def btn_click(item):
    global expression
    bool_value = 0

    if item == ".":
        if expression == "" or expression == "0.":
            expression = "0."
        else:
            if expression[-1] == ".": expression = expression
            else: 
                for i in range(10):
                    if expression[-1] == str(i):
                        bool_value = 1
                        if expression[-1] == ".": expression = expression
                        else: expression = expression + str(item)
                if bool_value == 0:
                    expression = expression + "0."
    elif expression == "":
        if item in list_of_operators:
            expression = "0" + str(item)
        elif item == ")": expression = expression
        else: expression = expression + str(item)

    elif expression == "0":
        if item == 0: expression = "0"

    elif expression[-1] == "." and item in list_of_operators:
        expression = expression + "0" + str(item)
    
    elif expression[-1] in list_of_operators and item in list_of_operators:
        expression = expression[:-1] + str(item)

    else:
        expression = expression + str(item)

    input_text.set(expression)

def bt_clear(): 
    global expression 
    expression = "" 
    input_text.set(0)
 
def bt_equal():
    global expression
    global error

    if error == 1: 
        error = 0
        input_text.set(expression)
        expression = ""

    else:
        if expression != "":
            result = str(eval(expression))
            if result == "0" or result == "0.0":
                expression = ""
            else:
                expression = result
            input_text.set(result)
        else: input_text.set("0")

π = math.pi

def cos(x):
    result = math.cos((x*math.pi)/180)

    if x%90 == 0:
        if round(result, 2) != 0:
            return round(result, 2)
        else: 
            return 0 
    return result

def sen(x):
    result = math.sin((x*math.pi)/180)

    if x%90 == 0:
        if round(result, 2) != 0:
            return round(result, 2)
        else: 
            return 0
        
    return result

def tan(x):
    global expression
    global error
    result = math.tan((x*math.pi)/180)

    if round(result, 2) != 0:
        if x%90 == 0:
            error = 1
            return "Entrada inválida"

    if round(result, 2) == 0: return 0

    return result

def btn_backspace():
    global expression

    expression = expression[:-1]

    if expression == "":
        input_text.set("0")
    else:
        input_text.set(expression)

def on_enter_symbols(e):
    e.widget['background'] = "#505050"

def on_leave_symbols(e):
    e.widget['background'] = "#404040"

def on_enter_numbers(e):
    e.widget['background'] = "#404040"

def on_leave_numbers(e):
    e.widget['background'] = "#505050"

def on_enter_equal(e):
    e.widget['background'] = "#FF4247"

def on_leave_equal(e):
    e.widget['background'] = "#FF686B"
 
expression = ""
error = 0
input_text = tk.StringVar()
input_text.set("0")
 
input_frame = tk.Frame(win, width=12, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=0)
 
input_frame.pack(side=tk.TOP)
 
input_field = tk.Entry(input_frame, fg = "white", font=('arial', 20, 'bold'), textvariable=input_text, width=50, bg="#303030", bd=5, relief=tk.FLAT, justify=tk.RIGHT)
 
input_field.grid(row=0, column=0)
 
input_field.pack(ipady=10)
 
btns_frame = tk.Frame(win, width=312, height=272.5, bg="#303030")

btns_frame.pack()

#primeira linha
 
clear = tk.Button(btns_frame, text = "C", fg = "white", activebackground="#404040", activeforeground="#909090", font=('arial', 14, 'bold'), width = 6, height = 2, bd = 0, bg = "#404040", cursor = "arrow", command = lambda: bt_clear())
clear.grid(row = 0, column = 0, padx = 1, pady = 1)
clear.bind("<Enter>", on_enter_symbols) 
clear.bind("<Leave>", on_leave_symbols)

left_parenthesis = tk.Button(btns_frame, text = "(", fg = "white", activebackground="#404040", activeforeground="#909090", font=('arial', 14, 'bold'), width = 6, height = 2, bd = 0, bg = "#404040", cursor = "arrow", command = lambda: btn_click("("))
left_parenthesis.grid(row = 0, column = 1, padx = 1, pady = 1)
left_parenthesis.bind("<Enter>", on_enter_symbols) 
left_parenthesis.bind("<Leave>", on_leave_symbols)

right_parenthesis = tk.Button(btns_frame, text = ")", fg = "white", activebackground="#404040", activeforeground="#909090", font=('arial', 14, 'bold'), width = 6, height = 2, bd = 0, bg = "#404040", cursor = "arrow", command = lambda: btn_click(")"))
right_parenthesis.grid(row = 0, column = 2, padx = 1, pady = 1)
right_parenthesis.bind("<Enter>", on_enter_symbols) 
right_parenthesis.bind("<Leave>", on_leave_symbols)

divide = tk.Button(btns_frame, text = "÷", fg = "white", activebackground="#404040", activeforeground="#909090", font=('arial', 14), width = 6, height = 2, bd = 0, bg = "#404040", cursor = "arrow", command = lambda: btn_click("/"))
divide.grid(row = 0, column = 3, padx = 1, pady = 1)
divide.bind("<Enter>", on_enter_symbols) 
divide.bind("<Leave>", on_leave_symbols)

backspace = tk.Button(btns_frame, text = "⌫", fg = "white", activebackground="#404040", activeforeground="#909090", font=('arial', 14), width = 6, height = 2, bd = 0, bg = "#404040", cursor = "arrow", command = lambda: btn_backspace())
backspace.grid(row = 0, column = 4, padx = 1, pady = 1)
backspace.bind("<Enter>", on_enter_symbols) 
backspace.bind("<Leave>", on_leave_symbols)

#segunda linha
 
seven = tk.Button(btns_frame, text = "7", fg = "white", activebackground="#353535", activeforeground="#909090", font=('arial', 14, 'bold'), width = 6, height = 2, bd = 0, bg = "#505050", cursor = "arrow", command = lambda: btn_click(7))
seven.grid(row = 1, column = 0, padx = 1, pady = 1)
seven.bind("<Enter>", on_enter_numbers) 
seven.bind("<Leave>", on_leave_numbers) 

eight = tk.Button(btns_frame, text = "8", fg = "white", activebackground="#353535", activeforeground="#909090", font=('arial', 14, 'bold'), width = 6, height = 2, bd = 0, bg = "#505050", cursor = "arrow", command = lambda: btn_click(8))
eight.grid(row = 1, column = 1, padx = 1, pady = 1)
eight.bind("<Enter>", on_enter_numbers) 
eight.bind("<Leave>", on_leave_numbers) 

nine = tk.Button(btns_frame, text = "9", fg = "white", activebackground="#353535", activeforeground="#909090", font=('arial', 14, 'bold'), width = 6, height = 2, bd = 0, bg = "#505050", cursor = "arrow", command = lambda: btn_click(9))
nine.grid(row = 1, column = 2, padx = 1, pady = 1)
nine.bind("<Enter>", on_enter_numbers) 
nine.bind("<Leave>", on_leave_numbers) 

multiply = tk.Button(btns_frame, text = "×", fg = "white", activebackground="#404040", activeforeground="#909090", font=('arial', 14), width = 6, height = 2, bd = 0, bg = "#404040", cursor = "arrow", command = lambda: btn_click("*")) 
multiply.grid(row = 1, column = 3, padx = 1, pady = 1)
multiply.bind("<Enter>", on_enter_symbols) 
multiply.bind("<Leave>", on_leave_symbols)

cossine = tk.Button(btns_frame, text = "cos", fg = "white", activebackground="#404040", activeforeground="#909090", font=('arial', 14), width = 6, height = 2, bd = 0, bg = "#404040", cursor = "arrow", command = lambda: btn_click("cos(")) 
cossine.grid(row = 1, column = 4, padx = 1, pady = 1)
cossine.bind("<Enter>", on_enter_symbols) 
cossine.bind("<Leave>", on_leave_symbols)

# terceira linha
 
four = tk.Button(btns_frame, text = "4", fg = "white", activebackground="#353535", activeforeground="#909090", font=('arial', 14, 'bold'), width = 6, height = 2, bd = 0, bg = "#505050", cursor = "arrow", command = lambda: btn_click(4))
four.grid(row = 2, column = 0, padx = 1, pady = 1)
four.bind("<Enter>", on_enter_numbers) 
four.bind("<Leave>", on_leave_numbers) 

five = tk.Button(btns_frame, text = "5", fg = "white", activebackground="#353535", activeforeground="#909090", font=('arial', 14, 'bold'), width = 6, height = 2, bd = 0, bg = "#505050", cursor = "arrow", command = lambda: btn_click(5))
five.grid(row = 2, column = 1, padx = 1, pady = 1)
five.bind("<Enter>", on_enter_numbers) 
five.bind("<Leave>", on_leave_numbers) 

six = tk.Button(btns_frame, text = "6", fg = "white", activebackground="#353535", activeforeground="#909090", font=('arial', 14, 'bold'), width = 6, height = 2, bd = 0, bg = "#505050", cursor = "arrow", command = lambda: btn_click(6))
six.grid(row = 2, column = 2, padx = 1, pady = 1)
six.bind("<Enter>", on_enter_numbers) 
six.bind("<Leave>", on_leave_numbers)  

minus = tk.Button(btns_frame, text = "-", fg = "white", activebackground="#404040", activeforeground="#909090", font=('arial', 14), width = 6, height = 2, bd = 0, bg = "#404040", cursor = "arrow", command = lambda: btn_click("-"))
minus.grid(row = 2, column = 3, padx = 1, pady = 1)
minus.bind("<Enter>", on_enter_symbols) 
minus.bind("<Leave>", on_leave_symbols)

sine = tk.Button(btns_frame, text = "sen", fg = "white", activebackground="#404040", activeforeground="#909090", font=('arial', 14), width = 6, height = 2, bd = 0, bg = "#404040", cursor = "arrow", command = lambda: btn_click("sen("))
sine.grid(row = 2, column = 4, padx = 1, pady = 1)
sine.bind("<Enter>", on_enter_symbols) 
sine.bind("<Leave>", on_leave_symbols)

# quarta linha
 
one = tk.Button(btns_frame, text = "1", fg = "white", activebackground="#353535", activeforeground="#909090", font=('arial', 14, 'bold'), width = 6, height = 2, bd = 0, bg = "#505050", cursor = "arrow", command = lambda: btn_click(1))
one.grid(row = 3, column = 0, padx = 1, pady = 1)
one.bind("<Enter>", on_enter_numbers) 
one.bind("<Leave>", on_leave_numbers)  

two = tk.Button(btns_frame, text = "2", fg = "white", activebackground="#353535", activeforeground="#909090", font=('arial', 14, 'bold'), width = 6, height = 2, bd = 0, bg = "#505050", cursor = "arrow", command = lambda: btn_click(2))
two.grid(row = 3, column = 1, padx = 1, pady = 1)
two.bind("<Enter>", on_enter_numbers) 
two.bind("<Leave>", on_leave_numbers)  

three = tk.Button(btns_frame, text = "3", fg = "white", activebackground="#353535", activeforeground="#909090", font=('arial', 14, 'bold'), width = 6, height = 2, bd = 0, bg = "#505050", cursor = "arrow", command = lambda: btn_click(3))
three.grid(row = 3, column = 2, padx = 1, pady = 1)
three.bind("<Enter>", on_enter_numbers) 
three.bind("<Leave>", on_leave_numbers)  

plus = tk.Button(btns_frame, text = "+", fg = "white", activebackground="#404040", activeforeground="#909090", font=('arial', 14), width = 6, height = 2, bd = 0, bg = "#404040", cursor = "arrow", command = lambda: btn_click("+"))
plus.grid(row = 3, column = 3, padx = 1, pady = 1)
plus.bind("<Enter>", on_enter_symbols) 
plus.bind("<Leave>", on_leave_symbols)

tangent = tk.Button(btns_frame, text = "tan", fg = "white", activebackground="#404040", activeforeground="#909090", font=('arial', 14), width = 6, height = 2, bd = 0, bg = "#404040", cursor = "arrow", command = lambda: btn_click("tan("))
tangent.grid(row = 3, column = 4, padx = 1, pady = 1)
tangent.bind("<Enter>", on_enter_symbols) 
tangent.bind("<Leave>", on_leave_symbols)

# quinta linha
 
zero = tk.Button(btns_frame, text = "0", fg = "white", activebackground="#353535", activeforeground="#909090", font = ('arial', 14, 'bold'), width = 6, height = 2, bd = 0, bg = "#505050", cursor = "arrow", command = lambda: btn_click(0))
zero.grid(row = 4, column = 1, padx = 1, pady = 1)
zero.bind("<Enter>", on_enter_numbers) 
zero.bind("<Leave>", on_leave_numbers) 

point = tk.Button(btns_frame, text = ".", fg = "white", activebackground="#404040", activeforeground="#909090", font=('arial', 14, 'bold'), width = 6, height = 2, bd = 0, bg = "#404040", cursor = "arrow", command = lambda: btn_click("."))
point.grid(row = 4, column = 2, padx = 1, pady = 1)
point.bind("<Enter>", on_enter_symbols) 
point.bind("<Leave>", on_leave_symbols)

equals = tk.Button(btns_frame, text = "=", fg = "#303030", activebackground="#F44F45", activeforeground="#505050", font=('arial', 14), width = 6, height = 2, bd = 0, bg = "#FF686B", cursor = "arrow", command = lambda: bt_equal())
equals.grid(row = 4, column = 3, padx = 1, pady = 1)
equals.bind("<Enter>", on_enter_equal) 
equals.bind("<Leave>", on_leave_equal)

pi_button = tk.Button(btns_frame, text = "π", fg = "white", activebackground="#404040", activeforeground="#909090", font=('arial', 14), width = 6, height = 2, bd = 0, bg = "#404040", cursor = "arrow", command = lambda: btn_click("π"))
pi_button.grid(row = 4, column = 4, padx = 1, pady = 1)
pi_button.bind("<Enter>", on_enter_symbols) 
pi_button.bind("<Leave>", on_leave_symbols)

win.mainloop()
