Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 12 is 12
True
>>> 12 is 12.
False
>>> id(12)
140712451036544
>>> id(12.)
2534712065048
>>> 12. is 12.
True
>>> 12 == 12.0
True
>>> # == content equality
>>> # is checks address id() : performs address equality
>>> #----------------------
>>> id(122.0)
2534712065048
>>> id(12.0)
2534712065024
>>> 12.0 is 12.0
True
>>> g1 = 12.0
>>> g1 = 12.0
>>> g1 is g2
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    g1 is g2
NameError: name 'g2' is not defined
>>> g2 = 12.0
>>> g1 = g2
>>> 
>>> g1 is g2
True
>>> id(g1)
2534712065048
>>> id(g2)
2534712065048
>>> # -----------------------
>>> # operators
>>> # membership operators
>>> # to check either an object is a member of collection or not
>>> s = 'virat kohli'
>>> s
'virat kohli'
>>> # 2 types : in,not in
>>> 'v' in s
True
>>> 'k' not in s
False
>>> # answer is in boolean form
>>> 'rohit' in s
False
>>> 'rohit' not in s
True
>>> 120 in s
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    120 in s
TypeError: 'in <string>' requires string as left operand, not int
>>> '120' in s
False
>>> k = [100,102,104]
>>> k
[100, 102, 104]
>>> 100 in k
True
>>> '100' in k
False
>>> k1 = [100,'100','100.0']
>>> 
>>> k
[100, 102, 104]
>>> k1
[100, '100', '100.0']
>>> '100' in k1
True
>>> #---------------------------------
>>> # bitwise operator: & and , | or , ~ not , ^ XOR
>>> #---------------------
>>> # print() function
>>> print()

>>> # print(value,....,sep = '--') # change sep
>>> # print (value,...., sep = '',end= '\n')
>>> print(100)
100
>>> print(100,200,300)
100 200 300
>>> print(100,'python',30.99)
100 python 30.99
>>> print(100,'python',30.99,sep = '--') # change seperator
100--python--30.99
>>> # seperator works between two objects only
>>> print(100,sep='==>')
100
>>> print(100,'A',sep='==>')
100==>A
>>> # end: default \n it means new line at end
>>> # we can modify end with any other string
>>> print(100,'A')
100 A
>>> print(100,'A',end='end of statement')
100 Aend of statement
>>> # ramesh is 28 years old
>>> print(100)
100
>>> print(100,end='\n\n')
100

>>> print(100,end='\n\n\n')
100


>>> # take the help of help() function
>>> help(print)
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.

>>> help(id)
Help on built-in function id in module builtins:

id(obj, /)
    Return the identity of an object.
    
    This is guaranteed to be unique among simultaneously existing objects.
    (CPython uses the object's memory address.)

>>> name = 'sarang'
     
>>> place = 'Pune'
     
>>> name
     
'sarang'
>>> place
     
'Pune'
>>> # hello, your name is sarang, and place is Pune
     
>>> print('hello, your name is :',name)
     
hello, your name is : sarang
>>> print('Hello,your name is :',name,', and place is:',place)
     
Hello,your name is : sarang , and place is: Pune
>>> # Q> can we use escape sequences: \n (new line), \t (tab means 4 spaces)
     
>>> print(Hello, your name is:',name,', and place is:',place)
	  
SyntaxError: invalid syntax
>>> print('hello, your name is :',name,' and place is :',place)
	  
hello, your name is : sarang  and place is : Pune
>>> print('Hello, your name is:',name,'\nand place is:',place )
	  
Hello, your name is: sarang 
and place is: Pune
>>> print('Hello, your name is:',name,',\nand place is:',place)
	  
Hello, your name is: sarang ,
and place is: Pune
>>> print('Hello,                your name is:',name,',\nand place is:',place)
	  
Hello,                your name is: sarang ,
and place is: Pune
>>> # space is also a part of a string
	  
>>> print('Hello, your name is:',name,',\tand place is:',place)
	  
Hello, your name is: sarang ,	and place is: Pune
>>> print(1,2,3)
	  
1 2 3
>>> print(1,2,3,sep='\t')
	  
1	2	3
>>> print(1,'\t',2,'\t',3)
	  
1 	 2 	 3
>>> print('Abhishek', 'Ingulkar')
	  
Abhishek Ingulkar
>>> print('Abhishek'+'Ingulkar')
	  
AbhishekIngulkar
>>> 'Abhishek' + 'Ingulkar' # it does concatenation
	  
'AbhishekIngulkar'
>>> 'Abhishek'+' Ingulkar'
	  
'Abhishek Ingulkar'
>>> 'Abhishek'+' '+'Ingulkar'
	  
'Abhishek Ingulkar'
>>> pi = 3.14
	  
>>> r = 4
	  
>>> print('area of circle is:',pi*r**2)
	  
area of circle is: 50.24
>>> area = pi*r**2
	  
>>> area
	  
50.24
>>> print('area of circle is:',area)
	  
area of circle is: 50.24
>>> # input(): it is a function, used to make input from user
	  
>>> r = input('enter the radius od circle:')
	  
enter the radius od circle:2.1
>>> r
	  
'2.1'
>>> type(r)
	  
<class 'str'>
>>> # input always takes value in str form
	  
>>> # so we need to convert/typecast
	  
>>> r = float(input('enter the radius of a circle:'))
	  
enter the radius of a circle:2.1
>>> r
	  
2.1
>>> type(r)
	  
<class 'float'>
>>> print('Area of circle is:',pi*r**2)
	  
Area of circle is: 13.8474
>>> #-------------------------
	  
>>> 12.33
	  
12.33
>>> int(12.33)
	  
12
>>> # typecast means converting a data from one type to other type
	  
>>> str(12.33)
	  
'12.33'
>>> print('Area of circle is:',round(pi*r**2,2))
	  
Area of circle is: 13.85
>>> #--------------END----ABHISHEK INGULKAR 3RD DAY SESSION----------
