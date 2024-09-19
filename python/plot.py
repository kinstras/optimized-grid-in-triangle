import numpy as np
import matplotlib.pyplot as plt
from utils import rotate_point, is_point_in_triangle

def update(val, ax, original_triangle, slider_angle, slider_vertical, L):
    angle = slider_angle.val
    vertical_shift = slider_vertical.val

    # Create a new rotated grid with points 1 meter apart
    rotated_grid_x, rotated_grid_y = np.meshgrid(np.arange(-10, L + 10, 1), 
                                                 np.arange(-10 + vertical_shift, L + vertical_shift + 10, 1))
    
    rotated_grid_x, rotated_grid_y = rotate_point(rotated_grid_x, rotated_grid_y, angle, L/2, L/2)

    ax.clear()
    
    # Draw the fixed triangle
    ax.plot(*zip(*(list(original_triangle) + [original_triangle[0]])), 'b-', label='Triangle')

    # Draw the rotated grid with points 1 meter apart
    ax.plot(rotated_grid_x, rotated_grid_y, 'o', color='orange', markersize=5)

    # Place red points on the grid within the triangle
    num_points = 0
    for x, y in zip(rotated_grid_x.flatten(), rotated_grid_y.flatten()):
        if is_point_in_triangle(x, y, original_triangle):
            ax.plot(x, y, 'o', color='red', markersize=5)
            num_points += 1

    # Display the number of grid points within the triangle
    ax.text(0.5, -1.5, f'NoP within the triangle: {num_points}', 
            horizontalalignment='center', verticalalignment='center', 
            fontsize=12, bbox=dict(facecolor='white', alpha=0.5))

    ax.set_aspect('equal')
    ax.set_xlim(-1, L + 1)
    ax.set_ylim(-1, L + 1)
    ax.legend()
    plt.draw()
