#Data types:
# [numeric]: 1. integer 2. float 3. complex number
# [sequence type] 1. string 2. list 3. tuple
# [dictionary]
# [set]

#Data types in python
#mutable (can be changes) :List , dictionary , byte array
#immutable(cannot be  changed): int, float,complex,string,tuple

#types
print("*****type*****")
a=5
print(a,type(a))
a=1+2j
print(a,type(a))
a=5.6
print(a,type(a))

#string
print("*****string*****")
s="this is a string"
print(s)
#multiline string
s='''line1
line2
line3'''
print(s)

#list
print("*****list*****")
a=[1,2.2,'ws']
print(a,type(a))
a[1]=3.5
print(a)

#tuple
print("*****tuple*****")
a=(5,'program',20)
print(a,type(a))
#a(2)=10  #cannot change values in tuple
print(a,type(a))

b=(10)
print(b,type(b))

#dictionary:unordered collection of key-value pair
print("*****dictionary*****")
d={
    'name':'python',
    'duration':'2 month'
}
print(d,type(d))
print(d['name'])
print(d['duration'])

#set
print("*****set*****")
my_set={1,2,3}
print(my_set)
my_set={1,1,2,2,3,3,4,4,5,6}  #set removes duplicates
print(my_set,type(my_set))

