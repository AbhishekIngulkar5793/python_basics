Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # ABHISHEK INGULKAR 7TH SESSION PRACTICE 8.9.22
>>> # THURSDAY
>>> s = 'python'
>>> s
'python'
>>> dir(s)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> 
s
>>> s
'python'
>>> s
'python'
>>> s = 'I love my India'
>>> s
'I love my India'
>>> # startswith()
>>> s.startswith('i')
False
>>> s.startswith('I')
True
>>> s.startswith('I love my India')
True
>>> s.startswith('dia')
False
>>> # endswith()
>>> s.endswith('dia')
True
>>> s.endswith('I love my India')
True
>>> s.endswith('XYZ')
False
>>> #-------------------------------------------
>>> x = 'abe'
>>> x
'abe'
>>> x.isalpha()
True
>>> x = '123xyz'
>>> x
'123xyz'
>>> x.isalpha()
False
>>> x.isalnum()
True
>>> x = '       '
>>> x
'       '
>>> x.isidentifier()
False
>>> x= '_'
>>> x.isidentifier()
True
>>> x = 'and'
>>> x.isidentifier()
True
>>> x = 'in'
>>> x.isidentifier()
True
>>> x = '#$'
>>> x.isidentifier()
False
>>> #---------------------
>>> # LIST
>>> # syntax: []
>>> []
[]
>>> type[]
SyntaxError: invalid syntax
>>> type([])
<class 'list'>
>>> # Features of a list
>>> k = [10,20,30,40,50]
>>> k
[10, 20, 30, 40, 50]
>>> type(k)
<class 'list'>
>>> # 1.Background data structure of an list is an array
>>> # 2. Indexing is possible in a list : +ve, -ve
>>> k
[10, 20, 30, 40, 50]
>>> k[2]
30
>>> k[-1]
50
>>> k[4]
50
>>> k[5]
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    k[5]
IndexError: list index out of range
>>> k[-3]
30
>>> # 3. It accepts homogeneous as well as hetrogeneous values
>>> k
[10, 20, 30, 40, 50]
>>> type(k[0])
<class 'int'>
>>> j = [12,45.67,'py',(4+5j)]
>>> j
[12, 45.67, 'py', (4+5j)]
>>> #--------------------
>>> # 4. Slicing is supported in a list
>>> k
[10, 20, 30, 40, 50]
>>> k[:]
[10, 20, 30, 40, 50]
>>> k[1:4]
[20, 30, 40]
>>> k[1:5]
[20, 30, 40, 50]
>>> k[-1:-5]
[]
>>> k[-1:]
[50]
>>> k[-1:-4]
[]
>>> k[-1:]
[50]
>>> k[-4:]
[20, 30, 40, 50]
>>> k[:-4]
[10]
>>> k[:-5]
[]
>>> h = ['ramesh','suresh','dinesh']
>>> h
['ramesh', 'suresh', 'dinesh']
>>> h[1:]
['suresh', 'dinesh']
>>> h[:1]
['ramesh']
>>> h[0]
'ramesh'
>>> h[-1][

	\

h
h
SyntaxError: invalid syntax
>>> h
['ramesh', 'suresh', 'dinesh']
>>> h[:-1]
['ramesh', 'suresh']
>>> #-------------------------
>>> k
[10, 20, 30, 40, 50]
>>> k[2]
30
>>> k[5]
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    k[5]
IndexError: list index out of range
>>> type(k)
<class 'list'>
>>> type(k[2])
<class 'int'>
>>> type(k)
<class 'list'>
>>> #------------------------
>>> # It preserves sequence order
>>> k
[10, 20, 30, 40, 50]
>>> h
['ramesh', 'suresh', 'dinesh']
>>> # It means it gives output in same order as that of given by us
>>> # There is one data structure in python who does not preserve sequence order
>>> # Its name is 'set'
>>> d = {'ramesh','suresh','dinesh'}
>>> d
{'ramesh', 'dinesh', 'suresh'}
>>> a = {0,9,8,7,6,5,4,3,2,1}
>>> a
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
>>> a = {1,2,3,4,5,6,7,8,9,0}
>>> a
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
>>> #=----------------
>>> # In list duplicates area allowed
>>> a = [1,2,3,1,2,2,3,1,2,3,1,1,1,2,3]
>>> a
[1, 2, 3, 1, 2, 2, 3, 1, 2, 3, 1, 1, 1, 2, 3]
>>> # But in a set duplicates are not allowed
>>> a ={1,2,3,1,2,3,1,1,2,3,3,1,2,3,1,2,3}
>>> a
{1, 2, 3}
>>> #-------------------
>>> #Q. Explain a list./ What are the different features of a list?
>>> # -------------------
>>> # 6. List is mutable in nature
>>> # Mutable: it means that if we are changing a data within a list, so changes will be performed in same object. Technically we call this process as a 'mutable'
>>> k
[10, 20, 30, 40, 50]
>>> # acccess 50
>>> k[4]
50
>>> # now check id
>>> id(k)
2539353937736
>>> # now perform changes in k
>>> k[4]
50
>>> k[4] = 500
>>> k
[10, 20, 30, 40, 500]
>>> id(k)
2539353937736
>>> # As we have seen above ,before and after changes we have the same id for k, such type of data structures are known as Mutable.
>>> # Changes performed are permanant
>>> k
[10, 20, 30, 40, 500]
>>> # Example : covid19
>>> c19 = ['alpha']
>>> id(c19)
2539353938056
>>> c19
['alpha']
>>> c19 = ['delta']
>>> c19
['delta']
>>> id(c19)
2539358750408
>>> c19
['delta']
>>> c19[0]
'delta'
>>> c19[0] = 'delta'
>>> c19[0] = 'alpha'
>>> c19
['alpha']
>>> id(c19)
2539358750408
>>> c19[0]
'alpha'
>>> c19[0] = 'omicron'
>>> c19
['omicron']
>>> id(c19)
2539358750408
>>> #-------------------
>>> k
[10, 20, 30, 40, 500]
>>> id(k)
2539353937736
>>> # clear() : It flushes out (removes) all elements in a list
>>> # k will be empty after applying clear()
>>> k.clear()
>>> k
[]
>>> id(k)
2539353937736
>>> #------------------------
>>> # Methods supported by a list
>>> k
[]
>>> # to add element we have two options
\
>>> # 1. append() and 2. extend(): both adds elements at the end
>>> k
[]
>>> k.append(100)
>>> k
[100]
>>> k.extend(100)
Traceback (most recent call last):
  File "<pyshell#167>", line 1, in <module>
    k.extend(100)
TypeError: 'int' object is not iterable
>>> k.append('java')
>>> k
[100, 'java']
>>> k.extend('java')
>>> k
[100, 'java', 'j', 'a', 'v', 'a']
>>> # if we want to add more number of elements
>>> k
[100, 'java', 'j', 'a', 'v', 'a']
>>> # instead of using append() use extend() for same example
>>> k.append(1,2,3)
Traceback (most recent call last):
  File "<pyshell#175>", line 1, in <module>
    k.append(1,2,3)
TypeError: append() takes exactly one argument (3 given)
>>> k.append(1)
>>> k
[100, 'java', 'j', 'a', 'v', 'a', 1]
>>> k.append('abhishek')
>>> k
[100, 'java', 'j', 'a', 'v', 'a', 1, 'abhishek']
>>> k.extend('abhishek')
>>> k
[100, 'java', 'j', 'a', 'v', 'a', 1, 'abhishek', 'a', 'b', 'h', 'i', 's', 'h', 'e', 'k']
>>> k.extend(992100)
Traceback (most recent call last):
  File "<pyshell#182>", line 1, in <module>
    k.extend(992100)
TypeError: 'int' object is not iterable
>>> k.extend('992100')
>>> k
[100, 'java', 'j', 'a', 'v', 'a', 1, 'abhishek', 'a', 'b', 'h', 'i', 's', 'h', 'e', 'k', '9', '9', '2', '1', '0', '0']
>>> #---------------------
>>> p = []
>>> p
[]
>>> p.extend('abhishek')
>>> p
['a', 'b', 'h', 'i', 's', 'h', 'e', 'k']
>>> p.append('abhishek')
>>> p
['a', 'b', 'h', 'i', 's', 'h', 'e', 'k', 'abhishek']
>>> # append: add object as it is.
>>> # extend: add each elements from the object
>>> p
['a', 'b', 'h', 'i', 's', 'h', 'e', 'k', 'abhishek']
>>> p.append([10,20,30])
>>> p
['a', 'b', 'h', 'i', 's', 'h', 'e', 'k', 'abhishek', [10, 20, 30]]
>>> help(p.append)
Help on built-in function append:

append(object, /) method of builtins.list instance
    Append object to the end of the list.

>>> help(p.extend)
Help on built-in function extend:

extend(iterable, /) method of builtins.list instance
    Extend list by appending elements from the iterable.

>>> # What is an iterable ?
>>> # Iterable means collection of elements
>>> # example: list,string
>>> x = 50000
>>> x
50000
>>> x[0]
Traceback (most recent call last):
  File "<pyshell#204>", line 1, in <module>
    x[0]
TypeError: 'int' object is not subscriptable
>>> x = '50000'
>>> x[0]
'5'
>>> 50000
50000
>>> '50000'
'50000'
>>> # -------------------
>>> dir(k)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> dir(list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> # Suppose if we want to take multiple elements as an input from the user
>>> # use eval()
>>> eval(input('enter numbers:'))
enter numbers:12,13,14,15,16,17,18
(12, 13, 14, 15, 16, 17, 18)
>>> #------ABHISHEK INGULKAR SEVENTH SESSION PRACTICE END---8.9.22:THURSDAY
