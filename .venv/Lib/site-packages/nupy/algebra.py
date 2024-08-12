from sympy import sympify, symbols


def evaluate(function, variable, value):
    x = symbols(variable)
    new_value = sympify(function).subs(x, value)
    return new_value
