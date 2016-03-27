# Matrix Algebra


import numpy as np

A = np.matrix('1 2 3; 2 7 4')
B = np.matrix('1 -1; 0 1')
C = np.matrix([[5,-1],[9,1],[6,0]])
D = np.matrix([[3,-2,-1],[1,2,3]])
u = np.array([[6,2,-3,5]])
v = np.array([[3,5,-1,4]])
w = np.array([[1],[8],[0],[5]])
alpha = 6

#Part 1
A.shape
#(2, 3)
B.shape
#(2, 2)
C.shape
#(3, 2)
D.shape
#(2, 3)
u.shape
#(1, 4)
w.shape
#(4, 1)


#Part 2
print(u + v)
#[[9 7 -4 9]]

print(u - v)
#[[3 -3 -2 1]]

print(a * u)
#[[36 12 -18 30]]

print(np.dot(u, v.T))
#[[51]]

print(np.linalg.norm(u))
#8.60232526704



#Part 3
print(np.add(A, C))
#operands could not be broadcast together with shapes (2,3) (3,2)

print(np.subtract(A, C.T))
#[[-4 -7 -3]
# [ 3  6  4]]

print(np.add(C.T, 3*D))
#[[14  3  3]
# [ 2  7  9]]

print(np.dot(B, A))
#[[ -1 -5 -1]
# [ 2  7  4]]

print(np.dot(B, A.T))
#shapes (2,2) and (3,2) not aligned: 2 (dim 1) != 3 (dim 0)
