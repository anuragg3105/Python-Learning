#Tuple= (),Immutable: cannot be changed,Ordered data type
#No delete or update function available
#Function: Min, max, count, index, sum
t=(10,20,30,40,50)
print(t[3],type(t))

p=(1 ) #If tuple contains single value then it is not tuple
r=("anu")
print(p,type(p))
print(r,type(r))

print("***  For loop in tuple method 1  ***")
t=(10,20,30,40,50)
l=len(t)
for a in range(l):
    print(t[a])
print("***  For loop in tuple method 2  ***")
for a in t:
    print(a)

print("****   Functions in tupe   ****")

t=(10,20,30,40,50)
print("****  min  ****")
print(min(t))
print("****  max  ****")
print(max(t))
print("****  count  ****")
print(t.count(20))
print("****  index  ****")
print(t.index(30))
print("****  sum  ****")
print(sum(t))
S=sum(t,200) #if you want to add any number in whole tuple sum
print(S)