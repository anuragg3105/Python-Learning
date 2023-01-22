#find() index() isalpha() isdigit() isalnum()

w="Welcome to paramount"

#**********  find()  ***********
print(w.find('e')) #only return 2st occurence index
print(w.find('o'))
print(w.find('m'))
print(w.find('t'))
print(w.find('z')) # return -1 if not found
#changing search start postion
print(w.find('e',2))

#********** index()  ***********
print(w.index('p'))
print(w.index('z'))  #index does not return -1 if not found
print(w.index('a',13))

a="welcome home"
print(a.isalpha())
print(a.isdigit())
print(a.isalnum())  #combination of alpha and num

b="123456"
print(b.isalpha())
print(b.isdigit())
print(b.isalnum())

c="welcomehome123"
print(c.isalpha())
print(c.isdigit())
print(c.isalnum())  #isalnum count space as a special character
                    # and returns false