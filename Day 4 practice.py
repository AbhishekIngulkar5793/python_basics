Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> id(12)
140712435963264
>>> id(12.0)
1866989485056
>>> a = 12
>>> id(a)
140712435963264
>>> #-----------------------
>>> print()

>>> help(print)
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.

>>> help(print())

Help on NoneType object:

class NoneType(object)
 |  Methods defined here:
 |  
 |  __bool__(self, /)
 |      self != 0
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.

>>> help(id)
Help on built-in function id in module builtins:

id(obj, /)
    Return the identity of an object.
    
    This is guaranteed to be unique among simultaneously existing objects.
    (CPython uses the object's memory address.)

>>> help(id())
     
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    help(id())
TypeError: id() takes exactly one argument (0 given)
>>> #---------------------------
     
>>> # type casting
     
>>> # type conversion
     
>>> # converting a data from one type to other
     
>>> a
     
12
>>> # convert a into a str
     
>>> str(a)
     
'12'
>>> type(a)
     
<class 'int'>
>>> a
     
12
>>> num = '23234'
     
>>> num
     
'23234'
>>> type(num)
     
<class 'str'>
>>> # convert num to float
     
>>> float(num)
     
23234.0
>>> # 2 types
     
>>> # 1. implicit conversion
     
>>> # 2. explicit conversion
     
>>> # A conversion performed by the python itself
     
>>> 10 + 20
     
30
>>> 10 + 20.
     
30.0
>>> 10/2
     
5.0
>>> #2. explicit conversion
     
>>> # a conversion performed by user as per requirement
     
>>> int(10+20)
     
30
>>> int(10+20.)
     
30
>>> num
     
'23234'
>>> # convert num into complex format
     
>>> complex(num)
     
(23234+0j)
>>> type(num)
     
<class 'str'>
>>> num = float(num)
     
>>> num
     
23234.0
>>> type(num)
     
<class 'float'>
>>> rate + 10
     
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    rate + 10
NameError: name 'rate' is not defined
>>> rate = 10
     
>>> rate
     
10
>>> qty = input('enter your quantity:')
     
enter your quantity:5
>>> qty
     
'5'
>>> # final bill
     
>>> rate * qty
     
'5555555555'
>>> # in the above case it is performing repetition
     
>>> rate * int(qty)
     
50
>>> #=-----------------------
     
>>> # number system:
     
>>> # binary [0,1]- base 2
     
>>> # octal [0,7]- base 8
     
>>> # decimal [0-9] - base 10
     
>>> # hexa decimal [0-9A-F]
     
>>> # default number system we have is decimal
     
>>> n= 100
     
>>> n
     
100
>>> # decimal to other number system conversion
     
>>> bin(n)
     
'0b1100100'
>>> bin(15)
     
'0b1111'
>>> help(bin)
     
Help on built-in function bin in module builtins:

bin(number, /)
    Return the binary representation of an integer.
    
    >>> bin(2796202)
    '0b1010101010101010101010'

>>> # octal
     
>>> oct(n)1
     
SyntaxError: invalid syntax
>>> oct(n)
     
'0o144'
>>> oct(9)
     
'0o11'
>>> bin(12.33)
     
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    bin(12.33)
TypeError: 'float' object cannot be interpreted as an integer
>>> bin(15)
     
'0b1111'
>>> bin(16)
     
'0b10000'
>>> oct('0b1111')
     
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    oct('0b1111')
TypeError: 'str' object cannot be interpreted as an integer
>>> 0b1111
     
15
>>> 0o11
     
9
>>> oct(0b1111)
     
'0o17'
>>> # hex
     
>>> n
     
100
>>> hex(n)
     
'0x64'
>>> 0x64
     
100
>>> 0o23
     
19
>>> 0O23
     
19
>>> #-----------------------
     
>>> # we can not use reserved words as in identifiers
     
>>> # keywords are reserved words in python
     
>>> impor keyword
     
SyntaxError: invalid syntax
>>> import keyword
     
>>> keyword.kwlist
     
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> in = 500
     
SyntaxError: invalid syntax
>>> or + '
     
SyntaxError: invalid syntax
>>> or = 'python'
     
SyntaxError: invalid syntax
>>> #---------------
     
>>> print = 10
     
>>> print
     
10
>>> id = 900
     
>>> id
     
900
>>> print()
     
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    print()
TypeError: 'int' object is not callable
>>> print100()
     
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    print100()
NameError: name 'print100' is not defined
>>> print(100)
     
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    print(100)
TypeError: 'int' object is not callable
>>> print(100)
     
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    print(100)
TypeError: 'int' object is not callable
>>> type(print)
     
<class 'int'>
>>> type(id)
     
<class 'int'>
>>> id(100)
     
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    id(100)
TypeError: 'int' object is not callable
>>> TypeError: 'int' object is not callable
     
SyntaxError: invalid syntax
>>> 
     
>>> 
     
>>> #---------END---- FIFTH SESSION------------ 1.9.22 THURSDAY--------
     
>>> 
