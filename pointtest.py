from point import *
p1 = point(3,[1.,2.,3.])
p2 = point(3,[6.,7.,8.])
print(p1)
print(p2)
print ("p1 + p2", p1.dist(p2))
print ("Inverted Direction of p2", p2.mirror())
