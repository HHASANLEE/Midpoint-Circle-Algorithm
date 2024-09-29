import matplotlib.pyplot as plt

def draw_circle(x_center, y_center, radius):
    # Function to plot the points
    def plot_circle_points(x_center, y_center, x, y):
        plt.plot(x_center + x, y_center + y, 'bo' )  # First Octant
        plt.plot(x_center - x, y_center + y, 'bo' )  # Second Octant
        plt.plot(x_center + x, y_center - y, 'bo' )  # Eighth Octant
        plt.plot(x_center - x, y_center - y, 'bo' )  # Seventh Octant
        plt.plot(x_center + y, y_center + x, 'bo' )  # Fourth Octant
        plt.plot(x_center - y, y_center + x, 'bo' )  # Third Octant
        plt.plot(x_center + y, y_center - x, 'bo' )  # Fifth Octant
        plt.plot(x_center - y, y_center - x, 'bo' )  # Sixth Octant

    # Starting point at (0, radius)
    x = 0
    y = radius
    d = 1 - radius  # Initial decision parameter

    plot_circle_points(x_center, y_center, x, y)

    while x < y:
        x += 1
        if d < 0:
            d += 2 * x + 1  # Choosing E pixel
        else:
            y -= 1
            d += 2 * (x - y) + 1  # Choosing SE pixel
        plot_circle_points(x_center, y_center, x, y)

# Example usage:
x_center = 0
y_center = 0
radius = 10
draw_circle(x_center, y_center, radius)

# Display the circle
plt.gca().set_aspect('equal', adjustable='box')
plt.show()