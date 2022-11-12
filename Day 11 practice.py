Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # ABHISHEK INGULKAR DAY 11 PRACTICE - 16/9/22
>>> # SET AND DICT
>>> # sewt
>>> # set operations
>>> dir(set)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
>>> s1={5,8,9,4,3}
>>> s2={11,22,5,8,9}
>>> # union
>>> s1.union(s2)
{3, 4, 5, 8, 9, 11, 22}
>>> # it takes all the values from both sets and combine them together
>>> # no duplicate elements are allowed
>>> 
>>> # intersection
>>> s1.intersection(s2)
{8, 9, 5}
>>> # intersection methods only fetches common elements from these sets
>>> #
>>> # difference
>>> # in difference method, it take all the values from set 1 except common values between set1 and set2
>>> s1
{3, 4, 5, 8, 9}
>>> s2
{5, 8, 9, 11, 22}
>>> s1.difference(s2)
{3, 4}
>>> s2.difference(s1)
{11, 22}
>>> 
>>> # if we want uncommon values from both sets
>>> s1.symmetric_difference_update({5,8,3,4,11})
>>> s1
{9, 11}
>>> s1.symmetric_difference_update(s2)
>>> s1
{5, 8, 22}
>>> s2
{5, 8, 9, 11, 22}
>>> id(s1)
1834834282760
>>> id(s2)
1834834283208
>>> 
>>> s1.difference_update(s2)
>>> s1
set()
>>> s2
{5, 8, 9, 11, 22}
>>> s1
set()
>>> id(s1)
1834834282760
>>> ########################
>>> s1
set()
>>> s1 = {22}
>>> s1
{22}
>>> s2
{5, 8, 9, 11, 22}
>>> s1 + s2
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    s1 + s2
TypeError: unsupported operand type(s) for +: 'set' and 'set'
>>> s1 - s2
set()
>>> s1
{22}
>>> s1 | s2
{5, 22, 8, 9, 11}
>>> # symmentric difference
>>> s1
{22}
>>> s1 = {1,11,21}
>>> s2 = {22,1,11,85}
>>> # isdisjoint
>>> s1.isdisjoint(s2)
False
>>> s1.isdisjoint({1,11,21})
False
>>> s1.isdisjoint({100,200})
True
>>> help(s1.isdisjoint)
Help on built-in function isdisjoint:

isdisjoint(...) method of builtins.set instance
    Return True if two sets have a null intersection.

>>> s1
{1, 11, 21}
>>> s2
{1, 11, 85, 22}
>>> s1.intersection(s2)
{1, 11}
>>> # is subset
>>> s1
{1, 11, 21}
>>> s2
{1, 11, 85, 22}
>>> s1.issubset(s2)
False
>>> s2.issubset(s1)
False
>>> s1.issubset({11,21})
False
>>> {11,21}.issubset(s1)
True
>>> {85}.issubset(s2)
True
>>> # check for superset
>>> # ################## ####
>>> 
>>> 
>>> 
>>> # dictionary
>>> dict
<class 'dict'>
>>> {}
{}
>>> type({})
<class 'dict'>
>>> type({()})
<class 'set'>
>>> # syntax of dict: {key:value}
>>> d = {'a':'Python','b':'Data'}
>>> d
{'a': 'Python', 'b': 'Data'}
>>> type(d)
<class 'dict'>
>>> # features of dict
>>> # duplicate keys are not allowed but the duplicate elements area allowed
>>> d
{'a': 'Python', 'b': 'Data'}
>>> {1:200,2:500,1:200}
{1: 200, 2: 500}
>>> # if we supply duplicate key then it will take last recent key:value pair
>>> # it acccepts all types of data (hetrogeneous data)
>>> # background data structure of dict is hash table
>>> # so, no indexing and slicing is possible in dict
>>> d
{'a': 'Python', 'b': 'Data'}
>>> d[0]
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    d[0]
KeyError: 0
>>> d[1]
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    d[1]
KeyError: 1
>>> d[:]
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    d[:]
TypeError: unhashable type: 'slice'
>>> d['a']
'Python'
>>> d['b']
'Data'
>>> d[5]
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    d[5]
KeyError: 5
>>> d['b'] # this is one way to access particular element with the key
'Data'
>>> # it is mutable in nature
>>> 
>>> ###########################
>>> 
>>> # methods of dict
>>> dir(dict)
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
>>> # get()
>>> \
    
>>> 
>>> d1
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    d1
NameError: name 'd1' is not defined
>>> d1 = {'a':100,'b':102,'c':1.22,55:'Py'}
>>> d1
{'a': 100, 'b': 102, 'c': 1.22, 55: 'Py'}
>>> d1.get(55)
'Py'
>>> d1.get('a') # we have to supply key as a n argument
100
>>> # if i supplied key which is not present in dict
>>> d1.get(100)
>>> d1.get(100,'nahiye')
'nahiye'
>>> d1.get('a','nahiye')
100
>>> d1.get('','nahiye')
'nahiye'
>>> d1.get('e',100)
100
>>> d1.get('e',500,800,55)
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    d1.get('e',500,800,55)
TypeError: get expected at most 2 arguments, got 4
>>> ########################
>>> d1
{'a': 100, 'b': 102, 'c': 1.22, 55: 'Py'}
>>> d1['a']
100
>>> d1.get('a')
100
>>> d1.get('e')
>>> d1.get('e','Value not present')
'Value not present'
>>> ########################
>>> 
3
>>> 
>>> # update
>>> d1
{'a': 100, 'b': 102, 'c': 1.22, 55: 'Py'}
>>> # we have to supply a dict inside update
>>> d1.update('DS':1020)
SyntaxError: invalid syntax
>>> d1.update({'DS':1020})
>>> d1
{'a': 100, 'b': 102, 'c': 1.22, 55: 'Py', 'DS': 1020}
>>> ##################
>>> # if i want only the keys
>>> d1
{'a': 100, 'b': 102, 'c': 1.22, 55: 'Py', 'DS': 1020}
>>> d1.keys()
dict_keys(['a', 'b', 'c', 55, 'DS'])
>>> d1.keys()[0]
Traceback (most recent call last):
  File "<pyshell#137>", line 1, in <module>
    d1.keys()[0]
TypeError: 'dict_keys' object does not support indexing
>>> li = list(d1.keys())
>>> li
['a', 'b', 'c', 55, 'DS']
>>> li[0]
'a'
>>> # if i want only values from the dict
>>> d1
{'a': 100, 'b': 102, 'c': 1.22, 55: 'Py', 'DS': 1020}
>>> d1.values()
dict_values([100, 102, 1.22, 'Py', 1020])
>>> # if i want both keys and values (key,value)
\
>>> d1
{'a': 100, 'b': 102, 'c': 1.22, 55: 'Py', 'DS': 1020}
>>> d1.items()
dict_items([('a', 100), ('b', 102), ('c', 1.22), (55, 'Py'), ('DS', 1020)])
>>> list.(d1.items())
SyntaxError: invalid syntax
>>> list.(d1.items())
SyntaxError: invalid syntax
>>> list(d1.items())
[('a', 100), ('b', 102), ('c', 1.22), (55, 'Py'), ('DS', 1020)]
>>> list(d1.items())[0]
('a', 100)
>>> ############# END###############
