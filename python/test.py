import numpy as np
import matplotlib.pyplot as plt
from utils import find_best_and_worst_grid_placement



def test_plot_improvement_vs_area(triangle):
    # Define the lengths over which to calculate improvements
    lengths = list(range(5, 21, 2)) + list(range(20, 101, 10))
    
    # Create a list to hold the improvement ratios and areas
    improvements_and_areas = []
    
    # Loop through each length and calculate improvements and area
    for L in lengths:
        #triangle = np.array([[1, 0.5], [L - 1, 5], [L / 4, L - 1]])  # Fixed triangle

        # Find best and worst grid placements and area
        best_angle, best_shift, max_points, worst_angle, worst_shift, min_points, area = find_best_and_worst_grid_placement(triangle, L)

        # Print length and area for debugging
        print(f"L = {L}, Area = {area:.2f}")

        # Calculate the percentage improvement
        average = (max_points + min_points) / 2
        percentage_improvement = ((max_points - average) / average) * 100

        # Print details for debugging
        print(f"Best angle: {best_angle:.2f}, Shift: {best_shift:.2f}, Max points: {max_points}")
        print(f"Worst angle: {worst_angle:.2f}, Shift: {worst_shift:.2f}, Min points: {min_points}")
        print(f"Improvement Ratio: {percentage_improvement:.2f}%\n")

        # Store the improvement ratio and area
        improvements_and_areas.append((percentage_improvement, area))
    
    # Unzip the stored data into two separate lists: one for improvements and one for areas
    improvement_ratios, areas = zip(*improvements_and_areas)
    
    # Plot the improvement ratio vs area
    plt.figure(figsize=(10, 6))
    plt.plot(areas, improvement_ratios, marker='o', linestyle='-', color='b')
    plt.title('Improvement Factor vs Area')
    plt.xlabel('Area (m^2)')
    plt.ylabel('Improvement Factor (%)')
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    test_plot_improvement_vs_area()
