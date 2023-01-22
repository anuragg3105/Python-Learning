#membership operator
str1="hello"
print('h' in str1)
print('H' in str1)  #python is case sensitive
print('i' in str1)
print('g' not in str1)

#searching in list
print("searching in list")
l=[10,20,30,40]
print(50 in l)
print(40 in l)
print(50 not in l)
print(40 not in l)

#identity operator
print("identity operator")
x=10
y=20
print(x is y)
print(x is y, x==y)
print(x is not y)
print(x is y, x!=y)