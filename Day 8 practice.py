Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # ABHISHEK INGULKAR DAY 8 PRACTICE
>>> # List
>>> # Mutable
>>> # Slicing, Indexing, Sequence order
>>> l = ['Rushi','Abhishek',84.4]
>>> l
['Rushi', 'Abhishek', 84.4]
>>> l.append(10)
>>> l
['Rushi', 'Abhishek', 84.4, 10]
>>> l.extend([5,6])
>>> l
['Rushi', 'Abhishek', 84.4, 10, 5, 6]
>>> l.append([1,2])
>>> l
['Rushi', 'Abhishek', 84.4, 10, 5, 6, [1, 2]]
>>> l.extend(5)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    l.extend(5)
TypeError: 'int' object is not iterable
>>> l.extend('string')
>>> l
['Rushi', 'Abhishek', 84.4, 10, 5, 6, [1, 2], 's', 't', 'r', 'i', 'n', 'g']
>>> l.clear()
>>> l
[]
>>> #Copy
>>> l1
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    l1
NameError: name 'l1' is not defined
>>> l1=[1,2,4,5,6]
>>> l1
[1, 2, 4, 5, 6]
>>> l1=l1.copy()
>>> l2 = l1.copy()
>>> l2
[1, 2, 4, 5, 6]
>>> l1
[1, 2, 4, 5, 6]
>>> id(l1)
1968032847752
>>> id(l2)
1968032847944
>>> l3 = l1
>>> id(i3)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    id(i3)
NameError: name 'i3' is not defined
>>> l3
[1, 2, 4, 5, 6]
>>> id(i3)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    id(i3)
NameError: name 'i3' is not defined
>>> id(l3)
1968032847752
>>> # Shallow copy: objects with same elements and having different id's
>>> # Deep copy: objects with same elements and having same id's
>>> l1.append(222)
>>> l1
[1, 2, 4, 5, 6, 222]
>>> l2
[1, 2, 4, 5, 6]
>>> l3
[1, 2, 4, 5, 6, 222]
>>> # Int. Que- What is shallow copy and deep copy ?
>>> # count()
>>> l1
[1, 2, 4, 5, 6, 222]
>>> l1.count(2)
1
>>> l1.append(222)
>>> l1.append(5)
>>> l1
[1, 2, 4, 5, 6, 222, 222, 5]
>>> l1.count(2)
1
>>> l1.count(222)
2
>>> l1.count(5)
2
>>> l1.count(500)
0
>>> # count returns zero(0) instead of 4 line error
>>> # insert
>>> l1
[1, 2, 4, 5, 6, 222, 222, 5]
>>> #l1.insert(index number,element)
>>> l1.index(2,32)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    l1.index(2,32)
ValueError: 2 is not in list
>>> l1.append(-1,2)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    l1.append(-1,2)
TypeError: append() takes exactly one argument (2 given)
>>> l1.insert(-1,2)
>>> l1
[1, 2, 4, 5, 6, 222, 222, 2, 5]
>>> l1.insert(9,90)
>>> l1
[1, 2, 4, 5, 6, 222, 222, 2, 5, 90]
>>> l1.insert(2,4)
>>> l1
[1, 2, 4, 4, 5, 6, 222, 222, 2, 5, 90]
>>> l1.insert(-7,22.2)
>>> l1
[1, 2, 4, 4, 22.2, 5, 6, 222, 222, 2, 5, 90]
>>> l1.insert(-11,11.1)
>>> l1
[1, 11.1, 2, 4, 4, 22.2, 5, 6, 222, 222, 2, 5, 90]
>>> l1.insert(-13,333)
>>> l1
[333, 1, 11.1, 2, 4, 4, 22.2, 5, 6, 222, 222, 2, 5, 90]
>>> l1.insert(-16,5)
>>> l1
[5, 333, 1, 11.1, 2, 4, 4, 22.2, 5, 6, 222, 222, 2, 5, 90]
>>> l1.insert(-22,4)
>>> l1
[4, 5, 333, 1, 11.1, 2, 4, 4, 22.2, 5, 6, 222, 222, 2, 5, 90]
>>> # insert will add element before index number
>>> len(l1)
16
>>> l1
[4, 5, 333, 1, 11.1, 2, 4, 4, 22.2, 5, 6, 222, 222, 2, 5, 90]
>>> # pop & remove
>>> l1
[4, 5, 333, 1, 11.1, 2, 4, 4, 22.2, 5, 6, 222, 222, 2, 5, 90]
>>> l1.pop(2)
333
>>> l1
[4, 5, 1, 11.1, 2, 4, 4, 22.2, 5, 6, 222, 222, 2, 5, 90]
>>> l1.pop(222)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    l1.pop(222)
IndexError: pop index out of range
>>> l1.pop(-1)
90
>>> l1.pop(-22)
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    l1.pop(-22)
IndexError: pop index out of range
>>> l1.pop()
5
>>> # pop() by default it will remove last element
>>> # pop() will return reoved element presenting on that particular index
>>> l1.pop(-3)
222
>>> # remove ()
>>> l1
[4, 5, 1, 11.1, 2, 4, 4, 22.2, 5, 6, 222, 2]
>>> l1.remove(50)
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    l1.remove(50)
ValueError: list.remove(x): x not in list
>>> l1.remove(222)
>>> l1
[4, 5, 1, 11.1, 2, 4, 4, 22.2, 5, 6, 2]
>>> l1
[4, 5, 1, 11.1, 2, 4, 4, 22.2, 5, 6, 2]
>>> l1.remove(4)
>>> l1
[5, 1, 11.1, 2, 4, 4, 22.2, 5, 6, 2]
>>> # remove(): it will remove the first occurance of that element
>>> # if we try to remove already removed element it will give error
>>> l1
[5, 1, 11.1, 2, 4, 4, 22.2, 5, 6, 2]
>>> l1.remove(4)
>>> l1
[5, 1, 11.1, 2, 4, 22.2, 5, 6, 2]
>>> l1.remove(4)
>>> l1
[5, 1, 11.1, 2, 22.2, 5, 6, 2]
>>> l1.remove(4)
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    l1.remove(4)
ValueError: list.remove(x): x not in list
>>> # Interview Question: what is the difference between pop() & remove() ?
>>> l1.remove()
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    l1.remove()
TypeError: remove() takes exactly one argument (0 given)
>>> # Reverse
>>> l1'
SyntaxError: EOL while scanning string literal
>>> l1
[5, 1, 11.1, 2, 22.2, 5, 6, 2]
>>> l1.reverse()
\
>>> l1
[2, 6, 5, 22.2, 2, 11.1, 1, 5]
>>> l1
[2, 6, 5, 22.2, 2, 11.1, 1, 5]
>>> l1.reverse()
>>> l1
[5, 1, 11.1, 2, 22.2, 5, 6, 2]
>>> l1[::-1]
[2, 6, 5, 22.2, 2, 11.1, 1, 5]
>>> l1
[5, 1, 11.1, 2, 22.2, 5, 6, 2]
>>> # From above example understand that reverse() is inplace while slicing is temporary operation
>>> # sort()
>>> l1
[5, 1, 11.1, 2, 22.2, 5, 6, 2]
>>> l1.sort()
>>> l1
[1, 2, 2, 5, 5, 6, 11.1, 22.2]
>>> l1
[1, 2, 2, 5, 5, 6, 11.1, 22.2]
>>> # by default sort() will sort the elements in asending order
>>> s = ['a','e','w','q','m','c','l']
>>> s
['a', 'e', 'w', 'q', 'm', 'c', 'l']
>>> s.sort()
>>> s
['a', 'c', 'e', 'l', 'm', 'q', 'w']
>>> s
['a', 'c', 'e', 'l', 'm', 'q', 'w']
>>> h = ['a','h',22,'q',88.8,5+3j,'b']
>>> h
['a', 'h', 22, 'q', 88.8, (5+3j), 'b']
>>> h.sort()
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    h.sort()
TypeError: '<' not supported between instances of 'int' and 'str'
>>> # If we want to sort in desending order
>>> l1
[1, 2, 2, 5, 5, 6, 11.1, 22.2]

>>> l1.sort(reverse = False)
>>> l1
[1, 2, 2, 5, 5, 6, 11.1, 22.2]
>>> l1.sort(reverse = True)
>>> l1
[22.2, 11.1, 6, 5, 5, 2, 2, 1]
>>> l1
[22.2, 11.1, 6, 5, 5, 2, 2, 1]
>>> l1.append(2+3j)
>>> l1
[22.2, 11.1, 6, 5, 5, 2, 2, 1, (2+3j)]
>>> l1.sort
<built-in method sort of list object at 0x000001CA37E61788>
>>> l1.sort()
Traceback (most recent call last):
  File "<pyshell#138>", line 1, in <module>
    l1.sort()
TypeError: '<' not supported between instances of 'complex' and 'int'
>>> l1.remove(2+5j)
Traceback (most recent call last):
  File "<pyshell#139>", line 1, in <module>
    l1.remove(2+5j)
ValueError: list.remove(x): x not in list
>>> l1.remove(2+3j)
>>> l1
[1, 2, 2, 5, 5, 6, 11.1, 22.2]
>>> l1.append(2.56)
>>> l1
[1, 2, 2, 5, 5, 6, 11.1, 22.2, 2.56]
>>> l1.sort()
>>> l1
[1, 2, 2, 2.56, 5, 5, 6, 11.1, 22.2]
>>> # reversed()
>>> # It reverse the elements of an object & output in the form of object referrence
>>> l1
[1, 2, 2, 2.56, 5, 5, 6, 11.1, 22.2]
>>> reversed(l1)
<list_reverseiterator object at 0x000001CA38145438>
>>> list(reversed(l1))
[22.2, 11.1, 6, 5, 5, 2.56, 2, 2, 1]
>>> # difference between reversed and reverse ?
>>> l1
[1, 2, 2, 2.56, 5, 5, 6, 11.1, 22.2]
>>> list(reversed('abhishek'))
['k', 'e', 'h', 's', 'i', 'h', 'b', 'a']
>>> s = 'abhishek'
>>> s[::-1]
'kehsihba'
\
>>> list(reversed(s))
['k', 'e', 'h', 's', 'i', 'h', 'b', 'a']
>>> ''.join(reversed(s))
'kehsihba'
>>> s
'abhishek'
>>> ''.join(list(s).reverse())
Traceback (most recent call last):
  File "<pyshell#159>", line 1, in <module>
    ''.join(list(s).reverse())
TypeError: can only join an iterable
>>> list(s)
['a', 'b', 'h', 'i', 's', 'h', 'e', 'k']
>>> list(s).reverse()
>>> s1=list(s).reverse()
>>> s1
>>> s1
>>> s1 = s.split()
>>> s1
['abhishek']
>>> s1.reverse
<built-in method reverse of list object at 0x000001CA3833BBC8>
>>> s1.reverse()
>>> s1
['abhishek']
>>> list(s)
['a', 'b', 'h', 'i', 's', 'h', 'e', 'k']
>>> sl = list(s)
>>> s1
['abhishek']
>>> list(s)
['a', 'b', 'h', 'i', 's', 'h', 'e', 'k']
>>> s1 = list(s)
>>> s1
['a', 'b', 'h', 'i', 's', 'h', 'e', 'k']
>>> s1.reverse()
>>> s1
['k', 'e', 'h', 's', 'i', 'h', 'b', 'a']
>>> ''.join(s1)
'kehsihba'
>>> ##------------END--------##
>>> 
