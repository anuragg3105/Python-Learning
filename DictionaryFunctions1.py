# del and pop
#Update
#Clear
#Add new key value

# del and pop
print("****  Delete by DEL  ****")
d={'name':'python', 'fees':2000, 'duration':'2 months'}
del d['fees']  #del does not return the deleted value
print(d)

print("****  Delete by POP  ****")
d={'name':'python', 'fees':2000, 'duration':'2 months'}
a=d.pop('duration')        #delete the value of key
print("Deleted value:",a)  #print the deleted value of key
print(d)

#Update
print("****  Update  ****")
d={'name':'python', 'fees':2000, 'duration':'2 months'}
d.update({'fees':8020})    #1st method
d['duration']="6 months"   #2nd method
d["name"]="Anurag"
print(d)

#Clear
print("****  Clear  ****")
d={'name':'python', 'fees':2000, 'duration':'2 months'}
d.clear()
print(d)

#Add new key value
print("****  Adding new value to dict  ****")
d={'name':'python', 'fees':2000, 'duration':'2 months'}
d['desc']="This is python"
d['school']="KV"
print(d)


