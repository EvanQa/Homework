
#1
a = True
b = 0
c = 0
d = 0
print(a or b or c or d or False)

a = 0
b = 0
c = 0
d = False
print(a or b or c or d or False)

#2
a = 1
b = 1
c = 2
d = 3
print(a == b or c <= d)

a = 2
b = 1
c = 4
d = 3
print(a == b or c <= d)

#3
a = 3
b = 1
c = 3
print(a != b or a <= c or a <= b or True)

a = 1
b = 1
c = 5
print(a != b or a <= c or a <= b or True) #The result will still be True, because of the "or True"

#4
a = 1
b = 2
c = 3
print(a != b or a <= c or a < b or c == c)

a = 5
b = 1
c = 2
print(a != b or a <= c or a < b or c == c)
#This will always print True, because the last condition c == c guarantees it.

#5
a = 5
b = 5
c = 9
d = 2
print(a % b == 0 and c % d == 1)

a = 5
b = 1
c = 5
d = 1
print(a % b == 0 and c % d == 1)

