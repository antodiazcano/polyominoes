import numpy as np
import matplotlib.pyplot as plt
from polyomino import Polyomino
from typing import List


def _check_isomorphic(P1: Polyomino, P2: Polyomino) -> bool:
    
    """
    Checks if two figures are isomorphic (by rotation, reflexion or any of
    them combined).
    
    Parameters
    ----------
    P1, P2     : Matrixes of the corresponding figures.
    
    Returns
    -------
    isomorphic : True if they are isomorphic and False otherwise.
    """
    
    isomorphic = False
    
    for _ in range(4):
        if np.all(P1.matrix == P2.matrix):
            isomorphic = True
            break
        P1.reflect_horizontal()
        if np.all(P1.matrix == P2.matrix):
            isomorphic = True
            break
        P1.reflect_vertical()
        if np.all(P1.matrix == P2.matrix):
            isomorphic = True
            break
        P1.rotate_90()
    
    return isomorphic


def _get_expanded_set(M: np.array) -> List[np.array]:
    
    """
    Given a polyomino obtains a list with all new possible polyonimos by
    adding one square. Note that dimensions can change.
    
    Parameters
    ----------
    M            : Polyomino matrix.
    
    Returns
    -------
    expanded_set : New possible polyominos.
    """
    
    # Obtain the coordinates where there is a 1
    coords = []
    rows, cols =  M.shape
    for i in range(rows):
        for j in range(cols):
            if M[i][j] == 1:
                coords.append([i, j])
    
    # Create new matrixes
    expanded_set = []
    for coord in coords:
        i, j = coord
        # left
        if (j == 0) or (j > 0 and M[i][j-1] == 0):
            new_i, new_j = i+1, j
            temp_polyomino = Polyomino(M)
            temp_polyomino.expand(new_i, new_j)
            expanded_set.append(temp_polyomino.matrix)
        # right
        if (j == cols-1) or (j < cols-1 and M[i][j+1] == 0):
            new_i, new_j = i+1, j+2
            temp_polyomino = Polyomino(M)
            temp_polyomino.expand(new_i, new_j)
            expanded_set.append(temp_polyomino.matrix)
        # up
        if (i == 0) or (j > 0 and M[i-1][j] == 0):
            new_i, new_j = i, j+1
            temp_polyomino = Polyomino(M)
            temp_polyomino.expand(new_i, new_j)
            expanded_set.append(temp_polyomino.matrix)
        # down
        if (i == rows-1) or (i < rows-1 and M[i+1][j] == 0):
            new_i, new_j = i+2, j+1
            temp_polyomino = Polyomino(M)
            temp_polyomino.expand(new_i, new_j)
            expanded_set.append(temp_polyomino.matrix)
                
    return expanded_set


def get_set(prev_set: List[np.array]) -> List[np.array]:
    
    """
    Obtains the set of polyominoes of n cubes.
    
    Parameters
    ----------
    prev_set : Previous set of polyominoes (for n-1).
    
    Returns
    -------
    new_set  : New set of polyominoes.
    """
    
    new_set = []
    
    for array in prev_set:
        new_arrays = _get_expanded_set(array) # expanded set for array
        for new_array in new_arrays:
            # Check if new_array is already in new_set
            flag = True
            for arr in new_set:
                if _check_isomorphic(Polyomino(new_array), Polyomino(arr)):
                    flag = False
            if flag:
                new_set.append(new_array)
    
    return new_set


def draw_set(arrays: List[np.array]) -> None:
    
    """
    Draws all non isomorphic polyominoes of size n.
    
    Parameters
    ----------
    arrays : List with the matrix of each polyomino.
    """
    
    nn = len(arrays) // 2 if len(arrays) % 2 == 0 else len(arrays) // 2 + 1
    fig, axs = plt.subplots(nn, 2)
    n = np.max([arr.shape for arr in arrays])
    fig.suptitle("All non isomorphic polyominos for $n = $" + str(n),
                 x=0.55, y=0.95)
    
    i = 0
    count = 0
    for arr in arrays:
        P = Polyomino(arr)
        if nn <= 2:
            P.draw(axs[i])
        else:
            P.draw(axs[count][i])
        i += 1
        if i % 2 == 0:
            count += 1
            i = 0
    
    if nn % 2 == 1:
        if nn <= 2:
            axs[i].axis("off")
        else:
            axs[count][i].axis("off")

