#Use iterate 2+ list at same time
l=[10,20,30,40]
l1=[3,4,5,6]
print("*** Zip function 2+ list iteration ***")
for a,b in zip(l,l1):
    print(a,b)

#if any one list contain more element
#then zip will only display common number of elements
print("*** ZIP ignores extra element of bigger list ***")
l=[1,2,3,4,5]
l1=[6,7,8,9]
for a,b in zip(l,l1):
    print(a,b)

print("****  other function 2+ list iteration  ****")
l=[10,20,30,40,50,60,70]
l1=[3,4,5,6,7,8]
t=len(l)

for h in range(t):
    print(l[h],l1[h])


