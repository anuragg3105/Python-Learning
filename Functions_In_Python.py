# #user defined functions

#without argument
def simple():
    print("***  Simple Function  ***")
    a=int(input("Enter value 1: "))
    b= int(input("Enter value 2: "))
    print("sum is : ",a+b)
simple()

#with argument
def advance(a,b):  #(a,b=5) means b will override if we pass new value for b
    print("***  Function with argument  ***")
    print("sum is : ",a+b)
a=int(input("Enter value 1: "))
b= int(input("Enter value 2: "))
advance(a,b)

def advance(a,b=5):  #(a,b=5) means b will override if we pass new value for b
    print("***  Function with argument  ***")
    print("sum is : ",a+b)
a=int(input("Enter value 1: "))
b= int(input("Enter value 2: "))
advance(a) #here b default value will be taken by system

#with return
def advance(a,b):
    print("***  Function with return  ***")
    s=a+b
    return(s)
a=int(input("Enter value 1: "))
b=int(input("Enter value 2: "))
output=advance(a,b)
print("sum is : :",output)