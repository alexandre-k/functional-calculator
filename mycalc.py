"""Calculator."""
import operator
import string
from typing import Dict, Callable, Tuple, Union

Operator = str
Operand = int
Computation = int
OPERATORS = Dict[Operator, Callable]
IO = Union[None]


def operators() -> OPERATORS:
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
        if any(digit not in string.digits for digit in val):
            print('Not a number!!')
            continue
        if val == 0:
            print('In the name of God, I disallow the use of 0.')
            continue
        return int(val)


def enter_op() -> Operator:
    """Input an operator."""
    while True:
        input_operator = input(' operator > ')
        if input_operator not in operators():
            print('Not an operator!!')
            continue
        return input_operator


def calculate(vals: Tuple[int, int], input_operator: Operator) -> Computation:
    """Calculate the operations between 2 numbers."""
    return choose_operator(input_operator)(vals[0], vals[1])


def calculator(pos: int = 0, last_val: int = 0, last_op: str = '+') -> IO:
    """
    Implementation of a basic calculator. Only +, -, /, * are
    accepted.
    """
    val = enter_num()
    input_operator = enter_op()
    result = calculate((last_val, val), last_op)
    if input_operator != '=':
        if pos > 0:
            print('[{0}] > {1} {2} {3} = {4}'.format(
                pos, last_val, last_op, val, result))
        pos += 1
        calculator(pos, last_val=result, last_op=input_operator)
    else:
        print('[{0}] > {1} {2} {3} = {4}'.format(
            pos, last_val, last_op, val, result))


if __name__ == '__main__':
    try:
        calculator()
    except KeyboardInterrupt:
        print('\nSee you my friend!')
