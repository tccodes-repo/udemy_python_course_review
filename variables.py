''' Session discusion on Python variables and dynamic typing
'''
a = 1
b = a

print(a)
print(b)
print(id(a))
print(id(b))

b = 17

print(a)
print(b)

print(id(a))
print(id(b))


name = "Keith"
name = 5



print(id(name))
name = name + " Kelly"
print(name)
print(id(name))



m = [1,2,3]
n = m
p = m.pop()
print(m)
print(n)

n = [8,9]
print(m)
print(n)

listA = [0]
listB = listA
listB.append(1)
print(listA)