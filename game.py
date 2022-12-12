import sys
import numpy as np

def ColWin(x, mat):
    for i in range(0,x):
        for j in range(0,x-2):
            if mat[i][j] != None:
                if mat[i][j] == mat[i][j+1] and mat[i][j] == mat[i][j+2]:
                    return mat[i][j]
    return -1

def RowWin(x, mat):
    for i in range(0,x):
        for j in range(0,x-2):
            if mat[j][i] != None:
                if mat[j][i] == mat[j+1][i] and mat[j][i] == mat[j+2][i]:
                    return mat[j][i]
    return -1

def checkDiagonals(x, mat):
    for i in range(2,x-2):
        for j in range(0,x-2):
            if mat[j][i] != None:
                m1 = mat[i][j]
                m2 = mat[i-1][j+1]
                m3 = mat[i-2][j+2]
                if m1==m2 and m1==m3:
                    return mat[i][j]

    for i in range(0,x-2):
        for j in range(0,x-2):
            if mat[j][i] != None:
                m1 = mat[i][j]
                m2 = mat[i+1][j+1]
                m3 = mat[i+2][j+2]
                if m1==m2 and m1==m3:
                    return mat[i][j]
    
    return -1

def checkWin(x,mat):
    winner = ColWin(x,mat)
    if winner != -1:
        print("Le gagnant est :", winner)
        quit()

    winner = RowWin(x,mat)
    if winner != -1:
        print("Le gagnant est :", winner)
        quit()

    winner = checkDiagonals(x, mat)
    if winner != -1:
        print("Le gagnant est :", winner)
        quit()



def Joue(taille, z, x, y, mat):
    if x=="STOP" or y=="STOP":
        quit()
    else:
        x=int(x)
        y=int(y)
        print(mat[x][y])
    if mat[x][y]!=None or (x<0 or x>=taille or y<0 and y>=taille):
        x=input()
        y=input()
        Joue(taille,z,x,y,mat)
    else:
        mat[x][y]=z

def End(taille):
    for i in range(0, taille):
        for j in range(0, taille):
            if mat[i][j]==None:
                return 0
    return -1

turn=0

for i in range(1, len(sys.argv)):
    print('argument:', i, 'value:', sys.argv[i])

rows = int(sys.argv[1])
cols = int(sys.argv[1])
taille = rows*cols
mat = np.array([None]*taille).reshape(rows,cols)
while End(rows)==0:
    c1=input()
    c2=input()
    Joue(rows, turn, c1, c2, mat)
    print(mat)
    checkWin(rows,mat)
    turn=(turn+1)%2
print('égalité')
quit()
#mat = [[0,2,7,4,5],[7,7,7,8,9],[7,11,7,12,13],[0,0,52,0,0], [0,0,52,0,0]]