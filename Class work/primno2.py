n=int(input("Enter the number: "))
c=0
for i in range(2,n//2+1):
    if n%i==0:
        c=1
        break
if c:
    print("Not a prime number")
else:
    print("prime number")