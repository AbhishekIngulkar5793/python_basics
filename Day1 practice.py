Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #Identifier
>>> 12
12
>>> # 12 is an object
>>> a = 12
>>> a
12
>>> # a is an identifier
>>> b=23.44
>>> b
23.44
>>> c="abhishek"
>>> c
'abhishek'
>>> a
12
>>> b
23.44
>>> c
'abhishek'
>>> # if u want to check what u have in your memory??
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'b', 'c']
>>> # identifiers are also known as variable
>>> # variable: whose value changes from object to object
>>> a
12
>>> x=12
>>> x
12
>>> a
12
>>> a=20
>>> a
20
>>> # rules for declaring an identifiers
>>> #1. Characters+words are allowed
>>> a
20
>>> x
12
>>> bank='SBI'
>>> bank
'SBI'
>>> name='Abhishek'
>>> name
'Abhishek'
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'b', 'bank', 'c', 'name', 'x']
>>> #2. _ underscore is a valid identifier
>>> _=450
>>> _
450
>>> #3. space is not allowed
>>> bank ifsc = 'SBI1234'
SyntaxError: invalid syntax
>>> bank_ifsc = 'SBI1234'
>>> bank_ifsc
'SBI1234'
>>> #########################
>>> #4. special symbols and characters are not allowed
>>> # !@#$%^&*() etc.
>>> $ = 'python'
SyntaxError: invalid syntax
>>> n@me = 'shyam'
SyntaxError: can't assign to operator
>>> a%b = 'sample'
SyntaxError: can't assign to operator
>>> ##################
>>> #5. number as a preffix is not allowed
>>> 3a = 45
SyntaxError: invalid syntax
>>> 5v = 'java'
SyntaxError: invalid syntax
>>> #6. number as a suffix allowed
>>> a3 = 45
>>> a3
45
>>> a_3
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    a_3
NameError: name 'a_3' is not defined
>>> a_3 = 45
>>> a_3
45
>>> #############################
>>> 12 = 100
SyntaxError: can't assign to literal
>>> # numbers are not a valid identifiers
>>> #####################
>>> 'tanvi'
'tanvi'
>>> "tanvi"
'tanvi'
>>> # x[identifier]'x'[string object]
>>> r12 = 'java'
>>> r12
'java'
>>> ######################
>>> # python is case sensitive
>>> m = 120
>>> m
120
>>> M = 340
>>> M
340
>>> m
120
>>> M
340
>>> py = 'python'
>>> Py = 'Python'
>>> py
'python'
>>> Py
'Python'
>>> ABC123
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    ABC123
NameError: name 'ABC123' is not defined
>>> 'ABC123'
'ABC123'
>>> # objects are directly available
>>> 10
10
>>> -2
-2
>>> 23.44
23.44
>>> 5+6j
(5+6j)
>>> 7t+4k
SyntaxError: invalid syntax
>>> 7t+4
SyntaxError: invalid syntax
>>> t7+4k
SyntaxError: invalid syntax
>>> t7+4
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    t7+4
NameError: name 't7' is not defined
>>> 'hello'
'hello'
>>> [12,3,4,5,6,7]
[12, 3, 4, 5, 6, 7]
>>> #################
>>> #operators
>>> #arithmatic
>>> # + - * / % // **
>>> 12+30
42
>>> 32-10
22
>>> 4*5
20
>>> 5/2
2.5
>>> # floor division
>>> 5//2
2
>>> 10/3
3.3333333333333335
>>> 10//3
3
>>> # interesting part
>>> # interesting fact
>>> type(10/2)
<class 'float'>
>>> type(10//2)
<class 'int'>
>>> # what is the difference between division and floor division?
>>> # / vs //
>>> #------------
>>> # exponential/power of operator
>>> # used for square,cube
>>> 4**2
16
>>> 3**3
27
>>> # num ** power
>>> 
