import random as rn

#Self made
a=input(print("Enter Your Rock/Paper/Scissor:"))
l=["rock","paper","scissor"]
x=rn.choice(l)
if a==x:
    print("Draw")
elif x=="rock" and a=="paper":
    print("You win")
    print("Your value: ",a," system value :",x)
elif x=="scissor" and a=="rock":
    print("You win")
    print("Your value: ",a," system value :",x)
elif x=="paper" and a=="scissor":
    print("You win")
    print("Your value: ",a," system value :",x)
elif x=="rock" and a=="scissor":
    print("You Loose")
    print("Your value: ",a," system value :",x)
elif x=="paper" and a=="rock":
    print("You Loose")
    print("Your value: ",a," system value :",x)
elif x=="scissor" and a=="paper":
    print("You Loose")
    print("Your value: ",a," system value :",x)
else:
    print("invalid input")

