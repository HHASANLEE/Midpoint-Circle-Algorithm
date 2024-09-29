import matplotlib.pyplot as plt

def DrawCircle(cx, cy, r):
    def plot_circle_points(cx, cy, x, y):
        plt.plot(cx + x, cy + y, 'bo' )  
        plt.plot(cx - x, cy + y, 'bo' )  
        plt.plot(cx + x, cy - y, 'bo' ) 
        plt.plot(cx - x, cy - y, 'bo' )  
        plt.plot(cx + y, cy + x, 'bo' )  
        plt.plot(cx - y, cy + x, 'bo' )  
        plt.plot(cx + y, cy - x, 'bo' )  
        plt.plot(cx - y, cy - x, 'bo' ) 

    x = 0
    y = r
    d = 1 - r

    plot_circle_points(cx, cy, x, y)

    while x < y:
        x += 1
        if d < 0:
            d += 2 * x + 1 
        else:
            y -= 1
            d += 2 * (x - y) + 1 
        plot_circle_points(cx, cy, x, y)

# Example :
cx = 0
cy = 0
r = 10
DrawCircle(cx, cy, r)

plt.gca().set_aspect('equal', adjustable='box')
plt.show()
