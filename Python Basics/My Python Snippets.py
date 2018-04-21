############################################################################################
### Float Numbers and Print formats 
############################################################################################
def funPi(n):
    x = float(22)/7
    #first generate the float object %n1.n2f format and then apply that format over the pi
    print 'Value of pi to {a} decimal places : %1.{a}f'.format(a=n) %(x)
	
# Generate a pyramid
from __future__ import print_function
for i in range(1,10,2):
    x= '*'*i
    print (x.center(10))	



############################################################################################
### LIST 
############################################################################################

# Unable to remove all elements of a LIST, while iterating through the list:
l=[(1, 1, 1), (1, 1, 2), (1, 1, 3)]
# Below will successfully remove the items in list when the condition is satisfied
# See Difference in for loop using "list(l)"
for itm in list(l):
    if itm[0]==itm[1] or itm[1]==itm[2] or itm[2]==itm[0]:
        print 'equal', itm
       	l.remove(itm)
        
# Below will leave last element in the LIST and not remove even if condition satisfying:
# See Difference in for loop using "l"
for itm in l:
	if itm[0]==itm[1] or itm[1]==itm[2] or itm[2]==itm[0]:
    print 'equal', itm
    l.remove(itm)  
				
############################################################################################
### LIST COMPREHENSION
############################################################################################

# Basic
comp=[x for x in 'apple']

#   Multiple variables to create list with tuple elements:
c_lst=[(x**2,y,z) for x in xrange(0,7) for y in xrange(1,4) for z in ['a','b']]

#Conditions:
c_even=[x for x in xrange(0,13) if x%2==0]
print c_even

#complex arithmetic to store related C and F in tuples: 
c_celsius_farenheit=[ (x, (float(9)/5)*x+32) for x in xrange(-20,20)]

#Generate Calendar for 2017, 2018:
Using TUPLE, IF, XRANGE, FOR, LIST COMPREHENSION
cal_1=[(year, month, day) for month in xrange(1,13) for day in xrange(1,32) if month in (1,3,5,7,8,10,12) for year in xrange(2017, 2019)]
cal_2=[(year, month, day) for month in xrange(1,13) for day in xrange(1,31) if month in (4,6,9,11) for year in xrange(2017, 2019)]
cal_3=[(year, month, day) for month in xrange(1,13) for day in xrange(1,30) if month==2 for year in xrange(2017, 2018)]

cal_year=cal_1+cal_2+cal_3
cal_year.sort()
cal_year

#Create list of 3 element tuples with distinct numbers in each tuple: creates 502 tuples in list. len(x)
x=[(a,b,c) for a in xrange(1,10) for b in xrange(1,10) for c in xrange(1,10)]
for i in list(x):
    if i[0]==i[1] or i[1]==i[2] or i[2]==i[0]:
        print i
        x.remove(i)

############################################################################################
### IF, THEN, ELIF, ELSE
############################################################################################

# POP, INSERT, UPDATE into a list with tuples.
d={'INNA':'Good', 'Otilia':'Better', 'Penna':'Best'}
v_name='Heroine'
v_desc='Beautiful'
#Set v_pop to 'Y' to remove from service
v_pop='N'
# Update desc if different entered, else Print, delete if Pop
if d.has_key(v_name):
    if v_pop=='N' and v_desc!=d[v_name]:
	d[v_name]=v_desc
	print 'In service and updated: {a}, {b}' .format(a=v_name,b=v_desc)
    elif v_pop=='Y':
	print 'Popped from service: {a}, {b}' .format(a=v_name,b=v_desc)
	del d[v_name]
    else:
	 print 'In service: {a}, {b}' .format(a=v_name,b=v_desc)
else:  # Insert if contestant not exists
    d[v_name]=v_desc    
    print 'Welcome to service: {a}, {b}' .format(a=v_name,b=v_desc)
		
# Find count of numbers in a range that are evenly divisible by 2, 3 and others
lst=xrange(4,10000)
two=three=others=0
for num in lst:
if num%2 == 0:
two += 1
elif num%3 == 0:
three += 1
else:
others += 1
print 'two={a}, three={b}, others={c}' .format(a=two, b=three, c=others)

############################################################################################
### FUNCTIONS
############################################################################################
#     Better method of checking for primes.		
# A factor is any number that can be multiplied by another number to get the same result
# if Square root of a number N is number X, then square X**2 is N. So N is evenly divisible by X. This concept is implemented below.
import math

def is_prime(num):
'''
Better method of checking for primes. 
'''
if num % 2 == 0 and num > 2:
	return False
	for i in range(3, int(math.sqrt(num)) + 1, 2):
		if num % i == 0:
		return False
return True

#Generating List of Prime Numbers till 'n' using Filter and Function:
def prime_check(n):
    #numbers only divisible by itself and 1 are primes. Even numbers are not primes.
    #it is sufficient to check if n is divisible by numbers from 3 to sqrt(n).
    if n%2 == 0:
        #print ('Even, Not a Prime')
        return False
    else:
        for i in range(3, n**1/2+1, 2):
            if n%i == 0:
                #print ('Not a Prime, divisible by {b}').format(b=i)
                return False
                break
        #print ('{a} is a prime').format(a=n)
        return True

n = 30
filter(lambda i: prime_check(i), xrange(3, n/2+1, 2))


#   Generate list of primes in an interval
import math
def list_primes(v_min, v_max):
    '''
    Generates the list of prime numbers between min and max arguments
    '''
    p_list=[]
    for num in xrange(v_min, v_max):
        if num % 2 != 0:  #exclude even number are they are not prime
            for i in xrange(3, int(math.sqrt(num))+1, 2): #checking only remaining odd numbers 
                if num % i == 0:
                # Break loop as not Prime
                    break
            else:
                p_list.append(num)
    return p_list


#   Check for a Palindrome without using reverse
def palindrome(a):
    str_nospace=a.replace(' ','')
    cnt=len(str_nospace)-1
    j=cnt/2
    i=0
    for i in xrange(0,j):
        if str_nospace[i]!=str_nospace[cnt]:
            cnt=cnt-1
            return 'false'
        else:
            cnt=cnt-1
    else:
        return 'true'

# Easy way check for palindrome
def palindrome(a):
    str_nospace=a.replace(' ','')
    if str_nospace[::-1]==str_nospace:
        return 'true'
    else:
        return 'false'

# Check for Panagram:
import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    lst_az=string.ascii_lowercase
    for a in lst_az:
        if a not in str1:
            return 'Not Pangram'
    else:
        return 'Is Pangram'
    pass

# Check for Anagram for 2 strings: Ignore Spaces and capitals
def anagram(s1,s2):
    a1=set(map(lambda x:x, s1))
    a2=set(map(lambda x:x, s2))
    if len(a1.symmetric_difference(a2))==0:
        return True
    else:
        return False
    pass


def anagram2(s1,s2):
    ls1=[]
    ls2=[]
    for i in s1:
        if i in ls1 or i ==' ':
            continue
        else:
            ls1.append(i)
    for i in s2:
        if i in ls2 or i ==' ':
            continue
        else:
            ls2.append(i)    
    if sorted(ls1)==sorted(ls2):
        return True
    else:
        return False  
    pass
    
    
# Function to convert list of 2 element tuples into a dictionary with validation
def list_tup_to_dict(lst):
    dic={}
    l=[]
    i=0    
    # Check if there are any duplicate tuple[0] elements in list and error out
    for a in lst:
        l.append(a[0]) # used 0 as we just need the index 0 element from every tuple ('k', 'v')
        #print a[i]
    if len(l)!=len(set(l)):
        return 'duplicate keys found'
    # Convert List of Tuples into Dictionary
    for tup in lst:
        dic[lst[i][0]]=lst[i][1]
        #print i, lst[i][0], lst[i][1]
        i+=1
    return dic

p=[('k4', 'v2'), ('k6', 'v1'), ('k2', 'v2'), ('k1', 'v1')]
list_tup_to_dict(p)

#Creating List of Tuples and Dictionary using the LIst and its index values.
ls=[1,2,3,4,5,6,7,8,9]
l=[]
d={}
for i, item in enumerate(ls):
    t=(i,item)
    l.append(t)
dic.update(l)    
print t

# Creating a dictionary with input of list, using the indexes as values.
def d_list(L):
    return dict(map(lambda x: x[::-1], enumerate(L)))
    pass
d_list(['a','b','c'])


# Comparing SETS if they are same, they will match if elements are same. 
# SORT is not required to be applied before comparing. Also there is no SORT method for SET

import string
def check_p(str, ):
    az=set(string.ascii_lowercase)
    ck= set(str.lower())
    l=list(az)
    l.extend(' ')
    s=set(l)
    print s, ck
    return s == ck

check_p("The quick brown fox jumps over the lazy dog")

# Comparing LISTS if they are same, the same elements need to be sorted same order to match in lists

import string
def check_p(str, ):
    az=set(string.ascii_lowercase)
    ck= set(str.lower())
    m=list(az)
    m.extend(' ')
    n=list(ck)
    print m, n
    return m.sort()== n.sort()

check_p("The quick brown fox jumps over the lazy dog")


def my_split(in_string):
    '''
    split function which removes multiple spaces and adds workds to a list
    '''
    prev_char = curr_char = prev_word = curr_word = ''
    lst = []
    
    for i in in_string:
        curr_char = i
        #add the word only if curr char is space and prev char is not space
        #prev char is not blank : edge case, where first char in string is space
        if curr_char == ' ' and prev_char != ' ' and prev_char != '':
            lst.append(prev_word)
            prev_word = ''
        #append only if curr char is not space
        elif curr_char != ' ':
            curr_word = prev_word + curr_char
            prev_word = curr_word

        prev_char = curr_char
    
    #append last word
    #edge case to handle if end of string has more than 1 space
    if curr_char != ' ':
        lst.append(curr_word)
    
    return lst

	
############################################################################################
### Errors and Exception Handling
############################################################################################
def ask():
    while True:
        try:
            num = input('Enter an integer:')
        except:
            print 'invalid entry, enter valid integer'
        else:           
            if num == int(num):
                print 'Square of integer is', num**2
                break
            else:
                print 'Enter valid integer as whole number'
                continue


############################################################################################
### Generators Function
############################################################################################				
# Function with generator to generate Fibonacci sequence:
def fiboa(n):
    a=0
    b=1
    for i in range(n):
        t = b
        b = t + a
        a = t
        yield b

def fibonew(n):
    a=0
    b=1
    for i in range(n):
        a, b = b, a + b
        yield b

for a in fibonew(4):
    print a

#Generate Fibonacci series to infinity using Generator Function
# The generator encapsulates an infinite loop, but this isn't a problem because you only get each answer every time you ask for it.
def fib():
    a,b=0,1
    while True:
        a,b=b,a+b
        yield a

n = fib()
next(n)


############################################################################################
### Regular Expressions
############################################################################################	
# Extract only the alphabets part from the input string and create the proper name.
text = 'k&( omal9angi '
pattern = '[a-z]+'
l = re.findall(pattern, text)
reduce(lambda x,y :x+y, l)   
		
