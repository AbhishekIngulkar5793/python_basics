Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # data types in python
>>> # 14 data types
>>> # numeric : int,float,complex
>>> 12
12
>>> 145
145
>>> 12.66
12.66
>>> 56.77
56.77
>>> # complex
>>> real part + imaginary part
SyntaxError: invalid syntax
>>> # real part+imaginary part
>>> 2 + 5
7
>>> 2
2
+
>>> 2 + 5j
(2+5j)
>>> 4J
4j
>>> 3 + 4i
SyntaxError: invalid syntax
>>> 4J
4j
>>> 4j
4j
>>> type(4j)
<class 'complex'>
>>> #---------------
>>> # string
>>> # syntax
>>> ''
''
>>> # empty string
>>> ""
''
>>> # string is one of the important data type which accepts all types of data
>>> 'af23'
'af23'
>>> '4354443^&*&&$&%&*^I^*'
'4354443^&*&&$&%&*^I^*'
>>> '
SyntaxError: EOL while scanning string literal
>>> '                        '
'                        '
>>> # each element inside a string is a one memory block
>>> s = 'AMITABH BACHCHAN'
>>> S
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    S
NameError: name 'S' is not defined
>>> S
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    S
NameError: name 'S' is not defined
>>> s
'AMITABH BACHCHAN'
>>> S
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    S
NameError: name 'S' is not defined
>>> s
'AMITABH BACHCHAN'
>>> # how many blocks/characters/elements/objects we have in s
>>> s
'AMITABH BACHCHAN'
>>> len(s)
16
>>> # string background data structure
>>> # string background data structure is ARRAY
>>> # each element of an array has an index
>>> # index starts with 0 always
>>> len(s)-1
15
>>> s
'AMITABH BACHCHAN'
>>> # index is used to fetch one element at a time
>>> s[15]
'N'
>>> s[11]
'H'
>>> # fetch B of AMITABH
>>> s[6]
'H'
>>> s[5]
'B'
>>> # check id of s
>>> id(s)
1586482075808
>>> id(s[5])
1586447531568
>>> # if we want to check total size in bytes
>>> s
'AMITABH BACHCHAN'
>>> s.__sizeof__()
65
>>> s[5]
'B'
>>> s[5].__sizeof__()
50
>>> # check -ve indexing
>>> # it starts with -1 and ends with -n
>>> # it starts with -1 and ends with -n
>>> # right to left traversing
>>> s
'AMITABH BACHCHAN'
>>> s[-1]
'N'
>>> s[-16]
'A'
>>> s[-8]
'B'
>>> #-----------------
>>> a = 'ABHISHEK'
>>> 
>>> A
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    A
NameError: name 'A' is not defined
>>> a
'ABHISHEK'
>>> len(a)
8
>>> # +ve indexing
>>> a
'ABHISHEK'
>>> a[2]
'H'
>>> a[6]
'E'
>>> a[8]
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    a[8]
IndexError: string index out of range
>>> a[7]
'K'
>>> len(a)
8
>>> # -ve indexing
>>> a[-3]
'H'
>>> a[]-8
SyntaxError: invalid syntax
>>> a[-8]
'A'
>>> #---------------\
>>> s
'AMITABH BACHCHAN'
>>> # if we want to access a specific part from a string then use SLICING
>>> s[:]
'AMITABH BACHCHAN'
>>> s[:6]
'AMITAB'
>>> s[6:]
'H BACHCHAN'
>>> #s[start_index:stop_index]
>>> # access amitabh
>>> s
'AMITABH BACHCHAN'
>>> s[0:6]
'AMITAB'
>>> s[:6]
'AMITAB'
>>> # access bachchan
>>> s[8:]
'BACHCHAN'
>>> s[8:15]
'BACHCHA'
>>> s[8:17]
'BACHCHAN'
>>> # BACH
>>> s[8:12]
'BACH'
>>> # AMIT
>>> s[:4]
'AMIT'
>>> # slicing with -ve index
>>> s
'AMITABH BACHCHAN'
>>> s[-8:]
'BACHCHAN'
>>> s[-8:-12\]
      
SyntaxError: unexpected character after line continuation character
>>> s[-8:-12]
      
''
>>> s[-3:]
      
'HAN'
>>> s[-16:-7]
      
'AMITABH B'
>>> #---------------
      
>>> # reading of string from right to left
      
>>> s
      
'AMITABH BACHCHAN'
>>> # reverse whole string
      
>>> s[::-1] #s[start_index:stop_index:step]
      
'NAHCHCAB HBATIMA'
>>> s[::1]
      
'AMITABH BACHCHAN'
>>> s[0:]
      
'AMITABH BACHCHAN'
>>> s[::-1]
      
'NAHCHCAB HBATIMA'
>>> # + means left to right
      
>>> # - means right to left
      
>>> s[-10::-1]
      
'HBATIMA'
>>> s[-10::-1]
      
'HBATIMA'
>>> s[-1:-9:-1]
      
'NAHCHCAB'
>>> #--------------------
      
>>> s
      
'AMITABH BACHCHAN'
>>> s[:7:-1]
      
'NAHCHCAB'
>>> s[6::-1]
      
'HBATIMA'
>>> s[1:7:-1]
      
''
>>> s[12221321312:43432423:324234]
      
''
>>> #----------END------FIFTH DAY SESSION --------2.9.22
