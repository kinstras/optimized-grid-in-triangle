import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from utils import rotate_point, is_point_in_triangle, count_points_in_triangle, find_best_and_worst_grid_placement
from plot import update
import time
from test import plot_improvement_vs_length

def main():
    
    # Start timing the execution
    start_time = time.time()
    
    # Define the grid and triangle parameters
    L = 51  # Maximum side length
    step = 1  # Grid spacing
    original_triangle = np.array([[1, 0.5], [L - 1, 1], [L / 2, L - 1]])  # Fixed triangle
   
    # Find the best and worst grid placements
    best_angle, best_shift, max_points, worst_angle, worst_shift, min_points = find_best_and_worst_grid_placement(original_triangle, L, step)
    print(min_points)
    # Calculate the percentage improvement
    average = (max_points - min_points)/2
    percentage_improvement = (average / min_points) * 100
    elapsed_time = time.time() - start_time

    # Print the results
    print(f"Time for L = {L} m: {elapsed_time:.2f} sec")
    print(f"\nBest position: {best_angle}° & vertical shift {best_shift}. Max nodes: {max_points}.")
    print(f"Worst position: {worst_angle}° & vertical shift {worst_shift}. Min nodes: {min_points}.")
    print(f"Improvement (%): {percentage_improvement:.2f}%.")

    # Set up the plot
    fig, ax = plt.subplots()
    plt.subplots_adjust(left=0.25, bottom=0.25)

    # Create sliders for angle and vertical shift
    ax_angle = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor='lightgoldenrodyellow')
    slider_angle = Slider(ax_angle, 'Angle', 0, 360, valinit=0, valstep=1)

    ax_vertical = plt.axes([0.05, 0.25, 0.0225, 0.63], facecolor='lightgoldenrodyellow')
    slider_vertical = Slider(ax_vertical, 'Vertical Shift', -L/2., L/2., valinit=0, valstep=0.1, orientation='vertical')

    # Update the plot when sliders are changed
    slider_angle.on_changed(lambda val: update(val, ax, original_triangle, slider_angle, slider_vertical, L))
    slider_vertical.on_changed(lambda val: update(val, ax, original_triangle, slider_angle, slider_vertical, L))
    update(0, ax, original_triangle, slider_angle, slider_vertical, L)
    
    
    #plot_improvement_vs_length()
    # Show the plot
    #plt.show()

if __name__ == "__main__":
    main()
