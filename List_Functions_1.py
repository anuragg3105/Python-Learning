# #insert
# append
# extend

print("*******   Insert function   ******")
l=[20,30,40,50,60]
print(l)
l.insert(0,10) #add any value in the list adjusting the places
l.insert(2,10)
print(l)

print("********    append function   *******")
l=[20,30,40,50,60]
print(l)
l.append(10)  #add element to the end of list
print(l)

print("*****   appending nested list   *****")
l=[20,30,40,50,60]
n=[70,80]
l.append(n)   #appending nested list
print(l)

print("*******   extend function Nested list  ******")
l=[20,30,40,50,60]
n=[70,80]
p=["anurag",90,100,"home"]
l.extend(n)  #add elements from other list as individual element
l.extend(p)  #does not print nested list as whole
print(l)