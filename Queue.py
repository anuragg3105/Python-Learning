# Queue is a linear data structure
# Store items in First in first out FIFO manner
# Operation:
# 1. enqueue: add an item to queue
# 2. dequeue: remove item from queue
# 3. front : gets the front item
# 4. rear : gets the last item

l=[]
while True:
    c=eval(input('''Enter operation type
    1. enqueue
    2. dequeue
    3. front element
    4. rear element
    5. Display queue
    6. exit
    '''))
    if c==1:
        n=input("Enter value")
        l.append(n)
        print(l)

    if c==2:
        if len(l)==0:
            print("empty stack")
        else :
           del l[0]
           print(l)
    if c==3:
        if len(l)==0:
            print("empty stack")
        else:
           print(l)
           print("front element is :", l[0])

    if c==4:
        if len(l)==0:
            print("empty stack")
        else:
           print(l)
           print("last element is :", l[-1])

    if c==5:
        print("display queue : ",l)

    elif c==6:
        break

    else:
        print("Invalid operation")
