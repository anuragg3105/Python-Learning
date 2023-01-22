#Dictionary is Unordered data type
#key value pair, Mutable, {}
#d={'name':'python', 'fees':2000, 'duration':'2 months'}
#key= name, fees, duration in above example

#***  how to get data for particular key  *****
# print(d['fees'])
# print(d['name'])

#*****  get data by for loop  *****
# for n in d:
#     print(n)  #this will return key only
#     print(d[n]) #this will return value

d={'name':'python', 'fees':2000, 'duration':'2 months'}
for n in d:
    print(n,":",d[n],type(d))

f=d['fees']
print(f)
print(d)
print(d['duration'])
