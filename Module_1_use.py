import Module_1_create

#method 1
print(Module_1_create.sum(10,20))
print(Module_1_create.mul(10,20))

#method 2
a=Module_1_create.sum(10,20)
b=Module_1_create.mul(10,20)
print("Sum is:", a,"Product is:",b)

#method 3
print("***  No need to use module.function name now  ***")
from Module_1_create import sum
print(sum(10,40))

#TO short module name - alias
import Module_1_create as mp
print("To make alias of module name")
print(mp.sum(10,60))
print(mp.mul(10,50))

#To call all function at once
print("***  To call all func at once  ***")
from Module_1_create import * #cannot use alias here
print(sum(10,20))
print(mul(10,40))





