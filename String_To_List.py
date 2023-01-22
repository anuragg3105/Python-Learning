# # Program to convert string/word into list
# # Split function
print("*** String to list using split function ***")
l=(input("Enter a String : "))
print(l)
m=l.split()
print(m)

print("*** String to list when multiple input ***")
a=[]
for i in range(1,4):
    n=input("Enter the value "+str(i)+":")
    a.append(n)
print(a)

#if you want to split one list also : m = n.split()
a=[]
for i in range(1,4):
    n=input("Enter the value "+str(i)+":")
    m = n.split()
    a.append(m)

print(a)