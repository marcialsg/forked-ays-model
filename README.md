# AYS-Model Documentation

## Introduction
`ays_show.py` (forked from [https://github.com/timziebart/ays-model/tree/master](https://github.com/timziebart/ays-model/tree/master)) is designed to simulate and visualize trajectories of a model based on different management scenarios. The model integrates equations using specific parameters and creates 3D plots of these trajectories. Users can select options, configure the simulation, and optionally save the output as an image.


## Requirements

### Setup
The code was tested with Python 3.5 under Ubuntu Xenial. If you want to run it on a different system, please contact [Tim.Kittel@pik-potsdam.de](mailto:Tim.Kittel@pik-potsdam.de).

The code relies on the **PyViability** library, which must be installed to ensure proper functionality. Below are the steps to set up the environment and install all necessary components:

1. **Clone the Repositories**: First, clone both the AYS model and the PyViability repositories from GitHub:

   ```bash
   git clone https://github.com/timkittel/ays-model.git
   git clone https://github.com/timkittel/PyViability.git
   ```

2. **Install Matplotlib**: It’s crucial to install a specific version of Matplotlib to avoid compatibility issues. Use the following command to install Matplotlib version 1.5.3:

   ```bash
   pip install matplotlib==1.5.3
   ```

3. **Install PyViability**: Change to the PyViability directory and install it in editable mode. This allows you to modify the code if necessary while still using it in your projects:

   ```bash
   cd PyViability
   pip install -e .
   cd ..
   ```

### Important Notes
- Ensure that you have the correct version of Matplotlib. If you install a newer version, you may encounter issues with the opacity of patches, resulting in incorrectly displayed plots. Stick to version 1.5.3 to ensure everything works as expected.

Make sure to follow these steps closely to set up your environment correctly before running the script.

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
