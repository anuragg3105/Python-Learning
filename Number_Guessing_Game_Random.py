import random
import random as rn

a=int(input(print("Enter Your Number :")))
x=rn.randint(1,10)
if a==x:
    print("Numbers are same")
    print(a," = ",x)
elif a<x:
    print("Numbers are not same")
    print(a, "is less than ", x)
elif a>x:
    print("Numbers are not same")
    print(a, "is more than ",x)
