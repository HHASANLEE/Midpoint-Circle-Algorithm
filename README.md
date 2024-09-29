1. Circle Equation
A circle's equation in a 2D plane with center (xc, yc) and radius r is:
          (x-xc)^2+(y-yc)^2=r^2
The Midpoint Circle Algorithm exploits the fact that for any point on the circle, the slope of the curve is between -1 and 0 in the first octant.
By calculating one octant of points and reflecting them, the algorithm draws the entire circle.

2. Starting Conditions
The algorithm starts at the top point of the circle, (0,r)and works its way counterclockwise, calculating the next point using the decision variable 𝑑
which helps to decide whether to move horizontally or diagonally:
          Starting point: (x,y)=(0,r)
          Decision parameter: d = -r

3. Decision Parameter
The decision parameter helps determine whether to move east (increment x) or southeast (increment x and decrement y) for each pixel along the circle's perimeter.
Formula:
For the current pixel (x,y), the next pixel can either be:
East (E): (x+1,y)
Southeast (SE): (x+1,y-1)

The algorithm uses the decision parameter d to choose between these two options:
If d<0, the next point is East (E), so only x is incremented.
If d≥0, the next point is Southeast (SE), so both x is incremented and y is decremented.

4.Updating the Decision Parameter
The decision parameter d is updated for the next iteration:
If the next point is East: dn=d+2x+1
If the next point is Southeast: dn=d+2x-2y+1
These updates allow the algorithm to use integer arithmetic, which is faster than floating-point calculations, making the algorithm efficient for computer graphics.

5.Symmetry
The algorithm computes points for only one octant of the circle. By leveraging symmetry, these points are reflected to the other seven octants.
This drastically reduces the number of points that need to be calculated.

Symmetric Points:
For every point (x,y) in the first octant, the corresponding points in the other octants are:
(x,y)
(-x,y)
(x,-y)
(-x,-y)
(y,x)
(-y,x)
(y,-x)
(-y,-x)

6. Loop Termination
The algorithm continues plotting points until x≥y, which indicates that the algorithm has covered the full octant.

7.Algorithm Steps
1) Initialize 𝑥=0,y=r, and d=1−r.
2) Plot the initial point (x,y) and reflect to other octants.
3) While x≤y, repeat:
   If d<0, move East: update d=d+2x+1.
   If d≥0, move Southeast: update d=d+2x−2y+1, and decrement y.
4) End when x>y.

8.The Midpoint Circle Algorithm is efficient because it only uses integer arithmetic, and it avoids expensive calculations 
like square roots and trigonometric functions. It is widely used in computer graphics systems for drawing circles and arcs.
