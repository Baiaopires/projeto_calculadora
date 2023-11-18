from tkinter import *
import math

win = Tk()
win.geometry("388x359")
win.resizable(0, 0)
win.title("Calculadora")

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
        if item in {"/", "*", "+", "-"}:
            expression = "0" + str(item)
        elif item == ")": expression = expression
        else: expression = expression + str(item)

    elif expression == "0":
        if item == 0: expression = "0"

    elif expression[-1] == "." and item in {"/", "*", "+", "-"}:
        expression = expression + "0" + str(item)
    
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
    input_text.set(expression)

 
expression = ""
error = 0
input_text = StringVar()
input_text.set("0")
 
input_frame = Frame(win, width=12, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=0, relief=GROOVE)
 
input_frame.pack(side=TOP)
 
input_field = Entry(input_frame, fg = "white", font=('arial', 20, 'bold'), textvariable=input_text, width=50, bg="#303030", bd=5, relief=FLAT, justify=RIGHT)
 
input_field.grid(row=0, column=0)
 
input_field.pack(ipady=10)
 
btns_frame = Frame(win, width=312, height=272.5, bg="#303030")
 
btns_frame.pack()

#primeira linha
 
clear = Button(btns_frame, text = "C", fg = "white", font=('arial', 14, 'bold'), width = 6, height = 2, bd = 0, bg = "#404040", cursor = "hand2", command = lambda: bt_clear()).grid(row = 0, column = 0, padx = 1, pady = 1)

left_parenthesis = Button(btns_frame, text = "(", fg = "white", font=('arial', 14, 'bold'), width = 6, height = 2, bd = 0, bg = "#404040", cursor = "hand2", command = lambda: btn_click("(")).grid(row = 0, column = 1, padx = 1, pady = 1)

right_parenthesis = Button(btns_frame, text = ")", fg = "white", font=('arial', 14, 'bold'), width = 6, height = 2, bd = 0, bg = "#404040", cursor = "hand2", command = lambda: btn_click(")")).grid(row = 0, column = 2, padx = 1, pady = 1)
 
divide = Button(btns_frame, text = "/", fg = "white", highlightcolor="#505050", highlightbackground="#505050", font=('arial', 14), width = 6, height = 2, bd = 0, bg = "#404040", cursor = "hand2", command = lambda: btn_click("/")).grid(row = 0, column = 3, padx = 1, pady = 1)

backspace = Button(btns_frame, text = "⌫", fg = "white", highlightcolor="#505050", highlightbackground="#505050", font=('arial', 14), width = 6, height = 2, bd = 0, bg = "#404040", cursor = "hand2", command = lambda: btn_backspace()).grid(row = 0, column = 4, padx = 1, pady = 1)
 
#segunda linha
 
seven = Button(btns_frame, text = "7", fg = "white", highlightcolor="#505050", highlightbackground="#505050", font=('arial', 14, 'bold'), width = 6, height = 2, bd = 0, bg = "#505050", cursor = "hand2", command = lambda: btn_click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
 
eight = Button(btns_frame, text = "8", fg = "white", highlightcolor="#505050", highlightbackground="#505050", font=('arial', 14, 'bold'), width = 6, height = 2, bd = 0, bg = "#505050", cursor = "hand2", command = lambda: btn_click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
 
nine = Button(btns_frame, text = "9", fg = "white", highlightcolor="#505050", highlightbackground="#505050", font=('arial', 14, 'bold'), width = 6, height = 2, bd = 0, bg = "#505050", cursor = "hand2", command = lambda: btn_click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
 
multiply = Button(btns_frame, text = "*", fg = "white", highlightcolor="#505050", highlightbackground="#505050", font=('arial', 14), width = 6, height = 2, bd = 0, bg = "#404040", cursor = "hand2", command = lambda: btn_click("*")).grid(row = 1, column = 3, padx = 1, pady = 1)

cossine = Button(btns_frame, text = "cos", fg = "white", highlightcolor="#505050", highlightbackground="#505050", font=('arial', 14), width = 6, height = 2, bd = 0, bg = "#404040", cursor = "hand2", command = lambda: btn_click("cos(")).grid(row = 1, column = 4, padx = 1, pady = 1)
 
# terceira linha
 
four = Button(btns_frame, text = "4", fg = "white", highlightcolor="#505050", highlightbackground="#505050", font=('arial', 14, 'bold'), width = 6, height = 2, bd = 0, bg = "#505050", cursor = "hand2", command = lambda: btn_click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
 
five = Button(btns_frame, text = "5", fg = "white", highlightcolor="#505050", highlightbackground="#505050", font=('arial', 14, 'bold'), width = 6, height = 2, bd = 0, bg = "#505050", cursor = "hand2", command = lambda: btn_click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
 
six = Button(btns_frame, text = "6", fg = "white", highlightcolor="#505050", highlightbackground="#505050", font=('arial', 14, 'bold'), width = 6, height = 2, bd = 0, bg = "#505050", cursor = "hand2", command = lambda: btn_click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
 
minus = Button(btns_frame, text = "-", fg = "white", highlightcolor="#505050", highlightbackground="#505050", font=('arial', 14), width = 6, height = 2, bd = 0, bg = "#404040", cursor = "hand2", command = lambda: btn_click("-")).grid(row = 2, column = 3, padx = 1, pady = 1)

sine = Button(btns_frame, text = "sen", fg = "white", highlightcolor="#505050", highlightbackground="#505050", font=('arial', 14), width = 6, height = 2, bd = 0, bg = "#404040", cursor = "hand2", command = lambda: btn_click("sen(")).grid(row = 2, column = 4, padx = 1, pady = 1)
 
# quarta linha
 
one = Button(btns_frame, text = "1", fg = "white", highlightcolor="#505050", highlightbackground="#505050", font=('arial', 14, 'bold'), width = 6, height = 2, bd = 0, bg = "#505050", cursor = "hand2", command = lambda: btn_click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
 
two = Button(btns_frame, text = "2", fg = "white", highlightcolor="#505050", highlightbackground="#505050", font=('arial', 14, 'bold'), width = 6, height = 2, bd = 0, bg = "#505050", cursor = "hand2", command = lambda: btn_click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
 
three = Button(btns_frame, text = "3", fg = "white", highlightcolor="#505050", highlightbackground="#505050", font=('arial', 14, 'bold'), width = 6, height = 2, bd = 0, bg = "#505050", cursor = "hand2", command = lambda: btn_click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
 
plus = Button(btns_frame, text = "+", fg = "white", highlightcolor="#505050", highlightbackground="#505050", font=('arial', 14), width = 6, height = 2, bd = 0, bg = "#404040", cursor = "hand2", command = lambda: btn_click("+")).grid(row = 3, column = 3, padx = 1, pady = 1)
 
tangent = Button(btns_frame, text = "tan", fg = "white", highlightcolor="#505050", highlightbackground="#505050", font=('arial', 14), width = 6, height = 2, bd = 0, bg = "#404040", cursor = "hand2", command = lambda: btn_click("tan(")).grid(row = 3, column = 4, padx = 1, pady = 1)

# quinta linha
 
zero = Button(btns_frame, text = "0", fg = "white", highlightcolor="#505050", highlightbackground="#505050", font = ('arial', 14, 'bold'), width = 6, height = 2, bd = 0, bg = "#505050", cursor = "hand2", command = lambda: btn_click(0)).grid(row = 4, column = 1, padx = 1, pady = 1)
 
point = Button(btns_frame, text = ".", fg = "white", highlightcolor="#505050", highlightbackground="#505050", font=('arial', 14, 'bold'), width = 6, height = 2, bd = 0, bg = "#404040", cursor = "hand2", command = lambda: btn_click(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
 
equals = Button(btns_frame, text = "=", fg = "#303030", highlightcolor="#FF686B", highlightbackground="#FF686B", font=('arial', 14), width = 6, height = 2, bd = 0, bg = "#FF686B", cursor = "hand2", command = lambda: bt_equal()).grid(row = 4, column = 3, padx = 1, pady = 1)

pi_button = Button(btns_frame, text = "π", fg = "white", highlightcolor="#505050", highlightbackground="#505050", font=('arial', 14), width = 6, height = 2, bd = 0, bg = "#404040", cursor = "hand2", command = lambda: btn_click("π")).grid(row = 4, column = 4, padx = 1, pady = 1)
 
win.mainloop()
