# Uncertainty-Calculator
Welcome to the Symbolic Uncertainty Calculator!
Author: Jacob Kosowski
Year: 2022
Version: 1.0.0

This program uses sympy to derive expressions and calculate their uncertainties. Also provides the 'true' value of the
original expression.

How to Use:
Pass arguments depending on your needs.\nThere are 3 acceptible arrangements of arguments: (1), (2), and (5) argument
arrangements. These arrangements are order-sensitive. Each arrangement functions differently, so make sure you are using
the right one for your needs.

(1): Running Functions. There are 3 functions that can be run with only one argument.
These are 'S', 'find_uncertainties', show_example_vars', and 'show_funcs'.
Ex: python uncertainties_calculator.py show_funcs

(2): Reading Function Help. This arrangement allows you to read the help-docs of a given function.
Ex. python uncertainties_calculator.py help show_funcs

(5): Running the Uncertainty Function 'S' Directly. For if you wish to bypass the interface and calculate uncertainties
from the commandline. Enter the function variables as arguments. Keep in mind the required typings.
You must enter:
The expression for which you want to compute uncertainties. Follow sympy's math syntax. Assume 'from sympy import *'.
Your variables. Delinate each with a ','. No spaces. Follow sympy's variable syntax. Assume 'from sympy.abc import*'
The values of your variables. Order them with respect to your list of variables. Delinate each with a ','.
The uncertainties of your variables. Order them with respect to your list of variables. Delinate each with a ','.
Ex. python uncertainties_calculator.py S x*mu x,mu 1.1,.3 .55,.01

The recommended function is 'find_uncertainties()'. This function will open up a windowed interface where you can insert
your variables and calculate your uncertainties.

Thank you for using this program! I hope it was useful for you.
