import numpy as np
import matplotlib.pyplot as plt
from utils import find_best_and_worst_grid_placement

# Function to calculate the improvement percentage for a given length L
def calculate_improvement(L, step=1):
    import pdb; pdb.set_trace()  # Start debugger here
    print("Data for L=",L)
    # Find the best and worst grid placements
    original_triangle = np.array([[1, 0.5], [L - 1, 1], [L / 2, L - 1]])  # Fixed triangle
   
    # Find the best and worst grid placements
    best_angle, best_shift, max_points, worst_angle, worst_shift, min_points = find_best_and_worst_grid_placement(original_triangle, L, step)
   
    print("min:", min_points)
    # Handle the case when min_points is zero to avoid division by zero error
    if min_points == 0:
        return 0
    average = (max_points - min_points)/2
    percentage_improvement = (average / min_points) * 100
    return percentage_improvement

# Function to plot the improvement factor vs length
def plot_improvement_vs_length(max_length=50):
    lengths = np.arange(1, max_length + 1, 10)
    improvements = [calculate_improvement(L) for L in lengths]

    plt.figure(figsize=(10, 6))
    plt.plot(lengths, improvements, marker='o', linestyle='-', color='b')
    plt.title('Improvement Factor vs Length')
    plt.xlabel('Length (m)')
    plt.ylabel('Improvement Factor (%)')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    plot_improvement_vs_length()
