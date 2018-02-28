import math


def print_matrix( matrix ):
    ctr = 0
    while (ctr < len(matrix)):
        print (matrix[ctr])
        ctr += 1;

def ident( matrix ):
    ident = []
    for r in range(4):
        ident.append([])
        for c in range(4):
            if r==c:
                ident[r].append(1)
            else:
                ident[r].append(0)
    return ident

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    temp = new_matrix(len(m2[0]), len(m2) )
    for r in range(len(m1[0])):
        for co in range(len(m2)):
            c=0
            for i in range( 4 ):
                c += m1[i][r] * m2[co][i]
            temp[co][r] = c
    for co in range(len(temp)):
        for r in range( len(temp[0]) ):
            m2[co][r] = temp[co][r]


def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
