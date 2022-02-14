#Imports
from sympy import *
from sympy.abc import *
import numpy as np
from tkinter import *
import sys



#Example Values
#-Default == Asteroseismic scaling relation for radius
example_expr = '(nu_max/nu_maxO) * (Delta_nu/Delta_nu_O)**(-2) * (T_eff/T_effO)**(0.5)'
example_vars = 'nu_max,nu_maxO,Delta_nu,Delta_nu_O,T_eff,T_effO'
example_values = '194.94, 3090, 14.2203, 135.1, 4999, 5777'
example_uncerts = '0.9, 30, 0.0057, 0.1, 80, 10'


def S(expression='', var_names=[''], var_values=[], var_uncert=[]):
    """
    Symbolically derives the expression in order to calculate uncertainties
    -expression=str, var_names=[str], var_values=[float], var_uncert=[float]
    -Used by the interactive functions, but can also be used independently
    -Example: python uncertainties_calculator.py S x*y x,y 2.0,4.0 0.1,0.2
    """
    variables_values = dict(zip(var_names, var_values))
    variables_uncertainties = dict(zip(var_names, var_uncert))
    
    for var in var_names:
        exec(var+'=symbols("'+var+'")')
  
    sym_expression = eval(str(expression)) #Converts to Symbolic Expression
    
    true_value = float(sym_expression.evalf(50,subs=variables_values))
    
    def partial_diff_eval(expr, dVar):
        return float(diff(expr,dVar).evalf(50,subs=variables_values))
    
    pde = 0
    for var in list(variables_uncertainties.keys()):
        pde += pow(partial_diff_eval(sym_expression,var) * variables_uncertainties[var],2)
    return sym_expression, "{:.5f}".format(true_value), "{:.5f}".format(np.sqrt(pde))

def _test_expression():
    """
    Test expression for debugging and demonstration
    -Asteroseismic scaling relation for radius
    """
    expr = example_expr
    vari = example_vars.split(',')
    vals = [float(_) for _ in example_values.split(',')]
    uncs = [float(_) for _ in example_uncerts.split(',')]
    
    solution = S(expr, vari, vals, uncs)
    print("Expression: " + expr)
    print("Value: " + solution[1] + u" \u00B1 " + solution[2]+
          "\t"+ str("{:.2f}".format(100*float(solution[2])/float(solution[1])))+ "%")   

def find_uncertainties():
    """
    Tkinter pop-up window input handling
    -Includes asteroseismic scaling relation for radius as an example
    """
    #Set up tkinter window
    win= Tk()
    win.geometry("1000x295")

    #Set up output labels    
    expr_label_text = StringVar()
    expr_label = Label(win,textvariable=expr_label_text)
    answer_label_text = StringVar()
    answer_label = Label(win,textvariable=answer_label_text)

    title = "Symbolic Uncertainties Calculator"
    authorline = "Jacob Kosowski, 2022"
    prompt1 = "Please enter expression for which you want to compute uncertainties. Follow sympy's math syntax. Assume \'from sympy import *\'."
    prompt2 = "Please enter your variables. Delinate each with a \'',\''. No spaces. Follow sympy's variable syntax. Assume \'from sympy.abc import *\'."
    prompt3 = "Please enter the values of your variables. Order them with respect to your list of variables. Delinate each with a \'',\'."
    prompt4 = "Please enter the uncertainties of your variables. Order them with respect to your list of variables. Delinate each with a \',\'."


    def on_button_clicked():

        if expr_label in globals():
            expr_label.after(1000, label.destroy())
            answer_label.after(1000, label.destroy())

        solution = S(expr_ent.get(), vars_ent.get().split(','),
                     [float(x) for x in values_ent.get().split(',')], [float(x) for x in uncert_ent.get().split(',')]) 

        expr_label_text.set("Expression: " + expr_ent.get())
        answer_label_text.set("Value: " + solution[1] + u" \u00B1 " + solution[2] +
                              "\t"+ str("{:.2f}".format(100*float(solution[2])/float(solution[1])))+ "%")

        expr_label.pack()
        answer_label.pack()

    #Create entry and button widgets
    expr_ent = Entry(win,width=950)
    vars_ent = Entry(win,width=950)
    values_ent = Entry(win,width=950)
    uncert_ent = Entry(win,width=950)
    uncert_btn=Button(win, text="Get Uncertainties", command= on_button_clicked)

    #Pack labels and entries
    Label(win,text=title, font=20).pack()
    Label(win,text=authorline).pack()
    Label(win,text=prompt1).pack()
    expr_ent.pack()
    Label(win,text=prompt2).pack()
    vars_ent.pack()
    Label(win,text=prompt3).pack()
    values_ent.pack()
    Label(win,text=prompt4).pack()
    uncert_ent.pack()
    uncert_btn.pack()

    #Insert example values
    expr_ent.insert(0,example_expr)
    vars_ent.insert(0,example_vars)
    values_ent.insert(0,example_values)
    uncert_ent.insert(0,example_uncerts)

    win.mainloop()
    
def show_example_vars():
    """
    Prints out example variables
    """
    print("Example Variables::")
    print("example_expr:\t" + example_expr)
    print("example_vars:\t" + example_vars)
    print("example_values:\t" + example_values)
    print("example_uncerts:\t" + example_uncerts)    
    
def show_funcs():
    """
    Prints out available functions
    """
    print("Available Functions::")
    print('S(expression='', var_names=[''], var_values=[], var_uncert=[])')
    print('find_uncertainties()')
    print('show_example_vars()')
    print('show_funcs()')
    
def _compare(a, b):
    if len(a) != len(b):
        return False
    for x, y in zip(a, b):
        if x == y:
            continue
        else:
            return False
    return True
    
def _help_and_greetings():
    print("Welcome to the Symbolic Uncertainty Calculator!\n"+
             "Author: Jacob Kosowski\n"+
             "Year: 2022\n"+
             "Version: 1.0.0\n\n"+
             "This program uses sympy to derive expressions and calculate their uncertainties. Also provides the 'true' value of the "+
             "original expression.\n\n"+
             "How to Use:\n"+
             "Pass arguments depending on your needs.\nThere are 3 acceptible arrangements of arguments: (1), (2), and (5) argument "+
             "arrangements. These arrangements are order-sensitive. Each arrangement functions differently, so make sure you are using "+
             "the right one for your needs.\n"+
             "(1): Running Functions. There are 3 functions that can be run with only one argument.\n"+
             "These are 'S', 'find_uncertainties', show_example_vars', and 'show_funcs'.\n"+
             "Ex: python uncertainties_calculator.py show_funcs\n\n"+
             "(2): Reading Function Help. This arrangement allows you to read the help-docs of a given function.\n"+
             "Ex. python uncertainties_calculator.py help show_funcs\n\n"+
             "(5): Running the Uncertainty Function 'S' Directly. For if you wish to bypass the interface and calculate uncertainties "+
             "from the commandline. Enter the function variables as arguments. Keep in mind the required typings.\n"+
             "You must enter:\n"+
             "The expression for which you want to compute uncertainties. Follow sympy's math syntax. Assume \'from sympy import *\'.\n"+
             "Your variables. Delinate each with a \'',\''. No spaces. Follow sympy's variable syntax. Assume \'from sympy.abc import "+
             "*\'.\n"+
             "The values of your variables. Order them with respect to your list of variables. Delinate each with a \'',\'.\n"+
             "The uncertainties of your variables. Order them with respect to your list of variables. Delinate each with a \',\'.\n"+
             "Ex. python uncertainties_calculator.py S 'x*mu' x,mu 1.1,.3 .55,.01\n\n"+
             "The recommended function is 'find_uncertainties()'. This function will open up a windowed interface where you can insert "+
             "your variables and calculate your uncertainties.\n\n"+
             "Thank you for using this program! I hope it was useful for you.")
    
def _arghandle(args):
    funcs_list = ['S','find_uncertainties', 'show_example_vars', 'show_funcs']
    if len(args) == 0:
        raise Exception("No arguments passed. Use the argument 'help' if you need it.")
    elif (len(args) == 1 and _compare(args[0],'help')):
        _help_and_greetings() 
       
    elif (len(args) == 1 and not _compare(args[0],'help')):
        for fnc in funcs_list:
            if (_compare(args[0],fnc)):
                exec(fnc+'()')
                return None
            else:
                continue
        raise Exception("Incorrect argument given")
    
    elif (len(args) == 2 and _compare(args[0],'help')):
        for fnc in funcs_list:
            if (_compare(args[1],fnc)):
                exec('help('+fnc+')')
                return None
            else:
                continue
        raise Exception("Incorrect function argument given")
    elif (len(args) == 2 and not _compare(args[0],'help')):
        raise Exception("The first of the (2) arguments must be 'help'")
    elif (len(args) == 5 and _compare(args[0],'S')):
        args[2] = args[2].split(',')
        args[3] = [float(_) for _ in args[3].split(',')]
        args[4] = [float(_) for _ in args[4].split(',')]

        if len(args[2]) != len(args[3]) and len(args[2]) != len(args[4]):
            raise Exception("var_names, var_values, and var_uncert must be of equal length")
        elif type(args[1]) != str:
            raise Exception("expression must be a string")
        elif all(args[2]) and isinstance(args[2], str):
            raise Exception("var_names must be a list of strings")
        elif all(args[3]) and isinstance(args[3], float):
            raise Exception("var_values must be a list of floats")
        elif all(args[4]) and isinstance(args[4], float):
            raise Exception("var_uncert must be a list of floats")
        else:
            solution = eval(args[0] + '(' + args[1] + ',' + str(args[2]) + ',' + str(args[3]) + ',' + str(args[4]) + ')')
            
            print("Expression: " + str(solution[0]))
            print("Value: " + solution[1] + u" \u00B1 " + solution[2]+
                  "\t"+ str("{:.2f}".format(100*float(solution[2])/float(solution[1])))+ "%")
            return None
    elif (len(args) == 5 and not _compare(args[0],'S')):
        raise Exception("The first of the (5) arguments must be 'S'")
    else:
        raise Exception("Incorrect number of arguments given. Need (1), (2), or (5)")
            
def main():
    _arghandle(sys.argv[1:])

if __name__ == "__main__":
    main()