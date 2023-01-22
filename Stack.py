#Stack is linear data structure
#Stck is last in/First out(LIFO)
# Stack operations:
# 1. push 2. pop 3. peek(display last element)
# 4. display(display list)

l=[]
while True:
    c=eval(input('''Enter operation type
    1. push
    2. pop
    3. peek
    4. display
    5. exit
    '''))
    if c==1:
        n=input("Enter value")
        l.append(n)
        print(l)

    if c==2:
        if len(l)==0:
            print("empty stack")
        else :
           p= l.pop()
           print(p)
           print(l)
    if c==3:
        if len(l)==0:
            print("empty stack")
        else:
           print(l)
           print("Last element is :", l[-1])

    if c==4:
        print("display stack : ",l)

    elif c==5:
        break

    else:
        print("Invalid operation")
