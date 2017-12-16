import operator
import string
from typing import Dict, Callable, Tuple, Union

Operator = str
Operand = int
Computation = int
Operators = Dict[Operator, Callable]
IO = Union[None]


def operators() -> Operators:
    """Mapping of symbols and operators."""
    return {
        '+': operator.add,
        '-': operator.sub,
        '/': operator.truediv,
        '*': operator.mul,
        '=': calculate
    }

def choose_operator(symbol: str) -> Callable:
    """Get correct operator depending on a symbol (e.g., +, *)."""
    strategy = operators()
    return strategy[symbol]


def enter_num() -> Operand:
    """Input a number."""
    while True:
        val = input(' operand  > ')
        if any(not digit in string.digits for digit in val):
            print('Not a number!!')
            continue
        return int(val)


def enter_op() -> Operator:
    """Input an operator."""
    while True:
        op = input(' operator > ')
        if not op in operators():
            print('Not an operator!!')
            continue
        return op


def calculate(vals : Tuple[int, int], op: Operator) -> Computation:
    """Calculate the operations between 2 numbers."""
    return choose_operator(op)(vals[0], vals[1])


def calculator(pos: int=0, last_val: int=0, last_op: str='+') -> IO:
    """
    Implementation of a basic calculator. Only +, -, /, * are
    accepted.
    """
    val = enter_num()
    op = enter_op()
    result = calculate((last_val, val), last_op)
    if op != '=':
        if pos > 0:
            print('[{0}] > {1} {2} {3} = {4}'.format(
                    pos, last_val, last_op, val, result))
        pos += 1
        calculator(pos, last_val=result, last_op=op)
    else:
        print('[{0}] > {1} {2} {3} = {4}'.format(
                pos, last_val, last_op, val, result))

if __name__ == '__main__':
    try:
       calculator()
    except KeyboardInterrupt:
        print('\nSee you my friend!')
