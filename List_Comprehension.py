# #list comprehension
# elelegant way to define and create list based on existing
# lists
#more compact and faster than function and loop

print('''
*****  normal list print  ******''')
l=[]
for a in range(1,101,1):
    l.append(a)
print(l)

#comprehension method
print('''
******  comprehension list print  ******''')
n=[m for m in range(1,101)]
print(n)

#filter in result
print('''
******  filters in comprehension list print  ******''')
n=[m for m in range(1,101) if m%2==0]
print(n)
n=[m for m in range(1,101) if m<=60]
print(n)
n=[m for m in range(1,101) if m>60]
print(n)

#practice
s="hello paramount"
d=[g for g in s]
print(d)
d=[g for g in s if g=='l']
print(d)