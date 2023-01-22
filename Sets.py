#Unordered data type, unindexed
#can be represented with set() function or {}
#set(),add(),pop(),remove(),clear(),discard()
print("****  Sets  ****")
s={10,10,20,20,30,30,30,40}
print(s)  #output can be in random order
#method 2
for a in s:
    print(a)

print("****  Function in Sets  ****")

print("*****   set()   *****")
l=[10,20,30,40,50]
a=set(l) #convert list/tuple into set
print(a)

print("*****   add()   *****")
a={10,20,30,40,50}
a.add(60)
print(a)

print("*****   pop()   *****")
a={10,20,30,40,50}
t=a.pop() #delete any element randomly
print(a,t)

print("*****   remove()   *****")
a={10,20,30,40,50}
a.remove(30)  #does not return deleted item
print(a)

print("*****   discard()   *****")
a={10,20,30,40,50}
a.discard(50)  #delete by value
print(a)

print("*****   clear()   *****")
a={10,20,30,40,50}
a.clear()  #does not return {} on clear because it can means
print(a)   #dictionary also

print("*****   update()   *****")
a={10,20,30,40,50}
l=[60,70,80,90]
a.update(l) #only add element, does not update existing values
print(a)