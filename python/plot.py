import numpy as np
import matplotlib.pyplot as plt
from utils import rotate_point, is_point_in_triangle, find_best_and_worst_grid_placement
import time 

triangle_defined = False # Flag to check if triangle is defined


def update(val, ax, original_triangle, slider_angle, slider_vertical, L):
    if original_triangle is not None and len(original_triangle) == 3:
        
        angle = slider_angle.val
        vertical_shift = slider_vertical.val

        # Extract the coordinates of the triangle vertices
        x_coords, y_coords = zip(*original_triangle)
        
        # Calculate the bounding box of the triangle
        min_x, max_x = min(x_coords), max(x_coords)
        min_y, max_y = min(y_coords), max(y_coords)

        # Create a scaled grid based on the bounding box of the triangle
        grid_x_range = np.arange(min_x - 5, max_x + 5, 1)  # 1 meter apart horizontally
        grid_y_range = np.arange(min_y - 5 + vertical_shift, max_y + 5 + vertical_shift, 4)  # 1 meter apart vertically
        
        # Create the meshgrid based on the triangle's bounding box
        rotated_grid_x, rotated_grid_y = np.meshgrid(grid_x_range, grid_y_range)

        # Rotate the grid points around the center of the triangle
        center_x, center_y = np.mean(x_coords), np.mean(y_coords)
        print("center_x:", center_x)
        print("center_y: ", center_y)
        rotated_grid_x, rotated_grid_y = rotate_point(rotated_grid_x, rotated_grid_y, angle, center_x, center_y)

        # Clear the axes but retain axis limits
        ax.clear()

        # Manually set the axis limits to prevent auto-rescaling
        ax.set_xlim([0, 20])
        ax.set_ylim([0, 20])
    
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
    text_x = (min_x + max_x) / 2  # Center horizontally
    text_y = min_y - 4  # Position below the triangle

    # Clear previous text if any
    for text in ax.texts:
        text.set_visible(False)

    # Add the text with improved styling
    ax.text(
        text_x, text_y, f'Number of Points within the Triangle: {num_points}', 
        horizontalalignment='center', 
        verticalalignment='center', 
        fontsize=9, 
        fontweight='bold', 
        color='darkblue', 
        bbox=dict(facecolor='lightyellow', alpha=0.7, edgecolor='black', boxstyle='round,pad=0.5'))
    plt.draw()

# Function to plot a triangle
def plot_triangle(ax, triangle):
    triangle = np.vstack([triangle, triangle[0]])  # Close the triangle
    ax.plot(triangle[:, 0], triangle[:, 1], 'r-')
    ax.set_xlim([0, 20])
    ax.set_ylim([0, 20])

# Function to handle mouse clicks and set triangle vertices
def onclick(event, ax, triangle, slider_angle, slider_vertical, L):
    
    if event.dblclick:  # Register double-clicks
        global triangle_defined
        # Capture the clicked point
        if len(triangle) < 3:
            triangle.append([event.xdata, event.ydata])
            ax.plot(event.xdata, event.ydata, 'bo')  # Mark the clicked point
            ax.set_xlim([0, 20])  # Manually reset the x-limits
            ax.set_ylim([0, 20])  # Manually reset the y-limits
            plt.draw()
        # Once 3 points are captured, plot the triangle
        if len(triangle) == 3:
            triangle_defined = True
            ax.clear()
            plot_triangle(ax, np.array(triangle))
            plt.draw()
            # Now allow updating with sliders
            update(0, ax, np.array(triangle), slider_angle, slider_vertical, L)
            analyze_triangle(triangle)

def analyze_triangle(triangle):
    if triangle_defined:  # Check if the triangle is defined
        # Start timing the execution
        start_time = time.time()
        
        best_angle, best_shift, max_points, worst_angle, worst_shift, min_points, Area = find_best_and_worst_grid_placement(triangle)
        
        average = (max_points + min_points)/2
        percentage_improvement = ((max_points - average)/average)* 100
        elapsed_time = time.time() - start_time
        
        
        # # Print the results
        print(f"Elapsed time: {elapsed_time:.2f} sec")
        print(f"\nBest position: {best_angle}° & vertical shift {best_shift}. Max nodes: {max_points}.")
        print(f"Worst position: {worst_angle}° & vertical shift {worst_shift}. Min nodes: {min_points}.")
        print(f"Improvement (%): {percentage_improvement:.2f}%.")
