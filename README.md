# Introduction

A **polyomino** is a plane geometric figure formed by joining one or more equal squares edge to edge. It is a polyform whose cells are squares. They are clasified by the number of squares they have, usually called ***n***. More information can be found in this [link](https://en.wikipedia.org/wiki/Polyomino). Some examples are the following:

![image](https://github.com/antodiazcano/polyominoes/assets/114878742/f0922c7e-ccf3-46ee-98b9-4f0295abf714)

The code in this repo obtains all possible non-isomorphic polyominoes made of *n* squares. It is important to emphasize in the non-isomorphic property to avoid adding the same ones but rotated, reflected or both at the same time. In the code they are represented by **binary matrixes** where a 1 means a square there and a 0 an empty cell.

# Explanation of the files

***_drawing.py*** contains the code to draw a polyomino given its matrix, ***polyomino.py*** is the class to represent polyominoes and apply transformations to them and ***search.py*** obtains the set of non-isomorphic polyominoes for *n*. Finally, some examples are in the notebook ***usage_example.ipynb***.
