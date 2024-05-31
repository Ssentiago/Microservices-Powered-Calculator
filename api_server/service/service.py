from decimal import Decimal

import sympy
from latex2sympy2 import latex2sympy

async def calculate_expression(expression):
    expression = expression.replace("÷", "/").replace("×", "*")
    result = latex2sympy(expression).evalf()
    return normalize_result(result)


def normalize_result(n: float):
    if all(x == '0' for x in str(n).split('.')[-1]):
        return str(int(n))
    return str(round(n, 2))


