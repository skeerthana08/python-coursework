#5. Membership Operators
name="keerthana"
name
'w' in name
'e' in name
's' in name
'kee' in name
'rteek' in name

l = [1,2,3]
l
3 not in l
 
t = (4,5,6)
t
5 in t 

s={'pfs', 'jfs', 'ds'}
s
'ds' in s
'da' in s
data = {'name':'keer', 'age': 21}
data
'name' in data
'keer' in data #only keys can be checked 
'course' not in data


#6.identity operators

n=[1,2,3]
m=[1,2,3]
id(n)
id(m)
n = l
n is m 
n is l
m is n
l is n
id(l)
n is not m 


#4.Python operators
#1.Arithmetic operators

a=20
a
b=30
b
print("addition of a and  b:", a+b)  
print("subtraction of a and  b:", a-b)
print("muultiplication of a and  b:",  a*b)
print("division of a and  b:", a/b)
print("float division of a and  b:", a//b)
print("modulus of a and  b:",a%b)
print("exponentation of a and  b:", a**b)



#2.Comparision operators

c=56
c
d=23
d
print("Equal to(c==d):", c==d)
print("Not Equal to(c!=d):", c!=d)
print("Greater than(c>d):", c>d)
print("Less than(c<d):", c<d)
print("Greater than or equal to(c>=d):", c>=d)
print("Less than or equal to(c<=d):", c<=d)

#7. bitwise operators
10 & 8 #and
10^8 #xor
10>>1 #right shift
10<<1#left shift
~10 #not
10|8 #or