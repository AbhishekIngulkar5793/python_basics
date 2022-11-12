Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # ABHISHEK INGULKAR DAY 12 PRACTICE #
>>> #dictionary
>>> # How to remove (key:value) pair?
>>> d1 = {'a':111,'b':222,'c':333,'d':444}
>>> d1
{'a': 111, 'b': 222, 'c': 333, 'd': 444}
>>> # pop()
>>> d1.pop('b')
222
>>> d1
{'a': 111, 'c': 333, 'd': 444}
>>> # it is an inplace operation
>>> # If i tried to remove already removed pair, then it raise an key error.
>>> d1.pop('b')
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    d1.pop('b')
KeyError: 'b'
>>> 
>>> # Instead of a key error if u want to specify your own value or message then,
>>> d1.pop('b','Nahiye')
'Nahiye'
>>> #-----------------------------------
>>> d1.pop(333)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    d1.pop(333)
KeyError: 333
>>> #---------------------------------------------------
>>> # popitem()
>>> d1
{'a': 111, 'c': 333, 'd': 444}
>>> d1.update('e':555)
SyntaxError: invalid syntax
>>> d1.update({'e':555})
>>> d1
{'a': 111, 'c': 333, 'd': 444, 'e': 555}
>>> d1.update({'a':1000})
>>> d1
{'a': 1000, 'c': 333, 'd': 444, 'e': 555}
>>> d1.popitem()
('e', 555)
>>> # popitem() will remove the last key:value pair from the dictionary
>>> # It is an inplace operation
>>> 
>>> #--------------------------------------------
>>> d2 = {'g':200,'f':500}
>>> d1.update(d2)
>>> d1
{'a': 1000, 'c': 333, 'd': 444, 'g': 200, 'f': 500}
>>> {10,25,45}
{25, 10, 45}
>>> 25%10
5
>>> 45%10
5
>>> 10%10
0
>>> #-------------------------------------------------
>>> d1
{'a': 1000, 'c': 333, 'd': 444, 'g': 200, 'f': 500}
>>> # setdefault()
>>> help(d1.setdefault)
Help on built-in function setdefault:

setdefault(key, default=None, /) method of builtins.dict instance
    Insert key with a value of default if key is not in the dictionary.
    
    Return the value for key if key is in the dictionary, else default.

>>> d1.setdefault('f')
500
>>> # If i supply key which is not present in the dictionary, then
>>> d1
{'a': 1000, 'c': 333, 'd': 444, 'g': 200, 'f': 500}
>>> d1.setdefault('z')
>>> d1
{'a': 1000, 'c': 333, 'd': 444, 'g': 200, 'f': 500, 'z': None}
>>> # It will add that not containing key into the dictionary and assign 'none' as its value.
>>> # and if we want to supply both key:value pair in the dictionary then ,
>>> # or add
>>> d1.setdefault('k',788)
788
>>> d1
{'a': 1000, 'c': 333, 'd': 444, 'g': 200, 'f': 500, 'z': None, 'k': 788}
>>> # If the key is present then it will return its value
>>> # If the key is not present then it will add that key in the dictionary with 'none' value
>>> #If we want to add key,value both, then supply both arguments in the function
>>> #-----------------------------------------
>>> # fromkeys()
>>> d2
{'g': 200, 'f': 500}
>>> d3 = {1:100,2:100,3:100}
>>> dic = {}
>>> dic.fromkeys([1,2,3,4],100)
{1: 100, 2: 100, 3: 100, 4: 100}
>>> # It will create a dictionary with different keys with same values
>>> # If i supplied list of values then, it will take the whole list of values as a single element and will add it to the different keys we want to provide
>>> dic.fromkeys([1,2,3,4],[100,200,300,400])
{1: [100, 200, 300, 400], 2: [100, 200, 300, 400], 3: [100, 200, 300, 400], 4: [100, 200, 300, 400]}
>>> # fromkeys() function is not inplace ie its temporary
>>> # ----------------------------------------------
>>> k1 = [1,2,3,4]
>>> k2 = [22,33,44,55]
>>> # zip
>>> zip(k1,k2)
<zip object at 0x000001B5018ACB48>
>>> dict(zip(k1,k2))
{1: 22, 2: 33, 3: 44, 4: 55}
>>> # if i want list then
>>> list(zip(k1,k2))
[(1, 22), (2, 33), (3, 44), (4, 55)]
>>> # if i want tuple
>>> tuple(zip(k1,k2))
((1, 22), (2, 33), (3, 44), (4, 55))
>>> #-----------------------------------------
>>> # range in python
>>> range(10)
range(0, 10)
>>> n = 10
>>> range(n)
range(0, 10)
>>> list(range(n))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(11,21))
[11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
>>> # range (start,stop,step)
>>> # Used to generate sequence of numbers in a given range
>>> # start- inclusive & stop- exclusive
>>> # If i want 1 to 100 numbers
>>> list(range(1,101))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
>>> # If i want even numbers from 1 to 100
>>> list(range(2,100,2))
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]
>>> # If i want odd numbers from 1 to 100
>>> [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]list(range(2,100,2))
SyntaxError: invalid syntax
>>> 
>>> 
>>> list(range(2,101,2))
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
>>> list(range(1,101,2))
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
>>>  # If i want 1 to 50 in reverse
>>> list(range(1,51,-1))
[]
>>> list(range(51,1,-1))
[51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
>>> list(range(51,0,-1))
[51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
>>> # -----------------------------------------
>>> # frozenset()
>>> # It has same properties like set except set is mutable and frozenset is immutable
>>> s = {1,2,3}
>>> s.add(5)
>>> s
{1, 2, 3, 5}
>>> f = frozenset()
>>> type(f)
<class 'frozenset'>
>>> f
frozenset()
>>> f.add(5)
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    f.add(5)
AttributeError: 'frozenset' object has no attribute 'add'
>>> f = frozenset([55,45,35])
>>> f
frozenset({35, 45, 55})
>>> dir(s)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
>>> dir(f)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'copy', 'difference', 'intersection', 'isdisjoint', 'issubset', 'issuperset', 'symmetric_difference', 'union']
>>> #Q. What is frozenset ? what is the diff between frozenset and set?
>>> # -----------------------------------------
>>> # byte
>>> # bytes
>>> # It generates array of bytes
>>> # when we supply iterable in bytes, it will give byte sequence
>>> bytes([10,20,30])
b'\n\x14\x1e'
>>> bytes(20)
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
>>> bytes([20])
b'\x14'
>>> bytes([10])
b'\n'
>>> bytes([30])
b'\x1e'
>>> # bytes is ranged based operation.
>>> # the range for bytes is fixed or limited to (0,256)
>>> bytes([500])
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    bytes([500])
ValueError: bytes must be in range(0, 256)
>>> bytes([256])
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    bytes([256])
ValueError: bytes must be in range(0, 256)
>>> bytes([255])
b'\xff'
>>> bytes(['a'])
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    bytes(['a'])
TypeError: 'str' object cannot be interpreted as an integer
>>> # background data structure of bytes is array
>>> # indexing in bytes
>>> b = bytes([2,4,5])
>>> b[0]
2
>>> # slicing in bytes
>>> b[:]
b'\x02\x04\x05'
>>> b[1:2]
b'\x04'
>>> # item assignment in bytes is not possible
>>> b[0] = 2
Traceback (most recent call last):
  File "<pyshell#136>", line 1, in <module>
    b[0] = 2
TypeError: 'bytes' object does not support item assignment
>>> # ---------------------------
>>> # bytearray
>>> bytearray([5,4,8])
bytearray(b'\x05\x04\x08')
>>> b1 = bytearray([5,4,8])
>>> b1[0]
5
>>> b1[:]
bytearray(b'\x05\x04\x08')
>>> b1[1:]
bytearray(b'\x04\x08')
>>> b1[0] = 56
>>> b1
bytearray(b'8\x04\x08')
>>> b1[0] = 100
>>> b1
bytearray(b'd\x04\x08')
>>> bytearray([100])
bytearray(b'd')
>>> bytearray([255])
bytearray(b'\xff')
>>> bytearray([256])
Traceback (most recent call last):
  File "<pyshell#150>", line 1, in <module>
    bytearray([256])
ValueError: byte must be in range(0, 256)
>>> #Q.	What  is bytes and bytearray ? differentiate between them
>>> # 12TH DAY PRACTICE SESSION END###########
