#sum of n 
def display(n):
  if n==0:
    return 0
  return n+display(n-1)
print(display(5))

#product of n
def display(n):
  if n==1:
    return n
  return n*display(n-1)
print(display(5))