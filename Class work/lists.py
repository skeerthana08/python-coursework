#Lists
#2.creating lists
l=[] 
l
l=list()  #constructor list
l
l=[1,2,"hi",1.3,1+3j,True] #heterogeneous
l
l=[[1,2],['a','b'],[True,False]] #nested lists
l
t=(1,2,3) #tuple
t
lfromt=list(t) #tuple to list conversion
lfromt
l=[1,2]
l
tfroml=tuple([1,2])  #list to tuple conversion
tfroml

s="python" #string
s
lfroms=list(s) #string to list conversion
lfroms


#3.accessing elements in a list
#indexing
lfroms
lfroms[0]

lfroms.index("p")

lfroms[-1]

#slicing
lfroms[1:3]
lfroms[-4:]

#4.modifying lists
n=[1,2,3]
n
n[2]=6  #changing elements
n

#adding and removing
n.append(5)  #append
n

n.insert(3,4)   #insert
n
n.extend([7,8,9])   #extend
n
n.append([2,6])  #append list
n
n.remove([2,6])   #remove list
n.append([2,6])
n
n.pop(2)    #pop out 2nd index
n.remove(2)    #remove 2
n.pop()   #pops out last element
n
del n[2]    #del element at index 2
n
n.clear()    #clears out the list 
n

#5.list methods
l=[1,2,3,4,3,4,2,1]
l
l.index(3)  #returns the index value of 3 

l.count(2)
l[4]  #find value of 4th index
l.sort()   #l changes (ascending order)
l.sort(reverse=True)   #(descending order)
l
sorted(l)  #l does not change
l
l.reverse()  #$reverses the list
l


#copying
#shallow copy
l
m=l.copy()   #shallow copy
m
m.append(100)    #if we add 100 to  m l does not change,100 is added to m only
m

n=l   #direct copy

n.append(2500)  #adding 2500 to n, it also adds in n and l
n
l
max(l)
min(l)
sum(l)
len(l)
any(l)
all(l)

k=[0,1,2]   #0,[],False," ", are false
k
any(k)  #Returns True if at least one element is True in the list.
all(k)   #Returns True if all elements areTrue in the list.

0 in k  #membership

nl=[[1,2,3],['a','b']]
n1
n1.index[1,2,3]