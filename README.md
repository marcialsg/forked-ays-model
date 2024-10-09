# AYS-Model Documentation

(Forked from [https://github.com/timziebart/ays-model/tree/master](https://github.com/timziebart/ays-model/tree/master))

## Requirements

### Setup
The code was tested with Python 3.5 on Ubuntu Xenial. If you plan to run it on a different system, please contact [Tim.Kittel@pik-potsdam.de](mailto:Tim.Kittel@pik-potsdam.de).

The code relies on the **PyViability** library, which must be installed for proper functionality. Below are the steps to set up the environment and install all necessary components:

1. **Clone the Repositories**: First, clone both the AYS model and the PyViability repositories from GitHub:

   ```bash
   git clone https://github.com/timkittel/ays-model.git
   git clone https://github.com/timkittel/PyViability.git
   ```

2. **Install Matplotlib**: To avoid compatibility issues, install Matplotlib version 1.5.3 using the following command:

   ```bash
   pip install matplotlib==1.5.3
   ```

3. **Install PyViability**: Navigate to the PyViability directory and install it in editable mode. This allows you to modify the code if necessary while still using it in your projects:

   ```bash
   cd PyViability
   pip install -e .
   cd ..
   ```

### Important Notes
- Ensure that you use the correct version of Matplotlib. Installing a newer version may cause issues with plot opacity, resulting in incorrect displays. Stick to version 1.5.3 to avoid these problems.

Follow these steps closely to set up your environment correctly before running the scripts.

---

### `ays_export` Script Overview

This script exports an AWS-TSM file to a text file. It reads the input file containing time-series data in TSM format, processes the header and state information, and saves it as a `.txt` file.

### How to Run the Script

1. **Command-Line Execution**:

   Open your terminal or command-line interface (CLI) and navigate to the folder where the script is located.

2. **Basic Command**:

   Use the following command format:
   ```bash
   python3 ays_export.py input-file [txt-file]
   ```

   - `input-file`: Path to the AWS-TSM file you want to convert.
   - `txt-file`: (Optional) The output text file where the results will be saved. If not provided, the output will be displayed on the screen.

3. **Force Overwrite Option**:

   Use the `--force` option to overwrite an existing text file. By default, the script does not allow overwriting unless this option is specified.
   ```bash
   python3 ays_export.py input-file txt-file --force
   ```

### Command-Line Arguments

- `input-file` (Required): Path to the input AWS-TSM file.
- `txt-file` (Optional): Path to the output text file. If omitted, the result will be printed in the terminal.
- `--force` (Optional): Use this option to overwrite an existing output file.

### Examples

#### Example 1: Export to a text file without overwriting
If you have a TSM file (`data.tsm`) and want to export it to a text file (`output.txt`), run:
```bash
python3 ays_export.py data.tsm output.txt
```

#### Example 2: Export with overwriting
To overwrite an existing `output.txt` file:
```bash
python3 ays_export.py data.tsm output.txt --force
```

#### Example 3: Display output without saving
To display the result on the screen without saving it to a file:
```bash
python3 ays_export.py data.tsm
```

### Error Handling

- If the output file (`txt-file`) already exists and `--force` is not specified, the script will raise an error to prevent accidental overwriting.
- The script checks that the `input-file` and `txt-file` are different. If you attempt to use the same file for both input and output, an error will be raised.

### Output

- The script will print the header (metadata) of the input AWS-TSM file.
- The data (states) will be saved in the text file or printed to the terminal if no output file is provided.
---

### `ays_general` Module Overview
The `ays_general.py` script provides a suite of utility functions and configurations for simulating, visualizing, handling signal interruptions, and managing data related to a specific model. The script essentially supports visualization, data handling, and other general utilities required by the model implemented in other parts of the 

## Module Breakdown
### 1. Imports
The module begins with importing a variety of standard libraries and custom modules:
- **pyviability**, **heapq**, **functools**, etc.: Used for customized viability computations, heap operations, and functional programming utilities.
- **matplotlib**, **mpl_toolkits.mplot3d**, **numpy**: Utilized for data visualization, including both 2D and 3D plotting, and array manipulations.
- **pickle**, **signal**, **sys**, **warnings**: Facilitate data serialization, signal management, system operations, and warning the user of certain conditions.
### 2. Version Management
The module manages versions using tuples and provides a function `versioninfo2version` to transform version tuple into string form. The versioning system ensures compatibility with older files and tracks changes over time.
### 3. Constants
Pre-defined constants include:
- **VERSION_INFO**: Denotes the current version as `(0, 3)`.
- **AZIMUTH** and **ELEVATION**: Define default view angles for 3D visualizations.
- **INFTY_SIGN**: Represents the infinity symbol used in graphs.
### 4. Visualization Utilities
The script provides functions for generating and manipulating plots:
- **create_figure**: Sets up the 3D plot figure with appropriate labels, tickers, and view angles.
- **add_boundary**: Establishes visible boundary planes in the 3D plot to highlight regions of interest.
- **animate**: Produces an animation of the 3D plot by rotating the view and saves it as a video file.
### 5. Data Transformation
The module includes transformations to handle compactification of data points for visualization:
- **compactification** and **inv_compactification**: Convert between compact and standard forms of data which help in dealing with infinity values during plotting.
- **transformed_space**: Configures axis tick values and labels for the transformed data representation.
### 6. File Handling
Functions related to file operations include:
- **load_result_file** and **save_result_file**: Load and save data files, checking compatibility and consistency in file versions.
- **reformat**: Changes the format of a given data file to achieve compatibility with the latest version.
- **_check_format**: Validates the consistency of header and data structures in a file.
- **_reformat**: Updates header and data to align with the latest version, maintaining consistency.
### 7. Signal Management
The script allows handling of system signals:
- **signal_handler** and **register_signals**: Provide a mechanism to manage interruptions due to various system signals, allowing graceful termination or specific handling routines.
### 8. Utility Functions
Additional utility functions include:
- **recursive_difference** and **get_changed_parameters**: Identify discrepancies between two parameter sets.
- **print_changed_parameters**: Outputs differences in parameters in a formatted style.
- **recursive_dict2string**: Converts dictionary objects into a neatly formatted string for displaying.

### Usage
This module is intended to be used in conjunction with model simulation scripts that require 3D visualization, data serialization, signal handling, and various utilities for managing model parameters and results. It provides high-level abstraction for many repetitive tasks otherwise separately handled in multiple scripts.
#### Example Usage:
```python
from ays_general import create_figure, add_boundary
fig, ax3d = create_figure(A_max=1000, W_mid=1e12, S_mid=1e9)
add_boundary(ax3d, sunny_boundaries=["planetary-boundary"], A_PB=300, W_SF=200, W_mid=1e12)
plt.show()
```
This example sets up a 3D figure and adds a boundary representing a planetary boundary given certain parameter values, then displays it.
By following this structure, `ays_general.py` supports various aspects of model management and visualization needed in broader simulation workflows.

---
### `ays_model` Module Documentation

The `ays_model.py` module is a component of a larger project that models certain ecological or economic systems. The module handles parameter management, differential equation definitions, and provides mechanisms for working with different management scenarios.

## Module Breakdown

### 1. Imports

The module imports several standard and custom libraries:

- **from __future__ import**: Ensures compatibility between Python 2 and 3, specifically for division and print function behaviors.
- **ays_general**: Holds general constants and utility functions.
- **pyviability**: Provides tools for viability theory, checking version compatibility.
- **numpy**: A numerical library for array operations.
- **warnings**: For issuing warnings to users, particularly concerning compatibility or import issues.
- **sys**: Provides access to system-specific parameters and functions.

### 2. Compatibility Checks

- The script issues warnings if run with Python 2 or with a version of `pyviability` other than 0.2.0.

### 3. Numba Integration

- **Numba** is a Just-In-Time (JIT) compiler used to speed up numerical functions.
- The script attempts to import Numba, setting flags based on the success of the import, and provides a fallback decorator if Numba is unavailable.

### 4. Management Options

- **Constants**:
  - `DEFAULT_NAME`: Default management option set to "default".
  - `MANAGEMENTS`: A dictionary mapping descriptive names to short codes for different scenario managements.
  
- **Function `get_management_parameter_dict()`**:
  - Takes a management scenario and a dictionary of all parameters.
  - Returns a copy of the parameters modified by scenario-specific values or raises an error if no modifications are found.

### 5. Parameters Definitions

- **Global Parameters**:
  - `AYS_parameters`: A dictionary holding numerical constants for the model, such as time constants, economic and environmental factors.
  - `boundary_parameters`: Dedicated to defining boundaries, particularly for atmospheric carbon and economic thresholds.
  - `grid_parameters`: Includes grid-related configurations for simulation, specifying scaling and boundary settings for the model's environment.

### 6. Key Functions

- **`globalize_dictionary()`**:
  - Makes the dictionary values available as global variables within the specified module.

- **Differential Equation Functions**:
  - `_AYS_rhs()`: The core differential equation representing the model. Calculates change rates for variables A, W, and S based on input parameters.
  - `AYS_rhs`: The Numba JIT-compiled version of `_AYS_rhs` (or the base function if Numba is not available).
  - `AYS_rescaled_rhs()`: Represents the system's right-hand side in a rescaled form, important for numerical stability and handling boundary conditions.
  
- **Boundary Condition Functions**:
  - `AYS_sunny_PB()`: Checks if conditions meet planetary boundaries.
  - `AYS_sunny_SF()`: Checks if conditions surpass the social foundation.
  - `AYS_sunny_PB_SF()`: Combines checks for both planetary boundaries and social foundation.

### Usage

This module is meant to be part of a larger simulation framework and should be used by importing it into a script or another module that coordinates parameter setting, simulation execution, and visualization. By changing management scenarios and tweaking parameters, users can explore different system behaviors and outcomes.

### Conclusion

The `ays_model.py` module provides a flexible framework for defining and manipulating the dynamics of a model under various scenarios. It integrates the use of JIT compilation for performance optimization and offers functions for boundary condition checking, making it suitable for simulating complex systems dynamics.


---

### `ays_reformat` Script Overview

`ays_reformat.py` is a script designed to reformat AWS TSM result files that are assumed to be in an old format. The script utilizes the functionality of the `ays_general` module to update these files to a more current format. It accepts file names as input via command-line arguments and applies the reformatting process to each specified file.


## Script Breakdown

### 1. Imports
The script imports the following Python modules and custom libraries:
- **ays_general**: Contains utility functions, including the `reformat` function used for updating file formats.
- **argparse** and **argcomplete**: Handle command-line arguments and auto-completion.

### 2. Main Code Execution

The script's main functionality is executed within the `if __name__ == "__main__":` block:

1. **Argument Parsing**:
   - Initializes an `ArgumentParser` to manage the command-line interface.
   - Uses the argument `files`, which represents one or more files expected to be in an old format that need reformatting.
   - Argument completion is enabled through `argcomplete`.

2. **File Reformatting**:
   - For each file specified in the command line arguments, the script calls the `reformat` function from the `ays_general` module.
   - The `verbose` option in the `reformat` function is set to 1, which typically indicates that the function will provide intermediate output or messages during the process.

### How to Use This Script

1. **Running the Script**:
   Save the script as `ays_reformat.py` and execute it from the terminal, providing the file(s) to be reformatted as arguments:

   ```bash
   ./ays_reformat.py file1.txt file2.txt
   ```

2. **Command-Line Arguments**:
   - `files` (positional argument): One or more file names expected to be in an old format that need to be reformatted.

**Example:**

```bash
./ays_reformat.py result1.txt result2.txt
```

This will apply the reformatting process to `result1.txt` and `result2.txt`, updating them to the current format with messages printed for each reformatting process due to verbosity being enabled.



### Conclusion

The `ays_reformat.py` script serves as a utility for updating AWS TSM result files from an older format to a current format. By specifying files through command-line arguments, users can streamline the reformatting process, benefiting from any enhancements or changes made in the `reformat` function of the `ays_general` module.

---

### `ays_show` Script Overview

`ays_show.py` is designed to simulate and visualize trajectories of a model based on different management scenarios. The model integrates equations using specific parameters and creates 3D plots of these trajectories. Users can select options, configure the simulation, and optionally save the output as an image.



## Script Breakdown

### 1. Imports
The script starts by importing several Python modules and custom libraries:
- **ays_model** and **ays_general**: Contain model definitions and utility functions.
- **numpy**: Provides array operations.
- **scipy.integrate**: Used for numerical integration (solving differential equations).
- **scipy.optimize**: Provides optimization tools to find the zeros of functions.
- **matplotlib**: Used to generate 2D and 3D plots.
- **argparse** and **argcomplete**: Handle command-line arguments and auto-completion.

### How to Use This Script

1. **Running the Script**:
   To run the script, save it as `ays_show.py` and execute it from the terminal:

   ```bash
   ./ays_show.py
   ```

2. **Command-Line Arguments**:
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
   - `-z`, `--zero`: Computes the zero of the system's right-hand side in the S=0 plane.

**Example:**

```bash
./ays_show.py dg-bifurcation-end -n 500 -s result.png
```

This runs the script with 500 initial conditions and saves the resulting plot as `result.png`.

### 3. How the Code Works
- **Parameters**: Globalized for easy access, and the `argparse` module handles command-line arguments.
- **Random Initialization**: The script initializes a specified number of random starting conditions in 3D space.
- **Time Integration**: It integrates the system's equations over a specified time frame using numerical methods.
- **Trajectory Calculation**: The script calculates the trajectories for the specified management options.
- **Visualization**: The trajectories are plotted in 3D space, with optional boundaries based on user preferences.
- **Saving Output**: If specified, the plot can be saved as an image file.

### Conclusion
This script provides a flexible way to explore different management scenarios within a model. By adjusting parameters and using the command-line interface, users can effectively visualize the system dynamics.

