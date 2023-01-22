#count, max, min, sort, reverse, index

l=[1,2,3,4,5,3,4,9,2,1,7,4,2,4,9]

#count
print('''***** count *****''')
a=l.count(2)
print(a)

#max
print('''***** max *****''')
print(max(l))
p=["hello","world"]
print('''***** max string*****''') #position of alphabet in numbers
print(max(p))

#min
print('''***** min *****''')
print(min(l))
p=["hello","world"]
print('''***** min string *****''')
print(min(p))

#sort
print('''***** sort *****''')
l.sort()       #a=sorted(l)
print(l)

#reverse
print('''***** reverse *****''')
l.reverse()
print(l)

#index
print('''***** index *****''')
print(l.index(5))
print(l.index(4))
p=["hello","paramount","anurag","boy","amazon"]
print(p.index("anurag"))

