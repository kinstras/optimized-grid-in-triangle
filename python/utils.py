import numpy as np
import random
import matplotlib.pyplot as plt 


# Function to rotate a point around a given center by a specified angle
def rotate_point(px, py, angle, cx, cy):
    radians = np.radians(angle)  # Convert angle to radians
    cos_theta = np.cos(radians)  # Calculate cosine of the angle
    sin_theta = np.sin(radians)  # Calculate sine of the angle
    # Apply rotation matrix to the point
    nx = cos_theta * (px - cx) - sin_theta * (py - cy) + cx
    ny = sin_theta * (px - cx) + cos_theta * (py - cy) + cy
    return nx, ny

# Function to check if a point is inside a given triangle
def is_point_in_triangle(px, py, tri):
    x1, y1 = tri[0]
    x2, y2 = tri[1]
    x3, y3 = tri[2]
    # Υπολογισμός των βαρυκεντρικών συντεταγμένων
    denominator = ((y2 - y3) * (x1 - x3) + (x3 - x2) * (y1 - y3))
    a = ((y2 - y3) * (px - x3) + (x3 - x2) * (py - y3)) / denominator
    b = ((y3 - y1) * (px - x3) + (x1 - x3) * (py - y3)) / denominator
    c = 1 - a - b

    # Έλεγχος αν το σημείο βρίσκεται εντός του τριγώνου
    return (a >= 0) and (b >= 0) and (c >= 0)

# Function to count the number of points within a triangle in a given grid
def count_points_in_triangle(grid_x, grid_y, triangle):
    count = 0
    # Iterate over all points in the grid
    for x, y in zip(grid_x.flatten(), grid_y.flatten()):
        if is_point_in_triangle(x, y, triangle):
            count += 1
    return count


# Function to find the best and worst grid placements within a triangle
def find_best_and_worst_grid_placement(triangle):
    max_points = 0
    min_points = float('inf')
    best_angle = 0
    best_shift = 0
    worst_angle = 0
    worst_shift = 0
    k=0

    x1, y1 = triangle[0]
    x2, y2 = triangle[1]
    x3, y3 = triangle[2]
   
  
    # Calculate area of the triangle using determinant method
    Area = 0.5 * (-y2 * x3 + x1 * (y2 - y3) + x2 * y3 - x3 * y2) 
    
    
    # Extract the coordinates of the triangle vertices
    x_coords, y_coords = zip(*triangle)
    
    # Calculate the bounding box of the triangle
    min_x, max_x = min(x_coords), max(x_coords)
    min_y, max_y = min(y_coords), max(y_coords)

    
    # Iterate over all possible angles and shifts
    for angle in range(0, 91, 5):
        for shift in np.arange(0, 1, step=0.1):
            
            # Create a scaled grid based on the bounding box of the triangle
            grid_x_range = np.arange(min_x - 5, max_x + 5, 1)  # 1 meter apart horizontally
            grid_y_range = np.arange(min_y - 5 + shift, max_y + 5 + shift, 4)  # 4 meter apart vertically
            
            # Create the meshgrid based on the triangle's bounding box
            rotated_grid_x, rotated_grid_y = np.meshgrid(grid_x_range, grid_y_range)

            # Rotate the grid points around the center of the triangle
            center_x, center_y = np.mean(x_coords), np.mean(y_coords)
            rotated_grid_x, rotated_grid_y = rotate_point(rotated_grid_x, rotated_grid_y, angle, center_x, center_y)

            # Count points within the triangle
            points_in_triangle = count_points_in_triangle(rotated_grid_x, rotated_grid_y, triangle)
            # Update best and worst placements
            if points_in_triangle > max_points:
                max_points = points_in_triangle
                best_angle = angle
                best_shift = shift
            if points_in_triangle < min_points:
                min_points = points_in_triangle
                worst_angle = angle
                worst_shift = shift
            k +=1
    
    
        
        
    return best_angle, best_shift, max_points, worst_angle, worst_shift, min_points, Area
    
    

# Function to handle mouse scroll events (zoom in/out)
def zoom(event, ax):
    base_scale = 1.2  # Define the zoom factor

    # Get the current axis limits
    cur_xlim = ax.get_xlim()
    cur_ylim = ax.get_ylim()

    # Calculate the mouse position in data coordinates
    xdata = event.xdata
    ydata = event.ydata

    # Determine the scale factor depending on the scroll direction
    if event.button == 'up':
        scale_factor = 1 / base_scale
    elif event.button == 'down':
        scale_factor = base_scale
    else:
        # Ignore any other scroll directions
        return

    # Update the limits based on the scale factor
    new_xlim = [0,xdata + (cur_xlim[1] - xdata) * scale_factor]
    new_ylim = [0,ydata + (cur_ylim[1] - ydata) * scale_factor]

    # Apply the new limits
    ax.set_xlim(new_xlim)
    ax.set_ylim(new_ylim)

    # Redraw the figure with updated limits
    plt.draw()
  
def clear_triangle(event, ax, triangle, slider_angle, slider_vertical):
    # Clear the current triangle points
    triangle.clear()  # Clear the triangle list
    ax.clear()  # Clear the current triangle points
    plt.draw()
    global triangle_defined
    triangle_defined = False  # Reset the triangle defined flag
   



