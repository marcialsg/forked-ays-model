
# AYS-Model Documentation

This documentation provides a detailed overview of the scripts included in the AYS model repository, which is forked from the original repository [here](https://github.com/timziebart/ays-model/tree/master). The AYS model is designed to simulate and analyze ecological or economic systems using Python. Each script in the repository serves a specific function, from exporting data to visualizing results. This document will guide you through the requirements, setup process, and functionality of each script.

## Contents
- [Requirements](#requirements)
  - [Setup](#setup)
  - [Important Notes](#important-notes)
- [Script Documentation](#script-documentation)
  - [`ays_export` Script Overview](#ays_export-script-overview)
  - [`ays_general` Module Overview](#ays_general-module-overview)
  - [`ays_model` Module Documentation](#ays_model-module-documentation)
  - [`ays_reformat` Script Overview](#ays_reformat-script-overview)
  - [`ays_tsm` Script Overview](#ays_tsm-script-overview)
  - [`ays_tsm_bifurc_show` Script Overview](#ays_tsm_bifurc_show-script-overview)
  - [`ays_tsm_show` Script Overview](#ays_tsm_show-script-overview)
  - [`ays_show` Script Overview](#ays_show-script-overview)

## Requirements

### Setup

The AYS model requires Python 3.5 and has been tested on Ubuntu Xenial. If you plan to run it on a different system, please contact [Tim.Kittel@pik-potsdam.de](mailto:Tim.Kittel@pik-potsdam.de).

The code relies on the **PyViability** library, which must be installed for proper functionality. Follow these steps to set up your environment and install all necessary components:

1. **Clone the Repositories**: First, clone both the AYS model and the PyViability repositories from GitHub:

   ```bash
   git clone https://github.com/timkittel/ays-model.git
   git clone https://github.com/timkittel/PyViability.git
   ```

2. **Install Matplotlib**: To avoid compatibility issues, install Matplotlib version 1.5.3 using the following command:

   ```bash
   pip install matplotlib==1.5.3
   ```

3. **Install PyViability**: Navigate to the PyViability directory and install it in editable mode, allowing you to modify the code if necessary while still using it in your projects:

   ```bash
   cd PyViability
   pip install -e .
   cd ..
   ```

### Important Notes

- Ensure that you use the correct version of Matplotlib. Installing a newer version may cause issues with plot opacity, resulting in incorrect displays. Stick to version 1.5.3 to avoid these problems.

Follow these steps closely to set up your environment correctly before running the scripts.

---

## Script Documentation

### `ays_export` Script Overview

This script exports an AWS-TSM file to a text file. It reads the input file containing time-series data in TSM format, processes the header and state information, and saves it as a `.txt` file.

#### How to Run the Script

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

#### Command-Line Arguments

- `input-file` (Required): Path to the input AWS-TSM file.
- `txt-file` (Optional): Path to the output text file. If omitted, the result will be printed in the terminal.
- `--force` (Optional): Use this option to overwrite an existing output file.

#### Examples

- **Example 1: Export to a text file without overwriting**

   ```bash
   python3 ays_export.py data.tsm output.txt
   ```

- **Example 2: Export with overwriting**

   ```bash
   python3 ays_export.py data.tsm output.txt --force
   ```

- **Example 3: Display output without saving**

   ```bash
   python3 ays_export.py data.tsm
   ```

#### Error Handling

- If the output file (`txt-file`) already exists and `--force` is not specified, the script will raise an error to prevent accidental overwriting.
- The script checks that the `input-file` and `txt-file` are different. If you attempt to use the same file for both input and output, an error will be raised.

#### Output

- The script will print the header (metadata) of the input AWS-TSM file.
- The data (states) will be saved in the text file or printed to the terminal if no output file is provided.

---

### `ays_general` Module Overview

The `ays_general.py` script provides a suite of utility functions and configurations for simulating, visualizing, handling signal interruptions, and managing data related to a specific model. The script supports visualization, data handling, and other general utilities required by the model implemented in other parts of the project.

#### Module Breakdown

1. **Imports**

   - **pyviability**, **heapq**, **functools**, etc.: Used for customized viability computations, heap operations, and functional programming utilities.
   - **matplotlib**, **mpl_toolkits.mplot3d**, **numpy**: Utilized for data visualization, including both 2D and 3D plotting, and array manipulations.
   - **pickle**, **signal**, **sys**, **warnings**: Facilitate data serialization, signal management, system operations, and warning users of certain conditions.

2. **Version Management**

   - The module manages versions using tuples and provides a function `versioninfo2version` to transform version tuples into string form. The versioning system ensures compatibility with older files and tracks changes over time.

3. **Constants**

   - **VERSION_INFO**: Denotes the current version as `(0, 3)`.
   - **AZIMUTH** and **ELEVATION**: Define default view angles for 3D visualizations.
   - **INFTY_SIGN**: Represents the infinity symbol used in graphs.

4. **Visualization Utilities**

   - **create_figure**: Sets up the 3D plot figure with appropriate labels, tickers, and view angles.
   - **add_boundary**: Establishes visible boundary planes in the 3D plot to highlight regions of interest.
   - **animate**: Produces an animation of the 3D plot by rotating the view and saves it as a video file.

5. **Data Transformation**

   - **compactification** and **inv_compactification**: Convert between compact and standard forms of data which help in dealing with infinity values during plotting.
   - **transformed_space**: Configures axis tick values and labels for the transformed data representation.

6. **File Handling**

   - **load_result_file** and **save_result_file**: Load and save data files, checking compatibility and consistency in file versions.
   - **reformat**: Changes the format of a given data file to achieve compatibility with the latest version.
   - **_check_format**: Validates the consistency of header and data structures in a file.
   - **_reformat**: Updates header and data to align with the latest version, maintaining consistency.

7. **Signal Management**

   - **signal_handler** and **register_signals**: Provide a mechanism to manage interruptions due to various system signals, allowing graceful termination or specific handling routines.

8. **Utility Functions**

   - **recursive_difference** and **get_changed_parameters**: Identify discrepancies between two parameter sets.
   - **print_changed_parameters**: Outputs differences in parameters in a formatted style.
   - **recursive_dict2string**: Converts dictionary objects into a neatly formatted string for displaying.

#### Usage

This module is intended to be used in conjunction with model simulation scripts that require 3D visualization, data serialization, signal handling, and various utilities for managing model parameters and results. It provides high-level abstraction for many repetitive tasks otherwise separately handled in multiple scripts.

##### Example Usage:

```python
from ays_general import create_figure, add_boundary
fig, ax3d = create_figure(A_max=1000, W_mid=1e12, S_mid=1e9)
add_boundary(ax3d, sunny_boundaries=["planetary-boundary"], A_PB=300, W_SF=200, W_mid=1e12)
plt.show()
```

This example sets up a 3D figure and adds a boundary representing a planetary boundary given certain parameter values, then displays it. By following this structure, `ays_general.py` supports various aspects of model management and visualization needed in broader simulation workflows.

---

### `ays_model` Module Documentation
The `ays_model.py` module is an integral part of a broader project aimed at modeling ecological or economic systems. This module specifically deals with parameter management, differential equation definitions, and provides mechanisms for exploring different management scenarios, allowing users to simulate and analyze the impacts of various policies or strategies.

#### Detailed Module Breakdown

1. **Imports**

   - **from __future__ import**: Ensures compatibility between Python 2 and 3, specifically regarding division and print function behaviors, making sure they act like Python 3 even in Python 2 environments.
   - **ays_general**: This import fetches the general constants and utility functions which are version-specific, ensuring that the module remains consistent with the rest of the project's components.
   - **pyviability**: A library providing tools rooted in viability theory, which is crucial for ensuring the system's parameters stay within a viable set over time. The module checks for version compatibility to prevent running with unsupported library versions.
   - **numpy**: A foundational numerical library that facilitates efficient array operations, essential for handling large datasets and performing mathematical computations needed for simulations.
   - **warnings**: Used to issue runtime warnings to users, particularly concerning compatibility issues or when imports fail, ensuring that users are aware of potential problems.
   - **sys**: Offers access to system-specific parameters and functions, particularly useful here for handling compatibility checks and module manipulations.

2. **Compatibility Checks**

   - The script is structured to issue warnings if it is executed with Python 2, as it is primarily tested with Python 3. Additionally, it warns users if the version of `pyviability` is not 0.2.0, which could lead to unexpected behavior due to changes in library functionalities.

3. **Numba Integration**

   - **Numba** is employed as a Just-In-Time (JIT) compiler to optimize numerical functions, enhancing performance by compiling Python functions to machine code at runtime. The script attempts to import Numba, and if unsuccessful, it sets a flag to false and falls back on a dummy decorator, ensuring the script remains functional without Numba, albeit at reduced efficiency.

4. **Management Options**

   - **Constants**:
     - `DEFAULT_NAME`: Represents the default management option, set to "default", indicating no specific management strategy is applied.
     - `MANAGEMENTS`: A dictionary that maps descriptive management strategy names to short codes. This allows for easy switching between different scenarios such as "degrowth" or "carbon capture storage".

   - **Function `get_management_parameter_dict()`**:
     - This function is pivotal for scenario analysis. It takes a management scenario and a dictionary of all system parameters, returning a modified copy that reflects the specific management strategy. If no changes are detected, it raises an error, ensuring users are alerted to potentially incorrect setups.

5. **Parameter Definitions**

   - These parameters define the system's state and boundaries, crucial for simulation accuracy and relevance.
   - **Global Parameters**:
     - `AYS_parameters`: This dictionary encompasses fundamental constants such as economic factors (e.g., GDP-related), environmental constants (e.g., carbon levels), and other factors (e.g., energy transformation efficiencies) that underpin the model's dynamics.
     - `boundary_parameters`: Defines critical thresholds like atmospheric carbon levels and economic benchmarks, ensuring simulations respect natural and socio-economic boundaries.
     - `grid_parameters`: Central to simulation setup, these parameters define the grid space over which simulations are run, including scaling factors and boundary adjustments for numerical stability.

6. **Key Functions**

   - **`globalize_dictionary()`**:
     - A utility function that imports dictionary values as global variables within a specified module. This is useful for dynamically adjusting simulations based on parameter changes without hardcoding values.

   - **Differential Equation Functions**:
     - `_AYS_rhs()`: The heart of the module, this function calculates the rates of change for variables A (atmospheric carbon), W (wealth), and S (social capital), based on the model's equations and input parameters. It forms the basis for the simulation's temporal evolution.
     - `AYS_rhs`: A JIT-compiled version of `_AYS_rhs`, significantly enhancing performance by reducing computation time, crucial for large-scale simulations.
     - `AYS_rescaled_rhs()`: Provides a rescaled version of the system's equations, improving numerical stability and allowing the model to handle boundary conditions more effectively, particularly important for maintaining accuracy over long simulation runs.

   - **Boundary Condition Functions**:
     - `AYS_sunny_PB()`: Evaluates whether the system's state respects planetary boundaries, a critical check for sustainable scenario validation.
     - `AYS_sunny_SF()`: Assesses whether the system's state exceeds the social foundation threshold, ensuring socio-economic sustainability.
     - `AYS_sunny_PB_SF()`: Combines checks for both planetary boundaries and social foundation, providing a holistic sustainability assessment.

#### Usage

This module is designed to be integrated into a larger simulation framework. Users can import it into their scripts or modules where they manage parameter configurations, execute simulations, and interpret results. By altering management scenarios and parameters, users can explore various system behaviors and outcomes, making it a powerful tool for policy analysis and decision-making.

#### Conclusion

The `ays_model.py` module offers a robust framework for defining and manipulating system dynamics under various scenarios. Its integration of JIT compilation for performance, along with comprehensive boundary condition checks, makes it well-suited for simulating complex system dynamics. This module empowers users to explore and understand the intricate interplay between ecological, economic, and social factors in their models.

---

### `ays_reformat` Script Overview

`ays_reformat.py` is a script designed to reformat AWS TSM result files that are assumed to be in an old format. The script utilizes the functionality of the `ays_general` module to update these files to a more current format. It accepts file names as input via command-line arguments and applies the reformatting process to each specified file.

#### Script Breakdown

1. **Imports**

   - **ays_general**: Contains utility functions, including the `reformat` function used for updating file formats.
   - **argparse** and **argcomplete**: Handle command-line arguments and auto-completion.

2. **Main Code Execution**

   The script's main functionality is executed within the `if __name__ == "__main__":` block:

   - **Argument Parsing**:
     - Initializes an `ArgumentParser` to manage the command-line interface.
     - Uses the argument `files`, which represents one or more files expected to be in an old format that need reformatting.
     - Argument completion is enabled through `argcomplete`.

   - **File Reformatting**:
     - For each file specified in the command line arguments, the script calls the `reformat` function from the `ays_general` module.
     - The `verbose` option in the `reformat` function is set to 1, which typically indicates that the function will provide intermediate output or messages during the process.

#### How to Use This Script

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

#### Conclusion

The `ays_reformat.py` script serves as a utility for updating AWS TSM result files from an older format to a current format. By specifying files through command-line arguments, users can streamline the reformatting process, benefiting from any enhancements or changes made in the `reformat` function of the `ays_general` module.

---

### `ays_tsm` Script Overview
The `ays_tsm.py` script is designed to perform an in-depth analysis of the AYS model utilizing the Tangent Space Method (TSM) within the PyViability package. This script enables users to simulate various scenarios, adjust model parameters, and compute viability metrics while accounting for different boundary conditions and management strategies. The results of the analysis are saved to a specified output file for further examination.

#### Background on Tangent Space Mapping (TSM)

Tangent Space Mapping (TSM) is a mathematical technique used to analyze data structured as Symmetric Positive-Definite (SPD) matrices, typically viewed as points on a Riemannian manifold, a type of curved space. By projecting these data points onto a tangent space, which is a flat approximation of the manifold at a specific point, TSM facilitates the application of conventional machine learning algorithms.

Basic Steps in TSM:

1. **Data Representation**: The data is represented as SPD matrices. For example, EEG signals are often transformed into covariance matrices.
2. **Riemannian Mean Calculation**: Calculate the Riemannian mean of the SPD matrices, which serves as a central reference on the manifold. This involves an iterative algorithm, as no closed-form solution exists.
3. **Mapping to Tangent Space**: Each SPD matrix is mapped onto the tangent space at the Riemannian mean using a logarithmic mapping function.
4. **Machine Learning Application**: Once the data is in the tangent space, standard machine learning algorithms can be applied for tasks such as classification.

#### Script Components and Functionality

1. **Imports and Dependencies**:
   - **ays_general** and **ays_model**: Provide general utility functions and model-specific configurations.
   - **pyviability**: Offers tools for viability kernel analysis and computational methods.
   - **numpy** and **scipy.optimize**: Support numerical operations and optimization routines, respectively.
   - **argparse** and **argcomplete**: Facilitate command-line argument parsing and enable shell auto-completion.
   - **os**, **sys**, **time**, and **datetime**: Manage system-level operations, time tracking, and filesystem interactions.

2. **Running the Script**:
   Execute it on the command line using:

   ```bash
   ./ays_tsm.py output-file -b [boundary] [options]
   ```

3. **Command-Line Arguments**:
   - **Positional Argument**:
     - `output_file`: Specifies the file to save the TSM analysis results.
   
   - **Required Argument**:
     - `-b`, `--boundaries`: Defines the boundary conditions for the simulation, with choices including `planetary-boundary`, `social-foundation`, or `both`.

   - **Optional Arguments**:
     - `--no-backscaling`: Prevents the backscaling of results.
     - `-d`, `--dry-run`: Sets up the simulation without executing the TSM computation or generating an output file.
     - `-e`, `--eddies`: Includes eddy calculations in the analysis.
     - `-f`, `--force`: Allows overwriting of an existing output file.
     - `-i`, `--integrate`: Opts for integration over linear approximation when running simulations.
     - `-n`, `--no-save`: Suppresses saving of the results.
     - `--num`: Specifies the grid size in terms of points per dimension, defaulting to `ays.grid_parameters["n0"]`.
     - `-p`, `--set-parameter`: Alters a model parameter to a specified value, using `eval` for value evaluation.
     - `--record-paths`: Records paths for potential reconstruction of simulations.
     - `--stop-when-finished`: Designates a computation step at which the process will halt after completion.
     - `-z`, `--zeros`: Estimates fixed points within the system.

   - **Management Arguments**:
     - Adds arguments dynamically based on management strategies defined in `ays.MANAGEMENTS`.

**Example Usage**:

```bash
./ays_tsm.py results.out -b both --force --num 100
```

This command initiates a TSM analysis with both boundary conditions, forces overwriting of `results.out`, and applies a 100-point grid per dimension.

4. **Code Workflow**:
   - **Argument Parsing**: Uses `argparse` to handle command-line inputs, setting parameters for simulation.
   - **Boundary and Parameter Configuration**: Processes and validates user inputs to configure model boundaries and parameters.
   - **Grid Creation**: Constructs a grid based on boundaries and specified grid parameters.
   - **Viability Computation**: Executes the TSM-based viability analysis, classifying the model's state topology.
   - **Output Management**: Saves the analysis results, including configurations and metadata, to the designated output file. If paths are recorded, they are also included.

### Conclusion
   The `ays_tsm.py` script is a comprehensive tool for examining the AYS model using TSM. It offers extensive configurability through command-line options, allowing users to perform detailed simulations tailored to specific research needs, thereby enriching the understanding of model dynamics and viability.
   

---

### `ays_tsm_bifurc_show` Script Overview

`ays_tsm_bifurc_show.py` is a Python script designed to visualize the results of bifurcation analysis in the AWS model. This script reads data from files generated by TSM analysis and creates plots to illustrate how different model parameters affect the system's behavior.

#### Script Breakdown

1. **Imports**

   - **pyviability and libviability (lv)**: Used for viability analysis and handling of regions and colors.
   - **ays_model, ays_show, ays_general**: Custom modules containing model definitions, utility functions, and plotting tools.
   - **scipy.spatial**: For spatial data structures and algorithms.
   - **numpy**: Provides support for array operations and numerical computations.
   - **pickle, argparse, argcomplete**: Handle serialization of data and command-line arguments with auto-completion.
   - **itertools, functools, datetime, os, sys**: Provide utilities for iteration, functional programming, date/time operations, and file system interactions.
   - **matplotlib**: Used for creating plots and visualizations.

#### How to Use This Script

1. **Running the Script**:
   Save the script as `ays_tsm_bifurc_show.py` and execute it from the terminal:

   ```bash
   ./ays_tsm_bifurc_show.py <parameter> <input_files...>
   ```

2. **Command-Line Arguments**:
   The script requires the following arguments:

   - `parameter`: The bifurcation parameter that is expected to change during the analysis.
   - `input_files`: One or more input files containing the results of the TSM analysis.

   Optional flags include:
   - `-s`, `--save-pic`: Save the resulting plot to a specified file.
   - `-v`, `--verbose`: Increase the verbosity level for more detailed output, can be used as `-v`, `-vv`, etc.

**Example:**

```bash
./ays_tsm_bifurc_show.py beta_DG analysis1.pkl analysis2.pkl -s bifurcation_plot.png
```

This command processes the specified analysis files and saves the resulting plot as `bifurcation_plot.png`.

#### Conclusion

This script provides a tool for analyzing and visualizing bifurcation phenomena within the AWS model. By handling multiple input files and dynamically plotting the data, users can explore how system dynamics change with varying parameters.

---

### `ays_tsm_show` Script Overview

`ays_tsm_show.py` is a script for visualizing and analyzing the results of a Time-Space Mapping (TSM) analysis performed on the AWS model. This script provides options to display different regions, set plot boundaries, analyze specific points, and visualize paths within the model space.

#### Script Breakdown

1. **Imports**

   - **pyviability**: For viability analysis functions.
   - **scipy.spatial**: Utilized for spatial computations such as triangulations.
   - **numpy**: Provides support for array operations.
   - **pickle, argparse, argcomplete**: For file handling and command-line argument parsing and auto-completion.
   - **sys, os, datetime**: System operations, path handling, and date/time utilities.
   - **functools**: High-order functions and operations on callable objects.
   - **matplotlib**: Used for generating 2D and 3D plots.

#### How to Use This Script

1. **Running the Script**:
   Save the script as `ays_tsm_show.py` and execute it from the terminal:

   ```bash
   ./ays_tsm_show.py <input-file>
   ```

2. **Command-Line Arguments**:
   The script provides a wide range of command-line arguments to customize the analysis and visualization. Users can specify the input file, analyze specific points, display regions, and set plot boundaries.

**Example:**

```bash
./ays_tsm_show.py results.pkl --show-region all -b "[[0,1],[0,1],[0,1]]" -s output.png
```

This command will plot all regions with specified boundaries and save the plot as `output.png`.

#### Conclusion

`ays_tsm_show.py` is a versatile tool for analyzing and visualizing TSM analysis results. By providing a comprehensive command-line interface, it allows users to explore different regions, analyze specific points, and customize visual output effectively.

---

### `ays_show` Script Overview

`ays_show.py` is designed to simulate and visualize trajectories of a model based on different management scenarios. The model integrates equations using specific parameters and creates 3D plots of these trajectories. Users can select options, configure the simulation, and optionally save the output as an image.

#### Script Breakdown

1. **Imports**

   - **ays_model** and **ays_general**: Contain model definitions and utility functions.
   - **numpy**: Provides array operations.
   - **scipy.integrate**: Used for numerical integration (solving differential equations).
   - **scipy.optimize**: Provides optimization tools to find the zeros of functions.
   - **matplotlib**: Used to generate 2D and 3D plots.
   - **argparse** and **argcomplete**: Handle command-line arguments and auto-completion.

#### How to Use This Script

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

### Conclusion

This script provides a flexible way to explore different management scenarios within a model. By adjusting parameters and using the command-line interface, users can effectively visualize the system dynamics.

```

This concludes the documentation, offering a comprehensive guide to the scripts in the AYS model repository. By following the instructions provided, users can effectively set up their environment, run the scripts, and explore various aspects of the model. The documentation is structured to guide university students in machine learning, helping them leverage the AYS model for their studies and projects.
```
