w="welcome home"
print(w[6])
print(w[-1])  #reverse index
print(w[-2])

#slicing of word in string
print(w[0:7])

#increment of 2 character
print(w[0::2])
print(w[3::2])

#reverse slicing
print(w[-1::-2])
print(w[-1::-1])
print(w[-2::-1])

#to reverse a string
print(w[-1::-1])

#*****************  String iteration  *************
w="welcome to paramount"
t=len(w)
print(t)
for i in range(t):
    print(w[i])
    i=i+1

#*************  reverse iteration  ****************
for i in range(t-1,-1,-1):
    print(w[i])

#without using range
w="welcome home"
for a in w:
    print(a)

