import array as a
an=[1,2,3,4,5,6,7,8,9,0]
b=a.array('i',an)

print(b[0])
print(b[:8])
print(b[8:])
print(b[-8:])
print(b[:-8])
print(b[0:4])

an[0]=10
an[1:4]=a.array('i',[11,22,33])

print(an)