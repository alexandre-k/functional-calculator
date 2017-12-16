# Functional calculator

## Overview

This is a calculator written in Python. It is written in a functional style,
inspired by Haskell for the type IO, which represents the IO monad for side effects.

The operators are only the basic ones, +, -, /, *.

The program is used as my answer for an assignment in a CS course at
the University of People.

## Sample output:

With the addition operator:
```
$ python mycalc.py
 operand  > 10
 operator > +
 operand  > 345
 operator > =
[1] > 10 + 345 = 355
```

With the multiplication operator:
```
$ python mycalc.py
 operand  > 12
 operator > *
 operand  > 54
 operator > =
[1] > 12 * 54 = 648
```

With successive operations:
```
$ python mycalc.py
 operand  > 16
 operator > -
 operand  > 2
 operator > *
[1] > 16 - 2 = 14
 operand  > 66
 operator > +
[2] > 14 * 66 = 924
 operand  > 12
 operator > / 
[3] > 924 + 12 = 936
 operand  > 5
 operator > =
[4] > 936 / 5 = 187.2
```
