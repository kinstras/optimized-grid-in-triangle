import numpy as np

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
    tolerance = 1e-9  # Small tolerance to handle floating point precision
    # Calculate area of the triangle using determinant method
    A = 0.5 * (-y2 * x3 + x1 * (y2 - y3) + x2 * y3 - x3 * y2)
    sign = -1 if A < 0 else 1
    # Calculate barycentric coordinates
    s = (y1 * x3 - x1 * y3 + (y3 - y1) * px + (x1 - x3) * py) * sign
    t = (x1 * y2 - y1 * x2 + (y1 - y2) * px + (x2 - x1) * py) * sign
    # Check if point is inside the triangle
    return s >= 0 and t >= 0 and (s + t) <= 2 * A * sign + tolerance

# Function to count the number of points within a triangle in a given grid
def count_points_in_triangle(grid_x, grid_y, triangle):
    count = 0
    # Iterate over all points in the grid
    for x, y in zip(grid_x.flatten(), grid_y.flatten()):
        if is_point_in_triangle(x, y, triangle):
            count += 1
    return count

# Function to find the best and worst grid placements within a triangle
def find_best_and_worst_grid_placement(triangle, L, step):
    max_points = 0
    min_points = float('inf')
    best_angle = 0
    best_shift = 0
    worst_angle = 0
    worst_shift = 0
    
    # Iterate over all possible angles and shifts
    for angle in range(0, 360):
        for shift in np.arange(-L/2., L/2., step):
            # Create a rotated grid
            rotated_grid_x, rotated_grid_y = np.meshgrid(np.arange(-10, L + 10, 1), 
                                                         np.arange(-10 + shift, L + shift + 10, 1))
            rotated_grid_x, rotated_grid_y = rotate_point(rotated_grid_x, rotated_grid_y, angle, L/2, L/2)
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
                
    return best_angle, best_shift, max_points, worst_angle, worst_shift, min_points
