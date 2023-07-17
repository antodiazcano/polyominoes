import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


WIDTH = 1
HEIGHT = 1
EPSILON = 0.1

AZUL_OSCURO = "#051C2C"
AZUL_ELECTRICO = "#0EA9F0"


def draw_polyomino(M: np.array, ax: plt.Axes) -> None:
    
    """
    Draws the figure represented by the binary matrix M.
    
    Parameters
    ----------
    M   : Matrix where a 1 represents a square in that coordinates and 0 if
          there is nothing in that position.
    axs : Matplotlib axes where to plot the figure.
    """
    
    rows, cols = M.shape
    ax.set_xlim(0-EPSILON, cols+EPSILON)
    ax.set_ylim(0-EPSILON, rows+EPSILON)
    ax.set_aspect("equal")
    ax.axis("off")
    
    for x in range(rows):
        for y in range(cols):
            if M[x][y] == 1:
                rect = Rectangle((y, rows-x-1), WIDTH, HEIGHT, facecolor=
                                 AZUL_ELECTRICO, edgecolor=AZUL_OSCURO)
                ax.add_patch(rect)

