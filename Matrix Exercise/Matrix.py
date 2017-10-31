'''
Miniproyecto 2
Por:
Karelys Lopez Rivera
'''


class MyMatrix(object):
    def __init__(self,row,col):
        self.row=row
        self.col=col
        self.mat=[]

        for i in range(row):
            r=[]
            for j in range(col):
                r.append(0)
            self.mat.append(r)
            
    def identity_matrix(self,row,col):
        self.row=row
        self.col=col
        self.mat=[[0 for x in range(row)] for y in range(row)]
        for i in range(0,row):
            self.mat[i][i]=1
            
    def set(self,row,col,value):
        self.mat[row][col]=value
        
    def get(self,row,col):
        return self.mat[row][col]
    
    def mult(self,matrixb):
        result= [[0 for _  in range(self.col)] for _ in range(self.row)]
        for i in range(self.row):
            for j in range(len(matrixb[0])):
                for x in range(len(matrixb)):
                    result[i][j] += self.mat[i][x]*matrixb[x][j]
        return result
    
    def add(self,matrixb):
        result = [[0 for _ in range(self.col)] for _ in range(self.row)]
        for i in range(len(self.mat)):
            for j in range(len(self.mat[0])):
                result[i][j]=self.mat[i][j]+matrixb[i][j]
        return result
    
    def transpose(self):
        result=[[0 for _ in range(self.col)] for _ in range(self.row)]
        for i in range(len(self.mat)):
            for j in range(len(self.mat[0])):
                result[j][i]=self.mat[i][j]
        return result

    def sub(self,matrixb):
        result = [[0 for _ in range(self.col)] for _ in range(self.row)]
        for i in range(len(self.mat)):
            for j in range(len(self.mat[0])):
                result[i][j]= abs(self.mat[i][j]-matrixb[i][j])
        return result
                                  
    def scalar(self,value):
        result=[[0 for _ in range(self.col)] for _ in range(self.row)]
        for i in range(len(self.mat)):
            for j in range(len(self.mat[0])):
                result[i][j]=self.mat[i][j]*value
        return result
                                  
    def __repr__(self):
        outStr= ""
        for i in range(self.row):
            outStr += 'Row %s = %s\n' % (i+1, self.mat[i])
        return outStr
    
if __name__=="__main__":
    matrix= MyMatrix(2,2)
    matrix.set(0,0,2)
    matrix.set(0,1,1)
    matrix.set(1,0,5)
    matrix.set(1,1,2)

    print("Matrix A")
    print(matrix)

    matrixb= MyMatrix(2,2)
    matrixb.set(0,0,3)
    matrixb.set(0,1,2)
    matrixb.set(1,0,7)
    matrixb.set(1,1,1)

    print("Matrix B")
    print (matrixb)

    print('Sum: ')
    print(matrix.add(matrixb.mat))

    print ('Sub: ')
    print (matrix.sub(matrixb.mat))

    print ('Scalar Multiplication')
    print (matrix.scalar(5))

    print ('Mult: ')
    print (matrix.mult(matrixb.mat))

    print ('Transpose')
    print (matrix.transpose())

    print ('Identity Matrix')
    matrix.identity_matrix(6,6)
    print (matrix)
           
    
    
