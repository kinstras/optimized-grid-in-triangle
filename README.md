# Optimal Grid Placement in Triangles


## Table of Contents
- [Project Overview](#-project-overview)
- [Technologies Used](#-technologies-used)
- [Real-World Applications](#-real-world-applications)
- [Highlights](#-highlights)
- [Installation](#-installation)
- [Usage](#-usage)
- [Screenshots](#-screenshots)
- [Contributing](#-contributing)
- [License](#-license)

## 🔍 Project Overview
- **Objective**: Optimize the placement of a grid within a triangle by rotating and shifting the grid to maximize or minimize the number of points inside the triangle.
- **Key Features**:
  - **Geometric Algorithms**: Utilizes advanced algorithms to rotate points and check point inclusion within a triangle.
  - **Interactive Visualization**: Employs `matplotlib` for dynamic visualizations, allowing users to interact with the grid and triangle using sliders.
  - **Optimization**: Implements techniques to find the optimal grid placement, enhancing computational efficiency.

## 🛠 Technologies Used
- **Python**: The core programming language for the project.
- **NumPy**: For numerical computations and grid manipulations.
- **Matplotlib**: For creating interactive plots and visualizations.

## 🌍 Real-World Applications
This project has direct applications in optimizing land field layouts, which can significantly enhance agricultural planning, land surveying, and resource management. By increasing the efficiency of grid placements, we can better utilize space and improve overall productivity.

## 📈 Highlights
- Achieved significant improvements in grid placement efficiency.
- Developed a user-friendly interface for interactive exploration of geometric configurations.
- Leveraged scientific computing techniques to solve complex geometric problems.

## 🚀 Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/optimal-grid-placement.git
    cd optimal-grid-placement
    ```
2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
<p>
    Alternatively, you can install each package individually using the following commands:
</p>

<ul>
    <li><code>numpy</code> - For numerical operations</li>
    <li><code>matplotlib</code> - For plotting graphs and visualizations</li>
    <li><code>time</code> - For compute execution time </li>
</ul>

<p>
    Make sure to install these packages in the same environment where you plan to run the code. If you encounter any issues, refer to the package documentation or seek help from the community.
</p>

## 💻 Usage
Run the project with the following command:
```bash
python main.py
```


## project_directory

├── python/

│ ├── main.py # Main script

│ ├── util.py # # Rotate a point around a given center by a specified angle && checks if a point is inside a given triangle

│ ├── plot.py # Updates GUI 

│ └── test.py # # Calculates and plot the improvement percentage for a given length L
