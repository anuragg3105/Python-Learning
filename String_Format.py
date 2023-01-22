#named indexes
txt1="welcome to {f}{l}".format(f="anurag",l="  house")

#numbered indexes
txt2="welcome to {0}{1}".format("anurag","  house")

#empty placeholder
txt3="welcome to {}{}{}".format("anurag"," house ","noida")
print(txt1)
print(txt2)
print(txt3)

q="welcome {1} to {0} home".format("guys","anurag")
r="welcome {lname} to {fname} home".format(lname="guys",fname="anurag")
print(q)
print(r)

#{l:10} means length is specified for the format block
d="welcome {b:10} to {a} home".format(b="guys",a="anurag")
print(d)
#output: "welcome guys       to anurag home"

#If you want string to be in left/center/right
print('''
****string format left center right adjustment*****
''')
d="welcome {b:>10} to {a} home".format(b="guys",a="anurag")
print(d)
d="welcome {b:^10} to {a} home".format(b="guys",a="anurag")
print(d)
d="welcome {b:<10} to {a} home".format(b="guys",a="anurag")
print(d)