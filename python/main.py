import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
from utils import rotate_point, is_point_in_triangle, count_points_in_triangle, find_best_and_worst_grid_placement, zoom, clear_triangle
from plot import update, plot_triangle, onclick
import time
from test import test_plot_improvement_vs_area

def main():
    # Set up the plot
    L = 40  # Length for the triangle's bounding box
    triangle = []  # Store the clicked points for the triangle

    # Set up the plot
    fig, ax = plt.subplots()
    plt.subplots_adjust(left=0.25, bottom=0.35)

    # Create sliders for angle and vertical shift
    ax_angle = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor='lightgoldenrodyellow')
    slider_angle = Slider(ax_angle, 'Angle', 0, 90, valinit=0, valstep=1)

    ax_vertical = plt.axes([0.05, 0.25, 0.0225, 0.63], facecolor='lightgoldenrodyellow')
    slider_vertical = Slider(ax_vertical, 'Vertical \nShift', -L / 2., L / 2., valinit=0, valstep=0.1, orientation='vertical')

    # Add a button to clear the plot
    ax_clear = plt.axes([0.75, 0.01, 0.1, 0.05])  # Position of the clear button
    button_clear = Button(ax_clear, 'Clear')

    # Connect the mouse click event to the plot
    fig.canvas.mpl_connect('button_press_event', lambda event: onclick(event, ax, triangle, slider_angle, slider_vertical, L))

    # Connect the button to the clear function
    button_clear.on_clicked(lambda event: clear_triangle(event, ax, triangle, slider_angle, slider_vertical))

    
    # Connect the scroll event for zooming with the mouse wheel
    fig.canvas.mpl_connect('scroll_event', lambda event: zoom(event, ax))

    

    # Update the plot when sliders are changed
    slider_angle.on_changed(lambda val: update(val, ax, np.array(triangle), slider_angle, slider_vertical, L))
    slider_vertical.on_changed(lambda val: update(val, ax, np.array(triangle), slider_angle, slider_vertical, L))
    
    
    # Show the plot
    plt.show()

if __name__ == "__main__":
    main()
