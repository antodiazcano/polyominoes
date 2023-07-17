import numpy as np
import matplotlib.pyplot as plt
from _drawing import draw_polyomino



class Polyomino:
    
    
    """ Class to represent a polycube by a binary matrix. """
    
    
    def __init__(self, M: np.array) -> None:
        
        """
        Constructor of the class.
        
        Parameters
        ----------
        M : Binary square matrix with a 1 if there is a cube in that position
            and 0 otherwise.
        """
        
        self.matrix = M
        
        
    def rotate_90(self, k: int = 1) -> None:
        
        """
        Rotates the matrix 90 degrees k times.
        
        Parameters
        ----------
        k : Number of times we do the rotation (note that with k=4 the
            resulting matrix is the same).
        """
        
        self.matrix = np.rot90(self.matrix, k)
    
    
    def reflect_vertical(self) -> None:
        
        """
        Reflects the matirx vertically.
        """
        
        self.matrix = np.flipud(self.matrix)
    
    
    def reflect_horizontal(self) -> None:
        
        """
        Reflects the matirx horizontally.
        """
        
        self.matrix = np.fliplr(self.matrix)
        
    
    def reduce(self) -> None:
        
        """
        Eliminates the rows and columns wich are all 0s to obtain the reduced
        version of the matrix.
        """
        
        for i in range(self.matrix.ndim):
            self.matrix = np.swapaxes(self.matrix, 0, i) # send i axis to front
            while np.all(self.matrix[0] == 0):
                self.matrix = self.matrix[1:]
            while np.all(self.matrix[-1] == 0):
                self.matrix = self.matrix[:-1]
            self.matrix = np.swapaxes(self.matrix, 0, i) # send i axis to its
                                                         # original position
        
        self.matrix = self.matrix.T
        
    
    def expand(self, i: int, j: int) -> None:
        
        """
        Expands a polyomino by adding one square. First it adds a zero pad
        around the matrix and then reduces the matrix if possible.
        
        Parameters
        ----------
        i, j : Coordinates of the added 1 in the new matrix.
        """
        
        # Zero padding
        rows, cols = self.matrix.shape
        new_array = np.zeros((rows+2, cols+2))
        new_array[1:1+rows, 1:1+cols] = self.matrix
        self.matrix = new_array
        
        # Add the 1 and reduce
        self.matrix[i][j] = 1
        self.reduce()
    
    
    def draw(self, axs: plt.Axes) -> None:
        
        """
        Draws the polyomino.
        
        Parameters
        ----------
        axs: Matplotlib axes where to plot the figure.
        """
        
        draw_polyomino(self.matrix, axs)
        
