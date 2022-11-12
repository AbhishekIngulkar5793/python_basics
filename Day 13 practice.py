Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ### ABHISHEK INGULKAR DAY 13 PRACTICE
>>> # revision of all data types we learned till today
>>> # comments
>>> # comments in python
>>> # it is a comment which is followed by hash '#'
>>> # this is a single line comment
>>> 
>>> """
This is python programming.
Python is dynamic
& case sensitive
"""
'\nThis is python programming.\nPython is dynamic\n& case sensitive\n'
>>> 
>>> def sample():
	""" SAMPLE FUNCTION"""
	print('This is sample')

	
>>> sample()
This is sample
>>> # """SAMPLE FUNCTION""" : it is a docstring
>>> # How to check docstring of function?
>>> sample.__doc__
' SAMPLE FUNCTION'
>>> 
>>> def py():
	"""This is python function
		python is case sensitive"""
	print('PYTHON')

	
>>> py
<function py at 0x000001C18E9901E0>
>>> py()
PYTHON
>>> py.__doc__
'This is python function\n\t\tpython is case sensitive'
>>> 
>>> 
>>> 
>>> #____----------------------------------_______________
>>> # data types in python
>>> # str,numeric,list,tuple,dict,set,bytes,bytearray
>>> 
>>> # str
>>> s = 'Abhi'
>>> id(s)
1930832666552
>>> s += 'shek'
>>> s
'Abhishek'
>>> id(s)
1930832651888
>>> s[0]
'A'
>>> s[:]
'Abhishek'
>>> s[::-1]
'kehsihbA'
>>> s[::2]
'Ahse'
>>> s[::3]
'Aie'
>>> # methods of string
>>> s
'Abhishek'
>>> s.upper()
'ABHISHEK'
>>> s.lower()
'abhishek'
>>> s.title()
'Abhishek'
>>> s.capitalize()
'Abhishek'
>>> s = 'abhishek sunil ingulkar'
>>> s
'abhishek sunil ingulkar'
>>> s.capitalize()
'Abhishek sunil ingulkar'
>>> s.title()
'Abhishek Sunil Ingulkar'
>>> s.casefold()
'abhishek sunil ingulkar'
>>> s.count(s)
1
>>> s
'abhishek sunil ingulkar'
>>> s.count(a)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    s.count(a)
NameError: name 'a' is not defined
>>> s.count('s')
2
>>> s.count('a')
2
>>> s.count('i')
3
>>> s.find(5)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    s.find(5)
TypeError: must be str, not int
>>> s.find('a')
0
>>> s.fine('i')
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    s.fine('i')
AttributeError: 'str' object has no attribute 'fine'
>>> s.find('i')
3
>>> s.find(l)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    s.find(l)
NameError: name 'l' is not defined
>>> s.find('l')
13
>>> s.index('h')
2
>>> s.index('m')
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    s.index('m')
ValueError: substring not found
>>> s.find('m')
-1
>>> s.count('m')
0
>>> s
'abhishek sunil ingulkar'
>>> s.replace('k','s')
'abhishes sunil ingulsar'
>>> s
'abhishek sunil ingulkar'
>>> s.startswith(i)
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    s.startswith(i)
NameError: name 'i' is not defined
>>> s.startswith('i')
False
>>> s.startswith('a')
True
>>> s.startswith('A')
False
>>> s.endswith('A')
False
>>> s.endswith('k')
False
>>> s.endswith('r')
True
>>> st = 'Python is case sensitive'
>>> st.split()
['Python', 'is', 'case', 'sensitive']
>>> st = 'python-is case sensitive'
>>> st.split()
['python-is', 'case', 'sensitive']
>>> st.split('-')
['python', 'is case sensitive']
>>> st
'python-is case sensitive'
>>> st = '                python is case sensitive'
>>> st
'                python is case sensitive'
>>> st.strip()
'python is case sensitive'
>>> st
'                python is case sensitive'
>>> st.lstrip()
'python is case sensitive'
>>> st = 'python is case sensitive*********'
>>> st
'python is case sensitive*********'
>>> st.rstrip()
'python is case sensitive*********'
>>> st.rstrip('*')
'python is case sensitive'
>>> st
'python is case sensitive*********'
>>> # format in str
>>> prof = 'data scientist'
>>> ex = 2
>>> 'My profession is {} and experience is {}'.format(prof,ex)
'My profession is data scientist and experience is 2'
>>>  # is methods
>>> s
'abhishek sunil ingulkar'
>>> s.isalpha()
False
>>> s.isdigit()
False
>>> s.isalpha()
False
>>> s.isspace()
False
>>> s.isupper()
False
>>> s.islower()
True
>>> s.isidentifier()
False
>>> # f'string
>>> prof
'data scientist'
>>> ex
2
>>> f'My profession is {prof} and my experience is {ex}
SyntaxError: EOL while scanning string literal
>>> f'My profession is {prof} and my experience is {ex}'
'My profession is data scientist and my experience is 2'
>>> 
>>> # list
>>> l = [1,2,5,8,7,8,7]
>>> l
[1, 2, 5, 8, 7, 8, 7]
>>> l.append(100)
>>> l
[1, 2, 5, 8, 7, 8, 7, 100]
>>> l.extend([24,34])
>>> l
[1, 2, 5, 8, 7, 8, 7, 100, 24, 34]
>>> l.clear()
>>> l
[]
>>> l
[]
>>> l = [1,2,5,8,7,8,7]
>>> l
[1, 2, 5, 8, 7, 8, 7]
>>> l2 = []
>>> l2
[]
>>> l2 = l.copy()
>>> l2
[1, 2, 5, 8, 7, 8, 7]
>>> id(l)
1930833017928
>>> id(l2)
1930833018056
>>> l = l1
Traceback (most recent call last):
  File "<pyshell#140>", line 1, in <module>
    l = l1
NameError: name 'l1' is not defined
>>> l1 = l
>>> l1
[1, 2, 5, 8, 7, 8, 7]
>>> id(l1)
1930833017928
>>> l.append(566)
>>> l
[1, 2, 5, 8, 7, 8, 7, 566]
>>> l1
[1, 2, 5, 8, 7, 8, 7, 566]
>>> l.insert(457)
Traceback (most recent call last):
  File "<pyshell#147>", line 1, in <module>
    l.insert(457)
TypeError: insert() takes exactly 2 arguments (1 given)
>>> l.insert(457,3)
>>> l
[1, 2, 5, 8, 7, 8, 7, 566, 3]
>>> l.insert(4,389)
>>> l
[1, 2, 5, 8, 389, 7, 8, 7, 566, 3]
>>> l.pop()
3
>>> l.pop()
566
>>> l
[1, 2, 5, 8, 389, 7, 8, 7]
>>> l.remove(389)
>>> l
[1, 2, 5, 8, 7, 8, 7]
>>> l.reverse()
>>> l
[7, 8, 7, 8, 5, 2, 1]
>>> l
[7, 8, 7, 8, 5, 2, 1]
>>> l[::-1]
[1, 2, 5, 8, 7, 8, 7]
>>> reversed(l)
<list_reverseiterator object at 0x000001C18E8FEA58>
>>> list(reversed(l))
[1, 2, 5, 8, 7, 8, 7]
>>> l1
[7, 8, 7, 8, 5, 2, 1]
>>> l
[7, 8, 7, 8, 5, 2, 1]
>>> l.sort()
>>> l
[1, 2, 5, 7, 7, 8, 8]
>>> l.sort(reverse=True)
>>> l
[8, 8, 7, 7, 5, 2, 1]
>>> sorted(l)
[1, 2, 5, 7, 7, 8, 8]
>>> l
[8, 8, 7, 7, 5, 2, 1]
>>> ####### Day 13 practice session end #########
