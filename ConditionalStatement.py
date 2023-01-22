a=int(input("enter any number:"))
if a%2==0:
    if a < 10:
        print("even and less than 10")
    elif a > 10:
        print("even and more than 10")

elif a%2!=0 :   #or we can use else directly
    if a<10:
        print("odd and less than 10")
    elif a>10:
         print("odd and more than 10")
