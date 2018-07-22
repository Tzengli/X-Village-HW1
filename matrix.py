import random

from copy import deepcopy


class Matrix:

    def __init__(self, nrows, ncols):
        """Construct a (nrows X ncols) matrix"""
        self.c=[]
        for i in range(nrows):
            self.d=[]
            for j in range(ncols):
                self.d.append(random.randint(0,9))
            self.c.append(self.d) 
            
    def display(self):
        for i in range(row):   
            for j in range(clown):
                print(self.c[i][j],end=' ')
            print('')

    def add(self,m):
        f = []
        for i in range(row):
            e = []
            for j in range(clown):
                e.append(matrix1.c[i][j]+m.c[i][j])
            f.append(e)    
        return f

    def minor(self,m):
        f = []
        for i in range(row):
            e = []
            for j in range(clown):
                e.append(matrix1.c[i][j]-m.c[i][j])
            f.append(e)    
        return f

    def transpose(self):
        result = Matrix(row, clown)
        for i in range(row):
            for j in range(clown):
                result.c[j][i] = matrix1.c[i][j]
        return result
                     

    def mul(self, m):
        """return a new Matrix object after multiplication"""
        
        result = Matrix(row, clown)
        for i in range(0,len(self.c)):
            for j in range(0,len(m.c[0])):
                result.c[i][j] = 0
                for p in range(0,len(self.c[0])):
                    result.c[i][j] = result.c[i][j] + self.c[i][p] * m.c[p][j]
                    
        return result
                     
   
row = int(input('please input rows:'))
clown = int(input('please input clowns:'))


matrix1 = Matrix(row,clown)
matrix2 = Matrix(row,clown)

print("matrix1 = ")
matrix1.display()
print('')
print("matrix2 = ")
matrix2.display()

print('--------A + B--------')
print(matrix1.add(matrix2))

print('--------A - B--------')
print(matrix1.minor(matrix2))

print('--------transpose A--------')
C = matrix1.transpose()
C.display()

print('--------A * B--------')
C = matrix1.mul(matrix2)
C.display()



