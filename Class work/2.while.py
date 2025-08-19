l=[1,2,3]
ind=0
while ind<len(l):
    print(l[ind])
    ind+=1

#Ascii values
s="python programming"
ind=0
n=len(s)
while ind<len(s):
    print(ord(s[ind]))
print(s)
    

#5 4 3 2 1
n=5
while n>0:
    print(n)
    n=n-1

#3 6 9 12 15 18
n=1
while n<7:
    print(n*3)
    n+=1


#1 8 27 64 125 216
n=1
while n<7:
    print(n**3)
    n+=1

#sum of no.s in a list
l=list(map(int,input().split()))
s=0
ind=0
while ind<len(l):
    s=s+l[ind]
    ind+=l
print(s)

#sum of each digit in a no.
n=int(input())
s=0
while n>0:
    s+=(n%10)
    n//10
print(s)



#palindrome
n=int(input())
temp=n
rev=0
while n>0:
    rev=rev*10+(n%10)
    n//=10
if rev==temp:
    print("palindrome")
else:
    print("not palindrome")



n=input()
full=len(n)-1
length=len(n)//2
ind=0

while ind<=length:
    if n[ind]!=n[full]:
        print("not palindrome")
        break
    ind+=1
    full-=1
else:
    print("palindrome")