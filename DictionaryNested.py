#Nested Dictionary
course={
    'php':{'duration':'2 months','amt':500},
    'python':{'duration':'3 months','amt':600},
    'java':{'duration':'4 months','amt':700}
}
print(course)

print("***  Update Nested Dictionary  ***")
course.update({'php':{'duration':'12 months'}})
course['java']['duration']:"19 months"
print(course)

print("***  ADD NEW KEY as nested dict  ***")
course['c++']={'duration':'7 months', 'amt':800}
print(course)

print("***  Print particular Nested Dictionary key value  ***")
print(course)
print(course['php']['duration'])

print("***  Print list using iteration  ***")
for a,b in course.items():
    print(a,b)

# for a,b in course.items():
#     print(a,b['duration'],b['amt'])
