#square of a no.
# square= lambda n:n**2
# print(square(4))

#even or odd
# evenorodd=lambda n:'even' if n%2==0 else 'odd' 
# print(evenorodd(10))

#max of 2 no.s
# maxof2=lambda a,b:'a' if a>b else 'b'
# print(maxof2(24,26))

#mul 2 no.s
# mul=lambda a,b:a*b
# print(mul(25,9))

#sort a list of tuples according to 3rd element
# l=[(1, 3, 2), (2, 1, 6), (4, 2, 1)]
# print(sorted(l,key=lambda i:i[2]))

#even using filter
# l=[1,2,3,4,5,6,7,8,9]
# elst=list(filter(lambda i:i%2==0,l))
# print(elst)

#square of each element using map
# l=[1,2,3,4,5,6,7,8,9]
# l1=list(map(lambda i:i**2,l))
# print(l1)

#Convert list of strings to uppercase using lambda
# l=["hello", "world"]
# l1=list(map(lambda i:i.upper(),l))
# print(l1)

#9.Sort list of dictionaries by key using lambda
# l=[{'name': 'A', 'age': 30}, {'name': 'B', 'age': 20},{'name': 'C', 'age': 25}, {'name': 'D', 'age': 18}]
# sortedl = sorted(l,key=lambda x: x['age'])
# print(sortedl)

#10.Write a lambda function that returns the length of a string.
# slen= lambda i:len(i)
# print(slen('hello'))

#11. Check if string starts with a vowel using lambda
# vowels='aeiouAEIOU'
# stwv=lambda i: True if i[0] in vowels else False
# print(stwv("apple"))

#12. Add 10 to each element using lambda and map()
# l=[1, 2, 3]
# l1=list(map(lambda i:i+10, l))
# print(l1)

#13. Filter strings longer than 3 characters
# l=["a", "the", "lamp", "cat"]
# l1=list(filter(lambda i:len(i)>3,l))
# print(l1)

#14. Multiply each number by its index using lambda
l=[1, 2, 3, 4]
l1=list(map(lambda i:i*l[i],l))
print(l1)