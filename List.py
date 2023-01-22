#list is mutable, comma separated, []
#print(L[3])
L=[1,2,3,4,'a','b','c']
a=len(L)
for i in range(a):
    print(L[i])

#nested list
print("nested list")
r=[1,2,3,[4,5],['a','b']]
print(r[3])
print(r[3][0])   #to display particular element in
print(r[3][1])   # nested list
print(r[4])

#slicing list
print("slicing list")
print(r[0:3])
print(r[0:5:2])   #gap of 2
print(r[0:5:3])   #gap of 3
print(r[0: :2])   #gap in range means full length
print(r[-1::-1])  #reverse list

print("general queries")
b=[1,2,3,[4,5],('a','b')]
print(b,type(b))
print(b[0:3])
print(b[1],b[4])
print(b[3][1],b[4])
print(b[-1: :-2])
print(b[-1: :-1])
