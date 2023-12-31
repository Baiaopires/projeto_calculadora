import tkinter as tk
import math
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D  # Importe para gráficos 3D
from sympy import symbols, diff, integrate, sympify

x, y, z = symbols('x y z')

windows_size = "482x484"

win = tk.Tk()
win.geometry("482x484")
win.resizable(1, 1)
win.title("Calculadora")
win.iconbitmap('calculator_icon-icons.com_54044.ico')
win.configure(bg="#303030")

list_of_variables = ["x", "y", "z"]
list_of_operators = ["/", "*", "+", "-", "**"]
list_of_functions = ["cos(", "sen(", "tan(", "log(", "sqrt(", "d_dx(", "d_dy(", "d_dz(", "integral_x(", "integral_y(", "integral_z("]
list_of_constants = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "π", "e"]

π = math.pi
e = math.e
number_of_rows = 7
number_of_columns = 6

history_list = []

# Função para adicionar uma expressão ao histórico
def add_to_history(expression, result):
    history_list.append(f"{expression} = {result}")

def btn_click(item):
    global expression
    bool_value = 0

    if item == ".":
        if expression == "" or expression == "0.":
            expression = "0."
        else:
            if expression[-1] == ".":
                expression = expression
            else:
                for i in range(10):
                    if expression[-1] == str(i):
                        bool_value = 1
                        if expression[-1] == ".":
                            expression = expression
                        else:
                            expression = expression + str(item)
                if bool_value == 0:
                    expression = expression + "0."
    elif expression == "":
        if item in list_of_operators:
            expression = "0" + str(item)
        elif item == ")":
            expression = expression
        else:
            expression = expression + str(item)

    elif expression == "0":
        if item == 0:
            expression = "0"

    elif expression[-1] == "." and item in list_of_operators:
        expression = expression + "0" + str(item)

    elif expression[-1] in list_of_operators and item in list_of_operators:
        expression = expression[:-1] + str(item)

    elif item in list_of_functions or item == "(" or item in list_of_variables:
        if expression[-1] in list_of_constants:
            expression = expression + "*" + str(item)
        else:
            expression = expression + str(item)

    else:
        expression = expression + str(item)

    input_text.set(expression)

def bt_clear():
    global expression

    expression = ""
    input_text.set(0)

history_text = tk.StringVar()
history_text.set("Histórico de Operações:\n")

def update_history(result):
    current_history = history_text.get()
    new_entry = f"{expression} = {result}\n"
    new_history = current_history + new_entry
    history_text.set(new_history)

def bt_equal():
    global expression
    global error

    try:
        if error == 1: 
            error = 0
            input_text.set(expression)
            expression = ""

        else:
            if expression != "":
                # Verifica se os parênteses estão balanceados
                if (expression.count('(') - expression.count(')')) > 0: 
                    for i in range(expression.count('(') - expression.count(')')): expression = expression + ")"                    
                
                if "sqrt(" in expression:
                    num = float(expression.split("sqrt(")[1].split(")")[0])
                    if num < 0:
                        raise ValueError("Entrada Inválida")

                result = str(eval(expression))

                bool_value = 0

                for i in list_of_variables:
                    if i in result: bool_value = 1

                if bool_value == 0:
                    result = str(round(eval(expression), 8))
                else: bool_value = 0

                if result == "0" or result == "0.0":
                    expression = ""
                else:
                    add_to_history(expression, result)
                    expression = result
                    
                input_text.set(result)
            else: input_text.set("0")

    except ZeroDivisionError:
        expression = ""
        input_text.set("Resultado indefinido")

    except ValueError as e:
        expression = ""
        input_text.set(str(e))

    except SyntaxError as e:
        input_text.set("Erro de sintaxe")

# Função para exibir o histórico de contas
def show_history():
    history_window = tk.Toplevel(win)
    history_window.title("Histórico de Contas")
    history_window.geometry(windows_size)
    history_window.configure(bg="#FF8000")
    history_window.iconbitmap('./counterclockwiserotatingarrowaroundaclock_79793.ICO')

    history_text = tk.Text(history_window, wrap=tk.WORD, font=('arial', 12), bg="#303030", fg="white")
    history_text.pack(expand=True, fill="both")

    # Adiciona as contas ao widget de texto
    for entry in history_list:
        history_text.insert(tk.END, entry + "\n")

    # Função para limpar o histórico
    def clear_history():
        history_text.delete(1.0, tk.END)
        history_list.clear()

     # Botão para limpar o histórico
    clear_button = tk.Button(history_window, text="Limpar Histórico", fg="white", activebackground="#FF8000", activeforeground="#DEDEDE", font=('arial', 12, 'bold'), width=1080, height=20, bd=0, bg="#FF8000", cursor="arrow", command=clear_history)
    clear_button.pack(side=tk.BOTTOM, pady=0, expand=False)
    clear_button.bind("<Enter>", on_enter_history_btn) 
    clear_button.bind("<Leave>", on_leave_history_btn)
        
def cos(x):
    result = math.cos((x * math.pi) / 180.0)

    if x % 90 == 0:
        if round(result, 6) != 0:
            return round(result, 6)
        else:
            return 0
    return round(result, 6)

def sin(x):
    result = math.sin((x * math.pi) / 180.0)

    if x % 90 == 0:
        if round(result, 6) != 0:
            return round(result, 6)
        else:
            return 0
    return round(result, 6)

expression = ""
error = 0

def tan(x):
    global expression
    global error

    if x % 90 == 0 and (x // 90) % 2 != 0:
        # Tangente indefinida para ângulos ímpares de múltiplos de 90 graus
        error = 1
        return "Tangente indefinida"
    
    result = math.tan((x * math.pi) / 180.0)

    if round(result, 6) == 0:
        return 0

    return result
        
def sqrt(x):
    result = math.sqrt(float(x))

    return result

def log(x):
    result = math.log10(x)

    return result

def plot_graph():
    try:
        # Obtenha a expressão atual do campo de entrada
        expression = input_text.get()
        if (expression.count('(') - expression.count(')')) > 0: 
            for i in range(expression.count('(') - expression.count(')')): expression = expression + ")"         
        
        # Crie uma expressão simbólica usando a biblioteca sympy
        x, y, z = symbols('x y z')  # Adicione z para gráficos 3D
        expr = sympify(expression)
        
        # Determine a dimensão da expressão
        if "y" in expression: dimension_count = 2
        else: dimension_count = 1

        #Definição da fonte do título
        csfont = {'fontname':'Arial'}

        if dimension_count == 1:
            # Gráfico 2D
            fig = plt.figure(facecolor='#303030')
            ax = fig.add_subplot(facecolor="#303030")

            x_vals = np.linspace(-50, 50, 100)
            y_vals = np.vectorize(lambda v: expr.subs(x, v))(x_vals)
            
            title = "Gráfico 2D da expressão y = " + expression

            ax.plot(x_vals, y_vals)
            ax.set_title(title, color='white', fontdict=csfont, fontweight="bold")
            ax.set_xlabel('x')
            ax.set_ylabel('y')
            ax.xaxis.label.set_color('white')
            ax.yaxis.label.set_color('white')
            ax.tick_params(axis='x', colors='white')
            ax.tick_params(axis='y', colors='white')
            for axis in ['top', 'bottom', 'left', 'right']:
                ax.spines[axis].set_color('white')

            plt.grid(color = '#505050', linestyle = 'dashed', linewidth = 1)
            plt.show()
            
        elif dimension_count == 2:
            # Gráfico 3D
            fig = plt.figure(facecolor='#303030')
            ax = fig.add_subplot(111, projection='3d', facecolor="#303030")
            
            x_vals = np.linspace(-50, 50, 100)
            y_vals = np.linspace(-50, 50, 100)
            X, Y = np.meshgrid(x_vals, y_vals)
            
            Z = np.vectorize(lambda v1, v2: expr.subs({x: v1, y: v2}))(X, Y)

            title = "Gráfico 3D da expressão z = " + expression

            ax.plot_surface(X, Y, Z, cmap='viridis')
            ax.set_title(title, color='white', fontdict=csfont, fontweight="bold")
            ax.set_xlabel('x')
            ax.set_ylabel('y')
            ax.set_zlabel('z')
            ax.xaxis.label.set_color('white')
            ax.yaxis.label.set_color('white')
            ax.zaxis.label.set_color('white')
            ax.tick_params(axis='x', colors='white')
            ax.tick_params(axis='y', colors='white')
            ax.tick_params(axis='z', colors='white')
            ax.spines['left'].set_color('white')
            ax.spines['top'].set_color('white')
            
            plt.show()
            
        else:
            print("A expressão tem mais de duas variáveis. Não é possível plotar automaticamente.")
            
    except Exception as e:
        # Trate qualquer exceção que possa ocorrer durante a plotagem
        print(f"Erro ao plotar o gráfico: {e}")
    
def btn_backspace():
    global expression

    expression = expression[:-1]

    if expression == "":
        input_text.set("0")
    else:
        input_text.set(expression)

def btn_plus_minus():
    global expression

    if expression == "": expression = expression
    else:
        if expression[0] == "-": expression = expression[1:]
        elif expression == "0": expression = expression
        else: expression = "-" + expression
    
        input_text.set(expression)

def d_dx(item):
    result = diff(item, x)

    return result

def d_dy(item):
    result = diff(item, y)

    return result

def d_dz(item):
    result = diff(item, z)

    return result

def integral_x(item):
    result = integrate(item, x)

    return result

def integral_y(item):
    result = integrate(item, y)

    return result

def integral_z(item):
    result = integrate(item, z)

    return result

def derivar_y(self):
    expr = self.entry.get()
    try:
        result = diff(expr, y)
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, str(result))
    except Exception as e:
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, "Erro")

def derivar_xy(self):
    expr = self.entry.get()
    try:
        result = diff(expr, x) + diff(expr, y)
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, str(result))
    except Exception as e:
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, "Erro")

def integrar_xy(self):
    expr = self.entry.get()
    try:
        result = integrate(expr, x) * integrate(expr, y)
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, str(result))
    except Exception as e:
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, "Erro")

#Criação da animação de cores ao passar o mouse em cima dos botões

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

def on_enter_history_btn(e):
    e.widget['background'] = "#D77C00"

def on_leave_history_btn(e):
    e.widget['background'] = "#FF9300"

#Função para que se possa escrever a expressão utilizando as teclas do teclado ao invés dos botões da calculadora
def on_key_press(event):
    key = event.char
    if key in list_of_constants:
        try:
            btn_click(int(key))
        except ValueError: pass
    elif key == "+":
        btn_click("+")
    elif key == "-":
        btn_click("-")
    elif key == "*":
        btn_click("*")
    elif key == "/":
        btn_click("/")
    elif key == "^^" or (event.keysym == "asciicircum" and event.state == 0):  # Corrigido para verificar Shift
        btn_click("**")
    elif key == "." or key == ",":
        btn_click(".")
    elif key == "enter":
        btn_click("=")
    elif key.lower() == "x":
        btn_click("x")
    elif key.lower() == "y":
        btn_click("y")
    elif key.lower() == "z":
        btn_click("z")
    elif key == "(":
        btn_click("(")
    elif key == ")":
        btn_click(")")
    elif key in "abcdefghijklmnopqrstuvwxz":
        btn_click(key)
    elif key == "\r":
        bt_equal()
    elif event.keysym == "BackSpace":
        btn_backspace()

win.bind("<Key>", on_key_press)
 
expression = ""
error = 0
input_text = tk.StringVar()
input_text.set("0")

#Criação da janela ao qual a parte principal da calculadora ficará 

input_frame = tk.Frame(win, width=12, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=0)
 
input_frame.pack(side=tk.TOP)
 
input_field = tk.Entry(input_frame, fg = "white", font=('arial', 20, 'bold'), textvariable=input_text, width=50, bg="#303030", bd=5, relief=tk.FLAT, justify=tk.RIGHT)
 
input_field.grid(row=0, column=0)
 
input_field.pack(ipady=10)
 
btns_frame = tk.Frame(win, width=312, height=272.5, bg="#303030")

btns_frame.pack()

#Abaixo, estão os botões que fazem parte da calculadora

#primeira linha

history_button = tk.Button(win, text="Histórico", fg="#303030", activebackground="#FF9300", activeforeground="#404040", font=('arial', 14, 'bold'), width=12, height=2, bd=0, bg="#FF9300", cursor="arrow", command=show_history)
history_button.place(x=4, y=4)
history_button.bind("<Enter>", on_enter_history_btn) 
history_button.bind("<Leave>", on_leave_history_btn)

clear = tk.Button(btns_frame, text = "C", fg = "white", activebackground="#404040", activeforeground="#909090", font=('arial', 14), width = 6, height = 2, bd = 0, bg = "#404040", cursor = "arrow", command = lambda: bt_clear())
clear.grid(row = 0, column = 0, padx = 1, pady = 1, sticky="NSEW")
clear.bind("<Enter>", on_enter_symbols) 
clear.bind("<Leave>", on_leave_symbols)

left_parenthesis = tk.Button(btns_frame, text = "(", fg = "white", activebackground="#404040", activeforeground="#909090", font=('arial', 14), width = 6, height = 2, bd = 0, bg = "#404040", cursor = "arrow", command = lambda: btn_click("("))
left_parenthesis.grid(row = 0, column = 1, padx = 1, pady = 1, sticky="NSEW")
left_parenthesis.bind("<Enter>", on_enter_symbols) 
left_parenthesis.bind("<Leave>", on_leave_symbols)

right_parenthesis = tk.Button(btns_frame, text = ")", fg = "white", activebackground="#404040", activeforeground="#909090", font=('arial', 14), width = 6, height = 2, bd = 0, bg = "#404040", cursor = "arrow", command = lambda: btn_click(")"))
right_parenthesis.grid(row = 0, column = 2, padx = 1, pady = 1, sticky="NSEW")
right_parenthesis.bind("<Enter>", on_enter_symbols) 
right_parenthesis.bind("<Leave>", on_leave_symbols)

divide = tk.Button(btns_frame, text = "÷", fg = "white", activebackground="#404040", activeforeground="#909090", font=('arial', 14), width = 6, height = 2, bd = 0, bg = "#404040", cursor = "arrow", command = lambda: btn_click("/"))
divide.grid(row = 0, column = 3, padx = 1, pady = 1, sticky="NSEW")
divide.bind("<Enter>", on_enter_symbols) 
divide.bind("<Leave>", on_leave_symbols)

backspace = tk.Button(btns_frame, text = "⌫", fg = "white", activebackground="#404040", activeforeground="#909090", font=('arial', 14), width = 6, height = 2, bd = 0, bg = "#404040", cursor = "arrow", command = lambda: btn_backspace())
backspace.grid(row = 0, column = 4, padx = 1, pady = 1, sticky="NSEW")
backspace.bind("<Enter>", on_enter_symbols) 
backspace.bind("<Leave>", on_leave_symbols)

modulo = tk.Button(btns_frame, text="amod", fg="white", activebackground="#404040", activeforeground="#909090", font=('arial', 14), width=6, height=2, bd=0, bg="#404040", cursor="arrow", command=lambda: btn_click("%"))
modulo.grid(row = 0, column = 5, padx=1, pady=1, sticky="NSEW")
modulo.bind("<Enter>", on_enter_symbols)
modulo.bind("<Leave>", on_leave_symbols)

#segunda linha
 
seven = tk.Button(btns_frame, text = "7", fg = "white", activebackground="#353535", activeforeground="#909090", font=('arial', 14, 'bold'), width = 6, height = 2, bd = 0, bg = "#505050", cursor = "arrow", command = lambda: btn_click(7))
seven.grid(row = 1, column = 0, padx = 1, pady = 1, sticky="NSEW")
seven.bind("<Enter>", on_enter_numbers) 
seven.bind("<Leave>", on_leave_numbers) 

eight = tk.Button(btns_frame, text = "8", fg = "white", activebackground="#353535", activeforeground="#909090", font=('arial', 14, 'bold'), width = 6, height = 2, bd = 0, bg = "#505050", cursor = "arrow", command = lambda: btn_click(8))
eight.grid(row = 1, column = 1, padx = 1, pady = 1, sticky="NSEW")
eight.bind("<Enter>", on_enter_numbers) 
eight.bind("<Leave>", on_leave_numbers) 

nine = tk.Button(btns_frame, text = "9", fg = "white", activebackground="#353535", activeforeground="#909090", font=('arial', 14, 'bold'), width = 6, height = 2, bd = 0, bg = "#505050", cursor = "arrow", command = lambda: btn_click(9))
nine.grid(row = 1, column = 2, padx = 1, pady = 1, sticky="NSEW")
nine.bind("<Enter>", on_enter_numbers) 
nine.bind("<Leave>", on_leave_numbers) 

multiply = tk.Button(btns_frame, text = "×", fg = "white", activebackground="#404040", activeforeground="#909090", font=('arial', 14), width = 6, height = 2, bd = 0, bg = "#404040", cursor = "arrow", command = lambda: btn_click("*")) 
multiply.grid(row = 1, column = 3, padx = 1, pady = 1, sticky="NSEW")
multiply.bind("<Enter>", on_enter_symbols) 
multiply.bind("<Leave>", on_leave_symbols)

cossine = tk.Button(btns_frame, text = "cos", fg = "white", activebackground="#404040", activeforeground="#909090", font=('arial', 14), width = 6, height = 2, bd = 0, bg = "#404040", cursor = "arrow", command = lambda: btn_click("cos(")) 
cossine.grid(row = 1, column = 4, padx = 1, pady = 1, sticky="NSEW")
cossine.bind("<Enter>", on_enter_symbols) 
cossine.bind("<Leave>", on_leave_symbols)

log_btn = tk.Button(btns_frame, text="log", fg="white", activebackground="#404040", activeforeground="#909090", font=('arial', 14), width=6, height=2, bd=0, bg="#404040", cursor="arrow", command=lambda: btn_click("log("))
log_btn.grid(row=1, column=5, padx=1, pady=1, sticky="NSEW")
log_btn.bind("<Enter>", on_enter_symbols)
log_btn.bind("<Leave>", on_leave_symbols)

# terceira linha
 
four = tk.Button(btns_frame, text = "4", fg = "white", activebackground="#353535", activeforeground="#909090", font=('arial', 14, 'bold'), width = 6, height = 2, bd = 0, bg = "#505050", cursor = "arrow", command = lambda: btn_click(4))
four.grid(row = 2, column = 0, padx = 1, pady = 1, sticky="NSEW")
four.bind("<Enter>", on_enter_numbers) 
four.bind("<Leave>", on_leave_numbers) 

five = tk.Button(btns_frame, text = "5", fg = "white", activebackground="#353535", activeforeground="#909090", font=('arial', 14, 'bold'), width = 6, height = 2, bd = 0, bg = "#505050", cursor = "arrow", command = lambda: btn_click(5))
five.grid(row = 2, column = 1, padx = 1, pady = 1, sticky="NSEW")
five.bind("<Enter>", on_enter_numbers) 
five.bind("<Leave>", on_leave_numbers) 

six = tk.Button(btns_frame, text = "6", fg = "white", activebackground="#353535", activeforeground="#909090", font=('arial', 14, 'bold'), width = 6, height = 2, bd = 0, bg = "#505050", cursor = "arrow", command = lambda: btn_click(6))
six.grid(row = 2, column = 2, padx = 1, pady = 1, sticky="NSEW")
six.bind("<Enter>", on_enter_numbers) 
six.bind("<Leave>", on_leave_numbers)  

minus = tk.Button(btns_frame, text = "-", fg = "white", activebackground="#404040", activeforeground="#909090", font=('arial', 14), width = 6, height = 2, bd = 0, bg = "#404040", cursor = "arrow", command = lambda: btn_click("-"))
minus.grid(row = 2, column = 3, padx = 1, pady = 1, sticky="NSEW")
minus.bind("<Enter>", on_enter_symbols) 
minus.bind("<Leave>", on_leave_symbols)

sine = tk.Button(btns_frame, text = "sen", fg = "white", activebackground="#404040", activeforeground="#909090", font=('arial', 14), width = 6, height = 2, bd = 0, bg = "#404040", cursor = "arrow", command = lambda: btn_click("sin("))
sine.grid(row = 2, column = 4, padx = 1, pady = 1, sticky="NSEW")
sine.bind("<Enter>", on_enter_symbols) 
sine.bind("<Leave>", on_leave_symbols)

sqrt_btn = tk.Button(btns_frame, text="√", fg="white", activebackground="#404040", activeforeground="#909090", font=('arial', 14), width=6, height=2, bd=0, bg="#404040", cursor="arrow", command=lambda: btn_click("sqrt("))
sqrt_btn.grid(row=2, column=5, padx=1, pady=1, sticky="NSEW")
sqrt_btn.bind("<Enter>", on_enter_symbols)
sqrt_btn.bind("<Leave>", on_leave_symbols)

# quarta linha
 
one = tk.Button(btns_frame, text = "1", fg = "white", activebackground="#353535", activeforeground="#909090", font=('arial', 14, 'bold'), width = 6, height = 2, bd = 0, bg = "#505050", cursor = "arrow", command = lambda: btn_click(1))
one.grid(row = 3, column = 0, padx = 1, pady = 1, sticky="NSEW")
one.bind("<Enter>", on_enter_numbers) 
one.bind("<Leave>", on_leave_numbers)  

two = tk.Button(btns_frame, text = "2", fg = "white", activebackground="#353535", activeforeground="#909090", font=('arial', 14, 'bold'), width = 6, height = 2, bd = 0, bg = "#505050", cursor = "arrow", command = lambda: btn_click(2))
two.grid(row = 3, column = 1, padx = 1, pady = 1, sticky="NSEW")
two.bind("<Enter>", on_enter_numbers) 
two.bind("<Leave>", on_leave_numbers)  

three = tk.Button(btns_frame, text = "3", fg = "white", activebackground="#353535", activeforeground="#909090", font=('arial', 14, 'bold'), width = 6, height = 2, bd = 0, bg = "#505050", cursor = "arrow", command = lambda: btn_click(3))
three.grid(row = 3, column = 2, padx = 1, pady = 1, sticky="NSEW")
three.bind("<Enter>", on_enter_numbers) 
three.bind("<Leave>", on_leave_numbers)  

plus = tk.Button(btns_frame, text = "+", fg = "white", activebackground="#404040", activeforeground="#909090", font=('arial', 14), width = 6, height = 2, bd = 0, bg = "#404040", cursor = "arrow", command = lambda: btn_click("+"))
plus.grid(row = 3, column = 3, padx = 1, pady = 1, sticky="NSEW")
plus.bind("<Enter>", on_enter_symbols) 
plus.bind("<Leave>", on_leave_symbols)

tangent = tk.Button(btns_frame, text = "tan", fg = "white", activebackground="#404040", activeforeground="#909090", font=('arial', 14), width = 6, height = 2, bd = 0, bg = "#404040", cursor = "arrow", command = lambda: btn_click("tan("))
tangent.grid(row = 3, column = 4, padx = 1, pady = 1, sticky="NSEW")
tangent.bind("<Enter>", on_enter_symbols) 
tangent.bind("<Leave>", on_leave_symbols)

power = tk.Button(btns_frame, text="^", fg="white", activebackground="#404040", activeforeground="#909090", font=('arial', 14), width=6, height=2, bd=0, bg="#404040", cursor="arrow", command=lambda: btn_click("**"))
power.grid(row=3, column=5, padx=1, pady=1, sticky="NSEW")
power.bind("<Enter>", on_enter_symbols)
power.bind("<Leave>", on_leave_symbols)


# quinta linha

plus_minus_bt = tk.Button(btns_frame, text = "±", fg = "white", activebackground="#353535", activeforeground="#909090", font = ('arial', 14), width = 6, height = 2, bd = 0, bg = "#505050", cursor = "arrow", command = lambda: btn_plus_minus())
plus_minus_bt.grid(row = 4, column = 0, padx = 1, pady = 1, sticky="NSEW")
plus_minus_bt.bind("<Enter>", on_enter_numbers) 
plus_minus_bt.bind("<Leave>", on_leave_numbers) 

zero = tk.Button(btns_frame, text = "0", fg = "white", activebackground="#353535", activeforeground="#909090", font = ('arial', 14, 'bold'), width = 6, height = 2, bd = 0, bg = "#505050", cursor = "arrow", command = lambda: btn_click(0))
zero.grid(row = 4, column = 1, padx = 1, pady = 1, sticky="NSEW")
zero.bind("<Enter>", on_enter_numbers) 
zero.bind("<Leave>", on_leave_numbers) 

point = tk.Button(btns_frame, text = ".", fg = "white", activebackground="#353535", activeforeground="#909090", font=('arial', 14), width = 6, height = 2, bd = 0, bg = "#505050", cursor = "arrow", command = lambda: btn_click("."))
point.grid(row = 4, column = 2, padx = 1, pady = 1, sticky="NSEW")
point.bind("<Enter>", on_enter_numbers) 
point.bind("<Leave>", on_leave_numbers)

equals = tk.Button(btns_frame, text = "=", fg = "#303030", activebackground="#F44F45", activeforeground="#505050", font=('arial', 14), width = 6, height = 2, bd = 0, bg = "#FF686B", cursor = "arrow", command = lambda: bt_equal())
equals.grid(row = 4, column = 3, padx = 1, pady = 1, sticky="NSEW")
equals.bind("<Enter>", on_enter_equal) 
equals.bind("<Leave>", on_leave_equal)

pi_button = tk.Button(btns_frame, text = "π", fg = "white", activebackground="#404040", activeforeground="#909090", font=('arial', 14), width = 6, height = 2, bd = 0, bg = "#404040", cursor = "arrow", command = lambda: btn_click("π"))
pi_button.grid(row = 4, column = 4, padx = 1, pady = 1, sticky="NSEW")
pi_button.bind("<Enter>", on_enter_symbols) 
pi_button.bind("<Leave>", on_leave_symbols)

euler_button = tk.Button(btns_frame, text = "e", fg = "white", activebackground="#404040", activeforeground="#909090", font=('arial', 14, 'italic'), width = 6, height = 2, bd = 0, bg = "#404040", cursor = "arrow", command = lambda: btn_click("e"))
euler_button.grid(row = 4, column = 5, padx = 1, pady = 1, sticky="NSEW")
euler_button.bind("<Enter>", on_enter_symbols) 
euler_button.bind("<Leave>", on_leave_symbols)

#sexta linha

x_button = tk.Button(btns_frame, text = "x", fg = "white", activebackground="#353535", activeforeground="#909090", font = ('arial', 14, 'italic'), width = 6, height = 2, bd = 0, bg = "#505050", cursor = "arrow", command = lambda: btn_click("x"))
x_button.grid(row = 5, column = 0, padx = 1, pady = 1, sticky="NSEW")
x_button.bind("<Enter>", on_enter_numbers) 
x_button.bind("<Leave>", on_leave_numbers)

y_button = tk.Button(btns_frame, text = "y", fg = "white", activebackground="#353535", activeforeground="#909090", font = ('arial', 14, 'italic'), width = 6, height = 2, bd = 0, bg = "#505050", cursor = "arrow", command = lambda: btn_click("y"))
y_button.grid(row = 5, column = 1, padx = 1, pady = 1, sticky="NSEW")
y_button.bind("<Enter>", on_enter_numbers) 
y_button.bind("<Leave>", on_leave_numbers)

z_button = tk.Button(btns_frame, text = "z", fg = "white", activebackground="#353535", activeforeground="#909090", font = ('arial', 14, 'italic'), width = 6, height = 2, bd = 0, bg = "#505050", cursor = "arrow", command = lambda: btn_click("z"))
z_button.grid(row = 5, column = 2, padx = 1, pady = 1, sticky="NSEW")
z_button.bind("<Enter>", on_enter_numbers) 
z_button.bind("<Leave>", on_leave_numbers)

diff_x = tk.Button(btns_frame, text = "dx", fg = "white", activebackground="#404040", activeforeground="#909090", font=('arial', 14, 'italic'), width = 6, height = 2, bd = 0, bg = "#404040", cursor = "arrow", command = lambda: btn_click("d_dx("))
diff_x.grid(row = 5, column = 3, padx = 1, pady = 1, sticky="NSEW")
diff_x.bind("<Enter>", on_enter_symbols) 
diff_x.bind("<Leave>", on_leave_symbols)

diff_y = tk.Button(btns_frame, text = "dy", fg = "white", activebackground="#404040", activeforeground="#909090", font=('arial', 14, 'italic'), width = 6, height = 2, bd = 0, bg = "#404040", cursor = "arrow", command = lambda: btn_click("d_dy("))
diff_y.grid(row = 5, column = 4, padx = 1, pady = 1, sticky="NSEW")
diff_y.bind("<Enter>", on_enter_symbols) 
diff_y.bind("<Leave>", on_leave_symbols)

diff_z = tk.Button(btns_frame, text = "dz", fg = "white", activebackground="#404040", activeforeground="#909090", font=('arial', 14, 'italic'), width = 6, height = 2, bd = 0, bg = "#404040", cursor = "arrow", command = lambda: btn_click("d_dz("))
diff_z.grid(row = 5, column = 5, padx = 1, pady = 1, sticky="NSEW")
diff_z.bind("<Enter>", on_enter_symbols) 
diff_z.bind("<Leave>", on_leave_symbols)

#setima linha

integral_x_bt = tk.Button(btns_frame, text="∫dx", fg="white", activebackground="#404040", activeforeground="#909090", font=('arial', 14, 'italic'), width=6, height=2, bd=0, bg="#404040", cursor="arrow", command=lambda: btn_click("integral_x("))
integral_x_bt.grid(row=6, column=0, padx=1, pady=1, sticky="NSEW")
integral_x_bt.bind("<Enter>", on_enter_symbols)
integral_x_bt.bind("<Leave>", on_leave_symbols)

integral_y_bt = tk.Button(btns_frame, text="∫dy", fg="white", activebackground="#404040", activeforeground="#909090", font=('arial', 14, 'italic'), width=6, height=2, bd=0, bg="#404040", cursor="arrow", command=lambda: btn_click("integral_y("))
integral_y_bt.grid(row=6, column=1, padx=1, pady=1, sticky="NSEW")
integral_y_bt.bind("<Enter>", on_enter_symbols)
integral_y_bt.bind("<Leave>", on_leave_symbols)

integral_z_bt = tk.Button(btns_frame, text="∫dz", fg="white", activebackground="#404040", activeforeground="#909090", font=('arial', 14, 'italic'), width=6, height=2, bd=0, bg="#404040", cursor="arrow", command=lambda: btn_click("integral_z("))
integral_z_bt.grid(row=6, column=2, padx=1, pady=1, sticky="NSEW")
integral_z_bt.bind("<Enter>", on_enter_symbols)
integral_z_bt.bind("<Leave>", on_leave_symbols)

plot_button = tk.Button(btns_frame, text="Plotar Gráfico", fg="white", activebackground="#404040", activeforeground="#909090", font=('arial', 14), width=12, height=2, bd=0, bg="#404040", cursor="arrow", command=plot_graph)
plot_button.grid(row=6, column=3, columnspan=6, padx=1, pady=1, sticky="NSEW")
plot_button.bind("<Enter>", on_enter_symbols)
plot_button.bind("<Leave>", on_leave_symbols)


for i in range(number_of_rows):
    tk.Grid.rowconfigure(btns_frame, i, weight=1)
for i in range(number_of_columns):
    tk.Grid.columnconfigure(btns_frame, i, weight=1, uniform='columns')

win.mainloop()
