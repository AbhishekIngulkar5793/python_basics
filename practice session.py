Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # python features
>>> # Identifiers and their rules
>>> # Operators in the python
>>> 
>>> # Features
>>> # 1 easy to code
>>> 
>>> # 2 open source
>>> # 3 OOP
>>> # 4 python is case sensitive
>>> # 5 Dynamic typed language
>>> a = 100
>>> a
100
>>> type(a)
<class 'int'>
>>> b = 1.5
>>> b
1.5
>>> type(b)
<class 'float'>
>>> 
>>> #-------------------
>>> # Identifiers
>>> 

>>> 
>>> a
100
>>> # here a is our identifier and 100 is our object
>>> 
>>> b = 'abhi'
>>> b
'abhi'
>>> sample = 'python'
>>> sample = 'python'
>>> sample
'python'
>>> id(sample)
1457698236936
>>> # rule 2
>>> # @ # $ % ^ &
>>> @ = 100
SyntaxError: invalid syntax
>>> # rule 3
>>> 10 = 'py'
SyntaxError: can't assign to literal
>>> # rule 4
>>> info sample = 500
SyntaxError: invalid syntax
>>> info
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    info
NameError: name 'info' is not defined
>>> info_sample = 500
>>> # number as a prefix is not allowed
>>> 10a = 500
SyntaxError: invalid syntax
>>> a_10 = 'abhishek'
>>> # we cannot assign keyword as a identifier
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> 
>>> 
>>> False = 'oop'
SyntaxError: can't assign to keyword
>>> # operators in python
>>> # 1 arithmatic
>>> # 2 logical
>>> # 3 assignment
>>> # 4 relational / conditional
>>> # membership
>>> 
>>> # 6 identity operator
>>> # logical operator
>>> 
>>> # Arithmatic +,-,*,/,//
>>> 10 + 20
30
>>> 'abhi' + 'shek'
'abhishek'
>>> 'abhi' + 18
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    'abhi' + 18
TypeError: can only concatenate str (not "int") to str
>>> 10 - 5
5
>>> 45 / 6
7.5
>>> 45 // 6
7
>>> 'abhi' - 'shek'
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    'abhi' - 'shek'
TypeError: unsupported operand type(s) for -: 'str' and 'str'
>>> 5 * 5
25
>>> 8 * 5
40
>>> 25 / 5
5.0
>>> 25 // 5
5
>>> 27 // 8
3
>>> 
>>>  45 % 5
SyntaxError: unexpected indent
>>> 
4
>>> 5
5
>>> 45 % 5
0
>>> 12 % 5
2
>>>  27
SyntaxError: unexpected indent
>>> 27 % 5
2
>>> 'ceil'
'ceil'
>>> 2**2
4
>>> 25**4
390625
>>> # Assignment operator
>>> # =,+=,-=,*=,/=
>>> a = 10
>>> a
10
>>> a + 10
20
>>> a
10
>>> a += 10
>>> a
20
>>> a - 5
15
>>> a
20
>>> a -= 5
>>> a
15
>>> a * 2
30
>>> a *= 2
>>> a
30
>>> a / 5
6.0
>>> a /= 5
>>> a
6.0
>>> # Relational operator
>>> # <,>,<=,>=,==,!=
>>> a
6.0
>>> a < 2
False
>>> a > 2
True
>>> a < 8
True
>>> a > 5
True
>>> a < 5
False
>>> a > 2
True
>>> a
6.0
>>> a <= 6.0
True
>>> a >= 6.0
True
>>> a != 6.0
False
>>> a != 7
True
>>> # Membership operators: in, not in
>>> li = [1,2,3,4]
>>> 5 in li
False
>>> 4 in li
True
>>> 5 not in li
True
>>> 10 not in li
True
>>> 2 in li
True
>>> 2 not in li
False
>>> s = 'shreyal'
>>> i in s
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    i in s
NameError: name 'i' is not defined
>>> 'i' in s
False
>>> 'h' in s
True
>>> 'yal' in s
True
>>> 'Shre' not in s
True
>>> # Identity operator
>>> id(s)
1457698855096
>>> # is , is not
>>> 12 is 12
True
>>> 12 is not 13
True
>>> 12 is 12.0
False
>>> 12 == 12.0
True
>>> id(12)
140712437798272
>>> id(12.0)
1457658575992
\
>>> 
>>> # why 12 == 12.0--True
>>> # and 12 is 12.0----false
>>> # == content equality
>>> # is address equality
>>> 12 is not 12.0
True
>>> # Logical operator
>>> # and , or , not
>>> # 0 0
>>> # 0 1
>>> # 1 0
>>> # 1 1
>>> # and
>>> # 0=false
>>> # 1=true
>>> 0 * 0
0
>>> x = 20
>>> y = 10
>>> x==20 and y==10
True
>>> x == 20
True
>>> y == 10
True
>>> x == 20 and y == 5
False
>>> x == 20 and y == 10.0
True
>>> z = 50
>>> x == 20 and y != 5 and z == 50
True
>>> x == 25 and y == 30 and z == 50
False
>>> #-----------------------
>>> # or
>>> # 0 0 = 0
>>> # 0 1 = 1
>>> # 1 0 = 1
>>> # 1 1 = 1
>>> x == 25 or y == 30 or z == 50
True
>>> x != 20 or y == 50
False
>>> x == 20 and y == 25 or z == 30
False
>>> #----------------
>>> 27/5
5.4
>>> 27%5
2
>>> not x == 20
False
>>> not True
False
>>> not False
True
>>> # Type casting in python
>>> # 1 implicit
>>> # 2 explicit
>>> 5 + 2.5
7.5
>>> 12 / 2
6.0
>>> a = 5.00
>>> a
5.0
>>> int(a)
5
>>> 12,45,85
(12, 45, 85)
>>> t = 12,45,85
>>> t
(12, 45, 85)
>>> type(t)
<class 'tuple'>
>>> [t]
[(12, 45, 85)]
>>> list(t)
[12, 45, 85]
>>> t
(12, 45, 85)
>>> type(t)
<class 'tuple'>
>>> #---------------END---------- GUEST LECTURE SESSION PRACTICE--------
