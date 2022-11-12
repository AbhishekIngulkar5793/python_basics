Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # ABHISHEK INGULKAR DAY 9 PRACTICE #
>>> l = ['abhishek','shreyal','nikita']
>>> l
['abhishek', 'shreyal', 'nikita']
>>> # sort above list on basis of length.
>>> l.sort(key=lambda x:len(x))
>>> l
['nikita', 'shreyal', 'abhishek']
>>> # sorted()
>>> sorted(l)
['abhishek', 'nikita', 'shreyal']
>>> # sort() is a method of list
>>> # sorted() function of Python
>>> # Interview Question: What is the difference between sort() and sorted()?
>>> sr = 'washim'
>>> sorted(sr)
['a', 'h', 'i', 'm', 's', 'w']
>>> sr
'washim'
>>> # sorted() is temporary
>>> # sort() is inpace
>>> # sorted() it always give list output
>>> sorted((4,5,6))
[4, 5, 6]
>>> # sorted() is applicable to str,list,tuple,set.
>>> #-----------------------\
>>> #tuple - ()
>>> #It has the same features like list except list is mutable and tuple is immuable.
>>> #Mutable: we can change the elements inside the object without changing its id
>>> #Immutable: we cant change the elements inside an object, and if we try to do so, then it will change the elements as well as will create a new object with new id.
>>> l
['nikita', 'shreyal', 'abhishek']
>>> l.append(4)
>>> l
['nikita', 'shreyal', 'abhishek', 4]
>>> l[1]
'shreyal'
>>> l[1]=55
>>> l
['nikita', 55, 'abhishek', 4]
>>> l
['nikita', 55, 'abhishek', 4]
>>> t = (4,8,9)
>>> t
(4, 8, 9)
>>> type(t)
<class 'tuple'>
>>> # Features of a tuple :
>>> # It supports indexing, slicing.
>>> # Background structure of a tuple is an array.
>>> t
(4, 8, 9)
>>> t[1]
8
>>> t[-1]
9
>>> type(t)
<class 'tuple'>
>>> t1[1]= 10
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    t1[1]= 10
NameError: name 't1' is not defined
>>> t[1]=10
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    t[1]=10
TypeError: 'tuple' object does not support item assignment
>>> # Item assignment is not allowed.
>>> ###########
>>> # Methods of tuple:
>>> dir(t)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
>>> # from above methods of tuple, we only require count(), and index()
>>> t1 = (44,5.4,88,55,44)
>>> t1
(44, 5.4, 88, 55, 44)
>>> # count()
>>> t1.count(44)
2
>>> t1.count(777)
0
>>> # index()
>>> t1
(44, 5.4, 88, 55, 44)
>>> t1.index(88)
2
>>> t1.index(44)
0
>>> t1.index(1111)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    t1.index(1111)
ValueError: tuple.index(x): x not in tuple
>>> 
>>> # tuple does not have any method for changing size, item assignment
>>> # it is immutable
>>> # Question: Explain list vs tuple?
>>> # Question: which one is better /
>>> # ?
>>> #-------------------
>>> l
['nikita', 55, 'abhishek', 4]
>>> t1
(44, 5.4, 88, 55, 44)
>>> # It lets size allocation
>>> l.__sizeof__()
96
>>> t1.__sizeof__()
64
>>> #Interview Question: why tuple occupies less memory?
>>> (1,2,3)+(4,5,6)
(1, 2, 3, 4, 5, 6)
>>> x = (1,2,3)
>>> y = (4,5,6)
>>> id(x)
1726012142144
>>> id(y)
1726012143080
>>> x = x+y
>>> x
(1, 2, 3, 4, 5, 6)
>>> id(x)
1726011804168
>>> l
['nikita', 55, 'abhishek', 4]
>>> l.append(5)
>>> id(l)
1726007154312
>>> l.append(44)
>>> id(l)
1726007154312
>>> l
['nikita', 55, 'abhishek', 4, 5, 44]
>>> x
(1, 2, 3, 4, 5, 6)
>>> id(x)
1726011804168
>>> x + (8,9)
(1, 2, 3, 4, 5, 6, 8, 9)
>>> id(x)
1726011804168
>>> l
['nikita', 55, 'abhishek', 4, 5, 44]
>>> #----------------------
>>> # Packing and unpacking
>>> 10,20,30
(10, 20, 30)
>>> tup = 10,20,30
>>> tup
(10, 20, 30)
>>> # As an output we are getting single object
>>> # This process is nothing but packing
>>> # combining elements in the single entity
>>> 
>>> #Unpacking
>>> tup[0]
10
>>> a = tup[0]
>>> a
10
>>> p1,p2,p3 = tup
>>> p1
10
>>> p2
20
>>> p3
30
>>> 
>>> # Separate out packed data is called unpacking.
>>> tup
(10, 20, 30)
>>> b = p1+p2
>>> b
30
>>> # Interview Question: What is packing and unpacking?
>>> # packing= combining multiple elements in a single entity.
>>> # unpacking= separating combined objects as a individual object.
>>> l
['nikita', 55, 'abhishek', 4, 5, 44]
>>> l + [100]
['nikita', 55, 'abhishek', 4, 5, 44, 100]
>>> l
['nikita', 55, 'abhishek', 4, 5, 44]
>>> id(l)
1726007154312
>>> l = l + 100
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    l = l + 100
TypeError: can only concatenate list (not "int") to list
>>> l = l +
SyntaxError: invalid syntax
>>> l = l + [100,200]
>>> l
['nikita', 55, 'abhishek', 4, 5, 44, 100, 200]
>>> id(l)
1726012113416
>>> a = 10
>>> a
10
>>> a = 100
>>> a
100
>>> tup
(10, 20, 30)
>>> li = list(tup)
4
>>> li = list(TUP)
Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    li = list(TUP)
NameError: name 'TUP' is not defined
>>> li = list(tup)
>>> li
[10, 20, 30]
>>> id(tup)
1726012141712
>>> id(li)
1726011952584
>>> id(p1)
140724871550272
>>> id(p2)
140724871550592
>>> ########## END ################
