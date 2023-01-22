# del
# pop()
# remove()
# clear()
#Update elements from list

print("*******Del function******")  #does not return the deleted value
l=[10,20,30,40,50]
print(l)
del l[2]
print(l)

print("*******POP function*******")  #POP also return the value deleted
t=[10,20,30,40,50,60]
print(t)
print(t.pop(2))  #t.pop(2) means 3rd element will be removed
print(t)

print("*******Remove function******")  #removed through value nor index
r=[10,20,30,40,50,60]
print(r)
r.remove(50)
print(r)

print("******clear function*******")
a=[10,20,30,40,50,60]
print(a)
a.clear()
print(a)

print("*******Update list elements******")

t=[1,2,3,4,5,6,7,8,9,10]
print(t)
t[0]=0
t[1]=0
t[9]=0
print(t)