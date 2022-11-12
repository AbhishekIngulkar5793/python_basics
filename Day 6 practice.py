Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # ABHISHEK INGULKAR 6TH DAY PRACTICE
>>> # string
>>> # array
>>> # Indexing: +ve  & -ve
>>> # slicing
>>> # It accepts all types of data
>>> '12321$%^&***'
'12321$%^&***'
>>> "____--233erwerw32#@$%#^&%^%$"
'____--233erwerw32#@$%#^&%^%$'
>>> # It preserves sequence order
>>> ########################
>>> 
>>> 
>>> # methods of a string
>>> # Methods
>>> s = 'welcome to batch 21'
>>> s.title()
'Welcome To Batch 21'
>>> # to convert letter into upper case
>>> s.upper()
'WELCOME TO BATCH 21'
>>> a = 'APPLE'
>>> # for lower case
>>> a.lower()
'apple'
>>> # All methods of a string gives a temporary output.
>>> # If we check a and s : thosa are unchanged
>>> a
'APPLE'
>>> s
'welcome to batch 21'
>>> #-----------
>>> s.title()
'Welcome To Batch 21'
>>> # Capitalize : to make the first letter of first word in CAPS
>>> s.capitalize()
'Welcome to batch 21'
>>> help(capitakize)
Traceback (most recent call last):h
  File "<pyshell#29>", line 1, in <module>
    help(capitakize)
NameError: name 'capitakize' is not defined
>>> help(capitalize)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    help(capitalize)
NameError: name 'capitalize' is not defined
>>> help(s.capitalize)
Help on built-in function capitalize:

capitalize() method of builtins.str instance
    Return a capitalized version of the string.
    
    More specifically, make the first character have upper case and the rest lower
    case.

>>> help(s.title)
Help on built-in function title:

title() method of builtins.str instance
    Return a version of the string where each word is titlecased.
    
    More specifically, words start with uppercased characters and all remaining
    cased characters have lower case.

>>> #--------------------
>>> s
'welcome to batch 21'
>>> # Lets find index
>>> s.index('21')
17
>>> s[17]
'2'
>>> ## It returns the lowest index.
>>> s
'welcome to batch 21'
>>> s.index('e')
1
>>> # If we want the highest index then use rindex() function
>>> s.rindex('e')
6
>>> #----------------------------
>>> # find() : It also gives index of an element
>>> s
'welcome to batch 21'
>>> s.find('batch')
11
>>> s.find('to')
8
>>> # The difference between index and find ?
>>> # If we try to find unknown thing ,an element is not present
>>> s
'welcome to batch 21'
>>> s.index('sholey')
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    s.index('sholey')
ValueError: substring not found
>>> s.find('sholey')
-1
>>> s
'welcome to batch 21'
>>> #--------------------------
>>> 
>>> s
>>> s
'welcome to batch 21'
>>> # LIST
>>> # List of string in which each word separated by a space shuld act as an indivisual
>>> # list==> []
>>> s.split()
['welcome', 'to', 'batch', '21']
>>> log = '2245-5678-8799'
>>> log.split('-')
['2245', '5678', '8799']
>>> f = 'kajol,karishma,katrina'
>>> f.split(',')
['kajol', 'karishma', 'katrina']
>>> f
'kajol,karishma,katrina'
>>> f.split(',')
['kajol', 'karishma', 'katrina']
>>> #---------------
>>> r='            rohit'
>>> r
'            rohit'
>>> # Remove the space using a strip method
>>> r.strip()
'rohit'
>>> g = '************abhishek*********'
>>> g
'************abhishek*********'
>>> g.strip('*')
'abhishek'
>>> g.lstrip()
'************abhishek*********'
>>> g.lstrip('*')
'abhishek*********'
>>> g.rstrip('*')
'************abhishek'
>>> #----------------------
>>> a = 'Abh**##ishek**'
>>> a
'Abh**##ishek**'
>>> a.strip('*')
'Abh**##ishek'
>>> # In order to remove an element present in between, then we will use replace method
>>> # a.replace(old,new)
>>> a.replace('**##','')
'Abhishek**'
>>> aa = a.replace('**##','')
>>> aa
'Abhishek**'
>>> aa.strip('*')
'Abhishek'
>>> aaa = aa.strip('*')
>>> aaa
'Abhishek'
>>> aaa.replace('bhi','kuchbhi')
'Akuchbhishek'
>>> fname = 'abhi'
>>> lname = 'ingulkar'
>>> fname
'abhi'
>>> lname
'ingulkar'
>>> # concatenate 2 strings
>>> fname + lname
'abhiingulkar'
>>> 'fname+''+lname'
'fname++lname'
>>> 'fname+' '+lname'
'fname++lname'
>>> fname +' '+ lname
'abhi ingulkar'
>>> aaa
'Abhishek'
>>> # Abhiek
>>> aaa[:4]
'Abhi'
>>> aaa[6:]
'ek'
>>> aaa[:4] + aaa[6:]
'Abhiek'
>>> # ----------------
>>> s
'welcome to batch 21'
>>> # If we want to count number of occurances
>>> s.count('e')
2
>>> s.count('PQR')
0
>>> s.count('PQR') # not present
0
>>> s.count('welcome')
1
>>> #--------------------------
>>> f
'kajol,karishma,katrina'
>>> result = f.split(',')
>>> result
['kajol', 'karishma', 'katrina']
>>> # Data is in the form of list of string
>>> # and i want a string now
>>> # then ,we can use join() method
>>> ','.join(result)
'kajol,karishma,katrina'
>>> f
'kajol,karishma,katrina'
>>> k = ['Gangadhar','hi','shaktimaan','hai']
>>> k
['Gangadhar', 'hi', 'shaktimaan', 'hai']
>>> # convert list to string
>>> ''.join(l)
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    ''.join(l)
NameError: name 'l' is not defined
>>> ''.join(k)
'Gangadharhishaktimaanhai'
>>> ' '.join(k)
'Gangadhar hi shaktimaan hai'
>>> s
'welcome to batch 21'
>>> s[:] # start:stop
'welcome to batch 21'
>>> s[0:7]
'welcome'
>>> help(s.find)
Help on built-in function find:

find(...) method of builtins.str instance
    S.find(sub[, start[, end]]) -> int
    
    Return the lowest index in S where substring sub is found,
    such that sub is contained within S[start:end].  Optional
    arguments start and end are interpreted as in slice notation.
    
    Return -1 on failure.

>>> help(s.count)
Help on built-in function count:

count(...) method of builtins.str instance
    S.count(sub[, start[, end]]) -> int
    
    Return the number of non-overlapping occurrences of substring sub in
    string S[start:end].  Optional arguments start and end are
    interpreted as in slice notation.

>>> #------ABHISHEK INGULKAR 6TH SESSION PRACTICE END----6.9.22
