Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 3j
3j
>>> type(3j)
<class 'complex'>
>>> 2+3j
(2+3j)
>>> type(2+3j)
<class 'complex'>
>>> ''
''
>>> type('')
<class 'str'>
>>> type("")
<class 'str'>
>>> r=4
>>> pi=3.14
>>> area=pi*r**2
>>> area
50.24
>>> r=5
>>> area
50.24
>>> area=pi*r**2
>>> area
78.5
>>> #------------------
>>> # operators
>>> # assignment operators
>>> a=100
a
>>> 
>>> a
100
>>> a=a+100
>>> a
200
>>> a+=100
a
>>> 
>>> 
>>> a
300
>>> a+=100 # a = a+100
>>> a
400
>>> # assignment operator
>>> # +=,-=,*=,/=,%=,//=,**=
>>> a
400
>>> a-= 200 # a = a - 200
>>> a
200
>>> a*= 2
>>> a
400
>>> a**= 2
>>> a
160000
>>> a%= 5
>>> a
0
>>> a/= 10
>>> a
0.0
>>> a= 200
>>> a%= 2
>>> a
0
>>> a=200
>>> a
200
>>> a/= 3
>>> a
66.66666666666667
>>> a//= 3
>>> a
22.0
>>> #----------------------------------
>>> # comparison or additional operators
>>> # comparison or additional operators
>>> #  comparison or conditional operators (above sentence is wrong)
>>> # when we want to compare 2 objects then use these operators
>>> # < ,> ,<= ,>= ,== ,!=
>>> a
22.0
>>> a=250
>>> a
250
>>> a
250
>>> 1>2
False
>>> 1<2
True
>>> # output is always in boolean form: true annd false
>>> 'python' = 'Python'
SyntaxError: can't assign to literal
>>> 'python' =='Python'
False
>>> # how to check two objects are same or not?
>>> # use id()==> returns address of that object
>>> # if address of two objects is same then both objects are identical
>>> # otherwise they are different
>>> id('Python')
1864501253656
>>> id('python')
1864536480208
>>> # as id is different here for both the objects hence we get false result
>>> x= 500
>>> y= 500
>>> x == y
True
>>> id(x)
1864537076720
>>> id(y)
1864537076656
>>> # == is used for content equality
>>> # not used for address equality
>>> # if we want to check for address equality
>>> # then use another operator
>>> # known as identity operator
>>> # is , is not.
>>> x==y
True
>>> id(x)
1864537076720
>>> id(y)
1864537076656
>>> x is y
False
>>> x
500
>>> y
500
>>> p1 = 'python'
>>> p1
'python'
>>> p2= 'Python'
>>> p2
'Python'
>>> p1 == p2 # content equality
False
>>> p1 is p2 # address equality
False
>>> # Que. What is ADDRESS EQUALITY AND CONTENT EQUALITY??
>>> P=10
>>> P
10
>>> Q=10
>>> Q
10
>>> P==Q
True
>>> # IT IS A CONTENT EQUALITY
>>> P is Q
True
>>> p=10
>>> p
10
>>> q=10.0
q
>>> 
>>> q
10.0
>>> p==q
True
>>> # content equality
>>> p is q
False
>>> # address equality
>>> id(p)
140712375342400
>>> id(q)
1864496823416
>>> id(p) == id(q)
False
>>> # not equal to, !=
>>> 12 != 67
True
>>> p1
'python'
>>> p2
'Python'
>>> p1 'Python'
SyntaxError: invalid syntax
>>> 
>>> 
>>> p1 !=p2
True
>>> #-----------------------------------
>>> e1= 22.22
>>> e1
22.22
>>> id(e1)
1864496823344
>>> d1 = 200
>>> d1
200
>>> id(d1)
140712375348480
>>> d2 = 200
>>> id (d2)
140712375348480
>>> #----------------------------------
>>> e1= 22.22
>>> e1
22.22
>>> id(e1)
1864496823464
>>> e2= 22.22
>>> e2
22.22
>>> id(e2)
1864496823488
>>> e3=22.22
>>> e3
22.22
>>> id(e3)
1864496821712
>>> id(200)
140712375348480
>>> id(d1)
140712375348480
>>> #-------------------------
>>> # logical operators
>>> # and , or , not.
>>> # used to compare outputs of 2 conditions
>>> nm = 'abhi'
>>> nm
'abhi'
>>> ag=25
>>> ag
25
>>> # it is a boolean output
>>> true and false
Traceback (most recent call last):
  File "<pyshell#154>", line 1, in <module>
    true and false
NameError: name 'true' is not defined
>>> true and true
Traceback (most recent call last):
  File "<pyshell#155>", line 1, in <module>
    true and true
NameError: name 'true' is not defined
>>> True and True
True
>>> True and False
False
>>> False and True
False
>>> False and False
False
>>> #------------------
>>> nm == 'abhi'
True
>>> ag== 25
True
>>> nm='abhi' and ag=25
SyntaxError: can't assign to operator
>>> nm=='abhi' and ag==25
True
>>> nm=='abhi' and ag==24
False
>>> nm=='shek' and ag==25
False
>>> nm== 'shek' and ag==24
False
>>> #------------------------
>>> # not:negation
>>> not True
False
>>> not False
True
>>> nm = 'abhishek'
>>> nm=='abhishek'
True
>>> nm=='abhi'
False
>>> ag==23
False
>>> ag==25
True
>>> not ag=23
SyntaxError: can't assign to operator
>>> not ag==23
True
>>> ag==25
True
>>> not ag==25
False
>>> report= '+ve'
>>> report
'+ve'
>>> report
'+ve'
>>> not report== '-ve'
True
>>> not report== '+ve'
False
>>> 
>>> 
>>> #----------------------------\
>>> 10 and 12
12
>>> 'abhi' and 'shrey'
'shrey'
>>> -1 and -3
-3
>>> 12.5 and 56.4
56.4
>>> # rule : if x value is true, then returns y value
>>> # x and y
\
>>> 
>>> bool(10)
True
>>> bool('abhi')
True
>>> bool('')
False
>>> bool(12.5)
True
>>> bool(56.4)
True
>>> bool(false)
Traceback (most recent call last):
  File "<pyshell#201>", line 1, in <module>
    bool(false)
NameError: name 'false' is not defined
>>> bool(False)
False
>>> bool(True)
True
>>> bool(0)
False
>>> # all objects are True always except False, none, '', 0
>>> bool()
False
>>> # Rule2: if x value is false then it returns x
>>> 0 and 2
0
>>> None and 'python'
>>> 
>>> None
>>> False and 34
False
>>> '' and 55
''
>>> #--------------END---------------
>>> # Second lecture 26.8.22
