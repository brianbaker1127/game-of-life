# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 13:40:14 2021

@author: Brian Baker
@email: BrianBaker2021@u.northwestern.edu

"""

import csv

def calculate_new_grid(M):
    """param: matrix -> List[List] of binary numbers 0 and 1
       rtype: matrix -> List[List] of binary numbers 0 and 1
       
       This function sweeps through the inputted matrix to determine
       which matrix elements survive the game of life. It returns the 
       new matrix.
    """
    
    """make a copy of matrix to write to"""
    
    M_new = [row[:] for row in M]
    
    
    gridwidth = len(M[0])
    grid_depth = len(M)
    
    alive = 1
    dead = 0
    resurrection_condition = 3
    underpopulation_threshold = 2 
    overcrowding_threshold = 3

    for i in range(grid_depth):
        for j in range(gridwidth):
            
            """reset the list of neighbors"""
            neighbors = []
           
            """find who the (up to 8 total) neighbors are:"""
            neighbors.append(fetch_neighbor(i-1,j,M))
            neighbors.append(fetch_neighbor(i+1,j,M))
            neighbors.append(fetch_neighbor(i,j-1,M))
            neighbors.append(fetch_neighbor(i,j+1,M))
            neighbors.append(fetch_neighbor(i-1,j-1,M))
            neighbors.append(fetch_neighbor(i-1,j+1,M))
            neighbors.append(fetch_neighbor(i+1,j-1,M))
            neighbors.append(fetch_neighbor(i+1,j+1,M))
            
            """count the survivors"""
            live_neighbors = neighbors.count(alive)
            
            """find out whether the matrix element is dead or alive"""
            element = M[i][j]
            
            if element == dead:
                """resurrect the element if it has exactly 3 live neighbors"""
                if live_neighbors == resurrection_condition:
                    M_new[i][j] = alive
                
                
            else:
                """kill the element if it doesn't have 2 or 3 live neighbors"""
                if live_neighbors < underpopulation_threshold or live_neighbors > overcrowding_threshold:
                    M_new[i][j] = dead
    
    return M_new
            
    
    
    
    
def fetch_neighbor(row,column,mat):
    """ param: row -> int
        param: column -> int
        param: matrix -> List[List]
        rtype: int - if neighbor exist and None - if neighbor does not exist, i.e. for boundary elements
        
        This function adds the value of a matrix element to a list, if it exists.
    """
    
    """need to handle the boundary elements - do NOT accept negative indices.
       If the indices are outside of the matrix range, return None."""
    if row < 0 or column < 0:
        return None
    
    try:
        return mat[row][column]
        
    except IndexError:
        pass
        
    
def filewrite(file_path, mat):
    """param: file_path -> string
       param: mat -> List[List]
    """
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(mat)
        
def fileread(file_path):
    """param: file_path -> string
       rtype: List[List]
    """
    with open(file_path, "r", newline="") as file:
        reader = csv.reader(file)
        return [[int(element) for element in row] for row in reader]
    

if __name__ == "__main__":
    
    inputmatrix = fileread("life grid.csv")
    outputmatrix = calculate_new_grid(inputmatrix)
    filewrite("life grid updated.csv",outputmatrix)   
        
    
    

