Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #ABHISHEK INGULKAR DAY 10 PRACTICE - SET 16/9/22
>>> 
>>> # set
>>> # syntax
>>> s = {()}
>>> d = {}
>>> type(s)
<class 'set'>
>>> type(d)
<class 'dict'>
>>> s = set()
>>> type(s)
<class 'set'>
>>> # properties of a set
>>> # it does not preserve sequence order
>>> # indexing and slicing is not allowed in a set
>>> # duplicate elements are not allowed in a set
>>> # background data structure of a set is hash table
>>> s = {25,40,85,89,25}
>>> s
{40, 25, 85, 89}
>>> s
{40, 25, 85, 89}
>>> s = {25,40,85,89,50}
>>> s
{89, 40, 50, 85, 25}
>>> s
{89, 40, 50, 85, 25}
>>> s[0]
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    s[0]
TypeError: 'set' object does not support indexing
s
>>> s
{89, 40, 50, 85, 25}
>>> # hash function
>>> # % - mod function
>>> \


    
>>> 
>>> 50%10
0
>>> 80%10
0
>>> 87%1p0
SyntaxError: invalid syntax
>>> 87%10
7
>>> 45%10
5
>>> 23.3%10
3.3000000000000007
>>> s[:]
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    s[:]
TypeError: 'set' object is not subscriptable
>>> s
{89, 40, 50, 85, 25}
>>> s.add(50)
>>> s
{89, 40, 50, 85, 25}
>>> # duplicate elements are not allowed
>>> s.add(90)
>>> s
{89, 40, 50, 85, 25, 90}
>>> l = [5,4,7,5,4,8,10]
>>> l
[5, 4, 7, 5, 4, 8, 10]
>>> set(l)
{4, 5, 7, 8, 10}
>>> # methods of a set
>>> dir(set)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
>>> 
>>> # add()
>>> s.add(100)
>>> s
{89, 100, 40, 50, 85, 25, 90}
>>> l
[5, 4, 7, 5, 4, 8, 10]
>>> s.add(11,55)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    s.add(11,55)
TypeError: add() takes exactly one argument (2 given)
>>> s.add((12,45))
>>> s
{89, 100, 40, (12, 45), 50, 85, 25, 90}
>>> s.add(l)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    s.add(l)
TypeError: unhashable type: 'list'
>>> s.add('python')
>>> s
{89, 'python', 100, 40, (12, 45), 50, 85, 25, 90}
>>> ###############
>>> 
>>> # if i want to add (12,45) separately
>>> # update()
>>> help(s.update)
Help on built-in function update:

update(...) method of builtins.set instance
    Update a set with the union of itself and others.

>>> s
{89, 'python', 100, 40, (12, 45), 50, 85, 25, 90}
>>> s.update((12,45))
>>> S
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    S
NameError: name 'S' is not defined
>>> s
{89, 'python', 100, 40, (12, 45), 12, 45, 50, 85, 25, 90}
>>> # if i add already supplied values in set
>>> s.update((12,45))
>>> s
{89, 'python', 100, 40, (12, 45), 12, 45, 50, 85, 25, 90}
>>> s.update([11,20])
>>> s
{89, 'python', 100, 40, (12, 45), 11, 12, 45, 50, 20, 85, 25, 90}
>>> s
{89, 'python', 100, 40, (12, 45), 11, 12, 45, 50, 20, 85, 25, 90}
>>> s.update('datascience')
>>> s
{11, 12, 20, 'python', 25, 40, 45, 50, (12, 45), 'e', 'c', 'd', 's', 't', 85, 89, 90, 'n', 100, 'i', 'a'}
>>> ######################
>>> x = {'abhishek','reva','akshay','anisa'}
>>> x
{'akshay', 'anisa', 'reva', 'abhishek'}
>>> # discard()
>>> help(x.discard)
Help on built-in function discard:

discard(...) method of builtins.set instance
    Remove an element from a set if it is a member.
    
    If the element is not a member, do nothing.

>>> x.discard('reva')
>>> x
{'akshay', 'anisa', 'abhishek'}
>>> x.add('suraj')
>>> x
{'akshay', 'abhishek', 'anisa', 'suraj'}
>>> len(x)
4
>>> x.discard('akshay')
>>> x
{'abhishek', 'anisa', 'suraj'}
>>> len(x)
3
>>> x.discard('anisa','abhishek')
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    x.discard('anisa','abhishek')
TypeError: discard() takes exactly one argument (2 given)
>>> ########################
>>> 
>>> 
>>> # pop()
>>> help(x.pop)
Help on built-in function pop:

pop(...) method of builtins.set instance
    Remove and return an arbitrary set element.
    Raises KeyError if the set is empty.

>>> s
{11, 12, 20, 'python', 25, 40, 45, 50, (12, 45), 'e', 'c', 'd', 's', 't', 85, 89, 90, 'n', 100, 'i', 'a'}
>>> s.pop()
11
>>> # it removes arbitrary element and returns the removed element
>>> x
{'abhishek', 'anisa', 'suraj'}
>>> x.pop()
'abhishek'
>>> x
{'anisa', 'suraj'}
>>> # arbitrary means- first or last element
>>> x
{'anisa', 'suraj'}
>>> s
{12, 20, 'python', 25, 40, 45, 50, (12, 45), 'e', 'c', 'd', 's', 't', 85, 89, 90, 'n', 100, 'i', 'a'}
>>> s.pop()
12
>>> s.pop()
20
>>> s.pop(11)
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    s.pop(11)
TypeError: pop() takes no arguments (1 given)
>>> s.pop()
'python'
>>> s
{25, 40, 45, 50, (12, 45), 'e', 'c', 'd', 's', 't', 85, 89, 90, 'n', 100, 'i', 'a'}
>>> ###############################
>>> 
>>> 3
3
>>> 
>>> 

>>> 

>>> 
>>> # remove()
>>> help(s.remove)
Help on built-in function remove:

remove(...) method of builtins.set instance
    Remove an element from a set; it must be a member.
    
    If the element is not a member, raise a KeyError.

>>> s.remove(20)
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    s.remove(20)
KeyError: 20
>>> 20 in s
False
>>> # remove() - we have to supply argument
>>> s.remove()
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    s.remove()
TypeError: remove() takes exactly one argument (0 given)
>>> #
>>> # what is discard, pop, and remove??
>>> # differentiate them.
>>> # pop()- removes arbitrary elements, takes zero arguments
>>> # discard() - removes the element if it is present
>>> # remove() - remove element, if not present raise key error
>>> 
>>> d = set()
>>> d
set()
>>> d.pop()
Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    d.pop()
KeyError: 'pop from an empty set'
>>> d.discard(10)
>>> d
set()
>>> d.remove(10)
Traceback (most recent call last):
  File "<pyshell#134>", line 1, in <module>
    d.remove(10)
KeyError: 10
>>> dir(set)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
>>> s.remove(10,20)
Traceback (most recent call last):
  File "<pyshell#136>", line 1, in <module>
    s.remove(10,20)
TypeError: remove() takes exactly one argument (2 given)
>>> l
[5, 4, 7, 5, 4, 8, 10]
>>> # reverse is a method of list
>>> # reversed is a python function
>>> # reversed is applicable for str,tuple,list
>>> l.reverse()
>>> l
[10, 8, 4, 5, 7, 4, 5]
>>> reversed(l)
<list_reverseiterator object at 0x0000018FDFC83668>
>>> l
[10, 8, 4, 5, 7, 4, 5]
>>> l1= reversed(l)
>>> l1
<list_reverseiterator object at 0x0000018FDFC83668>
>>> list(reversed(l))
[5, 4, 7, 5, 4, 8, 10]
>>> # reverse is inplace
>>> # reversed is temporary
>>> help(__sizeof__)
Traceback (most recent call last):
  File "<pyshell#150>", line 1, in <module>
    help(__sizeof__)
NameError: name '__sizeof__' is not defined
>>> help(l.__sizeof__)
Help on built-in function __sizeof__:

__sizeof__() method of builtins.list instance
    Return the size of the list in memory, in bytes.

>>> #---------END--------###
>>> 
