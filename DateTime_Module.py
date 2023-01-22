import datetime

x=datetime.datetime.now()
print(x)
x=datetime.datetime(2023,1,31)
print(x)
x=datetime.datetime(2023,1,31,3,25,46,46)
print(x)

#strftime()-format date and time
# %b   Dec      %Y  2023    %M 48mins
# %B   December %H  18 hrs
# %m   12       %I  6  hrs
# %y   23       %P  AM/PM

x=datetime.datetime.now()
m=x.strftime("%Y")
print(m)
m=x.strftime("%H")
print(m)
m=x.strftime("%M")
print(m)
m=x.strftime("%I")
print(m)