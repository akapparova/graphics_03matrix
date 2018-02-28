from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 255 ]
matrix = new_matrix(4, 4)



print ("matrix")
print_matrix(matrix)
print ("identity ")
ident(matrix)
print_matrix(matrix)

m1 = [[1,1,1,1],[2,2,2,2],[3,3,3,3],[4,4,4,4]]
print ("m1 " )
print_matrix(m1) 

print ("m2")
m2 = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
print_matrix(m2)


m2 = matrix_mult(m1, m2)

print ("new m2, after mult")
print_matrix(m2)


add_edge(m2, 4, 4, 4, 5, 5, 5)
print ("new m2, after adding edges")
print_matrix(m2)
