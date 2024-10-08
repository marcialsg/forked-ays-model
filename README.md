# AYS-Model Documentation

## Introduction
`ays_show.py` (forked from [https://github.com/timziebart/ays-model/tree/master](https://github.com/timziebart/ays-model/tree/master)) is designed to simulate and visualize trajectories of a model based on different management scenarios. The model integrates equations using specific parameters and creates 3D plots of these trajectories. Users can select options, configure the simulation, and optionally save the output as an image.

## Requirements
Ensure you have the following Python libraries installed before running the script:

```bash
pip install numpy scipy matplotlib argcomplete
```

## Script Breakdown

### 1. Imports
The script starts by importing several Python modules and custom libraries:
- **ays_model** and **ays_general**: Contain model definitions and utility functions.
- **numpy**: Provides array operations.
- **scipy.integrate**: Used for numerical integration (solving differential equations).
- **scipy.optimize**: Provides optimization tools to find the zeros of functions.
- **matplotlib**: Used to generate 2D and 3D plots.
- **argparse** and **argcomplete**: Handle command-line arguments and auto-completion.

## How to Use This Script

### 1. Running the Script
To run the script, save it as `run_model.py` and execute it from the terminal:

```bash
./ays_show.py
```

### 2. Command-Line Arguments
You can use the following arguments when running the script:

- `option` (positional argument): Choose a management option. Available options are:
  - The default option (`aws.DEFAULT_NAME`).
  - Management options defined in `aws.MANAGEMENTS`.
  - `"dg-bifurcation-end"`: Bifurcation at the end.
  - `"dg-bifurcation-middle"`: Bifurcation in the middle.
- `-m`, `--mode`: Specifies which parts should be sampled. The default is `"all"`. You can also choose `"lake"` for a lake-specific mode.
- `-n`, `--num`: Sets the number of initial conditions for the trajectories (default: 400).
- `--no-boundary`: If set, this flag removes boundaries in the plot.
- `-s`, `--save-pic`: Saves the plot to a specified file.
- `-z`, `--zero`: If set, this flag computes the zero of the system’s right-hand side in the S=0 plane.

**Example:**

```bash
./ays_show.py dg-bifurcation-end -n 500 -s result.png
```

This runs the script with 500 initial conditions and saves the resulting plot as `result.png`.

### 3. How the Code Works
- **Parameters**: Parameters for the model are globalized for easy access, and the `argparse` module is used to handle command-line arguments.
- **Random Initialization**: The script initializes a specified number of random starting conditions in 3D space.
- **Time Integration**: It integrates the system's equations over a specified time frame using numerical methods.
- **Trajectory Calculation**: The script calculates the trajectories for the specified management options using the initial conditions.
- **Visualization**: The trajectories are plotted in 3D space, and boundaries can be added based on user preferences.
- **Saving Output**: If specified, the resulting plot can be saved as an image file.

## Conclusion
This script provides a flexible way to explore different management scenarios within a model. By adjusting parameters and using the command-line interface, users can visualize the dynamics of the system effectively.
