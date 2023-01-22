#Get()
# Keys()
# Values()
# Items()

#Get()
print("*****  Get function ***** ")
d={'name':'python', 'fees':2000, 'duration':'2 months'}
print(d.get('name'))  #fetch value from key
print(d.get('fees'))
print(d.get('duration'))

print("*****  Key function ***** ")
print(d.keys())
print("*****  Values function ***** ")
print(d.values())
print("*****  Item function ***** ")
print(d.items())

print("*****  Key function 2***** ")
for a in d.keys():
    print(a)

print("*****  Values function 2 ***** ")
for a in d.values():
    print(a)

print("*****  Item function 2 ***** ")
for a,b in d.items():
    print(a," : ",b)