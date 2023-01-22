print('''
+add
- subtract
* multiply
/divide
''')
op=(input("Enter required operation:"))
a=float(input("Enter first number"))
b=float(input("Enter second number"))

if op=="+":
    sum=a+b
    print("Sum is:", sum)

elif op=="-":
    diff=a-b
    print("Difference is:", a-b)

elif op=="*":
    mul=a*b
    print("multiplication is:",mul)

elif op=="/":
    div=a/b
    print("division is", div)
    print("remainder is", a%b)
else:

    print("invalid input")