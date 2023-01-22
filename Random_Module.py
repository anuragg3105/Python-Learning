# randint()-Return number between a and b (both included)
# randrange()-Return number between a(included)and b(excluded)
# choice()-randon element from list
# random()- return random float no. b/w 0 and 1
# shuffle()- take sequence and return it in random order
# uniform()- return random float b/w two give no.

import random

#**********   randint  *************
print(random.randint(1,10)) #both 1 and 10 included

#**********   randrange **********
print(random.randrange(1,5)) #only 1 included, 5 excluded

#**********  choice  **********
l=[1,2,3,"anurag","hello",{1,2,3},[4,5,6],(7,8,9)]
print(random.choice(l))
#to see the type of random element
a=random.choice(l)
print(a,type(a))

#**********  random   **********
print(random.random())

#**********  shuffle   **********
l=[1,2,3,4,5,6,7,8,9,0]
random.shuffle(l)
print(l)

#**********  uniform   **********
print(random.uniform(7,9))