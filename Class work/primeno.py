n=int(input("Enter the number: "))
isprime=False
for i in range(2,n//2+1):
    if n%i==0:
        isprime=True
        break
if isprime:
    print("Not a prime number")
else:
    print("prime number")