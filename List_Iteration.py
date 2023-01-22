L=[1,2,'a','b',['p','q'],5,6]

print("method 1")
a=len(L)
for i in range(a):
    print(L[i])

print("method 2")
for i in L:
        print(i)

print("reverse list print")
for n in range(a-1,-1,-1):
    print(L[n])


