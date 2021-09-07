def checkBomb(field, x, y): 
    number = 0 
    # field mxn 
    m = len(field) 
    n = len(field[0]) 

    if x-1 >= 0 and field[x-1][y] == True: 
        number += 1 

    if x+1 < m and field[x+1][y] == True: 
        number += 1 

    if y-1 >= 0 and field[x][y-1] == True: 
        number += 1 

    if y+1 < n and field[x][y+1] == True: 
        number += 1 

    if x-1>=0 and y-1>=0 and field[x-1][y-1] == True: 
        number += 1 

    if x-1>=0 and y+1<n and field[x-1][y+1] == True: 
        number += 1 

    if x+1<m and y-1>=0 and field[x+1][y-1] == True:
        number += 1  

    if x+1<m and y+1<n and field[x+1][y+1] == True: 
        number += 1 

    return number 
def checkMatrix(field, matrix, x, y): 
    # matrix mxn
    m = len(field) 
    n = len(field[0]) 
    if x<0 or x>=m or y<0 or y>=n or matrix[x][y]!=-1:
        return
    first = checkBomb(field, x, y)  
    matrix[x][y] = first
    if first != 0: 
        return
    else:
        checkMatrix(field,matrix, x-1, y) 
        checkMatrix(field,matrix, x+1, y) 
        checkMatrix(field,matrix, x, y-1) 
        checkMatrix(field,matrix, x, y+1) 
        checkMatrix(field,matrix, x-1, y-1) 
        checkMatrix(field,matrix, x-1, y+1) 
        checkMatrix(field,matrix, x+1, y-1)  
        checkMatrix(field,matrix, x+1, y+1)  

def minesweeperClick(field, x, y): 
    """
    minesweeperClick [summary]

    Args:
        field ([type]): [description]
        x ([type]): [description]
        y ([type]): [description]

    Returns:
        [type]: [description]
    """
    matrix = [[-1]*len(field[0]) for _ in range(len(field))] 
    first = checkBomb(field, x, y) 
    if first == 0: 
        checkMatrix(field, matrix, x, y) 
        return matrix 
    else: 
        matrix[x][y] = first 
    return matrix 


# Test

field = [[True, False, True, True, False], 
         [True, False, False, False, False], 
         [False, False, False, False, False], 
         [True, False, False, False, False]] 
x = 3
y = 2

""" The output should be 
minesweeperClick(field, x, y) = [[-1, -1, -1, -1, -1], 
                                 [-1, 3, 2, 2, 1], 
                                 [-1, 2, 0, 0, 0], 
                                 [-1, 1, 0, 0, 0]] 
"""
print(minesweeperClick(field, x, y))