Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #### DAY 14 ABHISHEK INGULKAR PRACTICE SESSION ######
>>> []
[]
>>> k = [10,20,30,40,50]
>>> k
[10, 20, 30, 40, 50]
>>> # insert
>>> help(k.insert)
Help on built-in function insert:

insert(index, object, /) method of builtins.list instance
    Insert object before index.

>>> k
[10, 20, 30, 40, 50]
>>> # ADD 100 BETWEEN 10,20
>>> k.insert(1,100)
>>> k
[10, 100, 20, 30, 40, 50]
>>> # ADD 0 AT START
>>> k
[10, 100, 20, 30, 40, 50]
>>> # +ve index of 10
>>> k[0]
10
>>> k[-6]
10
>>> 
>>> k.insert(0,0)
>>> k
[0, 10, 100, 20, 30, 40, 50]
>>> len(k)
7
>>> # ADD 1000 AFTER 500
>>> # ABOVE COMMENT IS WRONG
>>> # ADD 500 AFTER 50
>>> k.insert(-1,500)
>>> k
[0, 10, 100, 20, 30, 40, 500, 50]
>>> k.remove(500)
>>> k
[0, 10, 100, 20, 30, 40, 50]
>>> k.insert(7,500)
>>> k
[0, 10, 100, 20, 30, 40, 50, 500]
>>> OR
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    OR
NameError: name 'OR' is not defined
>>> k.append(500)
>>> k
[0, 10, 100, 20, 30, 40, 50, 500, 500]
>>> k.remove(500)
>>> k
[0, 10, 100, 20, 30, 40, 50, 500]
>>> k
[0, 10, 100, 20, 30, 40, 50, 500]
>>> # ADD 1000 AFTER 500
>>> # BUT USING INSERT FUNCTION ONLY
>>> k.insert(8,1000)
>>> k
[0, 10, 100, 20, 30, 40, 50, 500, 1000]
>>> len(k)
9
>>> len(k)+1
10
>>> k.insert(len(k)+1,'abhishek')
>>> k
[0, 10, 100, 20, 30, 40, 50, 500, 1000, 'abhishek']
>>> #------------------------------------------------
>>> s1 = {1,2,3}
>>> s1
{1, 2, 3}
>>> s2 = {2,3,4,5}
>>> s1 + s2
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    s1 + s2
TypeError: unsupported operand type(s) for +: 'set' and 'set'
>>> s1 - s2
{1}
>>> s1
{1, 2, 3}
>>> s2
{2, 3, 4, 5}
>>> s1 | s2
{1, 2, 3, 4, 5}
>>> # union
>>> s1.union(s2)
{1, 2, 3, 4, 5}
>>> # now for difference
>>> s1
{1, 2, 3}
>>> s2
{2, 3, 4, 5}
>>> s1.difference(s2)
{1}
>>> s1 - s2
{1}
>>> # now for uncommon elements
>>> s1 & s2
{2, 3}
>>> s1.intersection(s2)
{2, 3}
>>> # now for symmetric difference
>>> s1.symmetric_difference(s2)
{1, 4, 5}
>>> s1 ^ s2
{1, 4, 5}
>>> #--------------------------------------
>>> a = 'AbhiSHEk'
>>> a
'AbhiSHEk'
>>> # lower()
>>> a.lower()
'abhishek'
>>> # upper()
>>> a.upper()
'ABHISHEK'
>>> # casefold()
>>> a.casefold()
'abhishek'
>>> # lower() and casefold() both do same things except: 1.lower()-supports ASCII & 2.casefold()- spports unicode.
>>> #----------------------
>>> # Bytes
>>> bytes[10,20,30]
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    bytes[10,20,30]
TypeError: 'type' object is not subscriptable
>>> bytes([10,20,30])
b'\n\x14\x1e'
>>> b1 = bytes([10,20,30])
>>> b1[0]
10
>>> b1[3]
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    b1[3]
IndexError: index out of range
>>> b1[2]
30
>>> bytes([10,20,255])
b'\n\x14\xff'
>>> # bytes has limiting range upto 255 only at 256 it will give range error
>>> b1
b'\n\x14\x1e'
>>> bytes([20,40,256])
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    bytes([20,40,256])
ValueError: bytes must be in range(0, 256)
>>> b1
b'\n\x14\x1e'
>>> b1[0]
10
>>> b1[0] = 23
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    b1[0] = 23
TypeError: 'bytes' object does not support item assignment
>>> # bytes is immutable which means we cant make any changes with same object
>>> dir(b1)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'center', 'count', 'decode', 'endswith', 'expandtabs', 'find', 'fromhex', 'hex', 'index', 'isalnum', 'isalpha', 'isascii', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> #-----------------------
>>> # bytearray()
>>> b2 = bytearray([10,20,30])
>>> b2
bytearray(b'\n\x14\x1e')
>>> bytearray([10,20,256])
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    bytearray([10,20,256])
ValueError: byte must be in range(0, 256)
>>> b2
bytearray(b'\n\x14\x1e')
>>> b2[0]
10
>>> b2[0] = 11
>>> b2
bytearray(b'\x0b\x14\x1e')
>>> b2[0]
11
>>> # in bytearray assignment operations are possible that means byteaaray is mutable in nature
>>> dir(b2)
['__add__', '__alloc__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'capitalize', 'center', 'clear', 'copy', 'count', 'decode', 'endswith', 'expandtabs', 'extend', 'find', 'fromhex', 'hex', 'index', 'insert', 'isalnum', 'isalpha', 'isascii', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'pop', 'remove', 'replace', 'reverse', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> #----------------------
>>> # set is mutable in nature whereas,
>>> # frozenset is immutable in nature
>>> f = frozenset({10,20,30})
>>> f
frozenset({10, 20, 30})
>>> dir(f)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'copy', 'difference', 'intersection', 'isdisjoint', 'issubset', 'issuperset', 'symmetric_difference', 'union']
>>> # differentiate between set and frozenset?
>>> #---------------------------
>>> # differentiate between sort and sorted ?
>>> # sort is method of list\
>>> # sorted is a built in function of python
>>> d = [99,120,34,2,14,0]
>>> d
[99, 120, 34, 2, 14, 0]
>>> d.sort() # for asending order by default with taking any argument it returns ascending order.
>>> d
[0, 2, 14, 34, 99, 120]
>>> d.sort(reverse = True)
>>> d
[120, 99, 34, 14, 2, 0]
>>> # now if we put in argument reverse=True. then it is sorting the list in desending order.
>>> d
[120, 99, 34, 14, 2, 0]
>>> sorted(d)
[0, 2, 14, 34, 99, 120]
>>> d
[120, 99, 34, 14, 2, 0]
>>> # sorted() is temporary operation ie it is not an inplace operation
>>> d
[120, 99, 34, 14, 2, 0]
>>> sorted(reverse=True)
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    sorted(reverse=True)
TypeError: sorted expected 1 arguments, got 0
>>> sorted(d(reverse=True))
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    sorted(d(reverse=True))
TypeError: 'list' object is not callable
>>> sorted(d,reverse=True)
[120, 99, 34, 14, 2, 0]
>>> d
[120, 99, 34, 14, 2, 0]
>>> # -------------------------
>>> # key in sort
>>> n = ['prajwalita','reva','sumit','abhishek','akshay','vicky']
>>> n
['prajwalita', 'reva', 'sumit', 'abhishek', 'akshay', 'vicky']
>>> # list of string we have
>>> # will go with sorted as it is giving temporary output
>>> sorted(n)
['abhishek', 'akshay', 'prajwalita', 'reva', 'sumit', 'vicky']
>>> # it sorts in Alphabetical order
>>> n
['prajwalita', 'reva', 'sumit', 'abhishek', 'akshay', 'vicky']
>>> # now, sort the list n, as per the length ?
>>> # names with minimum length will be first and then progress with maximum lengths of names.
>>> sorted(n,key=len)
['reva', 'sumit', 'vicky', 'akshay', 'abhishek', 'prajwalita']
>>> sorted(n,key=len,reverse=True)
['prajwalita', 'abhishek', 'akshay', 'sumit', 'vicky', 'reva']
>>> sorted(n,key=len)[::-1]
['prajwalita', 'abhishek', 'akshay', 'vicky', 'sumit', 'reva']
>>> ####################### DAY 14 PRECTICE SESSION ENDS##########
>>> 
